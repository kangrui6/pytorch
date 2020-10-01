from typing import List
from enum import Enum

# Defined in tools/autograd/init.cpp

class ProfilerState(Enum):
    Disable = 0
    CPU = 1
    CUDA = 2
    NVTX = 3


class ProfilerConfig:
    def __init__(
        self,
        state: ProfilerState,
        report_input_shapes: bool,
        profile_memory: bool,
        with_stack: bool
    ) -> None: ...
    ...


class ProfilerEvent:
    def cpu_elapsed_us(self, other: ProfilerEvent) -> float: ...
    def cpu_memory_usage(self) -> int: ...
    def cuda_elapsed_us(self, other: ProfilerEvent) -> float: ...
    def cuda_memory_usage(self) -> int: ...
    def device(self) -> int: ...
    def handle(self) -> int: ...
    def has_cuda(self) -> bool: ...
    def is_remote(self) -> bool: ...
    def kind(self) -> int: ...
    def name(self) -> str: ...
    def node_id(self) -> int: ...
    def sequence_nr(self) -> int: ...
    def shapes(self) -> List[List[int]]: ...
    def thread_id(self) -> int: ...
    ...


def _enable_profiler(config: ProfilerConfig) -> None: ...
def _disable_profiler() -> List[List[ProfilerEvent]]: ...
def _profiler_enabled() -> bool: ...
def _enable_record_function(enable: bool) -> None: ...
def _set_empty_test_observer(is_global: bool, sampling_prob: float) -> None: ...
