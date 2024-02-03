pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186

def n_root(n, prev_x, mult):
    prev_dif = float('inf')
    x = int(prev_x * mult )-1
    print('int ',x)
    while True:
        x +=1
        root = x ** (1 / n)
        dif = abs(pi - root)
        if prev_dif < dif:
            break
        prev_dif = dif

    return prev_dif, x - 1


prev_x = 10
mult = 1
best_match = float('inf')
for n in range(2, 40):
    dif, x = n_root(n, prev_x, mult)
    mult = x / prev_x
    print(mult, '=',x,'/',prev_x)
    prev_x = x

    print('\nn:', n)
    print('x:', x)
    print('dif:', dif)

    if best_match > dif:
        best_match = dif
        best_x = x
        best_n = n
    print('best match:', best_match)
    print('best_n:', best_n)

print('\n\nFinal result:')
print(best_match)
print(best_x ** (1 / best_n))
print(best_n)
print(best_x)