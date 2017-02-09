# coding: utf-8

"""
    Fitmarket

    Mali broj ljudi - donori - dijele dnevna mjerenja svoje težine.  Iz dnevne težine jednog donora određujemo vrijednosti dviju dionica:  - dionica X ima vrijednost koja odgovara težini donora na taj dan. - inverzna dionica ~X ima vrijednost (150 kg - X).  Primjetimo da:  - kako X raste, ~X pada. - X + ~X = 150 kg  Svaki igrač počinje igru sa 10,000 kg raspoloživog novca. Igrač koristi taj novac za trgovanje dionicama. Ukupna vrijednost igrača je zbroj rapoloživog novca i aktualne vrijednosti svih dionica koje posjeduje. Cilj igre je maksimizirati ukupnu vrijednost dobrim predviđanjem kretanja vrijednosti dionica. Na primjer, u prvom danu igrac kupi 125 dionica \"X\" za 80 kg. U drugom danu, dionica naraste na 82 kg. Ako igrac proda sve dionice \"X\", zaradio je 2 kg * 125 = 250 kg!  Igra ne dopušta donoru da trguje vlastitim dionicama. 

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class StatusApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def actual_state_get(self, **kwargs):
        """
        Dohvaca JSON sa trenutnim cijenama svih dionica.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.actual_state_get(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: list[Stock]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.actual_state_get_with_http_info(**kwargs)
        else:
            (data) = self.actual_state_get_with_http_info(**kwargs)
            return data

    def actual_state_get_with_http_info(self, **kwargs):
        """
        Dohvaca JSON sa trenutnim cijenama svih dionica.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.actual_state_get_with_http_info(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: list[Stock]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method actual_state_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `actual_state_get`")


        collection_formats = {}

        resource_path = '/actual_state'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'token' in params:
            query_params['token'] = params['token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Stock]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def mystate_get(self, **kwargs):
        """
        Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mystate_get(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mystate_get_with_http_info(**kwargs)
        else:
            (data) = self.mystate_get_with_http_info(**kwargs)
            return data

    def mystate_get_with_http_info(self, **kwargs):
        """
        Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mystate_get_with_http_info(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mystate_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `mystate_get`")


        collection_formats = {}

        resource_path = '/mystate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'token' in params:
            query_params['token'] = params['token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Status',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def plot_txt_get(self, **kwargs):
        """
        Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.plot_txt_get(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.plot_txt_get_with_http_info(**kwargs)
        else:
            (data) = self.plot_txt_get_with_http_info(**kwargs)
            return data

    def plot_txt_get_with_http_info(self, **kwargs):
        """
        Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.plot_txt_get_with_http_info(token=token_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: Autorizacijski token (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method plot_txt_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `plot_txt_get`")


        collection_formats = {}

        resource_path = '/plot_txt'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'token' in params:
            query_params['token'] = params['token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/csv'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='file',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
