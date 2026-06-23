# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class CreateEvaluatorRequest(DaraModel):
    def __init__(
        self,
        annotations: List[str] = None,
        config: Dict[str, Any] = None,
        description: str = None,
        display_name: str = None,
        metric_name: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        type: str = None,
        version: str = None,
        version_description: str = None,
        client_token: str = None,
    ):
        self.annotations = annotations
        self.config = config
        self.description = description
        self.display_name = display_name
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.name = name
        self.properties = properties
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.version = version
        self.version_description = version_description
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

