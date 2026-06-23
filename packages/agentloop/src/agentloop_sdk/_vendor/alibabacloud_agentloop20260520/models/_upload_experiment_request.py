# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UploadExperimentRequest(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        completed_tasks: int = None,
        data_source: Dict[str, Any] = None,
        evaluators: List[main_models.Evaluator] = None,
        executed_at: int = None,
        experiment_config: main_models.ExperimentConfig = None,
        experiment_plan_id: str = None,
        failed_tasks: int = None,
        record_id: str = None,
        record_name: str = None,
        total_tasks: int = None,
    ):
        self.completed_at = completed_at
        self.completed_tasks = completed_tasks
        self.data_source = data_source
        self.evaluators = evaluators
        self.executed_at = executed_at
        self.experiment_config = experiment_config
        self.experiment_plan_id = experiment_plan_id
        self.failed_tasks = failed_tasks
        self.record_id = record_id
        self.record_name = record_name
        self.total_tasks = total_tasks

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.experiment_config:
            self.experiment_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_tasks is not None:
            result['completedTasks'] = self.completed_tasks

        if self.data_source is not None:
            result['dataSource'] = self.data_source

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.executed_at is not None:
            result['executedAt'] = self.executed_at

        if self.experiment_config is not None:
            result['experimentConfig'] = self.experiment_config.to_map()

        if self.experiment_plan_id is not None:
            result['experimentPlanId'] = self.experiment_plan_id

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.record_name is not None:
            result['recordName'] = self.record_name

        if self.total_tasks is not None:
            result['totalTasks'] = self.total_tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedTasks') is not None:
            self.completed_tasks = m.get('completedTasks')

        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('executedAt') is not None:
            self.executed_at = m.get('executedAt')

        if m.get('experimentConfig') is not None:
            temp_model = main_models.ExperimentConfig()
            self.experiment_config = temp_model.from_map(m.get('experimentConfig'))

        if m.get('experimentPlanId') is not None:
            self.experiment_plan_id = m.get('experimentPlanId')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('recordName') is not None:
            self.record_name = m.get('recordName')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        return self

