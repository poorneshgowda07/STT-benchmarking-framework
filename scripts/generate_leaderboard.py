import os
import csv
import json
import glob

def main():
    base_dir = "c:/Users/poorn/Downloads/malpractice-detection-system-main (1)/stt-benchmarking"
    results_dir = os.path.join(base_dir, "benchmarks", "results")
    reports_dir = os.path.join(base_dir, "benchmarks", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    scorecards = []
    scorecard_files = glob.glob(os.path.join(results_dir, "*_scorecard.json"))
    for file in scorecard_files:
        with open(file, 'r', encoding='utf-8') as f:
            scorecards.append(json.load(f))
            
    # Sort by WER
    scorecards = sorted(scorecards, key=lambda x: x['accuracy']['average_wer'])
    
    csv_path = os.path.join(reports_dir, "leaderboard.csv")
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Model", "Avg WER", "Avg CER", "P50 Latency (ms)", "P95 Latency (ms)"])
        for sc in scorecards:
            writer.writerow([
                sc["model_id"],
                f"{sc['accuracy']['average_wer']:.4f}",
                f"{sc['accuracy']['average_cer']:.4f}",
                f"{sc['latency']['p50']:.2f}",
                f"{sc['latency']['p95']:.2f}"
            ])
            
    print(f"Generated CSV leaderboard at {csv_path}")

if __name__ == "__main__":
    main()
