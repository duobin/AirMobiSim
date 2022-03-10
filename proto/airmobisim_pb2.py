# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/airmobisim.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/airmobisim.proto',
  package='airmobisim',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16proto/airmobisim.proto\x12\nairmobisim\x1a\x1bgoogle/protobuf/empty.proto\"7\n\x0cWaypointList\x12\'\n\twaypoints\x18\x01 \x03(\x0b\x32\x14.airmobisim.Waypoint\":\n\x08Waypoint\x12\r\n\x05index\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\"(\n\x07UavList\x12\x1d\n\x04uavs\x18\x01 \x03(\x0b\x32\x0f.airmobisim.Uav\"A\n\x03Uav\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x01\"F\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x01\"8\n\rResponseQuery\x12\'\n\tresponses\x18\x01 \x03(\x0b\x32\x14.airmobisim.Response\"b\n\x08StartUav\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x0b\x63oordinates\x18\x02 \x03(\x0b\x32\x17.airmobisim.Coordinates\x12\r\n\x05speed\x18\x03 \x01(\x01\x12\r\n\x05\x61ngle\x18\x04 \x01(\x01\".\n\x0b\x43oordinates\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"\x15\n\x06Number\x12\x0b\n\x03num\x18\x01 \x01(\x05\x32\x84\x04\n\nAirMobiSim\x12\x37\n\x05Start\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12G\n\x12\x45xecuteOneTimeStep\x12\x16.google.protobuf.Empty\x1a\x19.airmobisim.ResponseQuery\x12\x38\n\x06\x46inish\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12>\n\x0fGetManagedHosts\x12\x16.google.protobuf.Empty\x1a\x13.airmobisim.UavList\x12\x43\n\x0fInsertWaypoints\x12\x18.airmobisim.WaypointList\x1a\x16.google.protobuf.Empty\x12\x39\n\tInsertUAV\x12\x14.airmobisim.StartUav\x1a\x16.google.protobuf.Empty\x12\x37\n\tDeleteUAV\x12\x12.airmobisim.Number\x1a\x16.google.protobuf.Empty\x12\x41\n\x13getNumberCurrentUAV\x12\x16.google.protobuf.Empty\x1a\x12.airmobisim.Numberb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_WAYPOINTLIST = _descriptor.Descriptor(
  name='WaypointList',
  full_name='airmobisim.WaypointList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='waypoints', full_name='airmobisim.WaypointList.waypoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=122,
)


_WAYPOINT = _descriptor.Descriptor(
  name='Waypoint',
  full_name='airmobisim.Waypoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='airmobisim.Waypoint.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='airmobisim.Waypoint.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='airmobisim.Waypoint.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='airmobisim.Waypoint.z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=182,
)


_UAVLIST = _descriptor.Descriptor(
  name='UavList',
  full_name='airmobisim.UavList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uavs', full_name='airmobisim.UavList.uavs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=224,
)


_UAV = _descriptor.Descriptor(
  name='Uav',
  full_name='airmobisim.Uav',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='airmobisim.Uav.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='airmobisim.Uav.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='airmobisim.Uav.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='airmobisim.Uav.z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='airmobisim.Uav.speed', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=291,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='airmobisim.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='airmobisim.Response.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='airmobisim.Response.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='airmobisim.Response.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='airmobisim.Response.z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='airmobisim.Response.speed', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=363,
)


_RESPONSEQUERY = _descriptor.Descriptor(
  name='ResponseQuery',
  full_name='airmobisim.ResponseQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='airmobisim.ResponseQuery.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=421,
)


_STARTUAV = _descriptor.Descriptor(
  name='StartUav',
  full_name='airmobisim.StartUav',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='airmobisim.StartUav.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='airmobisim.StartUav.coordinates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='airmobisim.StartUav.speed', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle', full_name='airmobisim.StartUav.angle', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=521,
)


_COORDINATES = _descriptor.Descriptor(
  name='Coordinates',
  full_name='airmobisim.Coordinates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='airmobisim.Coordinates.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='airmobisim.Coordinates.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='airmobisim.Coordinates.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=569,
)


_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='airmobisim.Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='airmobisim.Number.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=592,
)

