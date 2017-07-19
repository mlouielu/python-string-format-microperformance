Python string format micro-performance
--------------------------------------

Mesure Python string format micro-performance

via two cases:

```
s = '%d-%d-%d-%d-%d-%d-%d-%d-%d-%d' % (inputs1[0], inputs1[1], inputs1[2],
                                       inputs1[3], inputs1[4], inputs1[5],
                                       inputs1[6], inputs1[7], inputs1[8],
                                       inputs1[9])

s = '%s-%s-%s-%s-%s-%s-%s-%s-%s-%s' % (inputs2[0], inputs2[1], inputs2[2],
                                       inputs2[3], inputs2[4], inputs2[5],
                                       inputs2[6], inputs2[7], inputs2[8],
                                       inputs2[9])
```


Run benchmark
-------------

```
$ python format
.....................
```


Result
------

```
.....................
percentage: Median +- std dev: 3.47 us +- 0.39 us

.....................
format: Median +- std dev: 4.07 us +- 0.52 us

.....................
fstring: Median +- std dev: 4.01 us +- 0.42 us
```
