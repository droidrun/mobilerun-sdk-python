# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

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
    "TrajectoryTrajectoryTaskRunnerEvent",
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
    "TrajectoryTrajectoryScripterExecutorInputEvent",
    "TrajectoryTrajectoryScripterExecutorInputEventData",
    "TrajectoryTrajectoryScripterExecutorResultEvent",
    "TrajectoryTrajectoryScripterExecutorResultEventData",
    "TrajectoryTrajectoryPlanCreatedEvent",
    "TrajectoryTrajectoryPlanInputEvent",
    "TrajectoryTrajectoryPlanThinkingEvent",
    "TrajectoryTrajectoryTaskThinkingEvent",
    "TrajectoryTrajectoryTaskThinkingEventData",
    "TrajectoryTrajectoryTaskThinkingEventDataUsage",
    "TrajectoryTrajectoryTaskExecutionEvent",
    "TrajectoryTrajectoryTaskExecutionEventData",
    "TrajectoryTrajectoryTaskExecutionResultEvent",
    "TrajectoryTrajectoryTaskExecutionResultEventData",
    "TrajectoryTrajectoryTaskEndEvent",
    "TrajectoryTrajectoryTaskEndEventData",
    "TrajectoryTrajectoryCodeActExecuteEvent",
    "TrajectoryTrajectoryCodeActExecuteEventData",
    "TrajectoryTrajectoryCodeActResultEvent",
    "TrajectoryTrajectoryCodeActResultEventData",
    "TrajectoryTrajectoryTapActionEvent",
    "TrajectoryTrajectoryTapActionEventData",
    "TrajectoryTrajectorySwipeActionEvent",
    "TrajectoryTrajectorySwipeActionEventData",
    "TrajectoryTrajectoryDragActionEvent",
    "TrajectoryTrajectoryDragActionEventData",
    "TrajectoryTrajectoryInputTextActionEvent",
    "TrajectoryTrajectoryInputTextActionEventData",
    "TrajectoryTrajectoryKeyPressActionEvent",
    "TrajectoryTrajectoryKeyPressActionEventData",
    "TrajectoryTrajectoryStartAppEvent",
    "TrajectoryTrajectoryStartAppEventData",
    "TrajectoryTrajectoryRecordUiStateEvent",
    "TrajectoryTrajectoryRecordUiStateEventData",
    "TrajectoryTrajectoryWaitEvent",
    "TrajectoryTrajectoryWaitEventData",
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
    "TrajectoryTrajectoryScripterInputEvent",
    "TrajectoryTrajectoryScripterInputEventData",
    "TrajectoryTrajectoryScripterThinkingEvent",
    "TrajectoryTrajectoryScripterThinkingEventData",
    "TrajectoryTrajectoryScripterThinkingEventDataUsage",
    "TrajectoryTrajectoryScripterExecutionEvent",
    "TrajectoryTrajectoryScripterExecutionEventData",
    "TrajectoryTrajectoryScripterExecutionResultEvent",
    "TrajectoryTrajectoryScripterExecutionResultEventData",
    "TrajectoryTrajectoryScripterEndEvent",
    "TrajectoryTrajectoryScripterEndEventData",
    "TrajectoryTrajectoryTextManipulatorInputEvent",
    "TrajectoryTrajectoryTextManipulatorInputEventData",
    "TrajectoryTrajectoryTextManipulatorResultEvent",
    "TrajectoryTrajectoryTextManipulatorResultEventData",
]


class TrajectoryTrajectoryCreatedEventData(BaseModel):
    id: str

    token: str

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


class TrajectoryTrajectoryTaskRunnerEvent(BaseModel):
    data: object

    event: Literal["TaskRunnerEvent"]


class TrajectoryTrajectoryFinalizeEventData(BaseModel):
    reason: str

    success: bool


class TrajectoryTrajectoryFinalizeEvent(BaseModel):
    data: TrajectoryTrajectoryFinalizeEventData

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
    reason: str

    steps: int

    structured_output: Optional[object] = None

    success: bool


