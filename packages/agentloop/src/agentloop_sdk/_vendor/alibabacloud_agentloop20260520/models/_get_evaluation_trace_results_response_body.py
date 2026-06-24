# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from .. import models as main_models
from darabonba.model import DaraModel

class GetEvaluationTraceResultsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetEvaluationTraceResultsResponseBodyItems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetEvaluationTraceResultsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetEvaluationTraceResultsResponseBodyItems(DaraModel):
    def __init__(
        self,
        scores: List[Dict[str, str]] = None,
        trace_id: str = None,
    ):
        self.scores = scores
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scores is not None:
            result['scores'] = self.scores

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scores') is not None:
            self.scores = m.get('scores')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

