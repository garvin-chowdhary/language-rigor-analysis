from collections import Counter

def morphology_metrics(sentence):

    total_features = 0
    morph_tokens = 0

    feature_types = set()
    feature_combinations = Counter()

    for token in sentence:

        feats = token.get("feats", "_")

        if feats == "_":
            continue

        morph_tokens += 1

        split_feats = feats.split("|")

        total_features += len(split_feats)

        categories = []

        for feat in split_feats:

            if "=" in feat:
                category, value = feat.split("=", 1)

                feature_types.add(category)
                categories.append(category)

        categories.sort()

        feature_combinations[
            tuple(categories)
        ] += 1

    return {
        "total_features": total_features,
        "morph_tokens": morph_tokens,
        "feature_types": feature_types,
        "feature_combinations": feature_combinations
    }