class TrajectoryTrajectoryResultEvent(BaseModel):
    data: TrajectoryTrajectoryResultEventData
    """DroidAgent final result event.

    Returned by DroidAgent.run() with attributes:

    - success: Whether the task completed successfully
    - reason: Explanation of the result or error message
    - steps: Number of steps taken
    - structured_output: Extracted structured data (if output_model was provided)
    """

    event: Literal["ResultEvent"]


class TrajectoryTrajectoryManagerInputEvent(BaseModel):
    data: object
    """Trigger Manager workflow for planning"""

    event: Literal["ManagerInputEvent"]


class TrajectoryTrajectoryManagerPlanEventData(BaseModel):
    current_subgoal: str

    plan: str

    thought: str

    manager_answer: Optional[str] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryManagerPlanEvent(BaseModel):
    data: TrajectoryTrajectoryManagerPlanEventData
    """Coordination event from ManagerAgent to DroidAgent.

    Used for workflow step routing only (NOT streamed to frontend). For internal
    events with memory_update metadata, see ManagerPlanDetailsEvent.
    """

    event: Literal["ManagerPlanEvent"]


class TrajectoryTrajectoryExecutorInputEventData(BaseModel):
    current_subgoal: str


class TrajectoryTrajectoryExecutorInputEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorInputEventData
    """Trigger Executor workflow for action execution"""

    event: Literal["ExecutorInputEvent"]


class TrajectoryTrajectoryExecutorResultEventData(BaseModel):
    action: Dict[str, object]

    error: str

    outcome: bool

    summary: str

    full_response: Optional[str] = None


class TrajectoryTrajectoryExecutorResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResultEventData
    """Coordination event from ExecutorAgent to DroidAgent.

    Used for workflow step routing only (NOT streamed to frontend). For internal
    events with thought/action_json metadata, see ExecutorActionResultEvent.
    """

    event: Literal["ExecutorResultEvent"]


class TrajectoryTrajectoryScripterExecutorInputEventData(BaseModel):
    task: str


class TrajectoryTrajectoryScripterExecutorInputEvent(BaseModel):
    data: TrajectoryTrajectoryScripterExecutorInputEventData
    """Trigger ScripterAgent workflow for off-device operations"""

    event: Literal["ScripterExecutorInputEvent"]


class TrajectoryTrajectoryScripterExecutorResultEventData(BaseModel):
    code_executions: int

    message: str

    success: bool

    task: str


class TrajectoryTrajectoryScripterExecutorResultEvent(BaseModel):
    data: TrajectoryTrajectoryScripterExecutorResultEventData
    """Coordination event from ScripterAgent to DroidAgent.

    Used for workflow step routing only (NOT streamed to frontend).
    """

    event: Literal["ScripterExecutorResultEvent"]


class TrajectoryTrajectoryPlanCreatedEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["PlanCreatedEvent"]


class TrajectoryTrajectoryPlanInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["PlanInputEvent"]


class TrajectoryTrajectoryPlanThinkingEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["PlanThinkingEvent"]


class TrajectoryTrajectoryTaskThinkingEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryTaskThinkingEventData(BaseModel):
    code: Optional[str] = None

    thoughts: Optional[str] = None

    usage: Optional[TrajectoryTrajectoryTaskThinkingEventDataUsage] = None


class TrajectoryTrajectoryTaskThinkingEvent(BaseModel):
    data: TrajectoryTrajectoryTaskThinkingEventData

    event: Literal["TaskThinkingEvent"]


class TrajectoryTrajectoryTaskExecutionEventData(BaseModel):
    code: str

    globals: Optional[Dict[str, str]] = None

    locals: Optional[Dict[str, str]] = None


class TrajectoryTrajectoryTaskExecutionEvent(BaseModel):
    data: TrajectoryTrajectoryTaskExecutionEventData

    event: Literal["TaskExecutionEvent"]


class TrajectoryTrajectoryTaskExecutionResultEventData(BaseModel):
    output: str


class TrajectoryTrajectoryTaskExecutionResultEvent(BaseModel):
    data: TrajectoryTrajectoryTaskExecutionResultEventData

    event: Literal["TaskExecutionResultEvent"]


class TrajectoryTrajectoryTaskEndEventData(BaseModel):
    reason: str

    success: bool


class TrajectoryTrajectoryTaskEndEvent(BaseModel):
    data: TrajectoryTrajectoryTaskEndEventData

    event: Literal["TaskEndEvent"]


