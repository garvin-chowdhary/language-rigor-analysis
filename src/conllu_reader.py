def read_conllu(path):

    sentence = []

    with open(path, encoding="utf8") as f:

        for line in f:

            line = line.strip()

            # blank line means end of sentence
            if line == "":
                if sentence:
                    yield sentence
                    sentence = []
                continue

            # skip comments
            if line.startswith("#"):
                continue

            parts = line.split("\t")

            if len(parts) != 10:
                continue

            # skip multi-word tokens and empty nodes
            if "-" in parts[0] or "." in parts[0]:
                continue

            token = {
                "id": parts[0],
                "form": parts[1],
                "lemma": parts[2],
                "upos": parts[3],
                "xpos": parts[4],
                "feats": parts[5],
                "head": parts[6],
                "deprel": parts[7],
                "deps": parts[8],
                "misc": parts[9]
            }

            sentence.append(token)

    if sentence:
        yield sentence