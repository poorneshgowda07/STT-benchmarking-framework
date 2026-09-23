import json
import os
from typing import Dict, Any, List

class DatasetValidator:
    REQUIRED_KEYS = [
        "sample_id", "audio_path", "language", "speaker_id",
        "domain", "environment", "accent", "code_mixed",
        "duration_ms", "reference_text"
    ]
    
    @classmethod
    def validate_sample(cls, sample: Dict[str, Any]) -> bool:
        """Validate if a sample meets the required schema."""
        for key in cls.REQUIRED_KEYS:
            if key not in sample:
                return False
        return True
    
    @classmethod
    def process_manifest(cls, manifest_path: str) -> List[Dict[str, Any]]:
        """Process and validate an entire manifest."""
        valid_samples = []
        with open(manifest_path, 'r', encoding='utf-8') as f:
            for line in f:
                sample = json.loads(line)
                if cls.validate_sample(sample):
                    valid_samples.append(sample)
                else:
                    print(f"Skipping invalid sample: {sample.get('sample_id', 'Unknown')}")
        return valid_samples

def normalize_text(text: str) -> str:
    """Basic text normalization for ground truth alignment."""
    # Convert to lowercase, remove extra spaces
    import re
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Remove basic punctuation for standard metrics
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()
