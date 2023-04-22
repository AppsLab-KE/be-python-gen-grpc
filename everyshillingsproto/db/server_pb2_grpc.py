# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2
import user_pb2 as user__pb2


class DbServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HealthCheck = channel.unary_unary(
                '/db.DbService/HealthCheck',
                request_serializer=server__pb2.DefaultRequest.SerializeToString,
                response_deserializer=server__pb2.HealthResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/db.DbService/CreateUser',
                request_serializer=user__pb2.CreateUserReq.SerializeToString,
                response_deserializer=user__pb2.CreateUserRes.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/db.DbService/UpdateUser',
                request_serializer=user__pb2.UpdateUserReq.SerializeToString,
                response_deserializer=user__pb2.UpdateUserRes.FromString,
                )
        self.GetPagedUsers = channel.unary_unary(
                '/db.DbService/GetPagedUsers',
                request_serializer=user__pb2.GetPagedUsersReq.SerializeToString,
                response_deserializer=user__pb2.GetPagedUsersRes.FromString,
                )
        self.GetUserByField = channel.unary_unary(
                '/db.DbService/GetUserByField',
                request_serializer=user__pb2.GetByfieldReq.SerializeToString,
                response_deserializer=user__pb2.GetByfieldRes.FromString,
                )


class DbServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """USERS
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPagedUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByField(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DbServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=server__pb2.DefaultRequest.FromString,
                    response_serializer=server__pb2.HealthResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=user__pb2.CreateUserReq.FromString,
                    response_serializer=user__pb2.CreateUserRes.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=user__pb2.UpdateUserReq.FromString,
                    response_serializer=user__pb2.UpdateUserRes.SerializeToString,
            ),
            'GetPagedUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPagedUsers,
                    request_deserializer=user__pb2.GetPagedUsersReq.FromString,
                    response_serializer=user__pb2.GetPagedUsersRes.SerializeToString,
            ),
            'GetUserByField': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByField,
                    request_deserializer=user__pb2.GetByfieldReq.FromString,
                    response_serializer=user__pb2.GetByfieldRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'db.DbService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DbService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DbService/HealthCheck',
            server__pb2.DefaultRequest.SerializeToString,
            server__pb2.HealthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DbService/CreateUser',
            user__pb2.CreateUserReq.SerializeToString,
            user__pb2.CreateUserRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DbService/UpdateUser',
            user__pb2.UpdateUserReq.SerializeToString,
            user__pb2.UpdateUserRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPagedUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DbService/GetPagedUsers',
            user__pb2.GetPagedUsersReq.SerializeToString,
            user__pb2.GetPagedUsersRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db.DbService/GetUserByField',
            user__pb2.GetByfieldReq.SerializeToString,
            user__pb2.GetByfieldRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)