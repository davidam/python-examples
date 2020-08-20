import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

v = statistics.median_low(example_list)
print(v)

w = statistics.median_high(example_list)
print(w)

vv = statistics.median_grouped(example_list)
print(vv)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)

d = statistics.harmonic_mean(example_list)
print(d)

e = statistics.pvariance(example_list)
print(e)
