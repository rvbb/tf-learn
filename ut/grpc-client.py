# install grpc and environment
# python -m pip install --upgrade pip
# python -m pip install virtualenv
# virtualenv venv
# source venv/bin/activate
# python -m pip install --upgrade pip
# python -m pip install grpcio
# python -m pip install grpcio-tools

# generate code
# 4 python -m grpc_tools.protoc -Iut --python_out=ut/grpc_generated --grpc_python_out=ut/grpc_generated ut/CustomerCrud.proto

# 5 unit test

import sys

sys.path.append("./grpc_generated")
import google.auth
import google.auth.transport.grpc as grpc
import google.auth.transport.requests
from grpc_generated import CustomerCrud_pb2
from grpc_generated.CustomerCrud_pb2_grpc import CustomerCrudServiceStub


def run():
    print("GRPC Python Client")
    print(grpc.aio)
    # regular_endpoint = 'speech.googleapis.com:443'
    # mtls_endpoint = 'speech.mtls.googleapis.com:443'
    grpc_endpoint = 'localhost:20200'

    channel = grpc.aio.insecure_channel(grpc_endpoint)

    # credentials, _ = google.auth.default()
    # request = google.auth.transport.requests.Request()
    # channel = google.auth.transport.grpc.secure_authorized_channel(
    #     credentials, grpc_endpoint, request,
    #     ssl_credentials=grpc.ssl_channel_credentials())

    stub = CustomerCrudServiceStub.GreeterStub(channel)

    response = stub.read(CustomerCrud_pb2.CustomerRequest(id=43))
    print("response: " + response)
    print(": " + response.message)


if __name__ == '__main__':
    run()
