# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc-client.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11grpc-client.proto\x12\x0ckafkaservice\"0\n\x0eProduceRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x0fProduceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1f\n\x0e\x43onsumeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\"\"\n\x0f\x43onsumeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xaf\x01\n\x0cKafkaService\x12M\n\x0eProduceMessage\x12\x1c.kafkaservice.ProduceRequest\x1a\x1d.kafkaservice.ProduceResponse\x12P\n\x0f\x43onsumeMessages\x12\x1c.kafkaservice.ConsumeRequest\x1a\x1d.kafkaservice.ConsumeResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PRODUCEREQUEST']._serialized_start=35
  _globals['_PRODUCEREQUEST']._serialized_end=83
  _globals['_PRODUCERESPONSE']._serialized_start=85
  _globals['_PRODUCERESPONSE']._serialized_end=119
  _globals['_CONSUMEREQUEST']._serialized_start=121
  _globals['_CONSUMEREQUEST']._serialized_end=152
  _globals['_CONSUMERESPONSE']._serialized_start=154
  _globals['_CONSUMERESPONSE']._serialized_end=188
  _globals['_KAFKASERVICE']._serialized_start=191
  _globals['_KAFKASERVICE']._serialized_end=366
# @@protoc_insertion_point(module_scope)
