# -*- coding: utf-8 -*-
"""Mixin that overrides EvaluatorBase.aggregate() with logger-based output."""
import collections
import json
import logging
from collections import defaultdict

from agentscope.evaluate import MetricType

_logger = logging.getLogger("agentloop_sdk")


class AggregateMixin:
    """Override aggregate() to use logger.info instead of print()."""

    async def aggregate(self) -> None:
        meta_info: dict = {
            "total_tasks": len(self.benchmark),
            "total_repeats": self.n_repeat,
            "total_stats": {
                "llm": defaultdict(int),
                "agent": 0,
                "tool": defaultdict(int),
                "embedding": defaultdict(int),
                "chat_usage": {},
            },
            "repeats": {},
            "schema_version": 1,
        }

        for repeat_index in range(self.n_repeat):
            repeat_id = str(repeat_index)
            current_repeat: dict = {
                "completed_tasks": 0,
                "incomplete_tasks": 0,
                "metrics": {},
                "completed_ids": [],
                "incomplete_ids": [],
                "stats": {
                    "llm": defaultdict(int),
                    "agent": 0,
                    "tool": defaultdict(int),
                    "embedding": defaultdict(int),
                    "chat_usage": {},
                },
            }
            for task in self.benchmark:
                current_stats = self.storage.get_solution_stats(
                    task.id,
                    repeat_id,
                )

                for model_name, cnt in current_stats.get("llm", {}).items():
                    current_repeat["stats"]["llm"][model_name] += cnt

                current_repeat["stats"]["agent"] += current_stats.get(
                    "agent",
                    0,
                )

                for tool_name, cnt in current_stats.get("tool", {}).items():
                    current_repeat["stats"]["tool"][tool_name] += cnt

                for embedding_model, cnt in current_stats.get(
                    "embedding",
                    {},
                ).items():
                    current_repeat["stats"]["embedding"][
                        embedding_model
                    ] += cnt

                for model_name, usage in current_stats.get(
                    "chat_usage",
                    {},
                ).items():
                    if model_name not in current_repeat["stats"]["chat_usage"]:
                        current_repeat["stats"]["chat_usage"][
                            model_name
                        ] = defaultdict(int)
                    current_repeat["stats"]["chat_usage"][model_name][
                        "input_tokens"
                    ] += usage.get("input_tokens", 0)
                    current_repeat["stats"]["chat_usage"][model_name][
                        "output_tokens"
                    ] += usage.get("output_tokens", 0)

                for metric in task.metrics:
                    if metric.name not in current_repeat["metrics"]:
                        current_repeat["metrics"][metric.name] = {
                            "type": metric.metric_type,
                            "involved_tasks": 0,
                            "completed_tasks": 0,
                            "incomplete_tasks": 0,
                            "aggregation": {},
                            "distribution": collections.defaultdict(list),
                        }

                    current_repeat["metrics"][metric.name][
                        "involved_tasks"
                    ] += 1

                    if not self.storage.evaluation_result_exists(
                        task.id,
                        repeat_id,
                        metric.name,
                    ):
                        if task.id not in current_repeat["incomplete_ids"]:
                            current_repeat["incomplete_tasks"] += 1
                            current_repeat["incomplete_ids"].append(task.id)
                        current_repeat["metrics"][metric.name][
                            "incomplete_tasks"
                        ] += 1
                        continue

                    if task.id not in current_repeat["completed_ids"]:
                        current_repeat["completed_tasks"] += 1
                        current_repeat["completed_ids"].append(task.id)
                    current_repeat["metrics"][metric.name][
                        "completed_tasks"
                    ] += 1

                    eval_result = self.storage.get_evaluation_result(
                        task.id,
                        repeat_id,
                        metric.name,
                    )

                    if metric.metric_type == MetricType.CATEGORY:
                        current_repeat["metrics"][metric.name]["distribution"][
                            eval_result.result
                        ].append(
                            task.id,
                        )

                    elif metric.metric_type == MetricType.NUMERICAL:
                        current_repeat["metrics"][metric.name]["distribution"][
                            task.id
                        ] = eval_result.result

            _logger.info("Repeat ID: %s", repeat_id)

            for metric, value in current_repeat["metrics"].items():
                if value["type"] == MetricType.CATEGORY:
                    for category, task_ids in value["distribution"].items():
                        value["aggregation"][category] = (
                            len(task_ids) * 1.0 / value["involved_tasks"]
                        )

                elif value["type"] == MetricType.NUMERICAL:
                    scores = list(value["distribution"].values())
                    value["aggregation"] = {
                        "mean": sum(scores) / value["involved_tasks"],
                        "max": max(scores),
                        "min": min(scores),
                    }

                agg_str = json.dumps(
                    value["aggregation"],
                    indent=4,
                    ensure_ascii=False,
                ).replace("\n", "\n\t\t")
                _logger.info(
                    "Metric: %s | Type: %s | "
                    "Involved: %d | Completed: %d | Incomplete: %d\n"
                    "\t\tAggregation: %s",
                    metric,
                    value["type"],
                    value["involved_tasks"],
                    value["completed_tasks"],
                    value["incomplete_tasks"],
                    agg_str,
                )

            meta_info["repeats"][repeat_id] = current_repeat

            repeat_stats = current_repeat["stats"]

            for model_name, cnt in repeat_stats.get("llm", {}).items():
                meta_info["total_stats"]["llm"][model_name] += cnt

            meta_info["total_stats"]["agent"] += repeat_stats.get("agent", 0)

            for tool_name, cnt in repeat_stats.get("tool", {}).items():
                meta_info["total_stats"]["tool"][tool_name] += cnt

            for embedding_model, cnt in repeat_stats.get(
                "embedding",
                {},
            ).items():
                meta_info["total_stats"]["embedding"][embedding_model] += cnt

            for model_name, usage in repeat_stats.get(
                "chat_usage",
                {},
            ).items():
                if model_name not in meta_info["total_stats"]["chat_usage"]:
                    meta_info["total_stats"]["chat_usage"][
                        model_name
                    ] = defaultdict(int)
                meta_info["total_stats"]["chat_usage"][model_name][
                    "input_tokens"
                ] += usage.get("input_tokens", 0)
                meta_info["total_stats"]["chat_usage"][model_name][
                    "output_tokens"
                ] += usage.get("output_tokens", 0)

        self.storage.save_aggregation_result(meta_info)
