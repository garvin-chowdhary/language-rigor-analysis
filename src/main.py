from config import LANGUAGES, WEIGHTS
from collections import Counter

from conllu_reader import read_conllu
from dependency_analysis import dependency_depth
from morphology_analysis import morphology_metrics
from ambiguity_analysis import ambiguity_score
from metrics import rule_complexity, regularity_score
from rigor_score import calculate_rigor_score
from visualizer import plot_rigor_scores


def process_language(language, path):

    print(f"\nProcessing {language}...")

    sentences = list(read_conllu(path))

    print(f"{language}: {len(sentences)} sentences")

    total_tokens = 0
    total_depth = 0
    total_ambiguity = 0

    pos_counter = Counter()
    dep_counter = Counter()
    morphology_patterns = Counter()

    # Morphology tracking
    total_features = 0
    total_morph_tokens = 0

    feature_types = set()
    feature_combinations = Counter()

    for sentence in sentences:

        total_depth += dependency_depth(sentence)

        total_ambiguity += ambiguity_score(sentence)

        morph = morphology_metrics(sentence)

        total_features += morph["total_features"]
        total_morph_tokens += morph["morph_tokens"]

        feature_types.update(
            morph["feature_types"]
        )

        feature_combinations.update(
            morph["feature_combinations"]
        )

        for token in sentence:

            total_tokens += 1

            pos_counter[
                token["upos"]
            ] += 1

            dep_counter[
                token["deprel"]
            ] += 1

            feats = token.get("feats")

            if feats and feats != "_":
                morphology_patterns[
                    feats
                ] += 1

    # ----- Morphological Complexity Components -----

    avg_features_per_morph_word = (
    total_features /
    max(total_morph_tokens, 1)
    )

    morphological_coverage = (
        total_morph_tokens /
        max(total_tokens, 1)
    )

    combination_diversity = (
        len(feature_combinations) /
        max(total_morph_tokens, 1)
    )

    # Scale the tiny values into a useful range
    scaled_combination_diversity = (
        combination_diversity * 100
    )

    morphological_complexity = (
        0.60 * avg_features_per_morph_word +
        0.25 * morphological_coverage +
        0.15 * scaled_combination_diversity
    )

    metrics = {

        "rule_complexity":
            rule_complexity(
                pos_counter,
                dep_counter
            ),

        "strictness":
            total_depth /
            max(total_tokens, 1),

        "ambiguity":
            total_ambiguity /
            max(len(sentences), 1),

        "parsing_difficulty":
            total_depth /
            max(total_tokens, 1),

        "morphological_complexity":
            morphological_complexity,

        "regularity":
            regularity_score(
                morphology_patterns,
                total_tokens
            )
    }

    score = calculate_rigor_score(
        metrics,
        WEIGHTS
    )

    result = {
        "Language": language,
        "Score": score,
        **metrics
    }

    print(
        f"Done {language} | "
        f"Score: {score:.4f}"
    )

    print(
        f"Features/word: "
        f"{avg_features_per_morph_word:.3f}"
    )

    print(
        f"Coverage: "
        f"{morphological_coverage:.3f}"
    )

    

    print(
        f"Combination diversity: "
        f"{combination_diversity:.3f}"
    )

    return result


def main():

    print(
        "\nSTARTING MORPHOLOGICAL "
        "COMPLEXITY ANALYSIS\n"
    )

    results = []

    for language, path in LANGUAGES.items():

        results.append(
            process_language(
                language,
                path
            )
        )

    print("\nFINAL RESULTS\n")

    for result in results:
        print(result)

    plot_rigor_scores(
        results
    )

    return results


if __name__ == "__main__":
    main()