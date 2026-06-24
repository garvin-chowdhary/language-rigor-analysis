import matplotlib.pyplot as plt


def plot_rigor_scores(results):

    languages = [r["Language"] for r in results]
    scores = [r["Score"] for r in results]

    plt.figure()

    plt.bar(languages, scores)

    plt.title("Cross-Linguistic Structural Complexity Index")
    plt.xlabel("Language")
    plt.ylabel("Normalized Score (Z-score)")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()