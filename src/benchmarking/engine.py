import os
import json
import time
from typing import List, Dict, Any
from datetime import datetime

from src.audio.validator import DatasetValidator, normalize_text
from src.hashing.hasher import hash_audio, generate_run_hash
from src.providers.factory import ProviderFactory
from src.metrics.calculator import MetricCalculator

class BenchmarkEngine:
    def __init__(self, configs: Dict[str, Any], output_dir: str):
        self.configs = configs
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def run_benchmark(self, manifest_path: str, model_id: str, use_mock: bool = True):
        print(f"Starting benchmark for {model_id}...")
        
        # Load dataset
        samples = DatasetValidator.process_manifest(manifest_path)
        print(f"Loaded {len(samples)} valid samples.")
        
        # Find model config
        model_config = self.configs.get("models", {}).get(model_id)
        if not model_config:
            raise ValueError(f"Model {model_id} not found in configuration.")
            
        provider_name = model_config["provider"]
        provider_config = self.configs.get("providers", {}).get(provider_name, {})
        
        # Instantiate provider
        provider = ProviderFactory.get_provider(provider_name, provider_config, use_mock)
        
        results = []
        
        for sample in samples:
            print(f"Processing sample {sample['sample_id']}...")
            
            # Hashing
            # If audio path doesn't exist, we skip hashing or use a dummy for testing
            audio_hash = "dummy_hash"
            if os.path.exists(sample["audio_path"]):
                audio_hash = hash_audio(sample["audio_path"])
                
            run_hash = generate_run_hash(audio_hash, "config_hash_placeholder", model_id)
            
            # Transcription
            options = {"reference_text": sample["reference_text"]}
            if model_config.get("streaming"):
                stt_result = provider.transcribe_stream(sample["audio_path"], options)
            else:
                stt_result = provider.transcribe(sample["audio_path"], options)
                
            # Normalization and Metrics
            norm_ref = normalize_text(sample["reference_text"])
            norm_hyp = normalize_text(stt_result["transcript"])
            
            metrics = MetricCalculator.calculate_all(norm_ref, norm_hyp)
            
            # Result record
            record = {
                "sample_id": sample["sample_id"],
                "run_hash": run_hash,
                "audio_hash": audio_hash,
                "model_id": model_id,
                "provider": provider_name,
                "timestamp": datetime.utcnow().isoformat(),
                "reference": sample["reference_text"],
                "prediction": stt_result["transcript"],
                "metrics": metrics,
                "latency": stt_result["latency"]
            }
            results.append(record)
            
            # Store raw response
            self._store_raw_response(run_hash, provider_name, model_id, stt_result["raw_response"])
            
        # Store final results
        run_id = f"run_{int(time.time())}_{model_id}"
        results_file = os.path.join(self.output_dir, f"{run_id}.json")
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
            
        print(f"Benchmark complete. Results saved to {results_file}")
        return results_file
        
    def _store_raw_response(self, run_hash: str, provider: str, model: str, raw_response: Dict[str, Any]):
        raw_dir = os.path.join(self.output_dir, "raw_responses", model)
        os.makedirs(raw_dir, exist_ok=True)
        file_path = os.path.join(raw_dir, f"{run_hash}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(raw_response, f, indent=2)
