# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListTracePreviewResponseBody(DaraModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        next_cursor: main_models.ListTracePreviewResponseBodyNextCursor = None,
        request_id: str = None,
        size: int = None,
    ):
        self.items = items
        self.next_cursor = next_cursor
        self.request_id = request_id
        self.size = size

    def validate(self):
        if self.next_cursor:
            self.next_cursor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['items'] = self.items

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('nextCursor') is not None:
            temp_model = main_models.ListTracePreviewResponseBodyNextCursor()
            self.next_cursor = temp_model.from_map(m.get('nextCursor'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class ListTracePreviewResponseBodyNextCursor(DaraModel):
    def __init__(
        self,
        last_start_time_nano: str = None,
        last_trace_id: str = None,
    ):
        self.last_start_time_nano = last_start_time_nano
        self.last_trace_id = last_trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_start_time_nano is not None:
            result['lastStartTimeNano'] = self.last_start_time_nano

        if self.last_trace_id is not None:
            result['lastTraceId'] = self.last_trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastStartTimeNano') is not None:
            self.last_start_time_nano = m.get('lastStartTimeNano')

        if m.get('lastTraceId') is not None:
            self.last_trace_id = m.get('lastTraceId')

        return self

