import jiwer
from typing import Dict

class MetricCalculator:
    @staticmethod
    def calculate_wer(reference: str, hypothesis: str) -> float:
        try:
            return jiwer.wer(reference, hypothesis)
        except Exception:
            return 1.0

    @staticmethod
    def calculate_cer(reference: str, hypothesis: str) -> float:
        try:
            return jiwer.cer(reference, hypothesis)
        except Exception:
            return 1.0

    @staticmethod
    def calculate_mer(reference: str, hypothesis: str) -> float:
        try:
            return jiwer.mer(reference, hypothesis)
        except Exception:
            return 1.0

    @staticmethod
    def calculate_wil(reference: str, hypothesis: str) -> float:
        try:
            return jiwer.wil(reference, hypothesis)
        except Exception:
            return 1.0

    @staticmethod
    def calculate_all(reference: str, hypothesis: str) -> Dict[str, float]:
        return {
            "wer": MetricCalculator.calculate_wer(reference, hypothesis),
            "cer": MetricCalculator.calculate_cer(reference, hypothesis),
            "mer": MetricCalculator.calculate_mer(reference, hypothesis),
            "wil": MetricCalculator.calculate_wil(reference, hypothesis)
        }

def calculate_entity_accuracy(reference: str, hypothesis: str, entities: list) -> float:
    """Calculate accuracy for specific entities/keywords in the reference."""
    if not entities:
        return 1.0
    
    ref_lower = reference.lower()
    hyp_lower = hypothesis.lower()
    
    correct = sum(1 for ent in entities if ent.lower() in hyp_lower and ent.lower() in ref_lower)
    expected = sum(1 for ent in entities if ent.lower() in ref_lower)
    
    return correct / expected if expected > 0 else 1.0
