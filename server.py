#creating grpc service on basis of generated grpc files on giving service definition
import grpc
from concurrent import futures
import syntax_definition_pb2
import syntax_definition_pb2_grpc


#defining the server class by subclassing the handshakeservicer class
class Server(syntax_definition_pb2_grpc.HandShakeServicer):
    def DoingHandShake(self, request, context):
        #here do whatever you want and do your work
        return syntax_definition_pb2.ReplyMessage(message = f"you have send the message {request.message} and SERVER says hi to you")

def serve():
    #creating a thread pool to start the grpc service on those thread
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    #function to run on those threads
    syntax_definition_pb2_grpc.add_HandShakeServicer_to_server(Server(),server)
    server.add_insecure_port("[::]:5001")
    server.start()
    print("server started on port 5001")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()