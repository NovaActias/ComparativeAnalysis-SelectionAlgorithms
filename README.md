# Comparative Analysis of Selection Algorithms

A comprehensive performance analysis of three k-th element selection algorithms: **Quick Select**, **Heap Select**, and **Median of Medians Select**.

## Project Overview

This repository contains implementation and performance analysis of selection algorithms, with particular focus on:

- **Quick Select**: Partitioning-based algorithm with average O(n) complexity
- **Heap Select**: Heap-based algorithm with O(n + k log n) complexity  
- **Median of Medians Select**: Deterministic algorithm with guaranteed O(n) worst-case
- **Quick Select With Partition 3-Way**: Variant of Quick Select

## Project Structure

```
├── GraphGenerationCode/
│   ├── Algorithms/              # Algorithm implementations
│   │   ├── QuickSelect.py
│   │   ├── HeapSelect.py
│   │   ├── MedianOfMediansSelect.py
│   │   ├── QuickP3WSelect.py
│   │   └── Heap.py
│   ├── BenchmarkFinalData/      # Pre-generated benchmark data
│   │   ├── ArraySize.txt
│   │   ├── kValues.txt
│   │   ├── QuickSelectExecTimes/
│   │   ├── HeapSelectExecTimes/
│   │   ├── MediansSelectExecTimes/
│   │   └── WorstQuickP3WExecTimes/
│   ├── BenchmarksScripts/       # Scripts to generate new benchmarks
│   │   ├── Benchmark.py
│   │   └── BenchmarkConKIncrementale
│   ├── Languages/               # Localization files for graphs
│   │   ├── eng.txt
│   │   └── ita.txt
│   └── DrawGraph.py            # Graph generation
├── LICENSE
└── README.md
```

## How to Use

### Prerequisites
- Python 3.x
- matplotlib (for graph generation)

### Visualizing Graphs
The project includes several test scenarios:

- **k Random**: Randomly chosen k values
- **k = 1**: Minimum search (first element)
- **k = len(Array)**: Maximum search (last element)  
- **k = len(Array)//2**: Median search
- **k = 10x**: k values in multiples of 10 (0, 10, 20, ..., 1000)

To generate all the graphs used in the report:

```bash
cd GraphGenerationCode
python DrawGraph.py
```

This command will generate graphs showing:
- Individual performance of each algorithm randomly chosen k values (**k Random**)
- Comparisons with different k values (**k = 1**, **k = len(Array)**, **k = len(Array)//2**)
- Final comparison with k values in multiples of 10 (0, 10, 20, ..., 1000) (**k = 10x**)
- Final comparison (**k Random**)

### Running Benchmarks
**IMPORTANT**: The benchmark scripts were designed for macOS and Ubuntu. **Not recommended for Windows**

#### Compatibility Issues: Temporal and Naming Inconsistencies
**WARNING**: The benchmark timing generation code was developed approximately **one year earlier** than the graph generation code. 
This has led to several inconsistencies:
- `Benchmark.py` saves `times{AlgorithmName}.txt` while in the repository those files should be in `{AlgorithmName}ExecTimes/kIsRandom.txt`
- `Benchmark.py` uses `BenchmarkResults/` while repository uses `BenchmarkFinalData/`

So if you run `Benchmark.py`, you will need to **manually**:
- Modify the script if you want any other k-type autside of kIsRandom
- Use `BenchmarkKIs10x.py` if you want execution times for k values in multiples of 10 (0, 10, 20, ..., 1000)
- Move files from `BenchmarkResults/` directory to `BenchmarkFinalData/` to match the structure expected by `DrawGraph.py` (if you want to execute DrawGraph.py)

```bash
cd GraphGenerationCode/BenchmarksScripts
python Benchmark.py
```

## Benchmark Methodology

- **Array size range**: 100 - 100000 elements
- **Progression**: Geometric series with 100 steps
- **Tests per size**: 500 executions to ensure statistical accuracy
- **Array values**: Random numbers in range [-1000, 1000]
- **Precision**: Relative error < 1%

## Localization

Graphs support localization in:
- **English** (`Languages/eng.txt`)
- **Italian** (`Languages/ita.txt`)

To change language, modify the `langFilePath` variable in `DrawGraph.py`.
