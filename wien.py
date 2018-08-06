from sympy.solvers import solve
from sympy import Symbol
c = 0x01d28a9b0563afd0a615b5356015735d4df9b87164ab61f9a66905484bc152a405ce38ca83a2cca2e15ae4b3ec08eae20409263e672fc43f0a51346d940f546d7c9a25d935ca3c2f5401a08dddea575d119a185185cccd0d584a0f15b442457d6f95f9ee12c331f881dc8a4f8c0e0e61cc5b8bb2682b9eac076cc08efc983b4f48
e = 0xebb87cfd7eb8f5a04be73f35afcc8e86b6cfdcc8edbb8d469205a8c418bbd3b9e65f9fa52c664c51dfc88bc2c0f996f1dc4f6e24a15462660f462538ec41e80b34a684cdc6514a54f228a659cd3ca42c56309f3845a2b8a1a55c4cf326f86fb530e2e887c77028a78fa80959f1d9838ebabe9b277064fc2ba95b4ac0e9e435fd
N = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069

def cf_expansion(n, d):
e = []
q = n // d
r = n % d
e.append(q)def get_convergents(e):
n = []
d = []
for i in range(len(e)):
if i == 0:
    ni = e[i]
    di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else:
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]
            n.append(ni)
            d.append(di)
    yield (ni, di)
cf = cf_expansion(N, e)
conv = get_convergents(cf)
d = 0
for pd, pk in conv:
    if pk == 0:
        continue
        possible_phi = (e*pd - 1)//pk
        x = Symbol('x', integer=True)
        roots = solve(x**2 + (possible_phi - N - 1)*x + N, x)if len(roots) == 2:
        p, q = roots
    if p * q == N:
        d = pd
        break

m = hex(pow(c,d,N)).lstrip('0x').rstrip('L')
print m.decode('hex')
