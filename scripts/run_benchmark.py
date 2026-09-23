import os
import sys
import yaml
import argparse

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.benchmarking.engine import BenchmarkEngine

def load_configs(base_dir: str):
    configs = {}
    config_dir = os.path.join(base_dir, "configs")
    for file in os.listdir(config_dir):
        if file.endswith(".yaml"):
            name = file.replace(".yaml", "")
            with open(os.path.join(config_dir, file), 'r') as f:
                configs[name] = yaml.safe_load(f)
    return configs

def main():
    parser = argparse.ArgumentParser(description="Run STT Benchmark")
    parser.add_argument("--model", type=str, required=True, help="Model ID to benchmark, or 'all'")
    args = parser.parse_args()
    
    base_dir = "c:/Users/poorn/Downloads/malpractice-detection-system-main (1)/stt-benchmarking"
    configs = load_configs(base_dir)
    
    # Flatten config slightly for the engine
    flat_config = {
        "providers": configs["providers"]["providers"],
        "models": configs["models"]["models"]
    }
    
    output_dir = os.path.join(base_dir, "benchmarks", "runs")
    engine = BenchmarkEngine(flat_config, output_dir)
    
    manifest_path = os.path.join(base_dir, "data", "manifests", "test_dataset.jsonl")
    
    models_to_run = []
    if args.model == "all":
        models_to_run = list(flat_config["models"].keys())
    else:
        models_to_run = [args.model]
        
    for model_id in models_to_run:
        if model_id not in flat_config["models"]:
            print(f"Skipping unknown model: {model_id}")
            continue
        try:
            engine.run_benchmark(manifest_path, model_id, use_mock=True)
        except Exception as e:
            print(f"Failed to benchmark {model_id}: {e}")

if __name__ == "__main__":
    main()
