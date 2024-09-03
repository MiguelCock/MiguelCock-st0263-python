import grpc
import p2p_pb2
import p2p_pb2_grpc
from peer import Peer
from hash import hash_key


def run(user: Peer):
    action = input(
        "What do you want to do? (Add file/Get file/Get finger table): \n")

    if action == "Add file":
        user.files.append(input("Wich file: "))

    elif action == "Get file":
        file_id = hash_key(input("Wich file: "))
        file_socket = user.searchFile(file_id)
        with grpc.insecure_channel(file_socket) as channel:
            stub = p2p_pb2_grpc.P2PStub(channel)
            response = stub.SearchID(
                p2p_pb2.Request(self_id=user.id,
                                self_socket=user.socket,
                                id=user.id,
                                socket="",
                                info="geting file"))
            print(f"Server replied: {response.Responded}")

    elif action == "Get finger table":
        print("FT:", user.ft)
