import asyncio
import concurrent.futures
import time

from crewai.tools import BaseTool

from .cache import cache
from .monitoring import (
    fetch_logs,
    fetch_metrics,
    fetch_service_status,
)


async def retry_with_fallback(
    operation,
    fallback_value,
    retries=3,
):
    for attempt in range(1, retries + 1):

        try:
            return await operation()

        except Exception as error:

            print(
                f"[RETRY {attempt}/{retries}] "
                f"Operation failed: {error}"
            )

            if attempt < retries:
                await asyncio.sleep(1)

    print("[FALLBACK] Returning graceful fallback.")

    return fallback_value


async def investigate_service_async(
    service_name: str,
):
    start_time = time.perf_counter()

    logs_task = retry_with_fallback(
        lambda: fetch_logs(service_name),
        "LOG DATA UNAVAILABLE",
    )

    metrics_task = retry_with_fallback(
        lambda: fetch_metrics(service_name),
        {"status": "METRICS UNAVAILABLE"},
    )

    status_task = retry_with_fallback(
        lambda: fetch_service_status(service_name),
        {"status": "STATUS UNKNOWN"},
    )

    logs, metrics, status = await asyncio.gather(
        logs_task,
        metrics_task,
        status_task,
    )

    elapsed = time.perf_counter() - start_time

    print(
        f"[ASYNC] Monitoring sources collected in "
        f"{elapsed:.2f} seconds"
    )

    return {
        "logs": logs,
        "metrics": metrics,
        "service_status": status,
        "collection_time_seconds": round(
            elapsed,
            2,
        ),
    }


class AsyncSystemInvestigationTool(BaseTool):

    name: str = "Async System Investigation Tool"

    description: str = (
        "Investigates a service by concurrently collecting "
        "logs, system metrics, and service status. "
        "Uses asynchronous operations, caching, retry "
        "logic, and graceful fallback."
    )

    def _run(self, service_name: str) -> str:

        cache_key = f"investigation:{service_name}"

        cached_result = cache.get(cache_key)

        if cached_result is not None:
            return str(cached_result)

        def execute_async_collection():
            return asyncio.run(
                investigate_service_async(
                    service_name
                )
            )

        # CrewAI may already be running inside an
        # event loop. Execute our async operation
        # in a separate thread to avoid nesting
        # event loops.
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=1
        ) as executor:

            future = executor.submit(
                execute_async_collection
            )

            result = future.result()

        cache.set(
            cache_key,
            result,
            ttl=60,
        )

        return str(result)


async_investigation_tool = AsyncSystemInvestigationTool()