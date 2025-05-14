from agent import DiagnosisAgent
from inferencias import DoInferencias

answers1 = ["C4N", "M1S", "M2N", "P2S"]

recomendation = DoInferencias()
agent = DiagnosisAgent()

agent.recive_answers(answers1)

recomendation.tt_entails(agent.kb, "S1")