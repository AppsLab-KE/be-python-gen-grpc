# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x03otp\"\x10\n\x0e\x44\x65\x66\x61ultRequest\"!\n\x0eHealthResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2E\n\nOtpService\x12\x37\n\x0bHealthCheck\x12\x13.otp.DefaultRequest\x1a\x13.otp.HealthResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEFAULTREQUEST._serialized_start=21
  _DEFAULTREQUEST._serialized_end=37
  _HEALTHRESPONSE._serialized_start=39
  _HEALTHRESPONSE._serialized_end=72
  _OTPSERVICE._serialized_start=74
  _OTPSERVICE._serialized_end=143
# @@protoc_insertion_point(module_scope)