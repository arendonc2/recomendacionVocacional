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
                    "S1S ∧ S5S ∧ S8S ⇒ A5",
                    "P1S ∧ P5S ∧ M3S ∧ M4S ⇒ S1",
                    "P2S ∧ M1S ∧ M3S ∧ C3N ⇒ S2",
                    "P1S ∧ P5S ∧ M1S ∧ S10S ⇒ S3",
                    "P5S ∧ M4S ∧ S4S ∧ S3S ⇒ S4",
                    "C1S ∧ P3S ∧ M5S ∧ S8S ⇒ S5",
                    "C1S ∧ S10S ∧ M5S ∧ P4S ⇒ S6",
                    "M1S ∧ M4S ∧ C4S ∧ S9S ⇒ S7",
                    "C4S ∧ C3S ∧ S2S ∧ S5S ⇒ S8",
                    "P1S ∧ C2S ∧ S1S ∧ M5S ⇒ S9",
                    "P5S ∧ M3S ∧ M4S ∧ S4S ⇒ S10",
                    "M2S ∧ C4S ∧ S9S ∧ M5S ⇒ S11",
                    "S8S ∧ C3S ∧ M5S ∧ M1S ⇒ S12",
                    "P5S ∧ M4S ∧ S10S ∧ M1S ⇒ S13",
                    "S8S ∧ M5S ∧ P1S ∧ M3S ⇒ S14",
                    "P4S ∧ S9S ∧ M4S ∧ S4S ⇒ S15",
                    "P1S ∧ P5S ∧ M3S ∧ M2N ⇒ S16",
                    "M3S ∧ M2S ∧ P4S ∧ S10S ⇒ S17",
                    "M4S ∧ P1S ∧ P5S ∧ S4S ⇒ S18",
                    "C1S ∧ M1S ∧ S10S ∧ P4S ⇒ S19",
                    "S7S ∧ S5S ∧ C1S ∧ P3N ⇒ S20",
                    "P5S ∧ C1S ∧ S4S ∧ S6S ⇒ S21",
                    "P1S ∧ M1S ∧ S3S ∧ S4S ⇒ S22",
                    "C2S ∧ C4S ∧ M5S ∧ S9S ⇒ S23",
                    "S2S ∧ S1S ∧ C4S ∧ S8S ⇒ S24",
                    "C1S ∧ P3S ∧ M5S ∧ S6S ⇒ S25",
                    "P1S ∧ S1S ∧ S3S ∧ M5S ⇒ S26",
                    "P2S ∧ P1S ∧ M5S ∧ S1S ⇒ S27",
                    "S5S ∧ S8S ∧ C2S ∧ M3S ⇒ S28",
                    "P1S ∧ M3S ∧ C1S ∧ S6S ⇒ S29",
                    "P1S ∧ S1S ∧ M3S ∧ M5S ⇒ S30"
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