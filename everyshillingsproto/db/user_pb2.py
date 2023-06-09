# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x02\x64\x62\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\xf9\x01\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04hash\x18\t \x01(\t\x12\x10\n\x08verified\x18\n \x01(\x08\"Y\n\rCreateUserReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x15\n\rpassword_hash\x18\x04 \x01(\t\"\x82\x02\n\rCreateUserRes\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x0e\n\x06userID\x18\x07 \x01(\t\x12\x10\n\x08verified\x18\x08 \x01(\x08\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04hash\x18\t \x01(\t\"{\n\rUpdateUserReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x15\n\rpassword_hash\x18\x04 \x01(\t\x12\x10\n\x08verified\x18\x08 \x01(\x08\x12\x0e\n\x06userID\x18\x05 \x01(\t\"\xf4\x01\n\rUpdateUserRes\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x0e\n\x06userID\x18\x07 \x01(\t\x12\x10\n\x08verified\x18\x08 \x01(\x08\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"1\n\x10GetPagedUsersReq\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"J\n\x10GetPagedUsersRes\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x17\n\x05users\x18\x03 \x03(\x0b\x32\x08.db.User\"\xa2\x01\n\rGetByfieldReq\x12-\n\x06\x66ilter\x18\x01 \x03(\x0b\x32\x1d.db.GetByfieldReq.FilterEntry\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\r\n\x05limit\x18\x03 \x01(\x03\x1a\x43\n\x0b\x46ilterEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"(\n\rGetByfieldRes\x12\x17\n\x05users\x18\x01 \x03(\x0b\x32\x08.db.UserB1Z/github.com/AppsLab-KE/backend-everyshillings/dbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/AppsLab-KE/backend-everyshillings/db'
  _GETBYFIELDREQ_FILTERENTRY._options = None
  _GETBYFIELDREQ_FILTERENTRY._serialized_options = b'8\001'
  _USER._serialized_start=79
  _USER._serialized_end=328
  _CREATEUSERREQ._serialized_start=330
  _CREATEUSERREQ._serialized_end=419
  _CREATEUSERRES._serialized_start=422
  _CREATEUSERRES._serialized_end=680
  _UPDATEUSERREQ._serialized_start=682
  _UPDATEUSERREQ._serialized_end=805
  _UPDATEUSERRES._serialized_start=808
  _UPDATEUSERRES._serialized_end=1052
  _GETPAGEDUSERSREQ._serialized_start=1054
  _GETPAGEDUSERSREQ._serialized_end=1103
  _GETPAGEDUSERSRES._serialized_start=1105
  _GETPAGEDUSERSRES._serialized_end=1179
  _GETBYFIELDREQ._serialized_start=1182
  _GETBYFIELDREQ._serialized_end=1344
  _GETBYFIELDREQ_FILTERENTRY._serialized_start=1277
  _GETBYFIELDREQ_FILTERENTRY._serialized_end=1344
  _GETBYFIELDRES._serialized_start=1346
  _GETBYFIELDRES._serialized_end=1386
# @@protoc_insertion_point(module_scope)
