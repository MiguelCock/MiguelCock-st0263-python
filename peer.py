import p2p_pb2
import p2p_pb2_grpc


class Peer(p2p_pb2_grpc.P2PServicer):

    def __init__(self, id: int, socket: str):
        self.id = id
        self.socket = socket
        
        # SPECTED ID | ID | SOCKET
        self.ft = [[((id + 2**i) % 65536), id, socket] for i in range(16)]
        
        self.files = [""]

        # ID | SOCKET
        self.predecesor = [float("-Inf"), ""]
        self.antecesor = [float("-Inf"), ""]

    def Comunicate(self, request, context):
        return p2p_pb2.Respond(self_id=self.id,
                               self_socket=self.socket,
                               id=request.self_id,
                               socket=request.self_socket,
                               info="sending message")

    def Connect(self, request, context):
        from bootstrap import notify
        """
        self.insert(request.id, request.socket)
        for i in range(16):
            notify(self, request.id, request.socket, self.ft[i][2])
        """
        if request.id != self.id:
            self.ring(request.id, request.socket)
            notify(self, request.id, request.socket, self.predecesor[1])
        
        return p2p_pb2.Respond(self_id=self.id,
                               self_socket=self.socket,
                               id=request.self_id,
                               socket=request.self_socket,
                               info="new peer")

    def SearchID(self, request, context):
        from bootstrap import notify
        if self.hasFile(request.id):
            notify(self, request.id, request.socket, self.antecesor[1])
            
        return p2p_pb2.Respond(self_id=self.id,
                               self_socket=self.socket,
                               id=request.self_id,
                               socket=request.self_socket,
                               info="geting file id")

    """
    RETURN:
        param1: the index of the first peer with an id bigger than the searched id
        paran2: the index of the peer with equal id if found
        param3: the index of the last peer with an id smaller than the searched id.
    """
    def searchID(self, id: int):
        pos_big = 1
        pos_equal = False
        pos_close = 1
        close = self.ft[0][0]

        for i in range(1, 16):
            curr = self.ft[i][0]
            if curr > id:
                pos_big = i
            if curr == id:
                pos_equal = i
            if abs(close - id) > abs(curr - id):
                pos_close = i
                close = curr

        return pos_big, pos_equal, pos_close

    """
    if founded the id equal to the id in the table saves the socket

    """
    def insert(self, id: int, socket: str):

        for i in range(16):
            if self.id == self.ft[i][1]:
                self.ft[i][1] = id
                self.ft[i][2] = socket

        big, equal, close = self.searchID(id)
        if equal:
            if self.ft[equal][1] == id:
                return False
            self.ft[equal][1] = id
            self.ft[equal][2] = socket
        else:
            for p in self.ft:
                if p[1] == id:
                    return False
                if big and self.ft[big][0] != self.ft[big][1]:
                    self.ft[big][1] = id
                    self.ft[big][2] = socket
                if close:
                    self.ft[close][1] = id
                    self.ft[close][2] = socket

    """
    RETURN:
        If the id is equal the the self id returns the self
    """
    def searchFile(self, id: int):
        if id == self.id:
            return self.socket
        big, equal, close = self.searchID(id)
        if equal:
            return self.ft[equal][2]
        if close > id:
            return self.ft[close][2]
        if big < id:
            return self.ft[big][2]

    def ring(self, id: int,sokcet: str):
        if abs(self.id-1 - id) > abs(self.id-1 - self.antecesor[0]):
            self.antecesor[0] = id
            self.antecesor[1] = sokcet
        if abs(self.id+1 - id) > abs(self.id+1 - self.predecesor[0]):
            self.predecesor[0] = id
            self.predecesor[1] = sokcet

    def hasFile(self, id: int) -> bool:
        return id in self.files