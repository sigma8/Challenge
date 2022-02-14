
def firstAdd(M, N):
    try:
        M.sort()
        for i, j in enumerate(M):
            for z in range(i, len(M)):
                add_numbers = M[z] + j
                if add_numbers == N:
                    primero = j
                    segundo = M[z]
                    return add_numbers, primero, segundo
    except Exception:
        return 'is not what you need'


