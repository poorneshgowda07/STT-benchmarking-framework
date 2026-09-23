import os
import sys
import json
import glob

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.reporting.generator import ReportGenerator

def main():
    base_dir = "c:/Users/poorn/Downloads/malpractice-detection-system-main (1)/stt-benchmarking"
    results_dir = os.path.join(base_dir, "benchmarks", "results")
    evidence_dir = os.path.join(base_dir, "evidence", "errors")
    reports_dir = os.path.join(base_dir, "benchmarks", "reports")
    
    scorecards = {}
    scorecard_files = glob.glob(os.path.join(results_dir, "*_scorecard.json"))
    for file in scorecard_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            scorecards[data["model_id"]] = data
            
    evidence_data = {}
    evidence_files = glob.glob(os.path.join(evidence_dir, "*_evidence.json"))
    for file in evidence_files:
        model_id = os.path.basename(file).replace("_evidence.json", "")
        with open(file, 'r', encoding='utf-8') as f:
            evidence_data[model_id] = json.load(f)
            
    generator = ReportGenerator(reports_dir)
    generator.generate_markdown_report(scorecards, evidence_data)

if __name__ == "__main__":
    main()
