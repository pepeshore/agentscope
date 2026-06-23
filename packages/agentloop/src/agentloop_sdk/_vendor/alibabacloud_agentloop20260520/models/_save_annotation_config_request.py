# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveAnnotationConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        source_template_path: str = None,
        template_title: str = None,
    ):
        # This parameter is required.
        self.config = config
        self.source_template_path = source_template_path
        # This parameter is required.
        self.template_title = template_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.source_template_path is not None:
            result['sourceTemplatePath'] = self.source_template_path

        if self.template_title is not None:
            result['templateTitle'] = self.template_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('sourceTemplatePath') is not None:
            self.source_template_path = m.get('sourceTemplatePath')

        if m.get('templateTitle') is not None:
            self.template_title = m.get('templateTitle')

        return self

