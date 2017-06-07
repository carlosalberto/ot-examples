from ext import tracer
from ext.active_span_source import (
    AsyncioActiveSpanSource,
    ThreadActiveSpanSource,
)

from examples import asyncio, threads


# use a specific ActiveSpanSource implementation


if __name__ == '__main__':
    # asyncio examples
    tracer._active_span_source = AsyncioActiveSpanSource()
    asyncio.coroutine_continue_propagation()
    asyncio.coroutine_with_callbacks()

    # multi-threaded examples
    tracer._active_span_source = ThreadActiveSpanSource()
    threads.main_thread_instrumented_only()
    threads.main_thread_instrumented_children_continue()
    threads.main_thread_instrumented_children_not_continue()
    threads.main_thread_not_instrumented_children()
