# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEndpointConnectorResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        alias: str = None,
        connector_id: str = None,
        created_at: int = None,
        credential: Dict[str, str] = None,
        description: str = None,
        endpoint: str = None,
        headers: List[main_models.GetEndpointConnectorResponseBodyHeaders] = None,
        name: str = None,
        properties: Dict[str, str] = None,
        region_id: str = None,
        request_id: str = None,
        tags: List[str] = None,
        type: str = None,
        updated_at: int = None,
    ):
        self.agent_space = agent_space
        self.alias = alias
        self.connector_id = connector_id
        self.created_at = created_at
        self.credential = credential
        self.description = description
        self.endpoint = endpoint
        self.headers = headers
        self.name = name
        self.properties = properties
        self.region_id = region_id
        self.request_id = request_id
        self.tags = tags
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()

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

        if self.credential is not None:
            result['credential'] = self.credential

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        result['headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['headers'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('credential') is not None:
            self.credential = m.get('credential')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        self.headers = []
        if m.get('headers') is not None:
            for k1 in m.get('headers'):
                temp_model = main_models.GetEndpointConnectorResponseBodyHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetEndpointConnectorResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

