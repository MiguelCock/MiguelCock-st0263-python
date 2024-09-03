from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("self_id", "self_socket", "id", "socket", "info")
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_SOCKET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SOCKET_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    self_id: int
    self_socket: str
    id: int
    socket: str
    info: str
    def __init__(self, self_id: _Optional[int] = ..., self_socket: _Optional[str] = ..., id: _Optional[int] = ..., socket: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...

class Respond(_message.Message):
    __slots__ = ("self_id", "self_socket", "id", "socket", "info")
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_SOCKET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SOCKET_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    self_id: int
    self_socket: str
    id: int
    socket: str
    info: str
    def __init__(self, self_id: _Optional[int] = ..., self_socket: _Optional[str] = ..., id: _Optional[int] = ..., socket: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...
