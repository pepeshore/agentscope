# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from .. import models as main_models
from darabonba.model import DaraModel

class ListTracePreviewRequest(DaraModel):
    def __init__(
        self,
        cursor: main_models.ListTracePreviewRequestCursor = None,
        data_filter: main_models.DataFilter = None,
        end_time: int = None,
        size: int = None,
        start_time: int = None,
    ):
        self.cursor = cursor
        self.data_filter = data_filter
        self.end_time = end_time
        self.size = size
        self.start_time = start_time

    def validate(self):
        if self.cursor:
            self.cursor.validate()
        if self.data_filter:
            self.data_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor.to_map()

        if self.data_filter is not None:
            result['dataFilter'] = self.data_filter.to_map()

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.size is not None:
            result['size'] = self.size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            temp_model = main_models.ListTracePreviewRequestCursor()
            self.cursor = temp_model.from_map(m.get('cursor'))

        if m.get('dataFilter') is not None:
            temp_model = main_models.DataFilter()
            self.data_filter = temp_model.from_map(m.get('dataFilter'))

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class ListTracePreviewRequestCursor(DaraModel):
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

