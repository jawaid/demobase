"""Generated message classes for deploymentmanager version v2beta2.

The Deployment Manager API allows users to declaratively configure, deploy and
run complex solutions on the Google Cloud Platform.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages


package = 'deploymentmanager'


class Deployment(_messages.Message):
  """Deployment message type.

  Fields:
    description: An optional user-provided description of the deployment.
    fingerprint: Specifies a fingerprint for update() requests. A fingerprint
      is a randomly generated value that must be provided in update() requests
      to perform optimistic locking. This ensures optimistic concurrency so
      that only one update can be performed at a time.  The fingerprint is
      initially generated by Deployment Manager and changes after every
      request to modify data. To get the latest fingerprint value, perform a
      get() request to a deployment.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    insertTime: [Output Only] Timestamp when the deployment was created, in
      RFC3339 text format .
    intent: [Input Only] Specifies how Deployment Manager should apply this
      template. Possible options are PREVIEW, UPDATE, and CANCEL.  PREVIEW
      creates a deployment and creates "shell" resources but does not actually
      instantiate these resources. This allows you to preview what your
      deployment looks like. You can use this intent to preview updates to
      deployments or preview new deployments. You must provide a target.config
      with a configuration for this intent. After previewing a deployment, you
      can deploy your resources by making a request with the UPDATE intent or
      you can CANCEL the preview altogether. Note that the deployment will
      still exist after you cancel the preview and you must separately delete
      this deployment if you want to remove it.  UPDATE performs an update to
      the underlying resources in a deployment. If you provide a populated
      target.config field with this request, Deployment Manager uses that
      configuration to perform an update. If you had previewed this update
      beforehand, and do not supply a target.config or provide an empty
      target.config, Deployment Manager uses the last previewed configuration.
      CANCEL cancels an update that is in PREVIEW or UPDATE but does not undo
      any changes already made.
    manifest: [Output Only] URL of the manifest representing the last manifest
      that was successfully deployed.
    name: The name of the deployment, which must be unique within the project.
    state: [Output Only] The current state of the deployment. This can be
      DEPLOYED, DEPLOYMENT_FAILED, PREVIEWING, UPDATING, and CANCELING.
    target: [Input Only] The parameters that define your deployment, including
      the deployment configuration and relevant templates.
    update: [Output Only] If Deployment Manager is currently updating or
      previewing an update to this deployment, the updated configuration
      appears here.
    updateTime: [Output Only] Timestamp when the deployment was updated, in
      RFC3339 text format .
  """

  description = _messages.StringField(1)
  fingerprint = _messages.BytesField(2)
  id = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(4)
  intent = _messages.StringField(5)
  manifest = _messages.StringField(6)
  name = _messages.StringField(7)
  state = _messages.StringField(8)
  target = _messages.MessageField('TargetConfiguration', 9)
  update = _messages.MessageField('DeploymentUpdate', 10)
  updateTime = _messages.StringField(11)


class DeploymentUpdate(_messages.Message):
  """DeploymentUpdate message type.

  Fields:
    errors: [Output Only] List of all errors encountered while trying to enact
      the update.
    manifest: [Output Only] URL of the manifest representing the update
      configuration of this deployment.
  """

  errors = _messages.StringField(1, repeated=True)
  manifest = _messages.StringField(2)


class DeploymentmanagerDeploymentsDeleteRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsDeleteRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    project: The project ID for this request.
  """

  deployment = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class DeploymentmanagerDeploymentsGetRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsGetRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    project: The project ID for this request.
  """

  deployment = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class DeploymentmanagerDeploymentsInsertRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsInsertRequest object.

  Fields:
    deployment: A Deployment resource to be passed as the request body.
    project: The project ID for this request.
  """

  deployment = _messages.MessageField('Deployment', 1)
  project = _messages.StringField(2, required=True)


class DeploymentmanagerDeploymentsListRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: The project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)


class DeploymentmanagerDeploymentsPatchRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsPatchRequest object.

  Enums:
    CreatePolicyValueValuesEnum: Sets the policy to use for creating new
      resources.
    DeletePolicyValueValuesEnum: Sets the policy to use for deleting
      resources.
    UpdatePolicyValueValuesEnum: Sets the policy to use for updating
      resources.

  Fields:
    createPolicy: Sets the policy to use for creating new resources.
    deletePolicy: Sets the policy to use for deleting resources.
    deployment: The name of the deployment for this request.
    deploymentResource: A Deployment resource to be passed as the request
      body.
    project: The project ID for this request.
    updatePolicy: Sets the policy to use for updating resources.
  """

  class CreatePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for creating new resources.

    Values:
      ACQUIRE: <no description>
      CREATE_OR_ACQUIRE: <no description>
    """
    ACQUIRE = 0
    CREATE_OR_ACQUIRE = 1

  class DeletePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for deleting resources.

    Values:
      ABANDON: <no description>
      DELETE: <no description>
    """
    ABANDON = 0
    DELETE = 1

  class UpdatePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for updating resources.

    Values:
      PATCH: <no description>
      UPDATE: <no description>
    """
    PATCH = 0
    UPDATE = 1

  createPolicy = _messages.EnumField('CreatePolicyValueValuesEnum', 1, default=u'CREATE_OR_ACQUIRE')
  deletePolicy = _messages.EnumField('DeletePolicyValueValuesEnum', 2, default=u'DELETE')
  deployment = _messages.StringField(3, required=True)
  deploymentResource = _messages.MessageField('Deployment', 4)
  project = _messages.StringField(5, required=True)
  updatePolicy = _messages.EnumField('UpdatePolicyValueValuesEnum', 6, default=u'PATCH')


class DeploymentmanagerDeploymentsUpdateRequest(_messages.Message):
  """A DeploymentmanagerDeploymentsUpdateRequest object.

  Enums:
    CreatePolicyValueValuesEnum: Sets the policy to use for creating new
      resources.
    DeletePolicyValueValuesEnum: Sets the policy to use for deleting
      resources.
    UpdatePolicyValueValuesEnum: Sets the policy to use for updating
      resources.

  Fields:
    createPolicy: Sets the policy to use for creating new resources.
    deletePolicy: Sets the policy to use for deleting resources.
    deployment: The name of the deployment for this request.
    deploymentResource: A Deployment resource to be passed as the request
      body.
    project: The project ID for this request.
    updatePolicy: Sets the policy to use for updating resources.
  """

  class CreatePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for creating new resources.

    Values:
      ACQUIRE: <no description>
      CREATE_OR_ACQUIRE: <no description>
    """
    ACQUIRE = 0
    CREATE_OR_ACQUIRE = 1

  class DeletePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for deleting resources.

    Values:
      ABANDON: <no description>
      DELETE: <no description>
    """
    ABANDON = 0
    DELETE = 1

  class UpdatePolicyValueValuesEnum(_messages.Enum):
    """Sets the policy to use for updating resources.

    Values:
      PATCH: <no description>
      UPDATE: <no description>
    """
    PATCH = 0
    UPDATE = 1

  createPolicy = _messages.EnumField('CreatePolicyValueValuesEnum', 1, default=u'CREATE_OR_ACQUIRE')
  deletePolicy = _messages.EnumField('DeletePolicyValueValuesEnum', 2, default=u'DELETE')
  deployment = _messages.StringField(3, required=True)
  deploymentResource = _messages.MessageField('Deployment', 4)
  project = _messages.StringField(5, required=True)
  updatePolicy = _messages.EnumField('UpdatePolicyValueValuesEnum', 6, default=u'PATCH')


class DeploymentmanagerManifestsGetRequest(_messages.Message):
  """A DeploymentmanagerManifestsGetRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    manifest: The name of the manifest for this request.
    project: The project ID for this request.
  """

  deployment = _messages.StringField(1, required=True)
  manifest = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DeploymentmanagerManifestsListRequest(_messages.Message):
  """A DeploymentmanagerManifestsListRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: The project ID for this request.
  """

  deployment = _messages.StringField(1, required=True)
  filter = _messages.StringField(2)
  maxResults = _messages.IntegerField(3, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class DeploymentmanagerOperationsGetRequest(_messages.Message):
  """A DeploymentmanagerOperationsGetRequest object.

  Fields:
    operation: The name of the operation for this request.
    project: The project ID for this request.
  """

  operation = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class DeploymentmanagerOperationsListRequest(_messages.Message):
  """A DeploymentmanagerOperationsListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: The project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)


class DeploymentmanagerResourcesGetRequest(_messages.Message):
  """A DeploymentmanagerResourcesGetRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    project: The project ID for this request.
    resource: The name of the resource for this request.
  """

  deployment = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  resource = _messages.StringField(3, required=True)


class DeploymentmanagerResourcesListRequest(_messages.Message):
  """A DeploymentmanagerResourcesListRequest object.

  Fields:
    deployment: The name of the deployment for this request.
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: The project ID for this request.
  """

  deployment = _messages.StringField(1, required=True)
  filter = _messages.StringField(2)
  maxResults = _messages.IntegerField(3, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class DeploymentmanagerTypesListRequest(_messages.Message):
  """A DeploymentmanagerTypesListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: The project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)


