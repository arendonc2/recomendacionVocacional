from knowledgebase import KnowledgeBase

class DiagnosisAgent:
    def __init__(self):
        self.kb = KnowledgeBase()

    def recive_answers(self, answers):
        for answer in answers:
            self.kb.tell(answer)

    def recommendation(self):
        return self.kb.ask()