from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

class GreeterServicer(helloworld_pb2_grpc.Greeter):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        # self.db = route_guide_resources.read_route_guide_database()
        pass

    def SayHello(self, request, context):
        print(request)
        return helloworld_pb2.HelloReply(message="hola!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(
        GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
