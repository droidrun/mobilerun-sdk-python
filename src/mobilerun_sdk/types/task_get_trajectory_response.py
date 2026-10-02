# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TaskGetTrajectoryResponse",
    "Trajectory",
    "TrajectoryTrajectoryQueuedEvent",
    "TrajectoryTrajectoryQueuedEventData",
    "TrajectoryTrajectoryCreatedEvent",
    "TrajectoryTrajectoryCreatedEventData",
    "TrajectoryTrajectoryExceptionEvent",
    "TrajectoryTrajectoryExceptionEventData",
    "TrajectoryTrajectoryCancelEvent",
    "TrajectoryTrajectoryCancelEventData",
    "TrajectoryTrajectoryScreenshotEvent",
    "TrajectoryTrajectoryScreenshotEventData",
    "TrajectoryTrajectoryStartEvent",
    "TrajectoryTrajectoryFinalizeEvent",
    "TrajectoryTrajectoryFinalizeEventData",
    "TrajectoryTrajectoryStopEvent",
    "TrajectoryTrajectoryResultEvent",
    "TrajectoryTrajectoryResultEventData",
    "TrajectoryTrajectoryManagerInputEvent",
    "TrajectoryTrajectoryManagerPlanEvent",
    "TrajectoryTrajectoryManagerPlanEventData",
    "TrajectoryTrajectoryExecutorInputEvent",
    "TrajectoryTrajectoryExecutorInputEventData",
    "TrajectoryTrajectoryExecutorResultEvent",
    "TrajectoryTrajectoryExecutorResultEventData",
    "TrajectoryTrajectoryFastAgentInputEvent",
    "TrajectoryTrajectoryFastAgentResponseEvent",
    "TrajectoryTrajectoryFastAgentResponseEventData",
    "TrajectoryTrajectoryFastAgentResponseEventDataUsage",
    "TrajectoryTrajectoryFastAgentToolCallEvent",
    "TrajectoryTrajectoryFastAgentToolCallEventData",
    "TrajectoryTrajectoryFastAgentOutputEvent",
    "TrajectoryTrajectoryFastAgentOutputEventData",
    "TrajectoryTrajectoryFastAgentEndEvent",
    "TrajectoryTrajectoryFastAgentEndEventData",
    "TrajectoryTrajectoryFastAgentExecuteEvent",
    "TrajectoryTrajectoryFastAgentExecuteEventData",
    "TrajectoryTrajectoryFastAgentResultEvent",
    "TrajectoryTrajectoryFastAgentResultEventData",
    "TrajectoryTrajectoryToolExecutionEvent",
    "TrajectoryTrajectoryToolExecutionEventData",
    "TrajectoryTrajectoryRecordUiStateEvent",
    "TrajectoryTrajectoryRecordUiStateEventData",
    "TrajectoryTrajectoryManagerContextEvent",
    "TrajectoryTrajectoryManagerResponseEvent",
    "TrajectoryTrajectoryManagerResponseEventData",
    "TrajectoryTrajectoryManagerResponseEventDataUsage",
    "TrajectoryTrajectoryManagerPlanDetailsEvent",
    "TrajectoryTrajectoryManagerPlanDetailsEventData",
    "TrajectoryTrajectoryExecutorContextEvent",
    "TrajectoryTrajectoryExecutorContextEventData",
    "TrajectoryTrajectoryExecutorResponseEvent",
    "TrajectoryTrajectoryExecutorResponseEventData",
    "TrajectoryTrajectoryExecutorResponseEventDataUsage",
    "TrajectoryTrajectoryExecutorActionEvent",
    "TrajectoryTrajectoryExecutorActionEventData",
    "TrajectoryTrajectoryExecutorActionResultEvent",
    "TrajectoryTrajectoryExecutorActionResultEventData",
    "TrajectoryTrajectoryUserMessageEvent",
    "TrajectoryTrajectoryUserMessageEventData",
    "TrajectoryTrajectoryUnknownEvent",
]


class TrajectoryTrajectoryQueuedEventData(BaseModel):
    """Emitted to SSE clients when the task is waiting in the device queue."""

    id: str

    status: Optional[str] = None


class TrajectoryTrajectoryQueuedEvent(BaseModel):
    data: TrajectoryTrajectoryQueuedEventData
    """Emitted to SSE clients when the task is waiting in the device queue."""

    event: Literal["QueuedEvent"]


class TrajectoryTrajectoryCreatedEventData(BaseModel):
    id: str

    stream_url: str = FieldInfo(alias="streamUrl")


class TrajectoryTrajectoryCreatedEvent(BaseModel):
    data: TrajectoryTrajectoryCreatedEventData

    event: Literal["CreatedEvent"]


class TrajectoryTrajectoryExceptionEventData(BaseModel):
    exception: str


class TrajectoryTrajectoryExceptionEvent(BaseModel):
    data: TrajectoryTrajectoryExceptionEventData

    event: Literal["ExceptionEvent"]