class DeploymentsListResponse(_messages.Message):
  """A response containing a partial list of deployments and a page token used
  to build the next request if the request has been truncated.

  Fields:
    deployments: [Output Only] The deployments contained in this response.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
  """

  deployments = _messages.MessageField('Deployment', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ImportFile(_messages.Message):
  """ImportFile message type.

  Fields:
    content: The contents of the file.
    name: The name of the file.
  """

  content = _messages.StringField(1)
  name = _messages.StringField(2)


class Manifest(_messages.Message):
  """Manifest message type.

  Fields:
    config: [Output Only] The YAML configuration for this manifest.
    evaluatedConfig: [Output Only] The fully-expanded configuration file,
      including any templates and references.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    imports: [Output Only] The imported files for this manifest.
    insertTime: [Output Only] Timestamp when the manifest was created, in
      RFC3339 text format.
    layout: [Output Only] The YAML layout for this manifest.
    name: [Output Only] The name of the manifest.
    selfLink: [Output Only] Self link for the manifest.
  """

  config = _messages.StringField(1)
  evaluatedConfig = _messages.StringField(2)
  id = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  imports = _messages.MessageField('ImportFile', 4, repeated=True)
  insertTime = _messages.StringField(5)
  layout = _messages.StringField(6)
  name = _messages.StringField(7)
  selfLink = _messages.StringField(8)


class ManifestsListResponse(_messages.Message):
  """A response containing a partial list of manifests and a page token used
  to build the next request if the request has been truncated.

  Fields:
    manifests: [Output Only] Manifests contained in this list response.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
  """

  manifests = _messages.MessageField('Manifest', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Operation(_messages.Message):
  """An operation resource, used to manage asynchronous API requests.

  Messages:
    ErrorValue: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    WarningsValueListEntry: A WarningsValueListEntry object.

  Fields:
    clientOperationId: [Output Only] An optional identifier specified by the
      client when the mutation was initiated. Must be unique for all operation
      resources in the project.
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    endTime: [Output Only] The time that this operation was completed. This is
      in RFC3339 text format.
    error: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    httpErrorMessage: [Output Only] If the operation fails, this field
      contains the HTTP error message that was returned, such as NOT FOUND.
    httpErrorStatusCode: [Output Only] If the operation fails, this field
      contains the HTTP error message that was returned, such as 404.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    insertTime: [Output Only] The time that this operation was requested. This
      is in RFC3339 text format.
    kind: [Output Only] Type of the resource. Always compute#Operation for
      Operation resources.
    name: [Output Only] Name of the resource.
    operationType: [Output Only] Type of the operation, such as insert,
      update, and delete.
    progress: [Output Only] An optional progress indicator that ranges from 0
      to 100. There is no requirement that this be linear or support any
      granularity of operations. This should not be used to guess at when the
      operation will be complete. This number should monotonically increase as
      the operation progresses.
    region: [Output Only] URL of the region where the operation resides. Only
      applicable for regional resources.
    selfLink: [Output Only] Server defined URL for the resource.
    startTime: [Output Only] The time that this operation was started by the
      server. This is in RFC3339 text format.
    status: [Output Only] Status of the operation. Can be one of the
      following: PENDING, RUNNING, or DONE.
    statusMessage: [Output Only] An optional textual description of the
      current status of the operation.
    targetId: [Output Only] Unique target ID which identifies a particular
      incarnation of the target.
    targetLink: [Output Only] URL of the resource the operation is mutating.
    user: [Output Only] User who requested the operation, for example:
      user@example.com.
    warnings: [Output Only] If warning messages are generated during
      processing of the operation, this field will be populated.
    zone: [Output Only] URL of the zone where the operation resides.
  """

  class ErrorValue(_messages.Message):
    """[Output Only] If errors are generated during processing of the
    operation, this field will be populated.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request which
          caused the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class WarningsValueListEntry(_messages.Message):
    """A WarningsValueListEntry object.

    Messages:
      DataValueListEntry: A DataValueListEntry object.

    Fields:
      code: [Output Only] The warning type identifier for this warning.
      data: [Output Only] Metadata for this warning in key: value format.
      message: [Output Only] Optional human-readable details for this warning.
    """

    class DataValueListEntry(_messages.Message):
      """A DataValueListEntry object.

      Fields:
        key: [Output Only] A key for the warning data.
        value: [Output Only] A warning data value corresponding to the key.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    code = _messages.StringField(1)
    data = _messages.MessageField('DataValueListEntry', 2, repeated=True)
    message = _messages.StringField(3)

  clientOperationId = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  endTime = _messages.StringField(3)
  error = _messages.MessageField('ErrorValue', 4)
  httpErrorMessage = _messages.StringField(5)
  httpErrorStatusCode = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  id = _messages.IntegerField(7, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(8)
  kind = _messages.StringField(9, default=u'deploymentmanager#operation')
  name = _messages.StringField(10)
  operationType = _messages.StringField(11)
  progress = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  region = _messages.StringField(13)
  selfLink = _messages.StringField(14)
  startTime = _messages.StringField(15)
  status = _messages.StringField(16)
  statusMessage = _messages.StringField(17)
  targetId = _messages.IntegerField(18, variant=_messages.Variant.UINT64)
  targetLink = _messages.StringField(19)
  user = _messages.StringField(20)
  warnings = _messages.MessageField('WarningsValueListEntry', 21, repeated=True)
  zone = _messages.StringField(22)


class OperationsListResponse(_messages.Message):
  """A response containing a partial list of operations and a page token used
  to build the next request if the request has been truncated.

  Fields:
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
    operations: [Output Only] Operations contained in this list response.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Resource(_messages.Message):
  """Resource message type.

  Fields:
    finalProperties: [Output Only] The evaluated properties of the resource
      with references expanded. Returned as serialized YAML.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    insertTime: [Output Only] Timestamp when the resource was created or
      acquired, in RFC3339 text format .
    manifest: [Output Only] URL of the manifest representing the current
      configuration of this resource.
    name: [Output Only] The name of the resource as it appears in the YAML
      config.
    properties: [Output Only] The current properties of the resource before
      any references have been filled in. Returned as serialized YAML.
    type: [Output Only] The type of the resource, for example
      ?compute.v1.instance?, or ?replicaPools.v1beta2.instanceGroupManager?
    update: [Output Only] If Deployment Manager is currently updating or
      previewing an update to this resource, the updated configuration appears
      here.
    updateTime: [Output Only] Timestamp when the resource was updated, in
      RFC3339 text format .
    url: [Output Only] The URL of the actual resource.
  """

  finalProperties = _messages.StringField(1)
  id = _messages.IntegerField(2, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(3)
  manifest = _messages.StringField(4)
  name = _messages.StringField(5)
  properties = _messages.StringField(6)
  type = _messages.StringField(7)
  update = _messages.MessageField('ResourceUpdate', 8)
  updateTime = _messages.StringField(9)
  url = _messages.StringField(10)


class ResourceUpdate(_messages.Message):
  """ResourceUpdate message type.

  Fields:
    errors: [Output Only] List of all errors encountered while trying to enact
      update.intent.
    finalProperties: [Output Only] The expanded properties of the resource
      with reference values expanded. Returned as serialized YAML.
    intent: [Output Only] The intent of the resource, PREVIEW, UPDATE, or
      CANCEL.
    manifest: [Output Only] URL of the manifest representing the update
      configuration of this resource.
    properties: [Output Only] The set of updated properties for this resource,
      before references are expanded. Returned as serialized YAML.
    state: [Output Only] The state of the resource.
  """

  errors = _messages.StringField(1, repeated=True)
  finalProperties = _messages.StringField(2)
  intent = _messages.StringField(3)
  manifest = _messages.StringField(4)
  properties = _messages.StringField(5)
  state = _messages.StringField(6)


class ResourcesListResponse(_messages.Message):
  """A response containing a partial list of resources and a page token used
  to build the next request if the request has been truncated.

  Fields:
    nextPageToken: A token used to continue a truncated list request.
    resources: Resources contained in this list response.
  """

  nextPageToken = _messages.StringField(1)
  resources = _messages.MessageField('Resource', 2, repeated=True)


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


class TargetConfiguration(_messages.Message):
  """TargetConfiguration message type.

  Fields:
    config: The configuration to use for this deployment.
    imports: Specifies any files to import for this configuration. This can be
      used to import templates or other files. For example, you might import a
      text file in order to use the file in a template.
  """

  config = _messages.StringField(1)
  imports = _messages.MessageField('ImportFile', 2, repeated=True)


class Type(_messages.Message):
  """A resource type supported by Deployment Manager.

  Fields:
    name: Name of the type.
  """

  name = _messages.StringField(1)


class TypesListResponse(_messages.Message):
  """A response that returns all Types supported by Deployment Manager

  Fields:
    nextPageToken: A token used to continue a truncated list request.
    types: [Output Only] A list of resource types supported by Deployment
      Manager.
  """

  nextPageToken = _messages.StringField(1)
  types = _messages.MessageField('Type', 2, repeated=True)


