# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentloop20260520 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-zhangjiakou': 'agentloop.cn-zhangjiakou.aliyuncs.com',
            'cn-shanghai': 'agentloop.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'agentloop.cn-hongkong.aliyuncs.com',
            'cn-hangzhou': 'agentloop.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'agentloop.cn-beijing.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('agentloop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_contexts_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.AddContextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddContextsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.memory_type):
            body['memoryType'] = request.memory_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddContexts',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_contexts_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.AddContextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddContextsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.items):
            body['items'] = request.items
        if not DaraCore.is_null(request.memory_type):
            body['memoryType'] = request.memory_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddContexts',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_contexts(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.AddContextsRequest,
    ) -> main_models.AddContextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_contexts_with_options(agent_space, context_store_name, request, headers, runtime)

    async def add_contexts_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.AddContextsRequest,
    ) -> main_models.AddContextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_contexts_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def add_dataset_data_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_array):
            body['dataArray'] = request.data_array
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetData',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/rows',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dataset_data_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_array):
            body['dataArray'] = request.data_array
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetData',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/rows',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dataset_data(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
    ) -> main_models.AddDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_dataset_data_with_options(agent_space, dataset_name, request, headers, runtime)

    async def add_dataset_data_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.AddDatasetDataRequest,
    ) -> main_models.AddDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_dataset_data_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def add_mem_0memories_with_options(
        self,
        request: main_models.AddMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMem0MemoriesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def add_mem_0memories_with_options_async(
        self,
        request: main_models.AddMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMem0MemoriesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def add_mem_0memories(
        self,
        request: main_models.AddMem0MemoriesRequest,
    ) -> main_models.AddMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_mem_0memories_with_options(request, headers, runtime)

    async def add_mem_0memories_async(
        self,
        request: main_models.AddMem0MemoriesRequest,
    ) -> main_models.AddMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_mem_0memories_with_options_async(request, headers, runtime)

    def count_trace_preview_with_options(
        self,
        agent_space: str,
        request: main_models.CountTracePreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountTracePreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CountTracePreview',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/trace-preview/count',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountTracePreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_trace_preview_with_options_async(
        self,
        agent_space: str,
        request: main_models.CountTracePreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountTracePreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CountTracePreview',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/trace-preview/count',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountTracePreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_trace_preview(
        self,
        agent_space: str,
        request: main_models.CountTracePreviewRequest,
    ) -> main_models.CountTracePreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.count_trace_preview_with_options(agent_space, request, headers, runtime)

    async def count_trace_preview_async(
        self,
        agent_space: str,
        request: main_models.CountTracePreviewRequest,
    ) -> main_models.CountTracePreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.count_trace_preview_with_options_async(agent_space, request, headers, runtime)

    def create_agent_space_with_options(
        self,
        request: main_models.CreateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.agent_space):
            body['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_space_with_options_async(
        self,
        request: main_models.CreateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.agent_space):
            body['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_space(
        self,
        request: main_models.CreateAgentSpaceRequest,
    ) -> main_models.CreateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_space_with_options(request, headers, runtime)

    async def create_agent_space_async(
        self,
        request: main_models.CreateAgentSpaceRequest,
    ) -> main_models.CreateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_space_with_options_async(request, headers, runtime)

    def create_annotation_template_with_options(
        self,
        agent_space: str,
        request: main_models.CreateAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.details):
            body['details'] = request.details
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.template_path):
            body['templatePath'] = request.template_path
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_annotation_template_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.details):
            body['details'] = request.details
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.template_path):
            body['templatePath'] = request.template_path
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_annotation_template(
        self,
        agent_space: str,
        request: main_models.CreateAnnotationTemplateRequest,
    ) -> main_models.CreateAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_annotation_template_with_options(agent_space, request, headers, runtime)

    async def create_annotation_template_async(
        self,
        agent_space: str,
        request: main_models.CreateAnnotationTemplateRequest,
    ) -> main_models.CreateAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_annotation_template_with_options_async(agent_space, request, headers, runtime)

    def create_context_store_with_options(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_store_name):
            body['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_context_store_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_store_name):
            body['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_context_store(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
    ) -> main_models.CreateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_context_store_with_options(agent_space, request, headers, runtime)

    async def create_context_store_async(
        self,
        agent_space: str,
        request: main_models.CreateContextStoreRequest,
    ) -> main_models.CreateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_context_store_with_options_async(agent_space, request, headers, runtime)

    def create_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_context_store_apikey_with_options(agent_space, context_store_name, request, headers, runtime)

    async def create_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.CreateContextStoreAPIKeyRequest,
    ) -> main_models.CreateContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_context_store_apikey_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def create_dataset_with_options(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dataset_with_options(agent_space, request, headers, runtime)

    async def create_dataset_async(
        self,
        agent_space: str,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dataset_with_options_async(agent_space, request, headers, runtime)

    def create_endpoint_connector_with_options(
        self,
        agent_space: str,
        request: main_models.CreateEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.credential):
            body['credential'] = request.credential
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            body['headers'] = request.headers
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_connector_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.credential):
            body['credential'] = request.credential
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            body['headers'] = request.headers
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint_connector(
        self,
        agent_space: str,
        request: main_models.CreateEndpointConnectorRequest,
    ) -> main_models.CreateEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_endpoint_connector_with_options(agent_space, request, headers, runtime)

    async def create_endpoint_connector_async(
        self,
        agent_space: str,
        request: main_models.CreateEndpointConnectorRequest,
    ) -> main_models.CreateEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_endpoint_connector_with_options_async(agent_space, request, headers, runtime)

    def create_evaluation_task_with_options(
        self,
        agent_space: str,
        request: main_models.CreateEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.data_type):
            body['dataType'] = request.data_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.run_strategies):
            body['runStrategies'] = request.run_strategies
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.task_mode):
            body['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_evaluation_task_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.data_type):
            body['dataType'] = request.data_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.run_strategies):
            body['runStrategies'] = request.run_strategies
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.task_mode):
            body['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_evaluation_task(
        self,
        agent_space: str,
        request: main_models.CreateEvaluationTaskRequest,
    ) -> main_models.CreateEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_evaluation_task_with_options(agent_space, request, headers, runtime)

    async def create_evaluation_task_async(
        self,
        agent_space: str,
        request: main_models.CreateEvaluationTaskRequest,
    ) -> main_models.CreateEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_evaluation_task_with_options_async(agent_space, request, headers, runtime)

    def create_evaluator_with_options(
        self,
        agent_space: str,
        request: main_models.CreateEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.annotations):
            body['annotations'] = request.annotations
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.metric_name):
            body['metricName'] = request.metric_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_evaluator_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.annotations):
            body['annotations'] = request.annotations
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.metric_name):
            body['metricName'] = request.metric_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_evaluator(
        self,
        agent_space: str,
        request: main_models.CreateEvaluatorRequest,
    ) -> main_models.CreateEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_evaluator_with_options(agent_space, request, headers, runtime)

    async def create_evaluator_async(
        self,
        agent_space: str,
        request: main_models.CreateEvaluatorRequest,
    ) -> main_models.CreateEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_evaluator_with_options_async(agent_space, request, headers, runtime)

    def create_evaluator_skill_with_options(
        self,
        name: str,
        request: main_models.CreateEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluatorSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_evaluator_skill_with_options_async(
        self,
        name: str,
        request: main_models.CreateEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEvaluatorSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_evaluator_skill(
        self,
        name: str,
        request: main_models.CreateEvaluatorSkillRequest,
    ) -> main_models.CreateEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_evaluator_skill_with_options(name, request, headers, runtime)

    async def create_evaluator_skill_async(
        self,
        name: str,
        request: main_models.CreateEvaluatorSkillRequest,
    ) -> main_models.CreateEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_evaluator_skill_with_options_async(name, request, headers, runtime)

    def create_experiment_plan_with_options(
        self,
        agent_space: str,
        request: main_models.CreateExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.query_sql):
            body['querySql'] = request.query_sql
        if not DaraCore.is_null(request.selected_item_ids):
            body['selectedItemIds'] = request.selected_item_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_plan_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.query_sql):
            body['querySql'] = request.query_sql
        if not DaraCore.is_null(request.selected_item_ids):
            body['selectedItemIds'] = request.selected_item_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_plan(
        self,
        agent_space: str,
        request: main_models.CreateExperimentPlanRequest,
    ) -> main_models.CreateExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experiment_plan_with_options(agent_space, request, headers, runtime)

    async def create_experiment_plan_async(
        self,
        agent_space: str,
        request: main_models.CreateExperimentPlanRequest,
    ) -> main_models.CreateExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experiment_plan_with_options_async(agent_space, request, headers, runtime)

    def create_experiment_task_with_options(
        self,
        agent_space: str,
        request: main_models.CreateExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source):
            body['dataSource'] = request.data_source
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiment_plan_id):
            body['experimentPlanId'] = request.experiment_plan_id
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_task_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreateExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source):
            body['dataSource'] = request.data_source
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiment_plan_id):
            body['experimentPlanId'] = request.experiment_plan_id
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_task(
        self,
        agent_space: str,
        request: main_models.CreateExperimentTaskRequest,
    ) -> main_models.CreateExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experiment_task_with_options(agent_space, request, headers, runtime)

    async def create_experiment_task_async(
        self,
        agent_space: str,
        request: main_models.CreateExperimentTaskRequest,
    ) -> main_models.CreateExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experiment_task_with_options_async(agent_space, request, headers, runtime)

    def create_pipeline_with_options(
        self,
        agent_space: str,
        request: main_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.pipeline_name):
            body['pipelineName'] = request.pipeline_name
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        agent_space: str,
        request: main_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.pipeline_name):
            body['pipelineName'] = request.pipeline_name
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        agent_space: str,
        request: main_models.CreatePipelineRequest,
    ) -> main_models.CreatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(agent_space, request, headers, runtime)

    async def create_pipeline_async(
        self,
        agent_space: str,
        request: main_models.CreatePipelineRequest,
    ) -> main_models.CreatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(agent_space, request, headers, runtime)

    def delete_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_cms_workspace):
            query['deleteCmsWorkspace'] = request.delete_cms_workspace
        if not DaraCore.is_null(request.delete_mse_namespace):
            query['deleteMseNamespace'] = request.delete_mse_namespace
        if not DaraCore.is_null(request.delete_sls_project):
            query['deleteSlsProject'] = request.delete_sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_cms_workspace):
            query['deleteCmsWorkspace'] = request.delete_cms_workspace
        if not DaraCore.is_null(request.delete_mse_namespace):
            query['deleteMseNamespace'] = request.delete_mse_namespace
        if not DaraCore.is_null(request.delete_sls_project):
            query['deleteSlsProject'] = request.delete_sls_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_space(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
    ) -> main_models.DeleteAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_space_with_options(agent_space, request, headers, runtime)

    async def delete_agent_space_async(
        self,
        agent_space: str,
        request: main_models.DeleteAgentSpaceRequest,
    ) -> main_models.DeleteAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_space_with_options_async(agent_space, request, headers, runtime)

    def delete_annotation_config_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_annotation_config_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_annotation_config(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteAnnotationConfigRequest,
    ) -> main_models.DeleteAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_annotation_config_with_options(agent_space, dataset_name, request, headers, runtime)

    async def delete_annotation_config_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteAnnotationConfigRequest,
    ) -> main_models.DeleteAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_annotation_config_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def delete_annotation_template_with_options(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.DeleteAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_annotation_template_with_options_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.DeleteAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_annotation_template(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.DeleteAnnotationTemplateRequest,
    ) -> main_models.DeleteAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_annotation_template_with_options(agent_space, template_id, request, headers, runtime)

    async def delete_annotation_template_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.DeleteAnnotationTemplateRequest,
    ) -> main_models.DeleteAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_annotation_template_with_options_async(agent_space, template_id, request, headers, runtime)

    def delete_context_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.DeleteContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_context_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.DeleteContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_context(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.DeleteContextRequest,
    ) -> main_models.DeleteContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_context_with_options(agent_space, context_store_name, context_id, request, headers, runtime)

    async def delete_context_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.DeleteContextRequest,
    ) -> main_models.DeleteContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_context_with_options_async(agent_space, context_store_name, context_id, request, headers, runtime)

    def delete_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
    ) -> main_models.DeleteContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def delete_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextStoreRequest,
    ) -> main_models.DeleteContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def delete_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_context_store_apikey_with_options(agent_space, context_store_name, name, request, headers, runtime)

    async def delete_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.DeleteContextStoreAPIKeyRequest,
    ) -> main_models.DeleteContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_context_store_apikey_with_options_async(agent_space, context_store_name, name, request, headers, runtime)

    def delete_contexts_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_ids):
            query['contextIds'] = request.context_ids
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContexts',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contexts_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContextsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_ids):
            query['contextIds'] = request.context_ids
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContexts',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contexts(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextsRequest,
    ) -> main_models.DeleteContextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_contexts_with_options(agent_space, context_store_name, request, headers, runtime)

    async def delete_contexts_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.DeleteContextsRequest,
    ) -> main_models.DeleteContextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_contexts_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def delete_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def delete_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def delete_endpoint_connector_with_options(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.DeleteEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointConnectorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_connector_with_options_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.DeleteEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointConnectorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint_connector(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.DeleteEndpointConnectorRequest,
    ) -> main_models.DeleteEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_endpoint_connector_with_options(agent_space, connector_id, request, headers, runtime)

    async def delete_endpoint_connector_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.DeleteEndpointConnectorRequest,
    ) -> main_models.DeleteEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_endpoint_connector_with_options_async(agent_space, connector_id, request, headers, runtime)

    def delete_evaluation_run_with_options(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.DeleteEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluationRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluationRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluation_run_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.DeleteEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluationRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluationRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluation_run(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.DeleteEvaluationRunRequest,
    ) -> main_models.DeleteEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_evaluation_run_with_options(agent_space, task_id, run_id, request, headers, runtime)

    async def delete_evaluation_run_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.DeleteEvaluationRunRequest,
    ) -> main_models.DeleteEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_evaluation_run_with_options_async(agent_space, task_id, run_id, request, headers, runtime)

    def delete_evaluation_task_with_options(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.DeleteEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluation_task_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.DeleteEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluation_task(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.DeleteEvaluationTaskRequest,
    ) -> main_models.DeleteEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_evaluation_task_with_options(agent_space, task_id, request, headers, runtime)

    async def delete_evaluation_task_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.DeleteEvaluationTaskRequest,
    ) -> main_models.DeleteEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_evaluation_task_with_options_async(agent_space, task_id, request, headers, runtime)

    def delete_evaluator_with_options(
        self,
        agent_space: str,
        name: str,
        request: main_models.DeleteEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluator_with_options_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.DeleteEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluator(
        self,
        agent_space: str,
        name: str,
        request: main_models.DeleteEvaluatorRequest,
    ) -> main_models.DeleteEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_evaluator_with_options(agent_space, name, request, headers, runtime)

    async def delete_evaluator_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.DeleteEvaluatorRequest,
    ) -> main_models.DeleteEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_evaluator_with_options_async(agent_space, name, request, headers, runtime)

    def delete_evaluator_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluatorSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluator_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluatorSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluator_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteEvaluatorSkillRequest,
    ) -> main_models.DeleteEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_evaluator_skill_with_options(name, skill_name, request, headers, runtime)

    async def delete_evaluator_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteEvaluatorSkillRequest,
    ) -> main_models.DeleteEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_evaluator_skill_with_options_async(name, skill_name, request, headers, runtime)

    def delete_experiment_plan_with_options(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.DeleteExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_plan_with_options_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.DeleteExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_plan(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.DeleteExperimentPlanRequest,
    ) -> main_models.DeleteExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_plan_with_options(agent_space, plan_id, request, headers, runtime)

    async def delete_experiment_plan_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.DeleteExperimentPlanRequest,
    ) -> main_models.DeleteExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_plan_with_options_async(agent_space, plan_id, request, headers, runtime)

    def delete_experiment_record_with_options(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.DeleteExperimentRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentRecordResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentRecord',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_record_with_options_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.DeleteExperimentRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentRecordResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentRecord',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_record(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.DeleteExperimentRecordRequest,
    ) -> main_models.DeleteExperimentRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_record_with_options(agent_space, record_id, request, headers, runtime)

    async def delete_experiment_record_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.DeleteExperimentRecordRequest,
    ) -> main_models.DeleteExperimentRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_record_with_options_async(agent_space, record_id, request, headers, runtime)

    def delete_mem_0memories_with_options(
        self,
        tmp_req: main_models.DeleteMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMem0MemoriesResponse:
        tmp_req.validate()
        request = main_models.DeleteMem0MemoriesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'metadata', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.agent_id):
            query['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.app_id):
            query['app_id'] = request.app_id
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.metadata_shrink):
            query['metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        if not DaraCore.is_null(request.run_id):
            query['run_id'] = request.run_id
        if not DaraCore.is_null(request.user_id):
            query['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMem0MemoriesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_mem_0memories_with_options_async(
        self,
        tmp_req: main_models.DeleteMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMem0MemoriesResponse:
        tmp_req.validate()
        request = main_models.DeleteMem0MemoriesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'metadata', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.agent_id):
            query['agent_id'] = request.agent_id
        if not DaraCore.is_null(request.app_id):
            query['app_id'] = request.app_id
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.metadata_shrink):
            query['metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        if not DaraCore.is_null(request.run_id):
            query['run_id'] = request.run_id
        if not DaraCore.is_null(request.user_id):
            query['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMem0MemoriesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_mem_0memories(
        self,
        request: main_models.DeleteMem0MemoriesRequest,
    ) -> main_models.DeleteMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mem_0memories_with_options(request, headers, runtime)

    async def delete_mem_0memories_async(
        self,
        request: main_models.DeleteMem0MemoriesRequest,
    ) -> main_models.DeleteMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mem_0memories_with_options_async(request, headers, runtime)

    def delete_mem_0memory_with_options(
        self,
        memory_id: str,
        request: main_models.DeleteMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMem0MemoryResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_mem_0memory_with_options_async(
        self,
        memory_id: str,
        request: main_models.DeleteMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMem0MemoryResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_mem_0memory(
        self,
        memory_id: str,
        request: main_models.DeleteMem0MemoryRequest,
    ) -> main_models.DeleteMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mem_0memory_with_options(memory_id, request, headers, runtime)

    async def delete_mem_0memory_async(
        self,
        memory_id: str,
        request: main_models.DeleteMem0MemoryRequest,
    ) -> main_models.DeleteMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mem_0memory_with_options_async(memory_id, request, headers, runtime)

    def delete_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def delete_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def execute_query_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteQuery',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_query_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteQuery',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_query(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
    ) -> main_models.ExecuteQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_query_with_options(agent_space, dataset_name, request, headers, runtime)

    async def execute_query_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.ExecuteQueryRequest,
    ) -> main_models.ExecuteQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_query_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def get_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_space(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
    ) -> main_models.GetAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_space_with_options(agent_space, request, headers, runtime)

    async def get_agent_space_async(
        self,
        agent_space: str,
        request: main_models.GetAgentSpaceRequest,
    ) -> main_models.GetAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_space_with_options_async(agent_space, request, headers, runtime)

    def get_agent_space_for_cmsworkspace_with_options(
        self,
        workspace: str,
        request: main_models.GetAgentSpaceForCMSWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceForCMSWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpaceForCMSWorkspace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/cms-workspaces/{DaraURL.percent_encode(workspace)}/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceForCMSWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_space_for_cmsworkspace_with_options_async(
        self,
        workspace: str,
        request: main_models.GetAgentSpaceForCMSWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpaceForCMSWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpaceForCMSWorkspace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/cms-workspaces/{DaraURL.percent_encode(workspace)}/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpaceForCMSWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_space_for_cmsworkspace(
        self,
        workspace: str,
        request: main_models.GetAgentSpaceForCMSWorkspaceRequest,
    ) -> main_models.GetAgentSpaceForCMSWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_space_for_cmsworkspace_with_options(workspace, request, headers, runtime)

    async def get_agent_space_for_cmsworkspace_async(
        self,
        workspace: str,
        request: main_models.GetAgentSpaceForCMSWorkspaceRequest,
    ) -> main_models.GetAgentSpaceForCMSWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_space_for_cmsworkspace_with_options_async(workspace, request, headers, runtime)

    def get_annotation_config_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_config_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_config(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetAnnotationConfigRequest,
    ) -> main_models.GetAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_annotation_config_with_options(agent_space, dataset_name, request, headers, runtime)

    async def get_annotation_config_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetAnnotationConfigRequest,
    ) -> main_models.GetAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_annotation_config_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def get_annotation_template_with_options(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.GetAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_annotation_template_with_options_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.GetAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_annotation_template(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.GetAnnotationTemplateRequest,
    ) -> main_models.GetAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_annotation_template_with_options(agent_space, template_id, request, headers, runtime)

    async def get_annotation_template_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.GetAnnotationTemplateRequest,
    ) -> main_models.GetAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_annotation_template_with_options_async(agent_space, template_id, request, headers, runtime)

    def get_context_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.GetContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.formatted):
            query['formatted'] = request.formatted
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_context_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.GetContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.formatted):
            query['formatted'] = request.formatted
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_context(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.GetContextRequest,
    ) -> main_models.GetContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_with_options(agent_space, context_store_name, context_id, request, headers, runtime)

    async def get_context_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.GetContextRequest,
    ) -> main_models.GetContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_with_options_async(agent_space, context_store_name, context_id, request, headers, runtime)

    def get_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
    ) -> main_models.GetContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def get_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.GetContextStoreRequest,
    ) -> main_models.GetContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def get_context_store_apikey_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreAPIKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_context_store_apikey_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetContextStoreAPIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextStoreAPIKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_context_store_apikey(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_store_apikey_with_options(agent_space, context_store_name, name, request, headers, runtime)

    async def get_context_store_apikey_async(
        self,
        agent_space: str,
        context_store_name: str,
        name: str,
        request: main_models.GetContextStoreAPIKeyRequest,
    ) -> main_models.GetContextStoreAPIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_store_apikey_with_options_async(agent_space, context_store_name, name, request, headers, runtime)

    def get_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def get_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def get_endpoint_connector_with_options(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.GetEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointConnectorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_endpoint_connector_with_options_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.GetEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointConnectorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_endpoint_connector(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.GetEndpointConnectorRequest,
    ) -> main_models.GetEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_endpoint_connector_with_options(agent_space, connector_id, request, headers, runtime)

    async def get_endpoint_connector_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.GetEndpointConnectorRequest,
    ) -> main_models.GetEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_endpoint_connector_with_options_async(agent_space, connector_id, request, headers, runtime)

    def get_evaluation_results_with_options(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluator_name):
            query['evaluatorName'] = request.evaluator_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationResults',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}/results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_results_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.evaluator_name):
            query['evaluatorName'] = request.evaluator_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationResults',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}/results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_results(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationResultsRequest,
    ) -> main_models.GetEvaluationResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluation_results_with_options(agent_space, task_id, run_id, request, headers, runtime)

    async def get_evaluation_results_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationResultsRequest,
    ) -> main_models.GetEvaluationResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluation_results_with_options_async(agent_space, task_id, run_id, request, headers, runtime)

    def get_evaluation_run_with_options(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_run_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_run(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationRunRequest,
    ) -> main_models.GetEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluation_run_with_options(agent_space, task_id, run_id, request, headers, runtime)

    async def get_evaluation_run_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationRunRequest,
    ) -> main_models.GetEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluation_run_with_options_async(agent_space, task_id, run_id, request, headers, runtime)

    def get_evaluation_task_with_options(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_task_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_task(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskRequest,
    ) -> main_models.GetEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluation_task_with_options(agent_space, task_id, request, headers, runtime)

    async def get_evaluation_task_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskRequest,
    ) -> main_models.GetEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluation_task_with_options_async(agent_space, task_id, request, headers, runtime)

    def get_evaluation_task_stats_with_options(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTaskStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.days):
            query['days'] = request.days
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTaskStats',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTaskStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_task_stats_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTaskStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.days):
            query['days'] = request.days
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTaskStats',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTaskStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_task_stats(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskStatsRequest,
    ) -> main_models.GetEvaluationTaskStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluation_task_stats_with_options(agent_space, task_id, request, headers, runtime)

    async def get_evaluation_task_stats_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.GetEvaluationTaskStatsRequest,
    ) -> main_models.GetEvaluationTaskStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluation_task_stats_with_options_async(agent_space, task_id, request, headers, runtime)

    def get_evaluation_trace_results_with_options(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationTraceResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTraceResultsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTraceResults',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}/trace-results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTraceResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_trace_results_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationTraceResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluationTraceResultsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluationTraceResults',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-result/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}/trace-results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluationTraceResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_trace_results(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationTraceResultsRequest,
    ) -> main_models.GetEvaluationTraceResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluation_trace_results_with_options(agent_space, task_id, run_id, request, headers, runtime)

    async def get_evaluation_trace_results_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.GetEvaluationTraceResultsRequest,
    ) -> main_models.GetEvaluationTraceResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluation_trace_results_with_options_async(agent_space, task_id, run_id, request, headers, runtime)

    def get_evaluator_with_options(
        self,
        agent_space: str,
        name: str,
        request: main_models.GetEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluator_with_options_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.GetEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluator(
        self,
        agent_space: str,
        name: str,
        request: main_models.GetEvaluatorRequest,
    ) -> main_models.GetEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluator_with_options(agent_space, name, request, headers, runtime)

    async def get_evaluator_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.GetEvaluatorRequest,
    ) -> main_models.GetEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluator_with_options_async(agent_space, name, request, headers, runtime)

    def get_evaluator_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluatorSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluator_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEvaluatorSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluator_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetEvaluatorSkillRequest,
    ) -> main_models.GetEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_evaluator_skill_with_options(name, skill_name, request, headers, runtime)

    async def get_evaluator_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetEvaluatorSkillRequest,
    ) -> main_models.GetEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_evaluator_skill_with_options_async(name, skill_name, request, headers, runtime)

    def get_experiment_plan_with_options(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.GetExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_plan_with_options_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.GetExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_plan(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.GetExperimentPlanRequest,
    ) -> main_models.GetExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experiment_plan_with_options(agent_space, plan_id, request, headers, runtime)

    async def get_experiment_plan_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.GetExperimentPlanRequest,
    ) -> main_models.GetExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experiment_plan_with_options_async(agent_space, plan_id, request, headers, runtime)

    def get_experiment_task_with_options(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.GetExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_task_with_options_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.GetExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_task(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.GetExperimentTaskRequest,
    ) -> main_models.GetExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experiment_task_with_options(agent_space, record_id, request, headers, runtime)

    async def get_experiment_task_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.GetExperimentTaskRequest,
    ) -> main_models.GetExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experiment_task_with_options_async(agent_space, record_id, request, headers, runtime)

    def get_mem_0memories_with_options(
        self,
        request: main_models.GetMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.enable_graph):
            query['enable_graph'] = request.enable_graph
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v2/memories',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoriesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_mem_0memories_with_options_async(
        self,
        request: main_models.GetMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.enable_graph):
            query['enable_graph'] = request.enable_graph
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v2/memories',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoriesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_mem_0memories(
        self,
        request: main_models.GetMem0MemoriesRequest,
    ) -> main_models.GetMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mem_0memories_with_options(request, headers, runtime)

    async def get_mem_0memories_async(
        self,
        request: main_models.GetMem0MemoriesRequest,
    ) -> main_models.GetMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mem_0memories_with_options_async(request, headers, runtime)

    def get_mem_0memory_with_options(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoryResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_mem_0memory_with_options_async(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoryResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_mem_0memory(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryRequest,
    ) -> main_models.GetMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mem_0memory_with_options(memory_id, request, headers, runtime)

    async def get_mem_0memory_async(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryRequest,
    ) -> main_models.GetMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mem_0memory_with_options_async(memory_id, request, headers, runtime)

    def get_mem_0memory_history_with_options(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0MemoryHistory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}/history',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoryHistoryResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_mem_0memory_history_with_options_async(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMem0MemoryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMem0MemoryHistory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}/history',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMem0MemoryHistoryResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_mem_0memory_history(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryHistoryRequest,
    ) -> main_models.GetMem0MemoryHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mem_0memory_history_with_options(memory_id, request, headers, runtime)

    async def get_mem_0memory_history_async(
        self,
        memory_id: str,
        request: main_models.GetMem0MemoryHistoryRequest,
    ) -> main_models.GetMem0MemoryHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mem_0memory_history_with_options_async(memory_id, request, headers, runtime)

    def get_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
    ) -> main_models.GetPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def get_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.GetPipelineRequest,
    ) -> main_models.GetPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)

    def list_agent_spaces_with_options(
        self,
        request: main_models.ListAgentSpacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpaces',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_spaces_with_options_async(
        self,
        request: main_models.ListAgentSpacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpaces',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_spaces(
        self,
        request: main_models.ListAgentSpacesRequest,
    ) -> main_models.ListAgentSpacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_spaces_with_options(request, headers, runtime)

    async def list_agent_spaces_async(
        self,
        request: main_models.ListAgentSpacesRequest,
    ) -> main_models.ListAgentSpacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_spaces_with_options_async(request, headers, runtime)

    def list_annotation_templates_with_options(
        self,
        agent_space: str,
        request: main_models.ListAnnotationTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationTemplatesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationTemplates',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_annotation_templates_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListAnnotationTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationTemplatesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationTemplates',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_annotation_templates(
        self,
        agent_space: str,
        request: main_models.ListAnnotationTemplatesRequest,
    ) -> main_models.ListAnnotationTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_annotation_templates_with_options(agent_space, request, headers, runtime)

    async def list_annotation_templates_async(
        self,
        agent_space: str,
        request: main_models.ListAnnotationTemplatesRequest,
    ) -> main_models.ListAnnotationTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_annotation_templates_with_options_async(agent_space, request, headers, runtime)

    def list_context_store_apikeys_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStoreAPIKeys',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoreAPIKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_context_store_apikeys_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStoreAPIKeys',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/apikey',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoreAPIKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_context_store_apikeys(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_context_store_apikeys_with_options(agent_space, context_store_name, request, headers, runtime)

    async def list_context_store_apikeys_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.ListContextStoreAPIKeysRequest,
    ) -> main_models.ListContextStoreAPIKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_context_store_apikeys_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def list_context_stores_with_options(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_store_name):
            query['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            query['contextType'] = request.context_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStores',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_context_stores_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListContextStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.context_store_name):
            query['contextStoreName'] = request.context_store_name
        if not DaraCore.is_null(request.context_type):
            query['contextType'] = request.context_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContextStores',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContextStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_context_stores(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
    ) -> main_models.ListContextStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_context_stores_with_options(agent_space, request, headers, runtime)

    async def list_context_stores_async(
        self,
        agent_space: str,
        request: main_models.ListContextStoresRequest,
    ) -> main_models.ListContextStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_context_stores_with_options_async(agent_space, request, headers, runtime)

    def list_datasets_with_options(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['datasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasets_with_options(agent_space, request, headers, runtime)

    async def list_datasets_async(
        self,
        agent_space: str,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasets_with_options_async(agent_space, request, headers, runtime)

    def list_endpoint_connectors_with_options(
        self,
        request: main_models.ListEndpointConnectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointConnectors',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_endpoint_connectors_with_options_async(
        self,
        request: main_models.ListEndpointConnectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointConnectors',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_endpoint_connectors(
        self,
        request: main_models.ListEndpointConnectorsRequest,
    ) -> main_models.ListEndpointConnectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_endpoint_connectors_with_options(request, headers, runtime)

    async def list_endpoint_connectors_async(
        self,
        request: main_models.ListEndpointConnectorsRequest,
    ) -> main_models.ListEndpointConnectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_endpoint_connectors_with_options_async(request, headers, runtime)

    def list_evaluation_runs_with_options(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.ListEvaluationRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationRunsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.run_type):
            query['runType'] = request.run_type
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationRuns',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/runs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_runs_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.ListEvaluationRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationRunsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.run_type):
            query['runType'] = request.run_type
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationRuns',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/runs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_runs(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.ListEvaluationRunsRequest,
    ) -> main_models.ListEvaluationRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_evaluation_runs_with_options(agent_space, task_id, request, headers, runtime)

    async def list_evaluation_runs_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.ListEvaluationRunsRequest,
    ) -> main_models.ListEvaluationRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_evaluation_runs_with_options_async(agent_space, task_id, request, headers, runtime)

    def list_evaluation_tasks_with_options(
        self,
        request: main_models.ListEvaluationTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_mode):
            query['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationTasks',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_tasks_with_options_async(
        self,
        request: main_models.ListEvaluationTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.channel):
            query['channel'] = request.channel
        if not DaraCore.is_null(request.data_type):
            query['dataType'] = request.data_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_mode):
            query['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationTasks',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_tasks(
        self,
        request: main_models.ListEvaluationTasksRequest,
    ) -> main_models.ListEvaluationTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_evaluation_tasks_with_options(request, headers, runtime)

    async def list_evaluation_tasks_async(
        self,
        request: main_models.ListEvaluationTasksRequest,
    ) -> main_models.ListEvaluationTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_evaluation_tasks_with_options_async(request, headers, runtime)

    def list_evaluator_skill_versions_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListEvaluatorSkillVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorSkillVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluatorSkillVersions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorSkillVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluator_skill_versions_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListEvaluatorSkillVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorSkillVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluatorSkillVersions',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorSkillVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluator_skill_versions(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListEvaluatorSkillVersionsRequest,
    ) -> main_models.ListEvaluatorSkillVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_evaluator_skill_versions_with_options(name, skill_name, request, headers, runtime)

    async def list_evaluator_skill_versions_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListEvaluatorSkillVersionsRequest,
    ) -> main_models.ListEvaluatorSkillVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_evaluator_skill_versions_with_options_async(name, skill_name, request, headers, runtime)

    def list_evaluator_skills_with_options(
        self,
        name: str,
        request: main_models.ListEvaluatorSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluatorSkills',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluator_skills_with_options_async(
        self,
        name: str,
        request: main_models.ListEvaluatorSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluatorSkills',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluator_skills(
        self,
        name: str,
        request: main_models.ListEvaluatorSkillsRequest,
    ) -> main_models.ListEvaluatorSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_evaluator_skills_with_options(name, request, headers, runtime)

    async def list_evaluator_skills_async(
        self,
        name: str,
        request: main_models.ListEvaluatorSkillsRequest,
    ) -> main_models.ListEvaluatorSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_evaluator_skills_with_options_async(name, request, headers, runtime)

    def list_evaluators_with_options(
        self,
        request: main_models.ListEvaluatorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluators',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluators_with_options_async(
        self,
        request: main_models.ListEvaluatorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluatorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluators',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluators(
        self,
        request: main_models.ListEvaluatorsRequest,
    ) -> main_models.ListEvaluatorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_evaluators_with_options(request, headers, runtime)

    async def list_evaluators_async(
        self,
        request: main_models.ListEvaluatorsRequest,
    ) -> main_models.ListEvaluatorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_evaluators_with_options_async(request, headers, runtime)

    def list_experiment_plans_with_options(
        self,
        agent_space: str,
        request: main_models.ListExperimentPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.plan_name):
            query['planName'] = request.plan_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentPlans',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_plans_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListExperimentPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.plan_name):
            query['planName'] = request.plan_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentPlans',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_plans(
        self,
        agent_space: str,
        request: main_models.ListExperimentPlansRequest,
    ) -> main_models.ListExperimentPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experiment_plans_with_options(agent_space, request, headers, runtime)

    async def list_experiment_plans_async(
        self,
        agent_space: str,
        request: main_models.ListExperimentPlansRequest,
    ) -> main_models.ListExperimentPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experiment_plans_with_options_async(agent_space, request, headers, runtime)

    def list_experiment_tasks_with_options(
        self,
        agent_space: str,
        request: main_models.ListExperimentTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.experiment_name):
            query['experimentName'] = request.experiment_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_name):
            query['planName'] = request.plan_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentTasks',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_tasks_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListExperimentTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.experiment_name):
            query['experimentName'] = request.experiment_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_name):
            query['planName'] = request.plan_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentTasks',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_tasks(
        self,
        agent_space: str,
        request: main_models.ListExperimentTasksRequest,
    ) -> main_models.ListExperimentTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experiment_tasks_with_options(agent_space, request, headers, runtime)

    async def list_experiment_tasks_async(
        self,
        agent_space: str,
        request: main_models.ListExperimentTasksRequest,
    ) -> main_models.ListExperimentTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experiment_tasks_with_options_async(agent_space, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelines',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipelines',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
    ) -> main_models.ListPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(agent_space, request, headers, runtime)

    async def list_pipelines_async(
        self,
        agent_space: str,
        request: main_models.ListPipelinesRequest,
    ) -> main_models.ListPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(agent_space, request, headers, runtime)

    def list_trace_preview_with_options(
        self,
        agent_space: str,
        request: main_models.ListTracePreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTracePreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['cursor'] = request.cursor
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTracePreview',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/trace-preview/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTracePreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trace_preview_with_options_async(
        self,
        agent_space: str,
        request: main_models.ListTracePreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTracePreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['cursor'] = request.cursor
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTracePreview',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/trace-preview/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTracePreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trace_preview(
        self,
        agent_space: str,
        request: main_models.ListTracePreviewRequest,
    ) -> main_models.ListTracePreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_trace_preview_with_options(agent_space, request, headers, runtime)

    async def list_trace_preview_async(
        self,
        agent_space: str,
        request: main_models.ListTracePreviewRequest,
    ) -> main_models.ListTracePreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_trace_preview_with_options_async(agent_space, request, headers, runtime)

    def preview_pipeline_with_options(
        self,
        agent_space: str,
        request: main_models.PreviewPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewPipelineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/preview',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_pipeline_with_options_async(
        self,
        agent_space: str,
        request: main_models.PreviewPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewPipelineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_time):
            body['fromTime'] = request.from_time
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.to_time):
            body['toTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewPipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/preview',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_pipeline(
        self,
        agent_space: str,
        request: main_models.PreviewPipelineRequest,
    ) -> main_models.PreviewPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.preview_pipeline_with_options(agent_space, request, headers, runtime)

    async def preview_pipeline_async(
        self,
        agent_space: str,
        request: main_models.PreviewPipelineRequest,
    ) -> main_models.PreviewPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.preview_pipeline_with_options_async(agent_space, request, headers, runtime)

    def save_annotation_config_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.SaveAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.source_template_path):
            body['sourceTemplatePath'] = request.source_template_path
        if not DaraCore.is_null(request.template_title):
            body['templateTitle'] = request.template_title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_annotation_config_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.SaveAnnotationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveAnnotationConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.source_template_path):
            body['sourceTemplatePath'] = request.source_template_path
        if not DaraCore.is_null(request.template_title):
            body['templateTitle'] = request.template_title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAnnotationConfig',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(dataset_name)}/config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAnnotationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_annotation_config(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.SaveAnnotationConfigRequest,
    ) -> main_models.SaveAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.save_annotation_config_with_options(agent_space, dataset_name, request, headers, runtime)

    async def save_annotation_config_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.SaveAnnotationConfigRequest,
    ) -> main_models.SaveAnnotationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.save_annotation_config_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def search_context_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['filter'] = request.filter
        if not DaraCore.is_null(request.formatted):
            body['formatted'] = request.formatted
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.retrieval_option):
            body['retrievalOption'] = request.retrieval_option
        if not DaraCore.is_null(request.threshold):
            body['threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_context_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['filter'] = request.filter
        if not DaraCore.is_null(request.formatted):
            body['formatted'] = request.formatted
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.retrieval_option):
            body['retrievalOption'] = request.retrieval_option
        if not DaraCore.is_null(request.threshold):
            body['threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_context(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
    ) -> main_models.SearchContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_context_with_options(agent_space, context_store_name, request, headers, runtime)

    async def search_context_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.SearchContextRequest,
    ) -> main_models.SearchContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_context_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def search_mem_0memories_with_options(
        self,
        request: main_models.SearchMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.enable_graph):
            query['enable_graph'] = request.enable_graph
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v2/memories/search',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.SearchMem0MemoriesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def search_mem_0memories_with_options_async(
        self,
        request: main_models.SearchMem0MemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchMem0MemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.enable_graph):
            query['enable_graph'] = request.enable_graph
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchMem0Memories',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v2/memories/search',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.SearchMem0MemoriesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def search_mem_0memories(
        self,
        request: main_models.SearchMem0MemoriesRequest,
    ) -> main_models.SearchMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_mem_0memories_with_options(request, headers, runtime)

    async def search_mem_0memories_async(
        self,
        request: main_models.SearchMem0MemoriesRequest,
    ) -> main_models.SearchMem0MemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_mem_0memories_with_options_async(request, headers, runtime)

    def stop_experiment_task_with_options(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.StopExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopExperimentTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}/cancel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopExperimentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_experiment_task_with_options_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.StopExperimentTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopExperimentTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopExperimentTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/records/{DaraURL.percent_encode(record_id)}/cancel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopExperimentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_experiment_task(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.StopExperimentTaskRequest,
    ) -> main_models.StopExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_experiment_task_with_options(agent_space, record_id, request, headers, runtime)

    async def stop_experiment_task_async(
        self,
        agent_space: str,
        record_id: str,
        request: main_models.StopExperimentTaskRequest,
    ) -> main_models.StopExperimentTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_experiment_task_with_options_async(agent_space, record_id, request, headers, runtime)

    def update_agent_space_with_options(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_space_with_options_async(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.cms_workspace):
            body['cmsWorkspace'] = request.cms_workspace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpace',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_space(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
    ) -> main_models.UpdateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_space_with_options(agent_space, request, headers, runtime)

    async def update_agent_space_async(
        self,
        agent_space: str,
        request: main_models.UpdateAgentSpaceRequest,
    ) -> main_models.UpdateAgentSpaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_space_with_options_async(agent_space, request, headers, runtime)

    def update_annotation_template_with_options(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.UpdateAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.details):
            body['details'] = request.details
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.template_path):
            body['templatePath'] = request.template_path
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_annotation_template_with_options_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.UpdateAnnotationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.details):
            body['details'] = request.details
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.template_path):
            body['templatePath'] = request.template_path
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationTemplate',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/annotation/{DaraURL.percent_encode(agent_space)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_annotation_template(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.UpdateAnnotationTemplateRequest,
    ) -> main_models.UpdateAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_annotation_template_with_options(agent_space, template_id, request, headers, runtime)

    async def update_annotation_template_async(
        self,
        agent_space: str,
        template_id: str,
        request: main_models.UpdateAnnotationTemplateRequest,
    ) -> main_models.UpdateAnnotationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_annotation_template_with_options_async(agent_space, template_id, request, headers, runtime)

    def update_context_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.UpdateContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.experience):
            body['experience'] = request.experience
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.payload):
            body['payload'] = request.payload
        if not DaraCore.is_null(request.trigger_condition):
            body['triggerCondition'] = request.trigger_condition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_context_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.UpdateContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.experience):
            body['experience'] = request.experience
        if not DaraCore.is_null(request.metadata):
            body['metadata'] = request.metadata
        if not DaraCore.is_null(request.payload):
            body['payload'] = request.payload
        if not DaraCore.is_null(request.trigger_condition):
            body['triggerCondition'] = request.trigger_condition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContext',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}/context/{DaraURL.percent_encode(context_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_context(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.UpdateContextRequest,
    ) -> main_models.UpdateContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_context_with_options(agent_space, context_store_name, context_id, request, headers, runtime)

    async def update_context_async(
        self,
        agent_space: str,
        context_store_name: str,
        context_id: str,
        request: main_models.UpdateContextRequest,
    ) -> main_models.UpdateContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_context_with_options_async(agent_space, context_store_name, context_id, request, headers, runtime)

    def update_context_store_with_options(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_context_store_with_options_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContextStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.context_type):
            body['contextType'] = request.context_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContextStore',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/contextstore/{DaraURL.percent_encode(context_store_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContextStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_context_store(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
    ) -> main_models.UpdateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_context_store_with_options(agent_space, context_store_name, request, headers, runtime)

    async def update_context_store_async(
        self,
        agent_space: str,
        context_store_name: str,
        request: main_models.UpdateContextStoreRequest,
    ) -> main_models.UpdateContextStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_context_store_with_options_async(agent_space, context_store_name, request, headers, runtime)

    def update_dataset_with_options(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/dataset/{DaraURL.percent_encode(dataset_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dataset_with_options(agent_space, dataset_name, request, headers, runtime)

    async def update_dataset_async(
        self,
        agent_space: str,
        dataset_name: str,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dataset_with_options_async(agent_space, dataset_name, request, headers, runtime)

    def update_endpoint_connector_with_options(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.UpdateEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.credential):
            body['credential'] = request.credential
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            body['headers'] = request.headers
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_endpoint_connector_with_options_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.UpdateEndpointConnectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.credential):
            body['credential'] = request.credential
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            body['headers'] = request.headers
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointConnector',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoint-connectors/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(connector_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_endpoint_connector(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.UpdateEndpointConnectorRequest,
    ) -> main_models.UpdateEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_endpoint_connector_with_options(agent_space, connector_id, request, headers, runtime)

    async def update_endpoint_connector_async(
        self,
        agent_space: str,
        connector_id: str,
        request: main_models.UpdateEndpointConnectorRequest,
    ) -> main_models.UpdateEndpointConnectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_endpoint_connector_with_options_async(agent_space, connector_id, request, headers, runtime)

    def update_evaluation_run_with_options(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.UpdateEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluationRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluationRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_evaluation_run_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.UpdateEvaluationRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluationRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluationRun',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}/run/{DaraURL.percent_encode(run_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluationRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_evaluation_run(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.UpdateEvaluationRunRequest,
    ) -> main_models.UpdateEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_evaluation_run_with_options(agent_space, task_id, run_id, request, headers, runtime)

    async def update_evaluation_run_async(
        self,
        agent_space: str,
        task_id: str,
        run_id: str,
        request: main_models.UpdateEvaluationRunRequest,
    ) -> main_models.UpdateEvaluationRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_evaluation_run_with_options_async(agent_space, task_id, run_id, request, headers, runtime)

    def update_evaluation_task_with_options(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.UpdateEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.run_strategies):
            body['runStrategies'] = request.run_strategies
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_evaluation_task_with_options_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.UpdateEvaluationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.channel):
            body['channel'] = request.channel
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.data_filter):
            body['dataFilter'] = request.data_filter
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.run_strategies):
            body['runStrategies'] = request.run_strategies
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluationTask',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluation-task/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_evaluation_task(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.UpdateEvaluationTaskRequest,
    ) -> main_models.UpdateEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_evaluation_task_with_options(agent_space, task_id, request, headers, runtime)

    async def update_evaluation_task_async(
        self,
        agent_space: str,
        task_id: str,
        request: main_models.UpdateEvaluationTaskRequest,
    ) -> main_models.UpdateEvaluationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_evaluation_task_with_options_async(agent_space, task_id, request, headers, runtime)

    def update_evaluator_with_options(
        self,
        agent_space: str,
        name: str,
        request: main_models.UpdateEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.annotations):
            body['annotations'] = request.annotations
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_evaluator_with_options_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.UpdateEvaluatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.annotations):
            body['annotations'] = request.annotations
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluator',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluators/{DaraURL.percent_encode(agent_space)}/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_evaluator(
        self,
        agent_space: str,
        name: str,
        request: main_models.UpdateEvaluatorRequest,
    ) -> main_models.UpdateEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_evaluator_with_options(agent_space, name, request, headers, runtime)

    async def update_evaluator_async(
        self,
        agent_space: str,
        name: str,
        request: main_models.UpdateEvaluatorRequest,
    ) -> main_models.UpdateEvaluatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_evaluator_with_options_async(agent_space, name, request, headers, runtime)

    def update_evaluator_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluatorSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_evaluator_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateEvaluatorSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEvaluatorSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEvaluatorSkill',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/evaluator/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEvaluatorSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_evaluator_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateEvaluatorSkillRequest,
    ) -> main_models.UpdateEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_evaluator_skill_with_options(name, skill_name, request, headers, runtime)

    async def update_evaluator_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateEvaluatorSkillRequest,
    ) -> main_models.UpdateEvaluatorSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_evaluator_skill_with_options_async(name, skill_name, request, headers, runtime)

    def update_experiment_plan_with_options(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.UpdateExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_project):
            body['datasetProject'] = request.dataset_project
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.query_sql):
            body['querySql'] = request.query_sql
        if not DaraCore.is_null(request.selected_item_ids):
            body['selectedItemIds'] = request.selected_item_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_plan_with_options_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.UpdateExperimentPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_project):
            body['datasetProject'] = request.dataset_project
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.experiments):
            body['experiments'] = request.experiments
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.query_sql):
            body['querySql'] = request.query_sql
        if not DaraCore.is_null(request.selected_item_ids):
            body['selectedItemIds'] = request.selected_item_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperimentPlan',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_plan(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.UpdateExperimentPlanRequest,
    ) -> main_models.UpdateExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_experiment_plan_with_options(agent_space, plan_id, request, headers, runtime)

    async def update_experiment_plan_async(
        self,
        agent_space: str,
        plan_id: str,
        request: main_models.UpdateExperimentPlanRequest,
    ) -> main_models.UpdateExperimentPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_experiment_plan_with_options_async(agent_space, plan_id, request, headers, runtime)

    def update_mem_0memory_with_options(
        self,
        memory_id: str,
        request: main_models.UpdateMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'PUT',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMem0MemoryResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def update_mem_0memory_with_options_async(
        self,
        memory_id: str,
        request: main_models.UpdateMem0MemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMem0MemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        if not DaraCore.is_null(request.context_store_id):
            query['context_store_id'] = request.context_store_id
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.project_id):
            query['project_id'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMem0Memory',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'PUT',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMem0MemoryResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def update_mem_0memory(
        self,
        memory_id: str,
        request: main_models.UpdateMem0MemoryRequest,
    ) -> main_models.UpdateMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_mem_0memory_with_options(memory_id, request, headers, runtime)

    async def update_mem_0memory_async(
        self,
        memory_id: str,
        request: main_models.UpdateMem0MemoryRequest,
    ) -> main_models.UpdateMem0MemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_mem_0memory_with_options_async(memory_id, request, headers, runtime)

    def update_pipeline_with_options(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_policy):
            body['executePolicy'] = request.execute_policy
        if not DaraCore.is_null(request.pipeline):
            body['pipeline'] = request.pipeline
        if not DaraCore.is_null(request.sink):
            body['sink'] = request.sink
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/agentspace/{DaraURL.percent_encode(agent_space)}/pipeline/{DaraURL.percent_encode(pipeline_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(agent_space, pipeline_name, request, headers, runtime)

    async def update_pipeline_async(
        self,
        agent_space: str,
        pipeline_name: str,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pipeline_with_options_async(agent_space, pipeline_name, request, headers, runtime)

    def upload_experiment_with_options(
        self,
        agent_space: str,
        request: main_models.UploadExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.completed_at):
            body['completedAt'] = request.completed_at
        if not DaraCore.is_null(request.completed_tasks):
            body['completedTasks'] = request.completed_tasks
        if not DaraCore.is_null(request.data_source):
            body['dataSource'] = request.data_source
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.executed_at):
            body['executedAt'] = request.executed_at
        if not DaraCore.is_null(request.experiment_config):
            body['experimentConfig'] = request.experiment_config
        if not DaraCore.is_null(request.experiment_plan_id):
            body['experimentPlanId'] = request.experiment_plan_id
        if not DaraCore.is_null(request.failed_tasks):
            body['failedTasks'] = request.failed_tasks
        if not DaraCore.is_null(request.record_id):
            body['recordId'] = request.record_id
        if not DaraCore.is_null(request.record_name):
            body['recordName'] = request.record_name
        if not DaraCore.is_null(request.total_tasks):
            body['totalTasks'] = request.total_tasks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadExperiment',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_experiment_with_options_async(
        self,
        agent_space: str,
        request: main_models.UploadExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.completed_at):
            body['completedAt'] = request.completed_at
        if not DaraCore.is_null(request.completed_tasks):
            body['completedTasks'] = request.completed_tasks
        if not DaraCore.is_null(request.data_source):
            body['dataSource'] = request.data_source
        if not DaraCore.is_null(request.evaluators):
            body['evaluators'] = request.evaluators
        if not DaraCore.is_null(request.executed_at):
            body['executedAt'] = request.executed_at
        if not DaraCore.is_null(request.experiment_config):
            body['experimentConfig'] = request.experiment_config
        if not DaraCore.is_null(request.experiment_plan_id):
            body['experimentPlanId'] = request.experiment_plan_id
        if not DaraCore.is_null(request.failed_tasks):
            body['failedTasks'] = request.failed_tasks
        if not DaraCore.is_null(request.record_id):
            body['recordId'] = request.record_id
        if not DaraCore.is_null(request.record_name):
            body['recordName'] = request.record_name
        if not DaraCore.is_null(request.total_tasks):
            body['totalTasks'] = request.total_tasks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadExperiment',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(agent_space)}/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_experiment(
        self,
        agent_space: str,
        request: main_models.UploadExperimentRequest,
    ) -> main_models.UploadExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_experiment_with_options(agent_space, request, headers, runtime)

    async def upload_experiment_async(
        self,
        agent_space: str,
        request: main_models.UploadExperimentRequest,
    ) -> main_models.UploadExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_experiment_with_options_async(agent_space, request, headers, runtime)

    def validate_mem_0apikey_with_options(
        self,
        request: main_models.ValidateMem0APIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateMem0APIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateMem0APIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/ping',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateMem0APIKeyResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def validate_mem_0apikey_with_options_async(
        self,
        request: main_models.ValidateMem0APIKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateMem0APIKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_space):
            query['agentSpace'] = request.agent_space
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateMem0APIKey',
            version = '2026-05-20',
            protocol = 'HTTPS',
            pathname = f'/v1/ping',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateMem0APIKeyResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def validate_mem_0apikey(
        self,
        request: main_models.ValidateMem0APIKeyRequest,
    ) -> main_models.ValidateMem0APIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_mem_0apikey_with_options(request, headers, runtime)

    async def validate_mem_0apikey_async(
        self,
        request: main_models.ValidateMem0APIKeyRequest,
    ) -> main_models.ValidateMem0APIKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_mem_0apikey_with_options_async(request, headers, runtime)