class TrajectoryTrajectoryCancelEventData(BaseModel):
    reason: str


class TrajectoryTrajectoryCancelEvent(BaseModel):
    data: TrajectoryTrajectoryCancelEventData

    event: Literal["CancelEvent"]


class TrajectoryTrajectoryScreenshotEventData(BaseModel):
    index: int

    url: str


class TrajectoryTrajectoryScreenshotEvent(BaseModel):
    data: TrajectoryTrajectoryScreenshotEventData

    event: Literal["ScreenshotEvent"]


class TrajectoryTrajectoryStartEvent(BaseModel):
    data: object

    event: Literal["StartEvent"]


class TrajectoryTrajectoryFinalizeEventData(BaseModel):
    reason: str

    success: bool


class TrajectoryTrajectoryFinalizeEvent(BaseModel):
    data: TrajectoryTrajectoryFinalizeEventData

    event: Literal["FinalizeEvent"]


class TrajectoryTrajectoryStopEvent(BaseModel):
    data: object

    event: Literal["StopEvent"]


class TrajectoryTrajectoryResultEventData(BaseModel):
    """Final result of a task run."""

    message: Optional[str] = None

    steps: Optional[int] = None

    structured_output: Optional[Dict[str, object]] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryResultEvent(BaseModel):
    data: TrajectoryTrajectoryResultEventData
    """Final result of a task run."""

    event: Literal["ResultEvent"]


class TrajectoryTrajectoryManagerInputEvent(BaseModel):
    data: object

    event: Literal["ManagerInputEvent"]


class TrajectoryTrajectoryManagerPlanEventData(BaseModel):
    current_subgoal: str

    plan: str

    thought: str

    answer: Optional[str] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryManagerPlanEvent(BaseModel):
    data: TrajectoryTrajectoryManagerPlanEventData

    event: Literal["ManagerPlanEvent"]


class TrajectoryTrajectoryExecutorInputEventData(BaseModel):
    current_subgoal: str


class TrajectoryTrajectoryExecutorInputEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorInputEventData

    event: Literal["ExecutorInputEvent"]


class TrajectoryTrajectoryExecutorResultEventData(BaseModel):
    action: Dict[str, object]

    error: str

    outcome: bool

    summary: str


class TrajectoryTrajectoryExecutorResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResultEventData

    event: Literal["ExecutorResultEvent"]


class TrajectoryTrajectoryFastAgentInputEvent(BaseModel):
    data: object

    event: Literal["FastAgentInputEvent"]


class TrajectoryTrajectoryFastAgentResponseEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryFastAgentResponseEventData(BaseModel):
    thought: str

    code: Optional[str] = None

    tool_call_status: Optional[Literal["valid", "no_markup", "malformed"]] = None
    """Classification of tool-call markup in an LLM response."""

    usage: Optional[TrajectoryTrajectoryFastAgentResponseEventDataUsage] = None


class TrajectoryTrajectoryFastAgentResponseEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentResponseEventData

    event: Literal["FastAgentResponseEvent"]


class TrajectoryTrajectoryFastAgentToolCallEventData(BaseModel):
    tool_calls_repr: str


class TrajectoryTrajectoryFastAgentToolCallEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentToolCallEventData

    event: Literal["FastAgentToolCallEvent"]


class TrajectoryTrajectoryFastAgentOutputEventData(BaseModel):
    output: str


class TrajectoryTrajectoryFastAgentOutputEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentOutputEventData

    event: Literal["FastAgentOutputEvent"]


class TrajectoryTrajectoryFastAgentEndEventData(BaseModel):
    reason: str

    success: bool

    tool_call_count: Optional[int] = None


class TrajectoryTrajectoryFastAgentEndEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentEndEventData

    event: Literal["FastAgentEndEvent"]


class TrajectoryTrajectoryFastAgentExecuteEventData(BaseModel):
    instruction: str


class TrajectoryTrajectoryFastAgentExecuteEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentExecuteEventData

    event: Literal["FastAgentExecuteEvent"]


class TrajectoryTrajectoryFastAgentResultEventData(BaseModel):
    instruction: str

    reason: str

    success: bool


class TrajectoryTrajectoryFastAgentResultEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentResultEventData

    event: Literal["FastAgentResultEvent"]


class TrajectoryTrajectoryToolExecutionEventData(BaseModel):
    success: bool

    summary: str

    tool_args: Dict[str, object]

    tool_name: str


class TrajectoryTrajectoryToolExecutionEvent(BaseModel):
    data: TrajectoryTrajectoryToolExecutionEventData

    event: Literal["ToolExecutionEvent"]


class TrajectoryTrajectoryRecordUiStateEventData(BaseModel):
    index: int

    url: str


class TrajectoryTrajectoryRecordUiStateEvent(BaseModel):
    data: TrajectoryTrajectoryRecordUiStateEventData

    event: Literal["RecordUIStateEvent"]


