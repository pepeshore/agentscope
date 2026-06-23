# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class CreateExperimentTaskRequest(DaraModel):
    def __init__(
        self,
        data_source: main_models.CreateExperimentTaskRequestDataSource = None,
        evaluators: List[main_models.Evaluator] = None,
        experiment_plan_id: str = None,
        experiments: List[main_models.ExperimentConfig] = None,
    ):
        self.data_source = data_source
        self.evaluators = evaluators
        self.experiment_plan_id = experiment_plan_id
        self.experiments = experiments

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.experiments:
            for v1 in self.experiments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.experiment_plan_id is not None:
            result['experimentPlanId'] = self.experiment_plan_id

        result['experiments'] = []
        if self.experiments is not None:
            for k1 in self.experiments:
                result['experiments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSource') is not None:
            temp_model = main_models.CreateExperimentTaskRequestDataSource()
            self.data_source = temp_model.from_map(m.get('dataSource'))

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('experimentPlanId') is not None:
            self.experiment_plan_id = m.get('experimentPlanId')

        self.experiments = []
        if m.get('experiments') is not None:
            for k1 in m.get('experiments'):
                temp_model = main_models.ExperimentConfig()
                self.experiments.append(temp_model.from_map(k1))

        return self

class CreateExperimentTaskRequestDataSource(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        input: Dict[str, Any] = None,
        query_sql: str = None,
        selected_item_ids: List[str] = None,
        type: str = None,
    ):
        self.dataset_id = dataset_id
        self.input = input
        self.query_sql = query_sql
        self.selected_item_ids = selected_item_ids
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.input is not None:
            result['input'] = self.input

        if self.query_sql is not None:
            result['querySql'] = self.query_sql

        if self.selected_item_ids is not None:
            result['selectedItemIds'] = self.selected_item_ids

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('querySql') is not None:
            self.query_sql = m.get('querySql')

        if m.get('selectedItemIds') is not None:
            self.selected_item_ids = m.get('selectedItemIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

