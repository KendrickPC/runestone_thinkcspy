def rev(l):
    if not l: return []
    return [l[-1]] + rev(l[:-1])