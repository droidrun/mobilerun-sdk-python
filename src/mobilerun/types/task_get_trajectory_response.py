# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .usage_result import UsageResult

__all__ = [
    "TaskGetTrajectoryResponse",
    "Trajectory",
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
    "TrajectoryTrajectoryManagerPlanDetailsEvent",
    "TrajectoryTrajectoryManagerPlanDetailsEventData",
    "TrajectoryTrajectoryExecutorContextEvent",
    "TrajectoryTrajectoryExecutorContextEventData",
    "TrajectoryTrajectoryExecutorResponseEvent",
    "TrajectoryTrajectoryExecutorResponseEventData",
    "TrajectoryTrajectoryExecutorActionEvent",
    "TrajectoryTrajectoryExecutorActionEventData",
    "TrajectoryTrajectoryExecutorActionResultEvent",
    "TrajectoryTrajectoryExecutorActionResultEventData",
    "TrajectoryTrajectoryUserMessageEvent",
    "TrajectoryTrajectoryUserMessageEventData",
    "TrajectoryTrajectoryUnknownEvent",
]


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
    """Implicit entry event sent to kick off a `Workflow.run()`."""

    event: Literal["StartEvent"]


class TrajectoryTrajectoryFinalizeEventData(BaseModel):
    """Trigger finalization."""

    reason: str

    success: bool


class TrajectoryTrajectoryFinalizeEvent(BaseModel):
    data: TrajectoryTrajectoryFinalizeEventData
    """Trigger finalization."""

    event: Literal["FinalizeEvent"]


class TrajectoryTrajectoryStopEvent(BaseModel):
    data: object
    """Terminal event that signals the workflow has completed.

    The `result` property contains the return value of the workflow run. When a
    custom stop event subclass is used, the workflow result is that event instance
    itself.

    Examples:
    `python # default stop event: result holds the value return StopEvent(result={"answer": 42}) `

        Subclassing to provide a custom result:

        ```python
        class MyStopEv(StopEvent):
            pass

        @step
        async def my_step(self, ctx: Context, ev: StartEvent) -> MyStopEv:
            return MyStopEv(result={"answer": 42})
    """

    event: Literal["StopEvent"]


class TrajectoryTrajectoryResultEventData(BaseModel):
    """Lazy wrapper — avoids importing droidrun at module level.

    The worker uses droidrun's ResultEvent directly; this model only
    exists so the API OpenAPI schema can reference it without the heavy
    droidrun import.
    """

    message: Optional[str] = None

    steps: Optional[int] = None

    structured_output: Optional[Dict[str, object]] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryResultEvent(BaseModel):
    data: TrajectoryTrajectoryResultEventData
    """Lazy wrapper — avoids importing droidrun at module level.

    The worker uses droidrun's ResultEvent directly; this model only exists so the
    API OpenAPI schema can reference it without the heavy droidrun import.
    """

    event: Literal["ResultEvent"]


class TrajectoryTrajectoryManagerInputEvent(BaseModel):
    data: object
    """Trigger Manager workflow for planning"""

    event: Literal["ManagerInputEvent"]


class TrajectoryTrajectoryManagerPlanEventData(BaseModel):
    """Coordination event from ManagerAgent to DroidAgent.

    Used for workflow step routing only (NOT streamed to frontend).
    For internal events with memory_update metadata, see ManagerPlanDetailsEvent.
    """

    current_subgoal: str

    plan: str

    thought: str

    answer: Optional[str] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryManagerPlanEvent(BaseModel):
    data: TrajectoryTrajectoryManagerPlanEventData
    """Coordination event from ManagerAgent to DroidAgent.

    Used for workflow step routing only (NOT streamed to frontend). For internal
    events with memory_update metadata, see ManagerPlanDetailsEvent.
    """

    event: Literal["ManagerPlanEvent"]


class TrajectoryTrajectoryExecutorInputEventData(BaseModel):
    """Trigger Executor workflow for action execution"""

    current_subgoal: str


class TrajectoryTrajectoryExecutorInputEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorInputEventData
    """Trigger Executor workflow for action execution"""

    event: Literal["ExecutorInputEvent"]


class TrajectoryTrajectoryExecutorResultEventData(BaseModel):
    """Executor finished with action result."""

    action: Dict[str, object]

    error: str

    outcome: bool

    summary: str


class TrajectoryTrajectoryExecutorResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResultEventData
    """Executor finished with action result."""

    event: Literal["ExecutorResultEvent"]