class TrajectoryTrajectoryManagerContextEvent(BaseModel):
    data: object

    event: Literal["ManagerContextEvent"]


class TrajectoryTrajectoryManagerResponseEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryManagerResponseEventData(BaseModel):
    response: str

    usage: Optional[TrajectoryTrajectoryManagerResponseEventDataUsage] = None


class TrajectoryTrajectoryManagerResponseEvent(BaseModel):
    data: TrajectoryTrajectoryManagerResponseEventData

    event: Literal["ManagerResponseEvent"]


class TrajectoryTrajectoryManagerPlanDetailsEventData(BaseModel):
    plan: str

    subgoal: str

    thought: str

    answer: Optional[str] = None

    full_response: Optional[str] = None

    memory_update: Optional[str] = None

    progress_summary: Optional[str] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryManagerPlanDetailsEvent(BaseModel):
    data: TrajectoryTrajectoryManagerPlanDetailsEventData

    event: Literal["ManagerPlanDetailsEvent"]


class TrajectoryTrajectoryExecutorContextEventData(BaseModel):
    subgoal: str


class TrajectoryTrajectoryExecutorContextEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorContextEventData

    event: Literal["ExecutorContextEvent"]


class TrajectoryTrajectoryExecutorResponseEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryExecutorResponseEventData(BaseModel):
    response: str

    usage: Optional[TrajectoryTrajectoryExecutorResponseEventDataUsage] = None


class TrajectoryTrajectoryExecutorResponseEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResponseEventData

    event: Literal["ExecutorResponseEvent"]


class TrajectoryTrajectoryExecutorActionEventData(BaseModel):
    action_json: str

    description: str

    thought: str

    full_response: Optional[str] = None


class TrajectoryTrajectoryExecutorActionEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionEventData

    event: Literal["ExecutorActionEvent"]


class TrajectoryTrajectoryExecutorActionResultEventData(BaseModel):
    action: Dict[str, object]

    error: str

    success: bool

    summary: str

    full_response: Optional[str] = None

    thought: Optional[str] = None


class TrajectoryTrajectoryExecutorActionResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionResultEventData

    event: Literal["ExecutorActionResultEvent"]


class TrajectoryTrajectoryUserMessageEventData(BaseModel):
    """Tracks the lifecycle of an external user message: queued → applied | dropped."""

    action: str

    message_ids: List[str]

    consumer: Optional[str] = None

    reason: Optional[str] = None

    step_number: Optional[int] = None


class TrajectoryTrajectoryUserMessageEvent(BaseModel):
    data: TrajectoryTrajectoryUserMessageEventData
    """Tracks the lifecycle of an external user message: queued → applied | dropped."""

    event: Literal["UserMessageEvent"]


class TrajectoryTrajectoryUnknownEvent(BaseModel):
    event: str

    data: Optional[Dict[str, object]] = None


Trajectory: TypeAlias = Union[
    TrajectoryTrajectoryQueuedEvent,
    TrajectoryTrajectoryCreatedEvent,
    TrajectoryTrajectoryExceptionEvent,
    TrajectoryTrajectoryCancelEvent,
    TrajectoryTrajectoryScreenshotEvent,
    TrajectoryTrajectoryStartEvent,
    TrajectoryTrajectoryFinalizeEvent,
    TrajectoryTrajectoryStopEvent,
    TrajectoryTrajectoryResultEvent,
    TrajectoryTrajectoryManagerInputEvent,
    TrajectoryTrajectoryManagerPlanEvent,
    TrajectoryTrajectoryExecutorInputEvent,
    TrajectoryTrajectoryExecutorResultEvent,
    TrajectoryTrajectoryFastAgentInputEvent,
    TrajectoryTrajectoryFastAgentResponseEvent,
    TrajectoryTrajectoryFastAgentToolCallEvent,
    TrajectoryTrajectoryFastAgentOutputEvent,
    TrajectoryTrajectoryFastAgentEndEvent,
    TrajectoryTrajectoryFastAgentExecuteEvent,
    TrajectoryTrajectoryFastAgentResultEvent,
    TrajectoryTrajectoryToolExecutionEvent,
    TrajectoryTrajectoryRecordUiStateEvent,
    TrajectoryTrajectoryManagerContextEvent,
    TrajectoryTrajectoryManagerResponseEvent,
    TrajectoryTrajectoryManagerPlanDetailsEvent,
    TrajectoryTrajectoryExecutorContextEvent,
    TrajectoryTrajectoryExecutorResponseEvent,
    TrajectoryTrajectoryExecutorActionEvent,
    TrajectoryTrajectoryExecutorActionResultEvent,
    TrajectoryTrajectoryUserMessageEvent,
    TrajectoryTrajectoryUnknownEvent,
]


class TaskGetTrajectoryResponse(BaseModel):
    trajectory: List[Trajectory]
    """The trajectory of the task"""
