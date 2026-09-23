import os
import json
from typing import List, Dict, Any
from src.latency.analyzer import LatencyAnalyzer

class ScorecardGenerator:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def generate_scorecard(self, model_id: str, results: List[Dict[str, Any]]):
        if not results:
            return None
            
        total_samples = len(results)
        wers = [r["metrics"]["wer"] for r in results]
        cers = [r["metrics"]["cer"] for r in results]
        total_latencies = [r["latency"]["total"] for r in results]
        
        avg_wer = sum(wers) / total_samples if wers else 1.0
        avg_cer = sum(cers) / total_samples if cers else 1.0
        latency_stats = LatencyAnalyzer.calculate_percentiles(total_latencies)
        
        scorecard = {
            "model_id": model_id,
            "total_samples_evaluated": total_samples,
            "accuracy": {
                "average_wer": avg_wer,
                "average_cer": avg_cer
            },
            "latency": latency_stats,
            "reliability": {
                "failure_rate": 0.0, # Implement tracking timeouts/failures
                "timeout_rate": 0.0
            }
        }
        
        file_path = os.path.join(self.output_dir, f"{model_id}_scorecard.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(scorecard, f, indent=2)
            
        return scorecard
