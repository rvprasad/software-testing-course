def make_power_set(values):
    if not isinstance(values, list):
        raise ValueError("not a list")

    ret = set()
    prev_sets = set([frozenset(values)])
    while prev_sets:
        tmp1 = set()
        for s in prev_sets:
            ret.add(s)
            for v in s:
                tmp2 = s.difference([v])
                tmp1.add(tmp2)
        prev_sets = tmp1
    return ret

    
