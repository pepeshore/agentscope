# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetExperimentTaskResponseBody(DaraModel):
    def __init__(
        self,
        record: main_models.ExperimentRecord = None,
        request_id: str = None,
    ):
        self.record = record
        self.request_id = request_id

    def validate(self):
        if self.record:
            self.record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record is not None:
            result['record'] = self.record.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('record') is not None:
            temp_model = main_models.ExperimentRecord()
            self.record = temp_model.from_map(m.get('record'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

