import grpc
import grpc_gen.controller_pb2 as controller_pb2
import grpc_gen.controller_pb2_grpc as controller_pb2_grpc
from pynput import keyboard

grpc_channel = grpc.insecure_channel("localhost:6969")
controller = controller_pb2_grpc.ControllerStub(grpc_channel)


def on_press(key: keyboard.KeyCode):
    try:
        controller.PressedCharacter(
            controller_pb2.PressedCharacterRequest(character=key.char))
    except AttributeError:
        controller.PressedSpecial(
            controller_pb2.PressedSpecialRequest(key=key.__str__()))


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
