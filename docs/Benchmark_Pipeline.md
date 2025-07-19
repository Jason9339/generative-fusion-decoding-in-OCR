# Benchmark Pipeline

Scripts under `benchmarks/` provide utilities to run inference on datasets and to calculate mixed error rates (MER).

## Components
- **run_single_file.py** – transcribes a single audio file with configurable model settings.
- **run_benchmark.py** – downloads datasets, runs inference (GFD or Whisper) and stores results.
- **calculate_mer.py** – cleans predictions and ground truth, computing WER/MER for evaluation.

## Key Files
- `benchmarks/run_single_file.py`
- `benchmarks/run_benchmark.py`
- `benchmarks/calculate_mer.py`
