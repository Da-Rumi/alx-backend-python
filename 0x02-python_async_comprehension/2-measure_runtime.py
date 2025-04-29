#!/usr/bin/env python3
"""Task 2's module.
Measures the runtime of running async_comprehension four times in parallel.
"""

import asyncio
import time
from importlib import import_module

async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in parallel and returns total execution time."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
