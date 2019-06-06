# coding: utf-8

"""
    TrackingAPI

    API for retrieving tracking data and changing settings on LightBug & RemoteThings tracking devices  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lb_tracking_api.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_login(self, credentials, **kwargs):  # noqa: E501
        """Login a user with username/email and password.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login(credentials, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Credentials credentials: Body (JSON) (required)
        :param str include: Related objects to include in the response. See the description of return value for more details.
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_login_with_http_info(credentials, **kwargs)  # noqa: E501
        else:
            (data) = self.user_login_with_http_info(credentials, **kwargs)  # noqa: E501
            return data

    def user_login_with_http_info(self, credentials, **kwargs):  # noqa: E501
        """Login a user with username/email and password.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login_with_http_info(credentials, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Credentials credentials: Body (JSON) (required)
        :param str include: Related objects to include in the response. See the description of return value for more details.
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credentials', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credentials' is set
        if ('credentials' not in params or
                params['credentials'] is None):
            raise ValueError("Missing the required parameter `credentials` when calling `user_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credentials' in params:
            body_params = params['credentials']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_create_geofences(self, id, **kwargs):  # noqa: E501
        """Creates a new instance in geofences of this model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_create_geofences(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param Geofence data: Body (JSON)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_create_geofences_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_create_geofences_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def user_prototype_create_geofences_with_http_info(self, id, **kwargs):  # noqa: E501
        """Creates a new instance in geofences of this model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_create_geofences_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param Geofence data: Body (JSON)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_create_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_create_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_delete_geofences(self, id, **kwargs):  # noqa: E501
        """Deletes all geofences of this model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_delete_geofences(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_delete_geofences_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_delete_geofences_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def user_prototype_delete_geofences_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes all geofences of this model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_delete_geofences_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_delete_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_delete_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_destroy_by_id_geofences(self, id, fk, **kwargs):  # noqa: E501
        """Delete a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_destroy_by_id_geofences(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_destroy_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_destroy_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
            return data

    def user_prototype_destroy_by_id_geofences_with_http_info(self, id, fk, **kwargs):  # noqa: E501
        """Delete a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_destroy_by_id_geofences_with_http_info(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_destroy_by_id_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_destroy_by_id_geofences`")  # noqa: E501
        # verify the required parameter 'fk' is set
        if ('fk' not in params or
                params['fk'] is None):
            raise ValueError("Missing the required parameter `fk` when calling `user_prototype_destroy_by_id_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'fk' in params:
            path_params['fk'] = params['fk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences/{fk}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_find_by_id_geofences(self, id, fk, **kwargs):  # noqa: E501
        """Find a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_find_by_id_geofences(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_find_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_find_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
            return data

    def user_prototype_find_by_id_geofences_with_http_info(self, id, fk, **kwargs):  # noqa: E501
        """Find a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_find_by_id_geofences_with_http_info(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_find_by_id_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_find_by_id_geofences`")  # noqa: E501
        # verify the required parameter 'fk' is set
        if ('fk' not in params or
                params['fk'] is None):
            raise ValueError("Missing the required parameter `fk` when calling `user_prototype_find_by_id_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'fk' in params:
            path_params['fk'] = params['fk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences/{fk}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_get_devices(self, id, **kwargs):  # noqa: E501
        """Queries devices of user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_devices(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param str filter: JSON Filter object
        :return: list[Device]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_get_devices_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_get_devices_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def user_prototype_get_devices_with_http_info(self, id, **kwargs):  # noqa: E501
        """Queries devices of user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_devices_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param str filter: JSON Filter object
        :return: list[Device]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_get_devices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_get_devices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Device]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_get_geofences(self, id, **kwargs):  # noqa: E501
        """Queries geofences of user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_geofences(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param str filter: JSON Filter object
        :return: list[Geofence]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_get_geofences_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_get_geofences_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def user_prototype_get_geofences_with_http_info(self, id, **kwargs):  # noqa: E501
        """Queries geofences of user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_geofences_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param str filter: JSON Filter object
        :return: list[Geofence]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_get_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_get_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Geofence]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_get_mqtt_credentials(self, id, **kwargs):  # noqa: E501
        """user_prototype_get_mqtt_credentials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_mqtt_credentials(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_get_mqtt_credentials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_get_mqtt_credentials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def user_prototype_get_mqtt_credentials_with_http_info(self, id, **kwargs):  # noqa: E501
        """user_prototype_get_mqtt_credentials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_get_mqtt_credentials_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_get_mqtt_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_get_mqtt_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/getMqttCredentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_prototype_update_by_id_geofences(self, id, fk, **kwargs):  # noqa: E501
        """Update a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_update_by_id_geofences(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :param Geofence data: Body (JSON)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_prototype_update_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
        else:
            (data) = self.user_prototype_update_by_id_geofences_with_http_info(id, fk, **kwargs)  # noqa: E501
            return data

    def user_prototype_update_by_id_geofences_with_http_info(self, id, fk, **kwargs):  # noqa: E501
        """Update a related item by id for geofences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_prototype_update_by_id_geofences_with_http_info(id, fk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: user id (required)
        :param float fk: Foreign key for geofences (required)
        :param Geofence data: Body (JSON)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fk', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_prototype_update_by_id_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_prototype_update_by_id_geofences`")  # noqa: E501
        # verify the required parameter 'fk' is set
        if ('fk' not in params or
                params['fk'] is None):
            raise ValueError("Missing the required parameter `fk` when calling `user_prototype_update_by_id_geofences`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'fk' in params:
            path_params['fk'] = params['fk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/geofences/{fk}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)