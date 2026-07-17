def compare_versions(version1_nodes, version2_nodes):
    
    version1 = {
        node.heading: node.content_hash
        for node in version1_nodes
    }

    version2 = {
        node.heading: node.content_hash
        for node in version2_nodes
    }

    added = []
    removed = []
    modified = []
    unchanged = []

    for heading in version2:

        if heading not in version1:
            added.append(heading)

        elif version1[heading] != version2[heading]:
            modified.append(heading)

        else:
            unchanged.append(heading)

    for heading in version1:

        if heading not in version2:
            removed.append(heading)

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "unchanged": unchanged
    }