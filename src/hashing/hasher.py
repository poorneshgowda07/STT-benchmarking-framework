import hashlib
import json
import os
from typing import Dict, Any

def hash_audio(file_path: str) -> str:
    """Generate SHA-256 hash of an audio file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_config(config: Dict[str, Any]) -> str:
    """Generate SHA-256 hash of a configuration dictionary."""
    config_str = json.dumps(config, sort_keys=True)
    return hashlib.sha256(config_str.encode('utf-8')).hexdigest()

def generate_run_hash(audio_hash: str, config_hash: str, model_version: str) -> str:
    """Generate a unique hash for a benchmark run."""
    run_str = f"{audio_hash}-{config_hash}-{model_version}"
    return hashlib.sha256(run_str.encode('utf-8')).hexdigest()
