from engine import CarDiagnosticEngine
from facts import CarSymptom

if __name__ == "__main__":
    engine = CarDiagnosticEngine()
    engine.reset()
    
    print("--- Système Expert: Diagnostic Automobile ---")
    # Test 2: Voiture ne démarre pas + Phares allumés + Bruit de clic
    engine.declare(CarSymptom(engine_starts=False, lights_work=True, clicking_sound=True))
    engine.run()