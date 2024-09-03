import grpc
import p2p_pb2_grpc
from peer import Peer
from concurrent import futures


"""
Background daemon to listen for incoming connections and handle
them accordingly.
"""
def serve(user: Peer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2p_pb2_grpc.add_P2PServicer_to_server(user, server)
    server.add_insecure_port(user.socket)
    server.start()
    server.wait_for_termination()