_WAYPOINTLIST.fields_by_name['waypoints'].message_type = _WAYPOINT
_UAVLIST.fields_by_name['uavs'].message_type = _UAV
_RESPONSEQUERY.fields_by_name['responses'].message_type = _RESPONSE
_STARTUAV.fields_by_name['coordinates'].message_type = _COORDINATES
DESCRIPTOR.message_types_by_name['WaypointList'] = _WAYPOINTLIST
DESCRIPTOR.message_types_by_name['Waypoint'] = _WAYPOINT
DESCRIPTOR.message_types_by_name['UavList'] = _UAVLIST
DESCRIPTOR.message_types_by_name['Uav'] = _UAV
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ResponseQuery'] = _RESPONSEQUERY
DESCRIPTOR.message_types_by_name['StartUav'] = _STARTUAV
DESCRIPTOR.message_types_by_name['Coordinates'] = _COORDINATES
DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WaypointList = _reflection.GeneratedProtocolMessageType('WaypointList', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINTLIST,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.WaypointList)
  })
_sym_db.RegisterMessage(WaypointList)

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINT,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.Waypoint)
  })
_sym_db.RegisterMessage(Waypoint)

UavList = _reflection.GeneratedProtocolMessageType('UavList', (_message.Message,), {
  'DESCRIPTOR' : _UAVLIST,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.UavList)
  })
_sym_db.RegisterMessage(UavList)

Uav = _reflection.GeneratedProtocolMessageType('Uav', (_message.Message,), {
  'DESCRIPTOR' : _UAV,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.Uav)
  })
_sym_db.RegisterMessage(Uav)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.Response)
  })
_sym_db.RegisterMessage(Response)

ResponseQuery = _reflection.GeneratedProtocolMessageType('ResponseQuery', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEQUERY,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.ResponseQuery)
  })
_sym_db.RegisterMessage(ResponseQuery)

StartUav = _reflection.GeneratedProtocolMessageType('StartUav', (_message.Message,), {
  'DESCRIPTOR' : _STARTUAV,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.StartUav)
  })
_sym_db.RegisterMessage(StartUav)

Coordinates = _reflection.GeneratedProtocolMessageType('Coordinates', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATES,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.Coordinates)
  })
_sym_db.RegisterMessage(Coordinates)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'proto.airmobisim_pb2'
  # @@protoc_insertion_point(class_scope:airmobisim.Number)
  })
_sym_db.RegisterMessage(Number)



_AIRMOBISIM = _descriptor.ServiceDescriptor(
  name='AirMobiSim',
  full_name='airmobisim.AirMobiSim',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=595,
  serialized_end=1111,
  methods=[
  _descriptor.MethodDescriptor(
    name='Start',
    full_name='airmobisim.AirMobiSim.Start',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteOneTimeStep',
    full_name='airmobisim.AirMobiSim.ExecuteOneTimeStep',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RESPONSEQUERY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Finish',
    full_name='airmobisim.AirMobiSim.Finish',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetManagedHosts',
    full_name='airmobisim.AirMobiSim.GetManagedHosts',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_UAVLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertWaypoints',
    full_name='airmobisim.AirMobiSim.InsertWaypoints',
    index=4,
    containing_service=None,
    input_type=_WAYPOINTLIST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertUAV',
    full_name='airmobisim.AirMobiSim.InsertUAV',
    index=5,
    containing_service=None,
    input_type=_STARTUAV,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUAV',
    full_name='airmobisim.AirMobiSim.DeleteUAV',
    index=6,
    containing_service=None,
    input_type=_NUMBER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getNumberCurrentUAV',
    full_name='airmobisim.AirMobiSim.getNumberCurrentUAV',
    index=7,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_NUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AIRMOBISIM)

DESCRIPTOR.services_by_name['AirMobiSim'] = _AIRMOBISIM

# @@protoc_insertion_point(module_scope)
