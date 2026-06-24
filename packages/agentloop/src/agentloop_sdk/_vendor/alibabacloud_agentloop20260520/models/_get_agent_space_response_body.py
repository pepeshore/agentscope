# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from .. import models as main_models
from darabonba.model import DaraModel

class GetAgentSpaceResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        cms_workspace: str = None,
        cms_workspace_bind_type: str = None,
        create_time: str = None,
        description: str = None,
        mse_namespace: main_models.GetAgentSpaceResponseBodyMseNamespace = None,
        quota: main_models.GetAgentSpaceResponseBodyQuota = None,
        region_id: str = None,
        request_id: str = None,
        sls_project: str = None,
        update_time: str = None,
    ):
        self.agent_space = agent_space
        self.cms_workspace = cms_workspace
        self.cms_workspace_bind_type = cms_workspace_bind_type
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.mse_namespace = mse_namespace
        self.quota = quota
        self.region_id = region_id
        self.request_id = request_id
        self.sls_project = sls_project
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.mse_namespace:
            self.mse_namespace.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.cms_workspace is not None:
            result['cmsWorkspace'] = self.cms_workspace

        if self.cms_workspace_bind_type is not None:
            result['cmsWorkspaceBindType'] = self.cms_workspace_bind_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.mse_namespace is not None:
            result['mseNamespace'] = self.mse_namespace.to_map()

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sls_project is not None:
            result['slsProject'] = self.sls_project

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('cmsWorkspace') is not None:
            self.cms_workspace = m.get('cmsWorkspace')

        if m.get('cmsWorkspaceBindType') is not None:
            self.cms_workspace_bind_type = m.get('cmsWorkspaceBindType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('mseNamespace') is not None:
            temp_model = main_models.GetAgentSpaceResponseBodyMseNamespace()
            self.mse_namespace = temp_model.from_map(m.get('mseNamespace'))

        if m.get('quota') is not None:
            temp_model = main_models.GetAgentSpaceResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetAgentSpaceResponseBodyQuota(DaraModel):
    def __init__(
        self,
        context_store: int = None,
        dataset: int = None,
        pipeline: int = None,
    ):
        self.context_store = context_store
        self.dataset = dataset
        self.pipeline = pipeline

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_store is not None:
            result['contextStore'] = self.context_store

        if self.dataset is not None:
            result['dataset'] = self.dataset

        if self.pipeline is not None:
            result['pipeline'] = self.pipeline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextStore') is not None:
            self.context_store = m.get('contextStore')

        if m.get('dataset') is not None:
            self.dataset = m.get('dataset')

        if m.get('pipeline') is not None:
            self.pipeline = m.get('pipeline')

        return self

class GetAgentSpaceResponseBodyMseNamespace(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        return self

