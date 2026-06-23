# AgentLoop SDK

AgentLoop SDK 是阿里云 [AgentLoop 平台](https://cmsnext.console.aliyun.com/agentloop) 的 Python SDK，用于对 LLM Agent 应用进行离线实验评估。

## 安装

```bash
pip install -i https://test.pypi.org/simple/ agentloop_sdk
```

## 快速开始

```python
import asyncio
from agentloop_sdk import (
    AgentLoopConfig,
    EvaluatorConfig,
    http_solution_with,
    run_experiment_parallel,
)

config = AgentLoopConfig(
    agent_space="my-agent-space",
    dataset="my_dataset",
    region_id="cn-hangzhou",
    experiment_name="my-experiment",
    evaluators=[
        EvaluatorConfig(
            evaluator_ref="Builtin.agent_correctness",
            result_type="score",
            variable_mapping={
                "input": "experiment_input",
                "output": "experiment_output",
                "expected_output": "dataset.expected_output",
            },
        ),
    ],
)

solution = http_solution_with(
    url="https://your-agent-endpoint.com/invoke",
    headers={"key": "your-api-key"},
    body_builder=lambda task: {
        "input": task.input.get("input", ""),
        "stream": False,
    },
    timeout=60.0,
)

asyncio.run(run_experiment_parallel(config=config, solution_fn=solution, n_workers=4))
```

## 凭证配置

SDK 通过阿里云 AccessKey 进行认证，支持两种方式：

**方式一：环境变量（推荐）**

```bash
export AGENTLOOP_AK="your-access-key-id"
export AGENTLOOP_SK="your-access-key-secret"
```

也支持标准阿里云环境变量 `ALIBABA_CLOUD_ACCESS_KEY_ID` / `ALIBABA_CLOUD_ACCESS_KEY_SECRET`。

**方式二：直接传参**

```python
config = AgentLoopConfig(
    agent_space="my-agent-space",
    dataset="my_dataset",
    region_id="cn-hangzhou",
    access_key_id="your-ak",
    access_key_secret="your-sk",
)
```

## AgentLoopConfig

实验的核心配置类。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `agent_space` | `str` | 是 | AgentLoop 空间名称 |
| `dataset` | `str` | 是 | 数据集名称 |
| `region_id` | `str` | 是 | 阿里云地域 ID，如 `"cn-hangzhou"` |
| `experiment_name` | `str` | 否 | 实验名称，默认自动生成 |
| `experiment_config` | `dict` | 否 | 实验配置元数据，如 `{"agent_name": "..."}` |
| `evaluators` | `list[EvaluatorConfig]` | 否 | 评估器配置列表 |
| `project` | `str` | 否 | SLS 项目名，默认从 agent_space 自动解析 |
| `query` | `str` | 否 | 自定义 SQL 查询加载数据 |
| `max_rows` | `int` | 否 | 自动分页加载的最大行数，默认 1000 |
| `ground_truth_field` | `str` | 否 | 数据集中标准答案的字段名 |
| `custom_agentloop_endpoint` | `str` | 否 | 自定义 AgentLoop API 地址 |
| `custom_sls_endpoint` | `str` | 否 | 自定义 SLS 地址 |

## EvaluatorConfig

评估器配置，用于实验完成后自动触发平台侧评估。

```python
EvaluatorConfig(
    evaluator_ref="Builtin.agent_correctness",  # 平台内置评估器引用
    result_type="score",                         # 结果类型: "score" / "binary" / "text"
    variable_mapping={                           # 变量映射
        "input": "experiment_input",             # 实验输入
        "output": "experiment_output",           # 实验输出
        "expected_output": "dataset.expected_output",  # 数据集字段
    },
)
```

`variable_mapping` 的值支持三种来源：
- `"experiment_input"` — 实验的输入数据
- `"experiment_output"` — Solution 的输出结果
- `"dataset.<column>"` — 数据集中的指定列

## Solution 类型

Solution 定义了如何调用你的 Agent 并获取结果。SDK 提供 HTTP 和命令行两种内置方案。

### http_solution_with

适用于通过 HTTP 接口调用 Agent 的场景，支持普通 JSON 响应和 SSE 流式响应。

**普通 JSON 响应：**

```python
from agentloop_sdk import http_solution_with

solution = http_solution_with(
    url="https://your-agent-endpoint.com/invoke",
    headers={"key": "your-api-key"},
    body_builder=lambda task: {
        "input": task.input.get("input", ""),
        "stream": False,
    },
    timeout=60.0,
)
```

**SSE 流式响应：**

当 Agent 端点返回 `text/event-stream` 格式时，SDK 自动检测并解析 SSE，提取所有 `data:` 行内容拼接为最终结果。

```python
solution = http_solution_with(
    url="https://your-agent-endpoint.com/invoke",
    headers={"key": "your-api-key"},
    body_builder=lambda task: {
        "input": task.input.get("input", ""),
        "stream": True,
    },
    timeout=120.0,
)
```

如果 SSE 的每个 chunk 是 JSON，可以通过 `chunk_extractor` 指定提取哪个字段：

```python
# 每个 SSE chunk: data: {"output": "你好", "model": "qwen-max"}
# chunk_extractor 提取 output 字段，最终拼接为完整文本
solution = http_solution_with(
    url="https://your-agent-endpoint.com/invoke",
    headers={"key": "your-api-key"},
    body_builder=lambda task: {
        "input": task.input.get("input", ""),
        "stream": True,
    },
    timeout=120.0,
    chunk_extractor=lambda chunk: chunk.get("output", ""),
)
```

**参数说明：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `url` | `str` | 是 | 请求 URL |
| `method` | `str` | 否 | HTTP 方法，默认 `"POST"` |
| `headers` | `dict` | 否 | 请求头，默认 `{"Content-Type": "application/json"}` |
| `body_builder` | `Callable[[Task], Any]` | 否 | 根据 Task 动态构造请求体的函数 |
| `json` | `Any` | 否 | 静态 JSON 请求体（与 `body_builder` 二选一） |
| `timeout` | `float` | 否 | 超时时间（秒），默认 60 |
| `chunk_extractor` | `Callable[[Any], str]` | 否 | SSE chunk JSON 字段提取函数 |

### http_solution

底层 API，适用于需要完全控制请求构造的场景。

```python
from agentloop_sdk import http_solution, HttpRequestSpec

def build_request(task):
    return HttpRequestSpec(
        url="https://your-agent-endpoint.com/invoke",
        headers={"key": "your-api-key"},
        json={"input": task.input.get("input", "")},
    )

solution = http_solution(build_request, default_timeout=60.0)
```

### command_solution_with

适用于通过命令行调用本地 Agent 的场景。

```python
from agentloop_sdk import command_solution_with

# 静态命令
solution = command_solution_with(["python", "agent.py", "--input", "hello"])

# 根据 Task 动态构造命令
solution = command_solution_with(
    lambda task: ["python", "agent.py", "--input", task.input.get("input", "")],
    default_timeout=120.0,
)
```

### command_solution

底层 API，类似 `http_solution`，接受一个 `build_command` 函数。

```python
from agentloop_sdk import command_solution

def build_command(task):
    return ["python", "agent.py", "--input", task.input.get("input", "")]

solution = command_solution(build_command, default_timeout=120.0, cwd="/path/to/agent")
```

## 运行实验

SDK 提供串行和并行两种执行方式。

**串行执行：**

```python
from agentloop_sdk import run_experiment

await run_experiment(
    config=config,
    solution_fn=solution,
    result_dir="./results",
    n_repeat=1,
)
```

**并行执行（推荐）：**

```python
from agentloop_sdk import run_experiment_parallel

await run_experiment_parallel(
    config=config,
    solution_fn=solution,
    result_dir="./results",
    n_repeat=1,
    n_workers=4,  # 并发数
)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `config` | `AgentLoopConfig` | 实验配置 |
| `solution_fn` | `Callable` | Solution 函数 |
| `result_dir` | `str` | 本地结果保存目录，默认 `"./results"` |
| `n_repeat` | `int` | 每个 Task 重复次数，默认 1 |
| `n_workers` | `int` | 并发 worker 数（串行默认 1，并行默认 4） |

## W3C Trace Context

`http_solution` / `http_solution_with` 会自动在请求头中注入符合 W3C Trace Context 规范的 `traceparent` 头，并从响应头中提取 `eagleeye-traceId` 或 `traceId` 用于链路追踪关联。

## 完整示例

```python
import asyncio
from agentloop_sdk import (
    AgentLoopConfig,
    EvaluatorConfig,
    http_solution_with,
    run_experiment_parallel,
)

async def main():
    config = AgentLoopConfig(
        agent_space="default-cn-hangzhou",
        dataset="cc_dataset",
        region_id="cn-hangzhou",
        experiment_name="Offline-Experiment-LocalAgent",
        experiment_config={"agent_name": "LocalAgent"},
        evaluators=[
            EvaluatorConfig(
                evaluator_ref="Builtin.agent_correctness",
                result_type="score",
                variable_mapping={
                    "input": "experiment_input",
                    "output": "experiment_output",
                    "expected_output": "dataset.expected_output",
                },
            ),
        ],
    )

    solution = http_solution_with(
        url="https://your-agent-endpoint.com/invoke",
        headers={"key": "your-api-key"},
        body_builder=lambda task: {
            "input": task.input.get("input", ""),
            "stream": True,
        },
        timeout=120.0,
        chunk_extractor=lambda chunk: chunk.get("output", ""),
    )

    await run_experiment_parallel(
        config=config,
        solution_fn=solution,
        n_workers=4,
    )

if __name__ == "__main__":
    asyncio.run(main())
```
