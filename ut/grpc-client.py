#install grpc and environment
# python -m pip install --upgrade pip
# python -m pip install virtualenv
# virtualenv venv
# source venv/bin/activate
# python -m pip install --upgrade pip
#
# python -m pip install grpcio

#generate code
#python -m grpc_tools.protoc -Iut --python_out=ut/grpc_generated --grpc_python_out=ut/grpc_generated ut/CustomerCrud.proto

#unit test with print only

import grpc_generated.CustomerCrudServiceStub
from google.auth.transport import grpc


def run():
  channel = grpc.insecure_channel('localhost:20200')
  stub = CustomerCrudServiceStub.GreeterStub(channel)
  # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  # print("Greeter client received: " + response.message)
  # response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
  # print("Greeter client received: " + response.message)