import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        request = helloworld_pb2.HelloRequest(name="test")
        print("request: " + str(request)) 
        response = stub.SayHello(request)
        print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
