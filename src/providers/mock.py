import time
import random
from typing import Dict, Any
from .base import STTProvider

class MockProvider(STTProvider):
    def transcribe(self, audio_path: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
        start_time = time.time()
        
        # Simulate network and processing delay
        simulated_delay = random.uniform(0.5, 2.0)
        time.sleep(simulated_delay)
        
        # We try to read reference text from options if provided, or generate a dummy one
        reference_text = options.get('reference_text', 'this is a simulated transcript for testing')
        
        # Occasionally introduce a substitution error to simulate real STT
        words = reference_text.split()
        if len(words) > 3 and random.random() > 0.5:
            words[len(words)//2] = "error"
        transcript = " ".join(words)
        
        end_time = time.time()
        total_latency = (end_time - start_time) * 1000 # in ms
        
        return {
            "transcript": transcript,
            "latency": {
                "total": total_latency,
                "network": total_latency * 0.2,
                "inference": total_latency * 0.8
            },
            "raw_response": {"mock": True, "text": transcript},
            "confidence": 0.95
        }

    def transcribe_stream(self, audio_path: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
        # Simple stream simulation
        res = self.transcribe(audio_path, options)
        res["latency"]["first_partial"] = res["latency"]["total"] * 0.3
        res["latency"]["final"] = res["latency"]["total"]
        return res
