import asyncio


async def fetch_logs(service_name: str):
    await asyncio.sleep(1)

    return f"""
Service: {service_name}

ERROR payment-service:
Database connection pool exhausted.

Timestamp: 10:42:18

Error rate increased from 1% to 28%.

Multiple requests failed because no database
connections were available.
"""


async def fetch_metrics(service_name: str):
    await asyncio.sleep(1)

    return {
        "service": service_name,
        "cpu_usage": "82%",
        "memory_usage": "76%",
        "error_rate": "28%",
        "response_time": "4.8 seconds",
        "database_connections": "100% utilized",
    }


async def fetch_service_status(service_name: str):
    await asyncio.sleep(1)

    return {
        "service": service_name,
        "status": "DEGRADED",
        "availability": "72%",
        "database": "HEALTHY",
        "api": "DEGRADED",
    }