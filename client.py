import grpc

import syntax_definition_pb2
import syntax_definition_pb2_grpc

def client():
    with grpc.insecure_channel('localhost:5001') as channel:
        #so stub is for calling the server
        stub = syntax_definition_pb2_grpc.HandShakeStub(channel)
        #from the stub we are invoking the required function on our channel
        response = stub.DoingHandShake(syntax_definition_pb2.RequestMessage(message = "my name is ravindra"))
    print(f"response from the server {response.message}")

if __name__ == '__main__':
    client()