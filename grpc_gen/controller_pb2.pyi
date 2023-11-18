from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PressedCharacterRequest(_message.Message):
    __slots__ = ["character"]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    character: str
    def __init__(self, character: _Optional[str] = ...) -> None: ...

class PressedCharacterResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PressedSpecialRequest(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class PressedSpecialResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
