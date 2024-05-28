# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common.stat_grpc.statistics_pb2 as protobufs_dot_statistics__pb2


class StatisticsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStatisticsById = channel.unary_unary(
            '/Statistics/GetStatisticsById',
            request_serializer=protobufs_dot_statistics__pb2.GetStatisticsByIdRequest.SerializeToString,
            response_deserializer=protobufs_dot_statistics__pb2.GetStatisticsByIdReply.FromString,
        )
        self.GetTopPosts = channel.unary_unary(
            '/Statistics/GetTopPosts',
            request_serializer=protobufs_dot_statistics__pb2.GetTopPostsRequest.SerializeToString,
            response_deserializer=protobufs_dot_statistics__pb2.GetTopPostsReply.FromString,
        )
        self.GetTopUsers = channel.unary_unary(
            '/Statistics/GetTopUsers',
            request_serializer=protobufs_dot_statistics__pb2.EmptyRequest.SerializeToString,
            response_deserializer=protobufs_dot_statistics__pb2.GetTopUsersReply.FromString,
        )


class StatisticsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStatisticsById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatisticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetStatisticsById': grpc.unary_unary_rpc_method_handler(
            servicer.GetStatisticsById,
            request_deserializer=protobufs_dot_statistics__pb2.GetStatisticsByIdRequest.FromString,
            response_serializer=protobufs_dot_statistics__pb2.GetStatisticsByIdReply.SerializeToString,
        ),
        'GetTopPosts': grpc.unary_unary_rpc_method_handler(
            servicer.GetTopPosts,
            request_deserializer=protobufs_dot_statistics__pb2.GetTopPostsRequest.FromString,
            response_serializer=protobufs_dot_statistics__pb2.GetTopPostsReply.SerializeToString,
        ),
        'GetTopUsers': grpc.unary_unary_rpc_method_handler(
            servicer.GetTopUsers,
            request_deserializer=protobufs_dot_statistics__pb2.EmptyRequest.FromString,
            response_serializer=protobufs_dot_statistics__pb2.GetTopUsersReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Statistics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Statistics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStatisticsById(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Statistics/GetStatisticsById',
                                             protobufs_dot_statistics__pb2.GetStatisticsByIdRequest.SerializeToString,
                                             protobufs_dot_statistics__pb2.GetStatisticsByIdReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTopPosts(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Statistics/GetTopPosts',
                                             protobufs_dot_statistics__pb2.GetTopPostsRequest.SerializeToString,
                                             protobufs_dot_statistics__pb2.GetTopPostsReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTopUsers(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Statistics/GetTopUsers',
                                             protobufs_dot_statistics__pb2.EmptyRequest.SerializeToString,
                                             protobufs_dot_statistics__pb2.GetTopUsersReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
