"""Generated message classes for bigtableclusteradmin version v1.

This is a OnePlatform service.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages

from googlecloudapis.apitools.base.py import encoding


package = 'bigtableclusteradmin'


class BigtableclusteradminOperationsCancelRequest(_messages.Message):
  """A BigtableclusteradminOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: A string attribute.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class BigtableclusteradminOperationsDeleteRequest(_messages.Message):
  """A BigtableclusteradminOperationsDeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminOperationsGetRequest(_messages.Message):
  """A BigtableclusteradminOperationsGetRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminOperationsListRequest(_messages.Message):
  """A BigtableclusteradminOperationsListRequest object.

  Fields:
    filter: A string attribute.
    name: A string attribute.
    pageSize: A integer attribute.
    pageToken: A string attribute.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class BigtableclusteradminProjectsAggregatedClustersListRequest(_messages.Message):
  """A BigtableclusteradminProjectsAggregatedClustersListRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersDeleteRequest(_messages.Message):
  """A BigtableclusteradminProjectsZonesClustersDeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersGetRequest(_messages.Message):
  """A BigtableclusteradminProjectsZonesClustersGetRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersUndeleteRequest(_messages.Message):
  """A BigtableclusteradminProjectsZonesClustersUndeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesListRequest(_messages.Message):
  """A BigtableclusteradminProjectsZonesListRequest object.

  Fields:
    name: A string attribute.
  """

  name = _messages.StringField(1, required=True)


class CancelOperationRequest(_messages.Message):
  """A CancelOperationRequest object."""


class Cluster(_messages.Message):
  """A Cluster object.

  Enums:
    DefaultStorageTypeValueValuesEnum:

  Fields:
    currentOperation: A Operation attribute.
    defaultStorageType: A DefaultStorageTypeValueValuesEnum attribute.
    deleteTime: A string attribute.
    displayName: A string attribute.
    hddBytes: A string attribute.
    name: A string attribute.
    serveNodes: A integer attribute.
    ssdBytes: A string attribute.
  """

  class DefaultStorageTypeValueValuesEnum(_messages.Enum):
    """DefaultStorageTypeValueValuesEnum enum type.

    Values:
      HDD: <no description>
      SSD: <no description>
      UNKNOWN: <no description>
    """
    HDD = 0
    SSD = 1
    UNKNOWN = 2

  currentOperation = _messages.MessageField('Operation', 1)
  defaultStorageType = _messages.EnumField('DefaultStorageTypeValueValuesEnum', 2)
  deleteTime = _messages.StringField(3)
  displayName = _messages.StringField(4)
  hddBytes = _messages.IntegerField(5)
  name = _messages.StringField(6)
  serveNodes = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  ssdBytes = _messages.IntegerField(8)


class CreateClusterRequest(_messages.Message):
  """A CreateClusterRequest object.

  Fields:
    cluster: A Cluster attribute.
    clusterId: A string attribute.
    name: A string attribute.
  """

  cluster = _messages.MessageField('Cluster', 1)
  clusterId = _messages.StringField(2)
  name = _messages.StringField(3)


class Empty(_messages.Message):
  """A Empty object."""


class ListClustersResponse(_messages.Message):
  """A ListClustersResponse object.

  Fields:
    clusters: A Cluster attribute.
    failedZones: A Zone attribute.
  """

  clusters = _messages.MessageField('Cluster', 1, repeated=True)
  failedZones = _messages.MessageField('Zone', 2, repeated=True)


class ListOperationsResponse(_messages.Message):
  """A ListOperationsResponse object.

  Fields:
    nextPageToken: A string attribute.
    operations: A Operation attribute.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class ListZonesResponse(_messages.Message):
  """A ListZonesResponse object.

  Fields:
    zones: A Zone attribute.
  """

  zones = _messages.MessageField('Zone', 1, repeated=True)


class Operation(_messages.Message):
  """A Operation object.

  Messages:
    MetadataValue: A MetadataValue object.
    ResponseValue: A ResponseValue object.

  Fields:
    done: A boolean attribute.
    error: A Status attribute.
    metadata: A MetadataValue attribute.
    name: A string attribute.
    response: A ResponseValue attribute.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """A MetadataValue object.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Additional properties of type MetadataValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """A ResponseValue object.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Additional properties of type ResponseValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


class Status(_messages.Message):
  """A Status object.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: A integer attribute.
    details: A DetailsValueListEntry attribute.
    message: A string attribute.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Additional properties of type
        DetailsValueListEntry
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class Zone(_messages.Message):
  """A Zone object.

  Enums:
    StatusValueValuesEnum:

  Fields:
    displayName: A string attribute.
    name: A string attribute.
    status: A StatusValueValuesEnum attribute.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """StatusValueValuesEnum enum type.

    Values:
      EMERGENCY_MAINENANCE: <no description>
      OK: <no description>
      PLANNED_MAINTENANCE: <no description>
      UNKNOWN: <no description>
    """
    EMERGENCY_MAINENANCE = 0
    OK = 1
    PLANNED_MAINTENANCE = 2
    UNKNOWN = 3

  displayName = _messages.StringField(1)
  name = _messages.StringField(2)
  status = _messages.EnumField('StatusValueValuesEnum', 3)


