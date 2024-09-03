class Peer():

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket
        self.ft = [[((id + 2**i) % 16), id, socket] for i in range(4)]
        self.files = [None]

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

        for i in range(1, 4):
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


"""
testing

# ========================MAIN========================
p1 = Peer(0, "localhost:90909")
print("ID: 0 | ", p1.ft)
p2 = Peer(1, "localhost:40901")
print("ID: 1 | ", p2.ft)
p3 = Peer(3, "localhost:12012")
print("ID: 3 | ", p3.ft)
p4 = Peer(7, "localhost:3102")
print("ID: 7 | ", p4.ft)
p5 = Peer(10, "localhost:4132")
print("ID: 10 | ", p5.ft)
p6 = Peer(14, "localhost:1234")
print("ID: 14 | ", p6.ft)

print("================================")

print("5: ", p1.searchID(5))
print("3: ", p1.searchID(3))
print("8: ", p1.searchID(8))
print("6: ", p1.searchID(6))

print("================================")

p1.insert(5, "localhost:1")
p1.insert(8, "localhost:2")
p1.insert(5, "localhost:3")
p1.insert(8, "localhost:1234134")
print(p1.ft)
print("5: ", p1.searchID(5))
print("8: ", p1.searchID(8))

print("================================")

print("File 10", p1.searchFile(10))
print("File 4", p1.searchFile(4))
print("File 3", p1.searchFile(3))
print("File 0", p1.searchFile(0))
print("File 8", p1.searchFile(8))
"""