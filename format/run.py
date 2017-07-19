import perf
from benchmarks import BENCHS


def run():
    runner = perf.Runner()
    for bm_name, bm_func in BENCHS:
        runner.bench_func(bm_name, bm_func)


if __name__ == '__main__':
    run()
