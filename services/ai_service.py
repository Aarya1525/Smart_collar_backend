"""
Mock AI Service
---------------
In production this would call:
  - YAMNet + ResNet-18  for bark emotion classification
  - Random Forest       for IMU gait anomaly detection
  - EfficientNet-B0     for breed identification from photo

For local development / demo, we simulate AI responses.
"""
import random


class AIService:
    # ── Bark / Audio Classification ─────────────────────────────────────────
    BARK_CLASSES = [
        ("Distress Barking", 0.948, "Pain Bark"),
        ("Aggressive Barking", 0.871, "Aggression / Territory"),
        ("Playful Bark", 0.763, "Playful / Excited"),
        ("Howling", 0.812, "Loneliness / Night Call"),
    ]

    def classify_audio(self, wav_bytes: bytes) -> dict:
        """Simulate YAMNet + ResNet-18 bark classification."""
        label, prob, description = random.choice(self.BARK_CLASSES)
        return {
            "label": label,
            "probability": round(prob + random.uniform(-0.05, 0.05), 3),
            "description": description,
            "model": "YAMNet-ResNet18",
        }

    # ── Gait Anomaly Detection ───────────────────────────────────────────────
    def analyze_gait(self, movement: dict) -> dict:
        """Simulate Random Forest gait anomaly detection from MPU-6050 data."""
        rms = movement.get("accel_max_g", 1.0)
        variance = movement.get("accel_variance", 0.05)
        anomaly = variance > 0.12 or rms > 2.0
        return {
            "anomaly_detected": anomaly,
            "rms_value": round(rms, 3),
            "gait_state": "limping" if anomaly else movement.get("inferred_state", "normal"),
            "model": "RandomForest-Gait",
        }

    # ── Breed Classification ─────────────────────────────────────────────────
    BREEDS = [
        ("Indian Pariah", 96.4),
        ("Indian Spitz", 91.2),
        ("Labrador Mix", 83.5),
        ("German Shepherd Mix", 79.1),
    ]

    def classify_breed(self, image_bytes: bytes) -> dict:
        """Simulate EfficientNet-B0 breed classification."""
        breed, confidence = random.choice(self.BREEDS)
        return {
            "breed": breed,
            "confidence": round(confidence + random.uniform(-3, 3), 1),
            "model": "EfficientNet-B0",
        }

    # ── Temperature Alert ────────────────────────────────────────────────────
    def check_temperature(self, temp_c: float) -> dict:
        """Check if temperature reading indicates fever."""
        if temp_c > 40.0:
            return {"alert": True, "severity": "CRITICAL", "message": f"Fever detected: {temp_c}°C"}
        elif temp_c > 39.5:
            return {"alert": True, "severity": "WARNING", "message": f"Elevated temperature: {temp_c}°C"}
        return {"alert": False, "severity": None, "message": "Normal"}


# Singleton instance
ai_service = AIService()
