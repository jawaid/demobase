"""Generated client library for testing version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.testing.v1 import testing_v1_messages as messages


class TestingV1(base_api.BaseApiClient):
  """Generated client library for service testing version v1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'testing'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'TestingV1'
  _URL_VERSION = u'v1'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new testing handle."""
    url = url or u'https://testing.googleapis.com/'
    super(TestingV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_devices = self.ProjectsDevicesService(self)
    self.projects_testMatrices = self.ProjectsTestMatricesService(self)
    self.projects = self.ProjectsService(self)
    self.testEnvironmentCatalog = self.TestEnvironmentCatalogService(self)

  class ProjectsDevicesService(base_api.BaseApiService):
    """Service class for the projects_devices resource."""

    _NAME = u'projects_devices'

    def __init__(self, client):
      super(TestingV1.ProjectsDevicesService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'testing.projects.devices.create',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[u'sshPublicKey'],
              relative_path=u'v1/projects/{projectId}/devices',
              request_field=u'device',
              request_type_name=u'TestingProjectsDevicesCreateRequest',
              response_type_name=u'Device',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'testing.projects.devices.delete',
              ordered_params=[u'projectId', u'deviceId'],
              path_params=[u'deviceId', u'projectId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/devices/{deviceId}',
              request_field='',
              request_type_name=u'TestingProjectsDevicesDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'testing.projects.devices.get',
              ordered_params=[u'projectId', u'deviceId'],
              path_params=[u'deviceId', u'projectId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/devices/{deviceId}',
              request_field='',
              request_type_name=u'TestingProjectsDevicesGetRequest',
              response_type_name=u'Device',
              supports_download=False,
          ),
          'Keepalive': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'testing.projects.devices.keepalive',
              ordered_params=[u'projectId', u'deviceId'],
              path_params=[u'deviceId', u'projectId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/devices/{deviceId}/keepalive',
              request_field='',
              request_type_name=u'TestingProjectsDevicesKeepaliveRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'testing.projects.devices.list',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/projects/{projectId}/devices',
              request_field='',
              request_type_name=u'TestingProjectsDevicesListRequest',
              response_type_name=u'ListDevicesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a new GCE Android device.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the device type or project does not exist

      Args:
        request: (TestingProjectsDevicesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a GCE Android device instance.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the project does not exist

      Args:
        request: (TestingProjectsDevicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the GCE Android device.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the device type or project does not exist

      Args:
        request: (TestingProjectsDevicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Keepalive(self, request, global_params=None):
      """Issues a keep-alive to a GCE Android device instance.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the project does not exist

      Args:
        request: (TestingProjectsDevicesKeepaliveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Keepalive')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists all the current devices.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the project does not exist

      Args:
        request: (TestingProjectsDevicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDevicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsTestMatricesService(base_api.BaseApiService):
    """Service class for the projects_testMatrices resource."""

    _NAME = u'projects_testMatrices'

    def __init__(self, client):
      super(TestingV1.ProjectsTestMatricesService, self).__init__(client)
      self._method_configs = {
          'Cancel': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'testing.projects.testMatrices.cancel',
              ordered_params=[u'projectId', u'testMatrixId'],
              path_params=[u'projectId', u'testMatrixId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel',
              request_field='',
              request_type_name=u'TestingProjectsTestMatricesCancelRequest',
              response_type_name=u'CancelTestMatrixResponse',
              supports_download=False,
          ),
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'testing.projects.testMatrices.create',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/testMatrices',
              request_field=u'testMatrix',
              request_type_name=u'TestingProjectsTestMatricesCreateRequest',
              response_type_name=u'TestMatrix',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'testing.projects.testMatrices.delete',
              ordered_params=[u'projectId', u'testMatrixId'],
              path_params=[u'projectId', u'testMatrixId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/testMatrices/{testMatrixId}',
              request_field='',
              request_type_name=u'TestingProjectsTestMatricesDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'testing.projects.testMatrices.get',
              ordered_params=[u'projectId', u'testMatrixId'],
              path_params=[u'projectId', u'testMatrixId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/testMatrices/{testMatrixId}',
              request_field='',
              request_type_name=u'TestingProjectsTestMatricesGetRequest',
              response_type_name=u'TestMatrix',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'testing.projects.testMatrices.list',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1/projects/{projectId}/testMatrices',
              request_field='',
              request_type_name=u'TestingProjectsTestMatricesListRequest',
              response_type_name=u'ListTestMatricesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Cancels unfinished test executions in a test matrix.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the Test Matrix does not exist

      Args:
        request: (TestingProjectsTestMatricesCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CancelTestMatrixResponse) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Create(self, request, global_params=None):
      """Request to run a matrix of tests according to the given specifications.
Unsupported environments will be returned in the state UNSUPPORTED.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project
- INVALID_ARGUMENT - if the request is malformed

      Args:
        request: (TestingProjectsTestMatricesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestMatrix) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Delete all record of a test matrix plus any associated test executions.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the Test Matrix does not exist

      Args:
        request: (TestingProjectsTestMatricesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Check the status of a test matrix.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the Test Matrix does not exist

      Args:
        request: (TestingProjectsTestMatricesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestMatrix) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """List test matrices.
The matrices are returned in the order of newest first by submit time.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed

      Args:
        request: (TestingProjectsTestMatricesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTestMatricesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(TestingV1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }

  class TestEnvironmentCatalogService(base_api.BaseApiService):
    """Service class for the testEnvironmentCatalog resource."""

    _NAME = u'testEnvironmentCatalog'

    def __init__(self, client):
      super(TestingV1.TestEnvironmentCatalogService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'testing.testEnvironmentCatalog.get',
              ordered_params=[u'environmentType'],
              path_params=[u'environmentType'],
              query_params=[],
              relative_path=u'v1/testEnvironmentCatalog/{environmentType}',
              request_field='',
              request_type_name=u'TestingTestEnvironmentCatalogGetRequest',
              response_type_name=u'TestEnvironmentCatalog',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Get the catalog of supported test environments.

May return any of the following canonical error codes:

- INVALID_ARGUMENT - if the request is malformed
- NOT_FOUND - if the environment type does not exist
- INTERNAL - if an internal error occurred

      Args:
        request: (TestingTestEnvironmentCatalogGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestEnvironmentCatalog) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)
