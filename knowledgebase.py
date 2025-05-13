class KnowledgeBase:
    def __init__(self):
        self.rules=["P1S ∧ P5S ∧ M3S ∧ M4S ⇒ A1",
                    "P2N ∧ C3N ∧ M1S ⇒ A1",
                    "M2N ∧ M3S ∧ C1S ⇒ A1",
                    "P4S ∧ P3S ∧ M4S ⇒ A1",
                    "S10S ∧ M3S ∧ P5S ⇒ A1",
                    "P1S ∧ P2S ∧ M1S ∧ M3S ⇒ A1",
                    "C4S ∧ C5S ∧ S2S ⇒ A2",
                    "P2S ∧ S1S ∧ S4S ⇒ A2",
                    "C2S ∧ C4S ∧ M5S ⇒ A2",
                    "P3N ∧ M4S ∧ S9S ⇒ A2",
                    "C3S ∧ C4S ∧ S5S ⇒ A2",
                    "M5S ∧ S2S ∧ S8S ⇒ A2",
                    "P1S ∧ P5S ∧ M1S ∧ M4S ⇒ A3",
                    "P3S ∧ M2S ∧ M3S ⇒ A3",
                    "P4S ∧ M1S ∧ M4S ∧ C1S ⇒ A3",
                    "S3S ∧ S4S ∧ S10S ⇒ A3",
                    "C3N ∧ P2N ∧ M1S ∧ M4S ⇒ A3",
                    "P5S ∧ M3S ∧ S8S ⇒ A3",
                    "C1S ∧ C2N ∧ P5S ⇒ A4",
                    "M1S ∧ M4S ∧ S9S ⇒ A4",
                    "P1S ∧ C1S ∧ S4S ⇒ A4",
                    "S3S ∧ S7S ∧ S10S ⇒ A4",
                    "C2N ∧ C5N ∧ P4S ⇒ A4",
                    "M1S ∧ M5S ∧ S9S ⇒ A4",
                    "C2S ∧ C4S ∧ M5S ⇒ A5",
                    "P2S ∧ P1S ∧ S1S ⇒ A5",
                    "C1S ∧ C5S ∧ S8S ⇒ A5",
                    "S6S ∧ S9S ∧ M5S ⇒ A5",
                    "P3S ∧ P5N ∧ C2S ⇒ A5",
                    "S1S ∧ S5S ∧ S8S ⇒ A5"
                    ]
        self.answers = []

    def tell(self, answer):
        self.answers.append(answer)

    def ask(self):
        diagnoses = set()
        for answer in self.answers:
            if answer in self.rules:
                diagnoses.update(self.rules[answer].split("∨"))
        return diagnoses if diagnoses else {"Sin diagnóstico"}