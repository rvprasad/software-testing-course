import itertools
import sys
import helpers

def all_pairs_shortest_paths(edges):
    # check validity of input
    if not isinstance(edges, list):
        raise ValueError("input is not a list")
    if any(not isinstance(e, tuple) or len(e) != 3 or not isinstance(e[2], int) for e in edges):
        raise ValueError("invalid edges")
        
    if not edges:
        return []
        
    # check for non-positive weights
    if helpers.has_non_positive_weights(edges):
        raise ValueError("non-positive weights are not supported")
    
    # check for multiple edges
    if helpers.has_multiple_edges_between_nodes(edges):
        raise ValueError("multiple edges between nodes are not supported")
        
    # check for connectedness
    if helpers.is_disconnected(edges):
        raise ValueError("disconnected graphs are not supported")
    
    dist = {}
    nodes = helpers.get_nodes(edges)
    for n1 in nodes:
        for n2 in nodes:
            dist[(n1, n2)] = 0 if n1 == n2 else sys.maxsize
    for n1, n2, d in edges:
        dist[(n1, n2)] = d
        dist[(n2, n1)] = d
    for k in nodes:
        for n1 in nodes:
            for n2 in nodes:
                if dist[(n1, n2)] > dist[(n1, k)] + dist[(k, n2)]:
                    dist[(n1, n2)] = dist[(n1, k)] + dist[(k, n2)]

    for n1 in nodes:
        for n2 in nodes:
            if (n2, n1) in dist or n1 == n2:
                dist.pop((n1, n2))

    return [(k[0], k[1], dist[k]) for k in dist]
