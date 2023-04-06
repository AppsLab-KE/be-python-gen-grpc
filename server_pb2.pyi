from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAndSendOtpReq(_message.Message):
    __slots__ = ["otp_length", "phone_number"]
    OTP_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    otp_length: str
    phone_number: str
    def __init__(self, phone_number: _Optional[str] = ..., otp_length: _Optional[str] = ...) -> None: ...

class DefaultRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DefaultResponse(_message.Message):
    __slots__ = ["error", "message"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: bool
    message: str
    def __init__(self, message: _Optional[str] = ..., error: bool = ...) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
