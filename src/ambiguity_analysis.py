def ambiguity_score(sentence):

    ambiguous_labels = {
        "dep",
        "amod",
        "nmod"
    }

    ambiguous_count = 0

    for token in sentence:

        if token["deprel"] in ambiguous_labels:
            ambiguous_count += 1

    return ambiguous_count / max(len(sentence), 1)