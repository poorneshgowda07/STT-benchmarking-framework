import os
import json
from typing import List, Dict, Any

class EvidenceExtractor:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def extract_evidence(self, results: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        evidence = {
            "successes": [],
            "failures": []
        }
        
        for record in results:
            wer = record["metrics"].get("wer", 1.0)
            
            evidence_record = {
                "sample_id": record["sample_id"],
                "model": record["model_id"],
                "reference": record["reference"],
                "prediction": record["prediction"],
                "audio_hash": record["audio_hash"],
                "timestamp": record["timestamp"],
                "wer": wer
            }
            
            if wer == 0.0:
                evidence_record["reason"] = "Perfect transcription"
                evidence["successes"].append(evidence_record)
            elif wer > 0.5:
                evidence_record["error_type"] = "HIGH_WER"
                evidence_record["severity"] = "HIGH"
                evidence_record["difference"] = f"Expected: {record['reference']} | Got: {record['prediction']}"
                evidence["failures"].append(evidence_record)
                
        # Sort and limit to top examples
        evidence["successes"] = sorted(evidence["successes"], key=lambda x: x["wer"])[:5]
        evidence["failures"] = sorted(evidence["failures"], key=lambda x: x["wer"], reverse=True)[:5]
        
        return evidence
        
    def save_evidence(self, model_id: str, evidence: Dict[str, List[Dict[str, Any]]]):
        file_path = os.path.join(self.output_dir, f"{model_id}_evidence.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(evidence, f, indent=2)
