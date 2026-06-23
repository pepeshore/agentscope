# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListAnnotationTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[str] = None,
        request_id: str = None,
        templates: List[main_models.ListAnnotationTemplatesResponseBodyTemplates] = None,
    ):
        self.groups = groups
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.groups is not None:
            result['groups'] = self.groups

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groups') is not None:
            self.groups = m.get('groups')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.templates = []
        if m.get('templates') is not None:
            for k1 in m.get('templates'):
                temp_model = main_models.ListAnnotationTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class ListAnnotationTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        config: str = None,
        details: str = None,
        group: str = None,
        image: str = None,
        order: int = None,
        template_id: str = None,
        template_path: str = None,
        title: str = None,
        type: str = None,
    ):
        self.agent_space = agent_space
        self.config = config
        self.details = details
        self.group = group
        self.image = image
        self.order = order
        self.template_id = template_id
        self.template_path = template_path
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

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

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_path is not None:
            result['templatePath'] = self.template_path

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

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

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templatePath') is not None:
            self.template_path = m.get('templatePath')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

