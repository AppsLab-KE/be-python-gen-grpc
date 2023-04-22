from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAndSendOtpReq(_message.Message):
    __slots__ = ["phone_number"]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    def __init__(self, phone_number: _Optional[str] = ...) -> None: ...

class CreateAndSendOtpRes(_message.Message):
    __slots__ = ["message", "status_code", "tracking_uuid"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_UUID_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    tracking_uuid: str
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ..., tracking_uuid: _Optional[str] = ...) -> None: ...

class ResendOTPReq(_message.Message):
    __slots__ = ["tracking_id"]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    def __init__(self, tracking_id: _Optional[str] = ...) -> None: ...

class ResendOTPRes(_message.Message):
    __slots__ = ["message", "status_code", "tracking_uuid"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_UUID_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    tracking_uuid: str
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ..., tracking_uuid: _Optional[str] = ...) -> None: ...

class VerifyOTPReq(_message.Message):
    __slots__ = ["otp_code", "tracking_uuid"]
    OTP_CODE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_UUID_FIELD_NUMBER: _ClassVar[int]
    otp_code: str
    tracking_uuid: str
    def __init__(self, otp_code: _Optional[str] = ..., tracking_uuid: _Optional[str] = ...) -> None: ...

class VerifyOTPRes(_message.Message):
    __slots__ = ["message", "status_code"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
