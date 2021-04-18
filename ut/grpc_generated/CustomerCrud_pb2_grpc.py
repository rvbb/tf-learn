# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import CustomerCrud_pb2 as CustomerCrud__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CustomerCrudServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/com.rvbb.b2b.grpc.service.CustomerCrudService/create',
                request_serializer=CustomerCrud__pb2.CustomerRequest.SerializeToString,
                response_deserializer=CustomerCrud__pb2.CustomerResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/com.rvbb.b2b.grpc.service.CustomerCrudService/update',
                request_serializer=CustomerCrud__pb2.CustomerRequest.SerializeToString,
                response_deserializer=CustomerCrud__pb2.CustomerResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/com.rvbb.b2b.grpc.service.CustomerCrudService/delete',
                request_serializer=CustomerCrud__pb2.ID.SerializeToString,
                response_deserializer=CustomerCrud__pb2.CustomerResponse.FromString,
                )
        self.read = channel.unary_unary(
                '/com.rvbb.b2b.grpc.service.CustomerCrudService/read',
                request_serializer=CustomerCrud__pb2.ID.SerializeToString,
                response_deserializer=CustomerCrud__pb2.CustomerResponse.FromString,
                )
        self.listAll = channel.unary_unary(
                '/com.rvbb.b2b.grpc.service.CustomerCrudService/listAll',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=CustomerCrud__pb2.CustomerResponse.FromString,
                )


class CustomerCrudServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerCrudServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=CustomerCrud__pb2.CustomerRequest.FromString,
                    response_serializer=CustomerCrud__pb2.CustomerResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=CustomerCrud__pb2.CustomerRequest.FromString,
                    response_serializer=CustomerCrud__pb2.CustomerResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=CustomerCrud__pb2.ID.FromString,
                    response_serializer=CustomerCrud__pb2.CustomerResponse.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=CustomerCrud__pb2.ID.FromString,
                    response_serializer=CustomerCrud__pb2.CustomerResponse.SerializeToString,
            ),
            'listAll': grpc.unary_unary_rpc_method_handler(
                    servicer.listAll,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=CustomerCrud__pb2.CustomerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.rvbb.b2b.grpc.service.CustomerCrudService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerCrudService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.rvbb.b2b.grpc.service.CustomerCrudService/create',
            CustomerCrud__pb2.CustomerRequest.SerializeToString,
            CustomerCrud__pb2.CustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.rvbb.b2b.grpc.service.CustomerCrudService/update',
            CustomerCrud__pb2.CustomerRequest.SerializeToString,
            CustomerCrud__pb2.CustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.rvbb.b2b.grpc.service.CustomerCrudService/delete',
            CustomerCrud__pb2.ID.SerializeToString,
            CustomerCrud__pb2.CustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.rvbb.b2b.grpc.service.CustomerCrudService/read',
            CustomerCrud__pb2.ID.SerializeToString,
            CustomerCrud__pb2.CustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.rvbb.b2b.grpc.service.CustomerCrudService/listAll',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            CustomerCrud__pb2.CustomerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
