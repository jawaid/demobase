"""Generated message classes for container version v1beta2.

The Google Container Engine API is used for building and managing container
based applications, powered by the open source Kubernetes technology.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages


package = 'container'


class Cluster(_messages.Message):
  """A Cluster object.

  Enums:
    StatusValueValuesEnum: [Output only] The current status of this cluster.

  Fields:
    containerIpv4Cidr: The IP address range of the container pods in this
      cluster, in  CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one
      automatically chosen or specify a /14 block in 10.0.0.0/8 or
      172.16.0.0/12.
    creationTimestamp: [Output only] The time the cluster was created, in
      RFC3339 text format.
    currentMasterVersion: [Output only] The current software version of the
      master endpoint.
    currentNodeVersion: [Output only] The current version of the node software
      components. If they are currently at different versions because they're
      in the process of being upgraded, this reflects the minimum version of
      any of them.
    description: An optional description of this cluster.
    enableCloudLogging: Whether logs from the cluster should be made available
      via the Google Cloud Logging service. This includes both logs from your
      applications running in the cluster as well as logs from the Kubernetes
      components themselves.
    enableCloudMonitoring: Whether metrics from the cluster should be made
      available via the Google Cloud Monitoring service.
    endpoint: [Output only] The IP address of this cluster's Kubernetes master
      endpoint. The endpoint can be accessed from the internet at
      https://username:password@endpoint/.  See the masterAuth property of
      this resource for username and password information.
    initialClusterVersion: [Output only] The software version of Kubernetes
      master and kubelets used in the cluster when it was first created. The
      version can be upgraded over time.
    masterAuth: The authentication information for accessing the master.
    name: The name of this cluster. The name must be unique within this
      project and zone, and can be up to 40 characters with the following
      restrictions:   - Lowercase letters, numbers, and hyphens only. - Must
      start with a letter. - Must end with a number or a letter.
    network: The name of the Google Compute Engine network to which the
      cluster is connected.
    nodeConfig: Parameters used in creating the cluster's nodes. See the
      descriptions of the child properties of nodeConfig.
    nodeIpv4CidrSize: [Output only] The size of the address space on each node
      for hosting containers. This is provisioned from within the
      container_ipv4_cidr range.
    numNodes: The number of nodes to create in this cluster. You must ensure
      that your Compute Engine resource quota is sufficient for this number of
      instances. You must also have available firewall and routes quota.
    selfLink: [Output only] Server-defined URL for the resource.
    servicesIpv4Cidr: [Output only] The IP address range of the Kubernetes
      services in this cluster, in  CIDR notation (e.g. 1.2.3.4/29). Service
      addresses are typically put in the last /16 from the container CIDR.
    status: [Output only] The current status of this cluster.
    statusMessage: [Output only] Additional information about the current
      status of this cluster, if available.
    zone: [Output only] The name of the Google Compute Engine zone in which
      the cluster resides.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """[Output only] The current status of this cluster.

    Values:
      error: <no description>
      provisioning: <no description>
      reconciling: <no description>
      running: <no description>
      stopping: <no description>
    """
    error = 0
    provisioning = 1
    reconciling = 2
    running = 3
    stopping = 4

  containerIpv4Cidr = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  currentMasterVersion = _messages.StringField(3)
  currentNodeVersion = _messages.StringField(4)
  description = _messages.StringField(5)
  enableCloudLogging = _messages.BooleanField(6)
  enableCloudMonitoring = _messages.BooleanField(7)
  endpoint = _messages.StringField(8)
  initialClusterVersion = _messages.StringField(9)
  masterAuth = _messages.MessageField('MasterAuth', 10)
  name = _messages.StringField(11)
  network = _messages.StringField(12)
  nodeConfig = _messages.MessageField('NodeConfig', 13)
  nodeIpv4CidrSize = _messages.IntegerField(14, variant=_messages.Variant.INT32)
  numNodes = _messages.IntegerField(15, variant=_messages.Variant.INT32)
  selfLink = _messages.StringField(16)
  servicesIpv4Cidr = _messages.StringField(17)
  status = _messages.EnumField('StatusValueValuesEnum', 18)
  statusMessage = _messages.StringField(19)
  zone = _messages.StringField(20)


