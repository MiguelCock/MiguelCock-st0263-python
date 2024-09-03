
import grpc
import p2p_pb2
import p2p_pb2_grpc
from concurrent import futures
import sys
import threading as tr


class peer(p2p_pb2_grpc.P2P):

    def Comunicate(self, request, context):
        print(f"Received message: {request.Sended}")
        return p2p_pb2.Respond(Responded=request.Sended)


def serve(socket):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2p_pb2_grpc.add_P2PServicer_to_server(peer(), server)
    server.add_insecure_port(socket[1] + ':' + socket[2])
    server.start()
    print("Server started, listening on port " + socket[2])
    server.wait_for_termination()

def run():
    socket = input("tell something to someone: ").split()
    with grpc.insecure_channel(socket[0] + ':' + socket[1]) as channel:
        stub = p2p_pb2_grpc.P2PStub(channel)
        data = input("hola capo que quere:")
        response = stub.Comunicate(p2p_pb2.Send(Sended=data))
        print(f"Server replied: {response.Responded}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("missing socket")
    else:
        serving = tr.Thread(target=serve, args=[sys.argv], daemon=True)
        serving.start()

        while True:
            run()