# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
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
    "TrajectoryTrajectoryStopEvent",
    "TrajectoryTrajectoryResultEvent",
    "TrajectoryTrajectoryManagerInputEvent",
    "TrajectoryTrajectoryManagerPlanEvent",
    "TrajectoryTrajectoryExecutorInputEvent",
    "TrajectoryTrajectoryExecutorResultEvent",
    "TrajectoryTrajectoryScripterExecutorInputEvent",
    "TrajectoryTrajectoryScripterExecutorResultEvent",
    "TrajectoryTrajectoryPlanCreatedEvent",
    "TrajectoryTrajectoryPlanInputEvent",
    "TrajectoryTrajectoryPlanThinkingEvent",
    "TrajectoryTrajectoryTaskInputEvent",
    "TrajectoryTrajectoryTaskThinkingEvent",
    "TrajectoryTrajectoryTaskExecutionEvent",
    "TrajectoryTrajectoryTaskExecutionResultEvent",
    "TrajectoryTrajectoryTaskEndEvent",
    "TrajectoryTrajectoryCodeActExecuteEvent",
    "TrajectoryTrajectoryCodeActResultEvent",
    "TrajectoryTrajectoryTapActionEvent",
    "TrajectoryTrajectorySwipeActionEvent",
    "TrajectoryTrajectoryDragActionEvent",
    "TrajectoryTrajectoryInputTextActionEvent",
    "TrajectoryTrajectoryKeyPressActionEvent",
    "TrajectoryTrajectoryStartAppEvent",
    "TrajectoryTrajectoryRecordUiStateEvent",
    "TrajectoryTrajectoryWaitEvent",
    "TrajectoryTrajectoryManagerContextEvent",
    "TrajectoryTrajectoryManagerResponseEvent",
    "TrajectoryTrajectoryManagerPlanDetailsEvent",
    "TrajectoryTrajectoryExecutorContextEvent",
    "TrajectoryTrajectoryExecutorResponseEvent",
    "TrajectoryTrajectoryExecutorActionEvent",
    "TrajectoryTrajectoryExecutorActionResultEvent",
    "TrajectoryTrajectoryScripterInputEvent",
    "TrajectoryTrajectoryScripterThinkingEvent",
    "TrajectoryTrajectoryScripterExecutionEvent",
    "TrajectoryTrajectoryScripterExecutionResultEvent",
    "TrajectoryTrajectoryScripterEndEvent",
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
    data: Dict[str, object]

    event: Literal["StartEvent"]


class TrajectoryTrajectoryTaskRunnerEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskRunnerEvent"]


class TrajectoryTrajectoryFinalizeEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["FinalizeEvent"]


class TrajectoryTrajectoryStopEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["StopEvent"]


class TrajectoryTrajectoryResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ResultEvent"]


class TrajectoryTrajectoryManagerInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ManagerInputEvent"]


class TrajectoryTrajectoryManagerPlanEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ManagerPlanEvent"]


class TrajectoryTrajectoryExecutorInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorInputEvent"]


class TrajectoryTrajectoryExecutorResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorResultEvent"]


class TrajectoryTrajectoryScripterExecutorInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterExecutorInputEvent"]


class TrajectoryTrajectoryScripterExecutorResultEvent(BaseModel):
    data: Dict[str, object]

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


class TrajectoryTrajectoryTaskInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskInputEvent"]


class TrajectoryTrajectoryTaskThinkingEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskThinkingEvent"]


class TrajectoryTrajectoryTaskExecutionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskExecutionEvent"]


class TrajectoryTrajectoryTaskExecutionResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskExecutionResultEvent"]


class TrajectoryTrajectoryTaskEndEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TaskEndEvent"]


class TrajectoryTrajectoryCodeActExecuteEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["CodeActExecuteEvent"]


class TrajectoryTrajectoryCodeActResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["CodeActResultEvent"]


class TrajectoryTrajectoryTapActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["TapActionEvent"]


class TrajectoryTrajectorySwipeActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["SwipeActionEvent"]


class TrajectoryTrajectoryDragActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["DragActionEvent"]


class TrajectoryTrajectoryInputTextActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["InputTextActionEvent"]


class TrajectoryTrajectoryKeyPressActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["KeyPressActionEvent"]


class TrajectoryTrajectoryStartAppEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["StartAppEvent"]


class TrajectoryTrajectoryRecordUiStateEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["RecordUIStateEvent"]


class TrajectoryTrajectoryWaitEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["WaitEvent"]


class TrajectoryTrajectoryManagerContextEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ManagerContextEvent"]


class TrajectoryTrajectoryManagerResponseEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ManagerResponseEvent"]


class TrajectoryTrajectoryManagerPlanDetailsEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ManagerPlanDetailsEvent"]


class TrajectoryTrajectoryExecutorContextEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorContextEvent"]


class TrajectoryTrajectoryExecutorResponseEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorResponseEvent"]


class TrajectoryTrajectoryExecutorActionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorActionEvent"]


class TrajectoryTrajectoryExecutorActionResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ExecutorActionResultEvent"]


class TrajectoryTrajectoryScripterInputEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterInputEvent"]


class TrajectoryTrajectoryScripterThinkingEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterThinkingEvent"]


class TrajectoryTrajectoryScripterExecutionEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterExecutionEvent"]


class TrajectoryTrajectoryScripterExecutionResultEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterExecutionResultEvent"]


class TrajectoryTrajectoryScripterEndEvent(BaseModel):
    data: Dict[str, object]

    event: Literal["ScripterEndEvent"]


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
    TrajectoryTrajectoryTaskInputEvent,
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
]


class TaskGetTrajectoryResponse(BaseModel):
    trajectory: List[Trajectory]
    """The trajectory of the task"""