class TrajectoryTrajectoryCodeActExecuteEventData(BaseModel):
    instruction: str


class TrajectoryTrajectoryCodeActExecuteEvent(BaseModel):
    data: TrajectoryTrajectoryCodeActExecuteEventData

    event: Literal["CodeActExecuteEvent"]


class TrajectoryTrajectoryCodeActResultEventData(BaseModel):
    instruction: str

    reason: str

    success: bool


class TrajectoryTrajectoryCodeActResultEvent(BaseModel):
    data: TrajectoryTrajectoryCodeActResultEventData

    event: Literal["CodeActResultEvent"]


class TrajectoryTrajectoryTapActionEventData(BaseModel):
    action_type: str

    description: str

    x: int

    y: int

    element_bounds: Optional[str] = None

    element_index: Optional[int] = None

    element_text: Optional[str] = None


class TrajectoryTrajectoryTapActionEvent(BaseModel):
    data: TrajectoryTrajectoryTapActionEventData
    """Event for tap actions with coordinates"""

    event: Literal["TapActionEvent"]


class TrajectoryTrajectorySwipeActionEventData(BaseModel):
    action_type: str

    description: str

    duration_ms: int

    end_x: int

    end_y: int

    start_x: int

    start_y: int


class TrajectoryTrajectorySwipeActionEvent(BaseModel):
    data: TrajectoryTrajectorySwipeActionEventData
    """Event for swipe actions with coordinates"""

    event: Literal["SwipeActionEvent"]


class TrajectoryTrajectoryDragActionEventData(BaseModel):
    action_type: str

    description: str

    duration_ms: int

    end_x: int

    end_y: int

    start_x: int

    start_y: int


class TrajectoryTrajectoryDragActionEvent(BaseModel):
    data: TrajectoryTrajectoryDragActionEventData
    """Event for drag actions with coordinates"""

    event: Literal["DragActionEvent"]


class TrajectoryTrajectoryInputTextActionEventData(BaseModel):
    action_type: str

    description: str

    text: str


class TrajectoryTrajectoryInputTextActionEvent(BaseModel):
    data: TrajectoryTrajectoryInputTextActionEventData
    """Event for text input actions"""

    event: Literal["InputTextActionEvent"]


class TrajectoryTrajectoryKeyPressActionEventData(BaseModel):
    action_type: str

    description: str

    keycode: int

    key_name: Optional[str] = None


class TrajectoryTrajectoryKeyPressActionEvent(BaseModel):
    data: TrajectoryTrajectoryKeyPressActionEventData
    """Event for key press actions"""

    event: Literal["KeyPressActionEvent"]


class TrajectoryTrajectoryStartAppEventData(BaseModel):
    action_type: str

    description: str

    package: str

    activity: Optional[str] = None


class TrajectoryTrajectoryStartAppEvent(BaseModel):
    data: TrajectoryTrajectoryStartAppEventData
    """\"Event for starting an app"""

    event: Literal["StartAppEvent"]


class TrajectoryTrajectoryRecordUiStateEventData(BaseModel):
    ui_state: List[Dict[str, object]]


class TrajectoryTrajectoryRecordUiStateEvent(BaseModel):
    data: TrajectoryTrajectoryRecordUiStateEventData

    event: Literal["RecordUIStateEvent"]


class TrajectoryTrajectoryWaitEventData(BaseModel):
    action_type: str

    description: str

    duration: float


class TrajectoryTrajectoryWaitEvent(BaseModel):
    data: TrajectoryTrajectoryWaitEventData
    """Event for wait/sleep actions"""

    event: Literal["WaitEvent"]


class TrajectoryTrajectoryManagerContextEvent(BaseModel):
    data: object
    """Manager context prepared, ready for LLM call"""

    event: Literal["ManagerContextEvent"]


class TrajectoryTrajectoryManagerResponseEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryManagerResponseEventData(BaseModel):
    output_planning: str

    usage: Optional[TrajectoryTrajectoryManagerResponseEventDataUsage] = None


class TrajectoryTrajectoryManagerResponseEvent(BaseModel):
    data: TrajectoryTrajectoryManagerResponseEventData
    """Manager has received LLM response, ready for parsing.

    This event carries the raw validated LLM output before parsing.
    """

    event: Literal["ManagerResponseEvent"]


