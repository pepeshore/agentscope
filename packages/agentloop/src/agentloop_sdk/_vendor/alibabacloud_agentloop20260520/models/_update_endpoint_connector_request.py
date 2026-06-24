# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from .. import models as main_models
from darabonba.model import DaraModel

class UpdateEndpointConnectorRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        credential: Dict[str, str] = None,
        description: str = None,
        endpoint: str = None,
        headers: List[main_models.UpdateEndpointConnectorRequestHeaders] = None,
        name: str = None,
        properties: Dict[str, str] = None,
        tags: List[str] = None,
        client_token: str = None,
    ):
        self.alias = alias
        self.credential = credential
        self.description = description
        self.endpoint = endpoint
        self.headers = headers
        self.name = name
        self.properties = properties
        self.tags = tags
        self.client_token = client_token

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
        if self.alias is not None:
            result['alias'] = self.alias

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

        if self.tags is not None:
            result['tags'] = self.tags

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('credential') is not None:
            self.credential = m.get('credential')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        self.headers = []
        if m.get('headers') is not None:
            for k1 in m.get('headers'):
                temp_model = main_models.UpdateEndpointConnectorRequestHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateEndpointConnectorRequestHeaders(DaraModel):
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

