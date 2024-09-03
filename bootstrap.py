import grpc
import p2p_pb2
import p2p_pb2_grpc
from peer import Peer


"""
Asks the user for the sokcet of a peer that he knows to
tell the others about his existence and update the FT.
"""
def connect(user: Peer):
    socket = input("whom do you wanna connect to: (ip + "
                   " + port) ").split()
    notify(user, user.id, user.socket,socket[0] + ':' + socket[1])


"""
Notifies the user about a new peer that has joined the network.
"""
def notify(user: Peer, new_id: int, new_socket: str, socket: str):
    with grpc.insecure_channel(socket) as channel:
        stub = p2p_pb2_grpc.P2PStub(channel)
        response = stub.Connect(
            p2p_pb2.Request(self_id=user.id,
                            self_socket=user.socket,
                            id=new_id,
                            socket=new_socket,
                            info="new peer"))
        print(f"Server replied: {response}")

"""
"""
def gotFile(user: Peer, id: int, user_socket: str):
    with grpc.insecure_channel(user_socket) as channel:
        stub = p2p_pb2_grpc.P2PStub(channel)
        response = stub.Connect(
            p2p_pb2.Request(self_id=user.id,
                            self_socket=user.socket,
                            id=0,
                            socket=user_socket,
                            info="got the file {id}"))
        print(f"Server replied: {response}")