class ClusterUpdate(_messages.Message):
  """A ClusterUpdate object.

  Fields:
    desiredMasterVersion: The Kubernetes version to change the master to
      (typically an upgrade).
    desiredNodeVersion: The Kubernetes version to change the nodes to
      (typically an upgrade).
  """

  desiredMasterVersion = _messages.MessageField('ClusterVersion', 1)
  desiredNodeVersion = _messages.MessageField('ClusterVersion', 2)


class ClusterVersion(_messages.Message):
  """A ClusterVersion object.

  Fields:
    clusterVersion: The requested version. Omit to request the latest version
      offered by the server.
  """

  clusterVersion = _messages.StringField(1)


class ContainerProjectsClustersListRequest(_messages.Message):
  """A ContainerProjectsClustersListRequest object.

  Fields:
    projectId: The Google Developers Console project ID or  project number.
  """

  projectId = _messages.StringField(1, required=True)


class ContainerProjectsOperationsListRequest(_messages.Message):
  """A ContainerProjectsOperationsListRequest object.

  Fields:
    projectId: The Google Developers Console project ID or  project number.
  """

  projectId = _messages.StringField(1, required=True)


class ContainerProjectsZonesClustersCreateRequest(_messages.Message):
  """A ContainerProjectsZonesClustersCreateRequest object.

  Fields:
    createClusterRequest: A CreateClusterRequest resource to be passed as the
      request body.
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone in which the cluster
      resides.
  """

  createClusterRequest = _messages.MessageField('CreateClusterRequest', 1)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersDeleteRequest(_messages.Message):
  """A ContainerProjectsZonesClustersDeleteRequest object.

  Fields:
    clusterId: The name of the cluster to delete.
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone in which the cluster
      resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersGetRequest(_messages.Message):
  """A ContainerProjectsZonesClustersGetRequest object.

  Fields:
    clusterId: The name of the cluster to retrieve.
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone in which the cluster
      resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesClustersListRequest(_messages.Message):
  """A ContainerProjectsZonesClustersListRequest object.

  Fields:
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone in which the cluster
      resides.
  """

  projectId = _messages.StringField(1, required=True)
  zone = _messages.StringField(2, required=True)


class ContainerProjectsZonesClustersUpdateRequest(_messages.Message):
  """A ContainerProjectsZonesClustersUpdateRequest object.

  Fields:
    clusterId: The name of the cluster to upgrade.
    projectId: The Google Developers Console project ID or  project number.
    updateClusterRequest: A UpdateClusterRequest resource to be passed as the
      request body.
    zone: The name of the Google Compute Engine zone in which the cluster
      resides.
  """

  clusterId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  updateClusterRequest = _messages.MessageField('UpdateClusterRequest', 3)
  zone = _messages.StringField(4, required=True)


class ContainerProjectsZonesOperationsGetRequest(_messages.Message):
  """A ContainerProjectsZonesOperationsGetRequest object.

  Fields:
    operationId: The server-assigned name of the operation.
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone in which the operation
      resides. This is always the same zone as the cluster with which the
      operation is associated.
  """

  operationId = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ContainerProjectsZonesOperationsListRequest(_messages.Message):
  """A ContainerProjectsZonesOperationsListRequest object.

  Fields:
    projectId: The Google Developers Console project ID or  project number.
    zone: The name of the Google Compute Engine zone to return operations for.
  """

  projectId = _messages.StringField(1, required=True)
  zone = _messages.StringField(2, required=True)


class CreateClusterRequest(_messages.Message):
  """A CreateClusterRequest object.

  Fields:
    cluster: A cluster resource.
  """

  cluster = _messages.MessageField('Cluster', 1)


