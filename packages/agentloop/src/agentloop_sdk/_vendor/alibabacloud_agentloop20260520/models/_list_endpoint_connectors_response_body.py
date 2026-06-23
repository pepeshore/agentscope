# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListEndpointConnectorsResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_connectors: List[main_models.ListEndpointConnectorsResponseBodyEndpointConnectors] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.endpoint_connectors = endpoint_connectors
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.endpoint_connectors:
            for v1 in self.endpoint_connectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['endpointConnectors'] = []
        if self.endpoint_connectors is not None:
            for k1 in self.endpoint_connectors:
                result['endpointConnectors'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_connectors = []
        if m.get('endpointConnectors') is not None:
            for k1 in m.get('endpointConnectors'):
                temp_model = main_models.ListEndpointConnectorsResponseBodyEndpointConnectors()
                self.endpoint_connectors.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListEndpointConnectorsResponseBodyEndpointConnectors(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        alias: str = None,
        connector_id: str = None,
        created_at: int = None,
        description: str = None,
        endpoint: str = None,
        name: str = None,
        properties: Dict[str, str] = None,
        tags: List[str] = None,
        type: str = None,
        updated_at: int = None,
    ):
        self.agent_space = agent_space
        self.alias = alias
        self.connector_id = connector_id
        self.created_at = created_at
        self.description = description
        self.endpoint = endpoint
        self.name = name
        self.properties = properties
        self.tags = tags
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.alias is not None:
            result['alias'] = self.alias

        if self.connector_id is not None:
            result['connectorId'] = self.connector_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.tags is not None:
            result['tags'] = self.tags

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('connectorId') is not None:
            self.connector_id = m.get('connectorId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

