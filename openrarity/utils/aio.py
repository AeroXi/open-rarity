import asyncio
from typing import Any, Coroutine

from tqdm.asyncio import tqdm_asyncio  # type: ignore


async def semaphore_gather(num: int, coros: Coroutine[Any, Any, Any]) -> list[Any]:
    semaphore = asyncio.Semaphore(num)

    async def _wrap_coro(coro: Coroutine[Any, Any, Any]):
        async with semaphore:
            return await coro

    return await tqdm_asyncio.gather(  # type: ignore
        *(_wrap_coro(coro) for coro in coros)  # type: ignore
    )


def raise_exception(exception: Exception):
    raise exception