class TrajectoryTrajectoryManagerPlanDetailsEventData(BaseModel):
    current_subgoal: str

    plan: str

    thought: str

    full_response: Optional[str] = None

    manager_answer: Optional[str] = None

    memory_update: Optional[str] = None

    success: Optional[bool] = None


class TrajectoryTrajectoryManagerPlanDetailsEvent(BaseModel):
    data: TrajectoryTrajectoryManagerPlanDetailsEventData
    """Manager planning event with full state and metadata.

    This event is streamed to frontend/logging but NOT used for workflow
    coordination between ManagerAgent and DroidAgent.

    For workflow coordination, see ManagerPlanEvent in droid/events.py
    """

    event: Literal["ManagerPlanDetailsEvent"]


class TrajectoryTrajectoryExecutorContextEventData(BaseModel):
    messages: List[object]

    subgoal: str


class TrajectoryTrajectoryExecutorContextEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorContextEventData
    """Executor context prepared, ready for LLM call"""

    event: Literal["ExecutorContextEvent"]


class TrajectoryTrajectoryExecutorResponseEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryExecutorResponseEventData(BaseModel):
    response_text: str

    usage: Optional[TrajectoryTrajectoryExecutorResponseEventDataUsage] = None


class TrajectoryTrajectoryExecutorResponseEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorResponseEventData
    """Executor has received LLM response, ready for parsing.

    This event carries the raw LLM output before parsing.
    """

    event: Literal["ExecutorResponseEvent"]


class TrajectoryTrajectoryExecutorActionEventData(BaseModel):
    action_json: str

    description: str

    thought: str

    full_response: Optional[str] = None


class TrajectoryTrajectoryExecutorActionEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionEventData
    """Executor action selection event with thought process.

    This event is streamed to frontend/logging but NOT used for workflow
    coordination between ExecutorAgent and DroidAgent.

    For workflow coordination, see ExecutorInputEvent in droid/events.py
    """

    event: Literal["ExecutorActionEvent"]


class TrajectoryTrajectoryExecutorActionResultEventData(BaseModel):
    action: Dict[str, object]

    error: str

    outcome: bool

    summary: str

    action_json: Optional[str] = None

    full_response: Optional[str] = None

    thought: Optional[str] = None


class TrajectoryTrajectoryExecutorActionResultEvent(BaseModel):
    data: TrajectoryTrajectoryExecutorActionResultEventData
    """Executor action result event with full debug information.

    This event is streamed to frontend/logging but NOT used for workflow
    coordination between ExecutorAgent and DroidAgent.

    For workflow coordination, see ExecutorResultEvent in droid/events.py
    """

    event: Literal["ExecutorActionResultEvent"]


class TrajectoryTrajectoryScripterInputEventData(BaseModel):
    input: List[object]


class TrajectoryTrajectoryScripterInputEvent(BaseModel):
    data: TrajectoryTrajectoryScripterInputEventData
    """Input to LLM (chat history)."""

    event: Literal["ScripterInputEvent"]


class TrajectoryTrajectoryScripterThinkingEventDataUsage(BaseModel):
    request_tokens: int

    requests: int

    response_tokens: int

    total_tokens: int


class TrajectoryTrajectoryScripterThinkingEventData(BaseModel):
    thoughts: str

    code: Optional[str] = None

    full_response: Optional[str] = None

    usage: Optional[TrajectoryTrajectoryScripterThinkingEventDataUsage] = None


class TrajectoryTrajectoryScripterThinkingEvent(BaseModel):
    data: TrajectoryTrajectoryScripterThinkingEventData
    """LLM generated thought + code."""

    event: Literal["ScripterThinkingEvent"]


class TrajectoryTrajectoryScripterExecutionEventData(BaseModel):
    code: str


class TrajectoryTrajectoryScripterExecutionEvent(BaseModel):
    data: TrajectoryTrajectoryScripterExecutionEventData
    """Trigger code execution."""

    event: Literal["ScripterExecutionEvent"]


class TrajectoryTrajectoryScripterExecutionResultEventData(BaseModel):
    output: str


