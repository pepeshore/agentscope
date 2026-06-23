# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAnnotationConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_id: str = None,
        dataset_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        source_template_path: str = None,
        template_title: str = None,
        workspace: str = None,
    ):
        self.config = config
        self.config_id = config_id
        self.dataset_name = dataset_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.source_template_path = source_template_path
        self.template_title = template_title
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.config_id is not None:
            result['configId'] = self.config_id

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_template_path is not None:
            result['sourceTemplatePath'] = self.source_template_path

        if self.template_title is not None:
            result['templateTitle'] = self.template_title

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceTemplatePath') is not None:
            self.source_template_path = m.get('sourceTemplatePath')

        if m.get('templateTitle') is not None:
            self.template_title = m.get('templateTitle')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

