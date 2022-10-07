from math import log2

from open_rarity.models.collections import AttributeCounted, AttributeStatistic


def information_content(
    counts: list[AttributeCounted], total: int
) -> list[AttributeStatistic]:
    return [
        {
            **attr,
            "probability": attr["count"] / total,
            "ic": -log2(attr["count"] / total),
        }
        for attr in counts
    ]


def entropy(attr_stats: list[AttributeStatistic]):
    ...
