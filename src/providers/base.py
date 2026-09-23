from abc import ABC, abstractmethod
from typing import Dict, Any

class STTProvider(ABC):
    def __init__(self, name: str, config: Dict[str, Any]):
        self.name = name
        self.config = config

    @abstractmethod
    def transcribe(self, audio_path: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Transcribe audio file in batch mode.
        Should return a dictionary containing:
        - 'transcript': str
        - 'latency': Dict (breakdown)
        - 'raw_response': Dict (original provider response)
        - 'confidence': float (if available)
        - 'words': List (timestamps, if available)
        """
        pass
        
    @abstractmethod
    def transcribe_stream(self, audio_path: str, options: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Transcribe audio file in streaming mode.
        Should simulate streaming from file.
        Returns similar structure to `transcribe` plus streaming specific latencies.
        """
        pass
        
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "batch": True,
            "streaming": False,
            "diarization": False,
            "word_timestamps": False,
            "custom_vocabulary": False
        }
