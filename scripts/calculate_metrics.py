import os
import sys
import json
import glob

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.evidence.extractor import EvidenceExtractor
from src.scoring.scorecard import ScorecardGenerator

def main():
    base_dir = "c:/Users/poorn/Downloads/malpractice-detection-system-main (1)/stt-benchmarking"
    runs_dir = os.path.join(base_dir, "benchmarks", "runs")
    results_dir = os.path.join(base_dir, "benchmarks", "results")
    evidence_dir = os.path.join(base_dir, "evidence", "errors")
    
    extractor = EvidenceExtractor(evidence_dir)
    scorecard_gen = ScorecardGenerator(results_dir)
    
    run_files = glob.glob(os.path.join(runs_dir, "*.json"))
    
    for run_file in run_files:
        with open(run_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
            
        if not results:
            continue
            
        model_id = results[0]["model_id"]
        print(f"Calculating metrics for {model_id}...")
        
        # Extract evidence
        evidence = extractor.extract_evidence(results)
        extractor.save_evidence(model_id, evidence)
        
        # Generate scorecard
        scorecard_gen.generate_scorecard(model_id, results)
        
    print("Metric calculation and evidence extraction complete.")

if __name__ == "__main__":
    main()
