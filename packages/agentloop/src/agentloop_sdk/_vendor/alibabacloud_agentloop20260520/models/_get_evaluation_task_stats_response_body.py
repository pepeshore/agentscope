# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEvaluationTaskStatsResponseBody(DaraModel):
    def __init__(
        self,
        days: int = None,
        failed_count: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        request_id: str = None,
        success_count: int = None,
        total_count: int = None,
        total_tokens: int = None,
    ):
        self.days = days
        self.failed_count = failed_count
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success_count = success_count
        self.total_count = total_count
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['days'] = self.days

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success_count is not None:
            result['successCount'] = self.success_count

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

