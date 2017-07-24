import random
import string
import perf


def rstring(N=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


inputs1 = [random.randint(0, 2 ** 32 - 1) for i in range(10)]
inputs2 = [rstring(10) for i in range(10)]


def bench_fstring():
    s = f'{inputs1[0]}-{inputs1[1]}-{inputs1[2]}-{inputs1[3]}-{inputs1[4]}' \
        f'-{inputs1[5]}-{inputs1[6]}-{inputs1[7]}-{inputs1[8]}-{inputs1[9]}'

    s = f'{inputs2[0]}-{inputs2[1]}-{inputs2[2]}-{inputs2[3]}-{inputs2[4]}' \
        f'-{inputs2[5]}-{inputs2[6]}-{inputs2[7]}-{inputs2[8]}-{inputs2[9]}'

    return s


if __name__ == '__main__':
    runner = perf.Runner()
    runner.bench_func('fstring', bench_fstring)
