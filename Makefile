.PHONY: setup dataset benchmark metrics leaderboard report all test clean

setup:
	pip install -r requirements.txt
	cp -n .env.example .env

dataset:
	python scripts/prepare_dataset.py

benchmark:
	python scripts/run_benchmark.py --model all

metrics:
	python scripts/calculate_metrics.py

leaderboard:
	python scripts/generate_leaderboard.py

report:
	python scripts/generate_report.py

evaluate: metrics leaderboard report

all: dataset benchmark evaluate

test:
	pytest tests/

clean:
	rm -rf benchmarks/runs/*
	rm -rf benchmarks/results/*
	rm -rf benchmarks/reports/*
	rm -rf evidence/errors/*
	rm -rf data/manifests/*
