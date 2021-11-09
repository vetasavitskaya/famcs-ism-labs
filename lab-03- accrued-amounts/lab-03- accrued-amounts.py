import math
import numpy
import matplotlib.pyplot as plt


def continuous(a,b):
    return float(a+numpy.random.random()*(b-a))


def find_discrete(c, p):
    value = continuous(0, 1.0)
    q = [0, p[0], p[0] + p[1], 1.0]
    if q[0] <= value < q[1]:
        return c[0]
    elif q[1] <= value < q[2]:
        return c[1]
    elif q[2] <= value <= q[3]:
        return c[2]


def original_amount_p(accrued_amount_s_, number_of_days_t, d):
    return accrued_amount_s_ * (1 - (number_of_days_t * d) / 360.0)


def E(p):
    return numpy.mean(p)


def D(p):
    d=E([i**2 for i in p])-E(p)**2
    return d


def p_in_borders(p, lower, upper):
    res=0
    size= len(p)
    for i in p:
        if lower <= i <= upper:
            res=res+1
    return res/size


S = 245000
border_min = 240000
border_max = 241000
n = 1000
p = []
p1 = [0.6, 0.2, 0.2]
p2 = [0.7, 0.2, 0.1]
p3 = p1
c1 = [120, 80, 40]
c2 = [0.06, 0.062, 0.064]
c3 = [0.065, 0.068, 0.07]
l1, l2 = 0.075, 0.09

for i in range(0, n):
    t = find_discrete(c1, p1)
    if t == c1[0]:
        d = find_discrete(c2, p2)
    elif t == c1[1]:
        d = find_discrete(c3, p3)
    else:
        d = continuous(l1, l2)
    p.append(original_amount_p(S, t, d))

print("P_min=" + str(min(p)) + " P_max=" + str(max(p)))
print("E{P}=" + str(E(p)) + " D{P}=" + str(D(p)) + " standard dev=" + str(math.sqrt(D(p))))
print("P{" + str(border_min) + "<=P<=" + str(border_max) + "}=" + str( p_in_borders(p, border_min, border_max) * 100) + "%")