# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAnnotationTemplateRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        details: str = None,
        group: str = None,
        image: str = None,
        order: int = None,
        template_path: str = None,
        title: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.config = config
        self.details = details
        self.group = group
        self.image = image
        self.order = order
        self.template_path = template_path
        # This parameter is required.
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.details is not None:
            result['details'] = self.details

        if self.group is not None:
            result['group'] = self.group

        if self.image is not None:
            result['image'] = self.image

        if self.order is not None:
            result['order'] = self.order

        if self.template_path is not None:
            result['templatePath'] = self.template_path

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('details') is not None:
            self.details = m.get('details')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('templatePath') is not None:
            self.template_path = m.get('templatePath')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

