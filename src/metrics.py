import math
from collections import Counter


def entropy(counter):

    total = sum(counter.values())

    if total == 0:
        return 0

    return -sum(
        (c / total) * math.log((c / total) + 1e-9)
        for c in counter.values()
    )


def normalized_entropy(counter):

    ent = entropy(counter)

    return ent / math.log(len(counter) + 2)


def rule_complexity(pos_counter, dep_counter):

    return normalized_entropy(pos_counter) + normalized_entropy(dep_counter)


def regularity_score(patterns, total_tokens):

    if total_tokens == 0:
        return 0

    return sum(patterns.values()) / total_tokens