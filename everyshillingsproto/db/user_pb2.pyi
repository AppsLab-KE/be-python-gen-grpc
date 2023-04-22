from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserReq(_message.Message):
    __slots__ = ["email", "name", "password_hash", "phone_number"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    password_hash: str
    phone_number: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., password_hash: _Optional[str] = ...) -> None: ...

class CreateUserRes(_message.Message):
    __slots__ = ["created_at", "deleted_at", "email", "hash", "name", "phone_number", "updated_at", "userID", "verified"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    email: str
    hash: str
    name: str
    phone_number: str
    updated_at: _timestamp_pb2.Timestamp
    userID: str
    verified: bool
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., userID: _Optional[str] = ..., verified: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hash: _Optional[str] = ...) -> None: ...

class GetByfieldReq(_message.Message):
    __slots__ = ["filter", "limit", "offset"]
    class FilterEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filter: _containers.MessageMap[str, _any_pb2.Any]
    limit: int
    offset: int
    def __init__(self, filter: _Optional[_Mapping[str, _any_pb2.Any]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetByfieldRes(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class GetPagedUsersReq(_message.Message):
    __slots__ = ["limit", "offset"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetPagedUsersRes(_message.Message):
    __slots__ = ["limit", "offset", "users"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ..., users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UpdateUserReq(_message.Message):
    __slots__ = ["email", "name", "password_hash", "phone_number", "userID", "verified"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    password_hash: str
    phone_number: str
    userID: str
    verified: bool
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., password_hash: _Optional[str] = ..., verified: bool = ..., userID: _Optional[str] = ...) -> None: ...

class UpdateUserRes(_message.Message):
    __slots__ = ["created_at", "deleted_at", "email", "name", "phone_number", "updated_at", "userID", "verified"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    email: str
    name: str
    phone_number: str
    updated_at: _timestamp_pb2.Timestamp
    userID: str
    verified: bool
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., userID: _Optional[str] = ..., verified: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["created_at", "deleted_at", "email", "hash", "name", "phone_number", "updated_at", "userID", "verified"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    email: str
    hash: str
    name: str
    phone_number: str
    updated_at: _timestamp_pb2.Timestamp
    userID: str
    verified: bool
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., userID: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hash: _Optional[str] = ..., verified: bool = ...) -> None: ...
