from typing import Dict, Any
from .base import STTProvider
from .mock import MockProvider

# In a real implementation, we would import the actual providers here
# from .sarvam.adapter import SarvamAdapter
# from .google.adapter import GoogleAdapter

class ProviderFactory:
    @staticmethod
    def get_provider(provider_name: str, config: Dict[str, Any], use_mock: bool = False) -> STTProvider:
        if use_mock:
            return MockProvider(provider_name, config)
            
        # Real providers would be instantiated here based on name
        # if provider_name == "sarvam":
        #     return SarvamAdapter(provider_name, config)
        # elif provider_name == "google":
        #     return GoogleAdapter(provider_name, config)
        
        # Fallback to mock for development if not implemented
        print(f"Warning: Real provider '{provider_name}' not implemented yet. Using MockProvider.")
        return MockProvider(provider_name, config)
