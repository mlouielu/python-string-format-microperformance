from formats.benchmarks.bm_percentage import bench_percentage
from formats.benchmarks.bm_format import bench_format
from formats.benchmarks.bm_fstring import bench_fstring


BENCHS = [
    ('percentage', bench_percentage),
    ('format', bench_format),
    ('fstring', bench_fstring)
]