class TrajectoryTrajectoryFastAgentInputEvent(BaseModel):
    data: object
    """Input ready for LLM."""

    event: Literal["FastAgentInputEvent"]


class TrajectoryTrajectoryFastAgentResponseEventData(BaseModel):
    """LLM response received."""

    thought: str

    code: Optional[str] = None

    usage: Optional[UsageResult] = None


class TrajectoryTrajectoryFastAgentResponseEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentResponseEventData
    """LLM response received."""

    event: Literal["FastAgentResponseEvent"]


class TrajectoryTrajectoryFastAgentToolCallEventData(BaseModel):
    """Tool calls ready to execute."""

    tool_calls_repr: str


class TrajectoryTrajectoryFastAgentToolCallEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentToolCallEventData
    """Tool calls ready to execute."""

    event: Literal["FastAgentToolCallEvent"]


class TrajectoryTrajectoryFastAgentOutputEventData(BaseModel):
    """Tool execution result."""

    output: str


class TrajectoryTrajectoryFastAgentOutputEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentOutputEventData
    """Tool execution result."""

    event: Literal["FastAgentOutputEvent"]


class TrajectoryTrajectoryFastAgentEndEventData(BaseModel):
    """FastAgent finished."""

    reason: str

    success: bool

    tool_call_count: Optional[int] = None


class TrajectoryTrajectoryFastAgentEndEvent(BaseModel):
    data: TrajectoryTrajectoryFastAgentEndEventData
    """FastAgent finished."""

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
    """Emitted after every tool call dispatched through ToolRegistry."""

    success: bool

    summary: str

    tool_args: Dict[str, object]

    tool_name: str


class TrajectoryTrajectoryToolExecutionEvent(BaseModel):
    data: TrajectoryTrajectoryToolExecutionEventData
    """Emitted after every tool call dispatched through ToolRegistry."""

    event: Literal["ToolExecutionEvent"]


class TrajectoryTrajectoryRecordUiStateEventData(BaseModel):
    index: int

    url: str


class TrajectoryTrajectoryRecordUiStateEvent(BaseModel):
    data: TrajectoryTrajectoryRecordUiStateEventData

    event: Literal["RecordUIStateEvent"]


class TrajectoryTrajectoryManagerContextEvent(BaseModel):
    data: object
    """Context prepared, ready for LLM call."""

    event: Literal["ManagerContextEvent"]


class TrajectoryTrajectoryManagerResponseEventData(BaseModel):
    """LLM response received, ready for parsing."""

    response: str

    usage: Optional[UsageResult] = None


class TrajectoryTrajectoryManagerResponseEvent(BaseModel):
    data: TrajectoryTrajectoryManagerResponseEventData
    """LLM response received, ready for parsing."""

    event: Literal["ManagerResponseEvent"]


class TrajectoryTrajectoryManagerPlanDetailsEventData(BaseModel):
    """Plan parsed and ready (internal event with full details)."""

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
    """Plan parsed and ready (internal event with full details)."""

    event: Literal["ManagerPlanDetailsEvent"]


class TrajectoryTrajectoryExecutorContextEventData(BaseModel):
    """Context prepared, ready for LLM call."""

    subgoal: str


class TrajectoryTrajectoryExecutorContextEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorContextEventData
    """Context prepared, ready for LLM call."""

    event: Literal["ExecutorContextEvent"]


class TrajectoryTrajectoryExecutorResponseEventData(BaseModel):
    """LLM response received, ready for parsing."""

    response: str

    usage: Optional[UsageResult] = None


class TrajectoryTrajectoryExecutorResponseEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResponseEventData
    """LLM response received, ready for parsing."""

    event: Literal["ExecutorResponseEvent"]


class TrajectoryTrajectoryExecutorActionEventData(BaseModel):
    """Action parsed, ready to execute."""

    action_json: str

    description: str

    thought: str

    full_response: Optional[str] = None


class TrajectoryTrajectoryExecutorActionEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionEventData
    """Action parsed, ready to execute."""

    event: Literal["ExecutorActionEvent"]


class TrajectoryTrajectoryExecutorActionResultEventData(BaseModel):
    """Action execution result (internal event with full details)."""

    action: Dict[str, object]

    error: str

    success: bool

    summary: str

    full_response: Optional[str] = None

    thought: Optional[str] = None


class TrajectoryTrajectoryExecutorActionResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionResultEventData
    """Action execution result (internal event with full details)."""

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
