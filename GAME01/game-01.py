
def firstAdd(M, N):
    try:
        M.sort()
        return [(x, y, x + y) for x in M for y in M if x + y == N][0]
    except Exception:
        return 'is not what you need'
