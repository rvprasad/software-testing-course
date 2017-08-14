def get_nodes(edges):
    tmp1, tmp2, _ = zip(*edges)
    return set(tmp1 + tmp2)


def is_disconnected(edges):
    if not edges:
        return False
    else:
        visited = set()
        next = set([edges[0][0]])
        while visited ^ next and next:
            tmp1 = set(e[1] for e in edges if 
                e[0] in next and e[0] not in visited)
            tmp1.update(e[0] for e in edges if 
                e[1] in next and e[1] not in visited)
            visited |= next
            next = tmp1
        return len(get_nodes(edges) - visited) != 0


def has_multiple_edges_between_nodes(edges):
    tmp1 = set(((e[0], e[1]) if e[0] < e[1] else (e[1], e[0])) for e in edges)
    return len(tmp1) != len(edges)


def has_loops(edges):
    return edges and any(e[0] == e[1] for e in edges)
    

def has_non_positive_weights(edges):
    return any(e[2] < 1 for e in edges)