class TrajectoryTrajectoryScripterExecutionResultEvent(BaseModel):
    data: TrajectoryTrajectoryScripterExecutionResultEventData
    """Code execution result."""

    event: Literal["ScripterExecutionResultEvent"]


class TrajectoryTrajectoryScripterEndEventData(BaseModel):
    message: str

    success: bool

    code_executions: Optional[int] = None


class TrajectoryTrajectoryScripterEndEvent(BaseModel):
    data: TrajectoryTrajectoryScripterEndEventData
    """Script agent finished."""

    event: Literal["ScripterEndEvent"]


class TrajectoryTrajectoryTextManipulatorInputEventData(BaseModel):
    task: str


class TrajectoryTrajectoryTextManipulatorInputEvent(BaseModel):
    data: TrajectoryTrajectoryTextManipulatorInputEventData
    """Trigger TextManipulatorAgent workflow for text manipulation"""

    event: Literal["TextManipulatorInputEvent"]


class TrajectoryTrajectoryTextManipulatorResultEventData(BaseModel):
    code_ran: str

    task: str

    text_to_type: str


class TrajectoryTrajectoryTextManipulatorResultEvent(BaseModel):
    data: TrajectoryTrajectoryTextManipulatorResultEventData

    event: Literal["TextManipulatorResultEvent"]


Trajectory: TypeAlias = Union[
    TrajectoryTrajectoryCreatedEvent,
    TrajectoryTrajectoryExceptionEvent,
    TrajectoryTrajectoryCancelEvent,
    TrajectoryTrajectoryScreenshotEvent,
    TrajectoryTrajectoryStartEvent,
    TrajectoryTrajectoryTaskRunnerEvent,
    TrajectoryTrajectoryFinalizeEvent,
    TrajectoryTrajectoryStopEvent,
    TrajectoryTrajectoryResultEvent,
    TrajectoryTrajectoryManagerInputEvent,
    TrajectoryTrajectoryManagerPlanEvent,
    TrajectoryTrajectoryExecutorInputEvent,
    TrajectoryTrajectoryExecutorResultEvent,
    TrajectoryTrajectoryScripterExecutorInputEvent,
    TrajectoryTrajectoryScripterExecutorResultEvent,
    TrajectoryTrajectoryPlanCreatedEvent,
    TrajectoryTrajectoryPlanInputEvent,
    TrajectoryTrajectoryPlanThinkingEvent,
    TrajectoryTrajectoryTaskThinkingEvent,
    TrajectoryTrajectoryTaskExecutionEvent,
    TrajectoryTrajectoryTaskExecutionResultEvent,
    TrajectoryTrajectoryTaskEndEvent,
    TrajectoryTrajectoryCodeActExecuteEvent,
    TrajectoryTrajectoryCodeActResultEvent,
    TrajectoryTrajectoryTapActionEvent,
    TrajectoryTrajectorySwipeActionEvent,
    TrajectoryTrajectoryDragActionEvent,
    TrajectoryTrajectoryInputTextActionEvent,
    TrajectoryTrajectoryKeyPressActionEvent,
    TrajectoryTrajectoryStartAppEvent,
    TrajectoryTrajectoryRecordUiStateEvent,
    TrajectoryTrajectoryWaitEvent,
    TrajectoryTrajectoryManagerContextEvent,
    TrajectoryTrajectoryManagerResponseEvent,
    TrajectoryTrajectoryManagerPlanDetailsEvent,
    TrajectoryTrajectoryExecutorContextEvent,
    TrajectoryTrajectoryExecutorResponseEvent,
    TrajectoryTrajectoryExecutorActionEvent,
    TrajectoryTrajectoryExecutorActionResultEvent,
    TrajectoryTrajectoryScripterInputEvent,
    TrajectoryTrajectoryScripterThinkingEvent,
    TrajectoryTrajectoryScripterExecutionEvent,
    TrajectoryTrajectoryScripterExecutionResultEvent,
    TrajectoryTrajectoryScripterEndEvent,
    TrajectoryTrajectoryTextManipulatorInputEvent,
    TrajectoryTrajectoryTextManipulatorResultEvent,
]


class TaskGetTrajectoryResponse(BaseModel):
    trajectory: List[Trajectory]
    """The trajectory of the task"""
