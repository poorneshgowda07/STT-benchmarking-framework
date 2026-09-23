import os
import json

base_dir = "c:/Users/poorn/Downloads/malpractice-detection-system-main (1)/stt-benchmarking"
manifest_path = os.path.join(base_dir, "data/manifests/test_dataset.jsonl")

# Mock samples
samples = [
    {
        "sample_id": "sample_001",
        "audio_path": "dummy/path/audio1.wav",
        "language": "en",
        "speaker_id": "spk_1",
        "domain": "finance",
        "environment": "clean",
        "accent": "neutral",
        "code_mixed": False,
        "duration_ms": 2500,
        "reference_text": "I want to apply for a credit card"
    },
    {
        "sample_id": "sample_002",
        "audio_path": "dummy/path/audio2.wav",
        "language": "hi-IN",
        "speaker_id": "spk_2",
        "domain": "general",
        "environment": "telephony",
        "accent": "indian",
        "code_mixed": True,
        "duration_ms": 3200,
        "reference_text": "Mera account number hai nine eight seven"
    },
    {
        "sample_id": "sample_003",
        "audio_path": "dummy/path/audio3.wav",
        "language": "en",
        "speaker_id": "spk_1",
        "domain": "finance",
        "environment": "noisy",
        "accent": "indian",
        "code_mixed": False,
        "duration_ms": 1500,
        "reference_text": "EMI of twenty five thousand"
    }
]

os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
with open(manifest_path, 'w', encoding='utf-8') as f:
    for sample in samples:
        f.write(json.dumps(sample) + "\n")

print(f"Prepared test dataset at {manifest_path}")
