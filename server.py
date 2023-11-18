from concurrent import futures

import grpc
import grpc_gen.controller_pb2 as controller_pb
import grpc_gen.controller_pb2_grpc as controller_pb_grpc


class Controller(controller_pb_grpc.ControllerServicer):
    def PressedCharacter(self, request: controller_pb.PressedCharacterRequest, context):
        print(f"Pressed: {request.character}")
        return controller_pb.PressedCharacterResponse()

    def PressedSpecial(self, request: controller_pb.PressedSpecialRequest, context):
        print(f"Pressed: {request.key}")
        return controller_pb.PressedSpecialResponse()


def serve():
    port = '6969'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    controller_pb_grpc.add_ControllerServicer_to_server(Controller(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server listening on {port}")
    server.wait_for_termination()


serve()
