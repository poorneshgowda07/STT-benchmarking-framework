import os
import json
from typing import Dict, Any

class ReportGenerator:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def generate_markdown_report(self, scorecards: Dict[str, Any], evidence_data: Dict[str, Any]):
        report_lines = [
            "# STT Benchmark Report",
            "",
            "## Executive Summary",
            "This report details the benchmarking of various Speech-to-Text models.",
            "",
            "## Leaderboard",
            "| Model | Avg WER | Avg CER | Latency P95 (ms) |",
            "|---|---|---|---|"
        ]
        
        # Sort by WER for leaderboard
        sorted_models = sorted(scorecards.items(), key=lambda x: x[1]['accuracy']['average_wer'])
        
        for model_id, scorecard in sorted_models:
            wer = f"{scorecard['accuracy']['average_wer']:.2%}"
            cer = f"{scorecard['accuracy']['average_cer']:.2%}"
            p95 = f"{scorecard['latency']['p95']:.2f}"
            report_lines.append(f"| {model_id} | {wer} | {cer} | {p95} |")
            
        report_lines.extend([
            "",
            "## Individual Model Scorecards"
        ])
        
        for model_id, scorecard in scorecards.items():
            report_lines.extend([
                f"### {model_id}",
                f"- **Total Samples:** {scorecard['total_samples_evaluated']}",
                f"- **Average WER:** {scorecard['accuracy']['average_wer']:.2%}",
                f"- **Latency P50:** {scorecard['latency']['p50']:.2f} ms",
                f"- **Latency P95:** {scorecard['latency']['p95']:.2f} ms",
                ""
            ])
            
        report_lines.extend(["", "## Evidence Samples", ""])
        
        for model_id, evidence in evidence_data.items():
            report_lines.extend([f"### {model_id} Failures"])
            for fail in evidence.get("failures", []):
                report_lines.extend([
                    f"**Sample ID:** {fail['sample_id']}",
                    f"- **Expected:** {fail['reference']}",
                    f"- **Predicted:** {fail['prediction']}",
                    f"- **WER:** {fail['wer']:.2%}",
                    ""
                ])
                
        md_content = "\n".join(report_lines)
        file_path = os.path.join(self.output_dir, "benchmark_report.md")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print(f"Generated Markdown report at {file_path}")
