from typing import Callable

import psutil
from prometheus_fastapi_instrumentator.metrics import Info
from prometheus_client import Gauge


def resource_usage() -> Callable[[Info], None]:
    system_usage = Gauge(
        "system_usage", "Hold current system resource usage", ["resource_type"]
    )

    def instrumentation(info: Info) -> None:
        system_usage.labels("CPU").set(psutil.cpu_percent())
        system_usage.labels("Memory").set(psutil.virtual_memory()[2])

    return instrumentation
