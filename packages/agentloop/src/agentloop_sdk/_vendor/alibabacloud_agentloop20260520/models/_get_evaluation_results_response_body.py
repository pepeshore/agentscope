# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEvaluationResultsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        offset: int = None,
        request_id: str = None,
        results: List[main_models.GetEvaluationResultsResponseBodyResults] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.offset = offset
        self.request_id = request_id
        self.results = results
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.offset is not None:
            result['offset'] = self.offset

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.GetEvaluationResultsResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetEvaluationResultsResponseBodyResults(DaraModel):
    def __init__(
        self,
        channel: str = None,
        data_end_time: int = None,
        data_link: Dict[str, Any] = None,
        data_start_time: int = None,
        error_code: str = None,
        error_message: str = None,
        eval_id: str = None,
        eval_info: Dict[str, Any] = None,
        eval_meta: Dict[str, Any] = None,
        eval_metrics: Dict[str, Any] = None,
        evaluation_process: str = None,
        evaluator_name: str = None,
        explanation: str = None,
        result_type: str = None,
        score_name: str = None,
        score_value: float = None,
        status: str = None,
        timestamp: int = None,
    ):
        self.channel = channel
        self.data_end_time = data_end_time
        self.data_link = data_link
        self.data_start_time = data_start_time
        self.error_code = error_code
        self.error_message = error_message
        self.eval_id = eval_id
        self.eval_info = eval_info
        self.eval_meta = eval_meta
        self.eval_metrics = eval_metrics
        self.evaluation_process = evaluation_process
        self.evaluator_name = evaluator_name
        self.explanation = explanation
        self.result_type = result_type
        self.score_name = score_name
        self.score_value = score_value
        self.status = status
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.data_end_time is not None:
            result['dataEndTime'] = self.data_end_time

        if self.data_link is not None:
            result['dataLink'] = self.data_link

        if self.data_start_time is not None:
            result['dataStartTime'] = self.data_start_time

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.eval_id is not None:
            result['evalId'] = self.eval_id

        if self.eval_info is not None:
            result['evalInfo'] = self.eval_info

        if self.eval_meta is not None:
            result['evalMeta'] = self.eval_meta

        if self.eval_metrics is not None:
            result['evalMetrics'] = self.eval_metrics

        if self.evaluation_process is not None:
            result['evaluationProcess'] = self.evaluation_process

        if self.evaluator_name is not None:
            result['evaluatorName'] = self.evaluator_name

        if self.explanation is not None:
            result['explanation'] = self.explanation

        if self.result_type is not None:
            result['resultType'] = self.result_type

        if self.score_name is not None:
            result['scoreName'] = self.score_name

        if self.score_value is not None:
            result['scoreValue'] = self.score_value

        if self.status is not None:
            result['status'] = self.status

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('dataEndTime') is not None:
            self.data_end_time = m.get('dataEndTime')

        if m.get('dataLink') is not None:
            self.data_link = m.get('dataLink')

        if m.get('dataStartTime') is not None:
            self.data_start_time = m.get('dataStartTime')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('evalId') is not None:
            self.eval_id = m.get('evalId')

        if m.get('evalInfo') is not None:
            self.eval_info = m.get('evalInfo')

        if m.get('evalMeta') is not None:
            self.eval_meta = m.get('evalMeta')

        if m.get('evalMetrics') is not None:
            self.eval_metrics = m.get('evalMetrics')

        if m.get('evaluationProcess') is not None:
            self.evaluation_process = m.get('evaluationProcess')

        if m.get('evaluatorName') is not None:
            self.evaluator_name = m.get('evaluatorName')

        if m.get('explanation') is not None:
            self.explanation = m.get('explanation')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        if m.get('scoreName') is not None:
            self.score_name = m.get('scoreName')

        if m.get('scoreValue') is not None:
            self.score_value = m.get('scoreValue')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

