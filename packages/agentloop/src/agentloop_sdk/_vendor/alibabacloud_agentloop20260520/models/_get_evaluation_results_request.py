# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEvaluationResultsRequest(DaraModel):
    def __init__(
        self,
        evaluator_name: str = None,
        max_results: int = None,
        offset: int = None,
        status: str = None,
    ):
        self.evaluator_name = evaluator_name
        self.max_results = max_results
        self.offset = offset
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluator_name is not None:
            result['evaluatorName'] = self.evaluator_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.offset is not None:
            result['offset'] = self.offset

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('evaluatorName') is not None:
            self.evaluator_name = m.get('evaluatorName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

