# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dataset_name: str = None,
        description: str = None,
        schema_shrink: str = None,
    ):
        self.client_token = client_token
        self.dataset_name = dataset_name
        self.description = description
        self.schema_shrink = schema_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.description is not None:
            result['description'] = self.description

        if self.schema_shrink is not None:
            result['schema'] = self.schema_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('schema') is not None:
            self.schema_shrink = m.get('schema')

        return self

