import numpy as np
from typing import List, Dict

class LatencyAnalyzer:
    @staticmethod
    def calculate_percentiles(latencies: List[float]) -> Dict[str, float]:
        if not latencies:
            return {"p50": 0.0, "p75": 0.0, "p90": 0.0, "p95": 0.0, "p99": 0.0}
        
        return {
            "p50": float(np.percentile(latencies, 50)),
            "p75": float(np.percentile(latencies, 75)),
            "p90": float(np.percentile(latencies, 90)),
            "p95": float(np.percentile(latencies, 95)),
            "p99": float(np.percentile(latencies, 99))
        }

    @staticmethod
    def calculate_rtf(audio_duration_ms: float, total_latency_ms: float) -> float:
        """Real-Time Factor: processing_time / audio_duration"""
        if audio_duration_ms == 0:
            return 0.0
        return total_latency_ms / audio_duration_ms

    @staticmethod
    def aggregate_latency_components(breakdowns: List[Dict[str, float]]) -> Dict[str, float]:
        """Aggregate breakdown (e.g. inference, network) across runs."""
        if not breakdowns:
            return {}
        
        aggregated = {}
        for key in breakdowns[0].keys():
            values = [b.get(key, 0.0) for b in breakdowns]
            aggregated[f"{key}_avg"] = sum(values) / len(values)
            
        return aggregated