class ListAggregatedClustersResponse(_messages.Message):
  """A ListAggregatedClustersResponse object.

  Fields:
    clusters: A list of clusters in the project, across all zones.
  """

  clusters = _messages.MessageField('Cluster', 1, repeated=True)


class ListAggregatedOperationsResponse(_messages.Message):
  """A ListAggregatedOperationsResponse object.

  Fields:
    operations: A list of operations in the project, across all zones.
  """

  operations = _messages.MessageField('Operation', 1, repeated=True)


class ListClustersResponse(_messages.Message):
  """A ListClustersResponse object.

  Fields:
    clusters: A list of clusters in the project in the specified zone.
  """

  clusters = _messages.MessageField('Cluster', 1, repeated=True)


class ListOperationsResponse(_messages.Message):
  """A ListOperationsResponse object.

  Fields:
    operations: A list of operations in the project in the specified zone.
  """

  operations = _messages.MessageField('Operation', 1, repeated=True)


class MasterAuth(_messages.Message):
  """The authentication information for accessing the master endpoint.
  Authentication is done using HTTP basic authentication.

  Fields:
    password: The password to use for HTTP basic authentication when accessing
      the Kubernetes master endpoint. Because the master endpoint is open to
      the internet, you should create a strong password.
    user: The username to use for HTTP basic authentication when accessing the
      Kubernetes master endpoint.
  """

  password = _messages.StringField(1)
  user = _messages.StringField(2)


class NodeConfig(_messages.Message):
  """A NodeConfig object.

  Fields:
    diskSizeGb: Size of the disk attached to each node, specified in GB. The
      smallest allowed disk size is 10GB, and the default is 100GB.
    machineType: The name of a Google Compute Engine machine type (e.g.
      n1-standard-1).  If unspecified, the default machine type is
      n1-standard-1.
    scopes: The optional set of Google API scopes to be made available on all
      of the node VMs under the "default" service account. In addition to the
      scopes specified, the following scopes will always be added to ensure
      the correct functioning of the cluster:   -
      https://www.googleapis.com/auth/compute, -
      https://www.googleapis.com/auth/devstorage.read_only
  """

  diskSizeGb = _messages.IntegerField(1)
  machineType = _messages.StringField(2)
  scopes = _messages.StringField(3, repeated=True)


class Operation(_messages.Message):
  """Defines the operation resource. All fields are output only.

  Enums:
    OperationTypeValueValuesEnum: The operation type.
    StatusValueValuesEnum: The current status of the operation.

  Fields:
    name: The server-assigned ID for the operation.
    operationType: The operation type.
    selfLink: Server-defined URL for the resource.
    status: The current status of the operation.
    statusMessage: If an error has occurred, a textual description of the
      error.
    targetLink: Server-defined URL for the target of the operation.
    zone: The name of the Google Compute Engine zone in which the operation is
      taking place.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    """The operation type.

    Values:
      createCluster: <no description>
      deleteCluster: <no description>
      upgradeMaster: <no description>
      upgradeNodes: <no description>
    """
    createCluster = 0
    deleteCluster = 1
    upgradeMaster = 2
    upgradeNodes = 3

  class StatusValueValuesEnum(_messages.Enum):
    """The current status of the operation.

    Values:
      done: <no description>
      pending: <no description>
      running: <no description>
    """
    done = 0
    pending = 1
    running = 2

  name = _messages.StringField(1)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 2)
  selfLink = _messages.StringField(3)
  status = _messages.EnumField('StatusValueValuesEnum', 4)
  statusMessage = _messages.StringField(5)
  targetLink = _messages.StringField(6)
  zone = _messages.StringField(7)


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


class UpdateClusterRequest(_messages.Message):
  """A UpdateClusterRequest object.

  Fields:
    update: A description of the update.
  """

  update = _messages.MessageField('ClusterUpdate', 1)


