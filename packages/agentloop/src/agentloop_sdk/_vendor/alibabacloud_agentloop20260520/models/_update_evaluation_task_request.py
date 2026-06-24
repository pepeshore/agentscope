# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from .. import models as main_models
from darabonba.model import DaraModel

class UpdateEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        config: Dict[str, str] = None,
        data_filter: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        run_strategies: main_models.RunStrategies = None,
        status: str = None,
        tags: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.channel = channel
        self.config = config
        self.data_filter = data_filter
        self.description = description
        self.evaluators = evaluators
        self.run_strategies = run_strategies
        self.status = status
        self.tags = tags
        self.client_token = client_token

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.run_strategies:
            self.run_strategies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.config is not None:
            result['config'] = self.config

        if self.data_filter is not None:
            result['dataFilter'] = self.data_filter

        if self.description is not None:
            result['description'] = self.description

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.run_strategies is not None:
            result['runStrategies'] = self.run_strategies.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('dataFilter') is not None:
            self.data_filter = m.get('dataFilter')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('runStrategies') is not None:
            temp_model = main_models.RunStrategies()
            self.run_strategies = temp_model.from_map(m.get('runStrategies'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

