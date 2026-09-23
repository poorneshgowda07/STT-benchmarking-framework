# Production-Grade STT Benchmarking & Evaluation Repository

A comprehensive framework for evaluating Speech-to-Text (STT) models across multiple providers including Sarvam, Google, OpenAI, Deepgram, and AssemblyAI.

## Features
- **Reproducible Pipeline**: Uses SHA-256 hashing for audio and configs.
- **Metrics**: WER, CER, MER, WIL, and Latency (P50, P95).
- **Latency Optimization**: Measures first partial, endpointing, and total latencies.
- **Reporting**: Generates Leaderboards (CSV) and detailed Reports (Markdown).
- **Evidence Collection**: Saves exact inputs/outputs for both successes and failures to prevent hidden errors.

## Installation
```bash
git clone <repo>
cd stt-benchmarking

pip install -r requirements.txt
cp .env.example .env
```

## Usage
Run the full benchmarking pipeline using the Makefile:
```bash
make all
```

Or step-by-step:
```bash
python scripts/prepare_dataset.py
python scripts/run_benchmark.py --model all
python scripts/calculate_metrics.py
python scripts/generate_leaderboard.py
python scripts/generate_report.py
```

## Structure
- `configs/`: Provider, model, and scoring configurations.
- `src/`: Core logic (adapters, hashing, metrics, scoring).
- `scripts/`: CLI entrypoints.
- `benchmarks/`: Generated output results and reports.
- `evidence/`: Examples of STT successes and failures.

## Adding a New Provider
Implement `STTProvider` in `src/providers/base.py` and register it in `src/providers/factory.py`.
