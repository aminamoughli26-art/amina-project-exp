
from facts import CarSymptom

class CarDiagnosticEngine:
    def __init__(self):
        self.facts = []

    def reset(self):
        self.facts = []

    def declare(self, fact):
        self.facts.append(fact)

    def run(self):
        print("\n[Moteur d'Inférence]: Analyse des symptômes en cours...")
        for fact in self.facts:
            attrs = fact.attributes
            if not attrs.get('engine_starts', True) and not attrs.get('lights_work', True):
                print("====================================")
                print("[Diagnostic]: La batterie est à plat ou défectueuse!")
                print("[Solution]: Essayez de recharger la batterie ou remplacez-la.")
                return
            elif not attrs.get('engine_starts', True) and attrs.get('lights_work', True) and attrs.get('clicking_sound', False):
                print("====================================")
                print("[Diagnostic]: Le problème vient du Démarreur (Starter)!")
                print("[Solution]: Vérifiez les connexions du démarreur chez un électricien auto.")
                return