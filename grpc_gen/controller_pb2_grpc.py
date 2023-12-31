# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_gen import controller_pb2 as grpc__gen_dot_controller__pb2


class ControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PressedCharacter = channel.unary_unary(
                '/controller.Controller/PressedCharacter',
                request_serializer=grpc__gen_dot_controller__pb2.PressedCharacterRequest.SerializeToString,
                response_deserializer=grpc__gen_dot_controller__pb2.PressedCharacterResponse.FromString,
                )
        self.PressedSpecial = channel.unary_unary(
                '/controller.Controller/PressedSpecial',
                request_serializer=grpc__gen_dot_controller__pb2.PressedSpecialRequest.SerializeToString,
                response_deserializer=grpc__gen_dot_controller__pb2.PressedSpecialResponse.FromString,
                )


class ControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PressedCharacter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PressedSpecial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PressedCharacter': grpc.unary_unary_rpc_method_handler(
                    servicer.PressedCharacter,
                    request_deserializer=grpc__gen_dot_controller__pb2.PressedCharacterRequest.FromString,
                    response_serializer=grpc__gen_dot_controller__pb2.PressedCharacterResponse.SerializeToString,
            ),
            'PressedSpecial': grpc.unary_unary_rpc_method_handler(
                    servicer.PressedSpecial,
                    request_deserializer=grpc__gen_dot_controller__pb2.PressedSpecialRequest.FromString,
                    response_serializer=grpc__gen_dot_controller__pb2.PressedSpecialResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'controller.Controller', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Controller(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PressedCharacter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/controller.Controller/PressedCharacter',
            grpc__gen_dot_controller__pb2.PressedCharacterRequest.SerializeToString,
            grpc__gen_dot_controller__pb2.PressedCharacterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PressedSpecial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/controller.Controller/PressedSpecial',
            grpc__gen_dot_controller__pb2.PressedSpecialRequest.SerializeToString,
            grpc__gen_dot_controller__pb2.PressedSpecialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
