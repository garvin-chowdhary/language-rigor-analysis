def dependency_depth(sentence):

    children = {}
    roots = []

    for token in sentence:

        try:
            tid = int(token["id"])
            head = int(token["head"])
        except ValueError:
            continue

        if head == 0:
            roots.append(tid)
        else:
            children.setdefault(head, []).append(tid)

    def dfs(node, visited):

        if node in visited:
            return 0

        visited.add(node)

        max_child_depth = 0

        for child in children.get(node, []):
            max_child_depth = max(
                max_child_depth,
                dfs(child, visited.copy())
            )

        return 1 + max_child_depth

    if not roots:
        return 1

    return max(dfs(root, set()) for root in roots)