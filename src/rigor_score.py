def calculate_rigor_score(metrics, weights):

    score = 0

    for k, v in metrics.items():

        score += v * weights.get(k, 0)

    return score