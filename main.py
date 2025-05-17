import re

class KnowledgeBase:
    def __init__(self):
        # Mapeo de códigos de área a nombres legibles
        self.area_names = {
            'A1': 'Tecnología y Transformación Digital',
            'A2': 'Salud y Bienestar',
            'A3': 'Ingeniería, Industria y Energía',
            'A4': 'Negocios, Finanzas y Derecho',
            'A5': 'Educación, Ciencias Sociales y Humanidades'
        }
        # Reglas proposicionales para inferir áreas (A1–A5)
        self.area_rules = [
            "P1S ∧ P5S ∧ M3S ∧ M4S ⇒ A1", "P2N ∧ C3N ∧ M1S ⇒ A1", "M2N ∧ M3S ∧ C1S ⇒ A1",
            "P4S ∧ P3S ∧ M4S ⇒ A1", "S10S ∧ M3S ∧ P5S ⇒ A1", "P1S ∧ P2S ∧ M1S ∧ M3S ⇒ A1",
            "C4S ∧ C5S ∧ S2S ⇒ A2", "P2S ∧ S1S ∧ S4S ⇒ A2", "C2S ∧ C4S ∧ M5S ⇒ A2",
            "P3N ∧ M4S ∧ S9S ⇒ A2", "C3S ∧ C4S ∧ S5S ⇒ A2", "M5S ∧ S2S ∧ S8S ⇒ A2",
            "P1S ∧ P5S ∧ M1S ∧ M4S ⇒ A3", "P3S ∧ M2S ∧ M3S ⇒ A3", "P4S ∧ M1S ∧ M4S ∧ C1S ⇒ A3",
            "S3S ∧ S4S ∧ S10S ⇒ A3", "C3N ∧ P2N ∧ M1S ∧ M4S ⇒ A3", "P5S ∧ M3S ∧ S8S ⇒ A3",
            "C1S ∧ C2N ∧ P5S ⇒ A4", "M1S ∧ M4S ∧ S9S ⇒ A4", "P1S ∧ C1S ∧ S4S ⇒ A4",
            "S3S ∧ S7S ∧ S10S ⇒ A4", "C2N ∧ C5N ∧ P4S ⇒ A4", "M1S ∧ M5S ∧ S9S ⇒ A4",
            "C2S ∧ C4S ∧ M5S ⇒ A5", "P2S ∧ P1S ∧ S1S ⇒ A5", "C1S ∧ C5S ∧ S8S ⇒ A5",
            "S6S ∧ S9S ∧ M5S ⇒ A5", "P3S ∧ P5N ∧ C2S ⇒ A5", "S1S ∧ S5S ∧ S8S ⇒ A5"
        ]
        # Opciones de carrera para cada área
        self.career_options = {
            'A1': ["Ingeniería de Sistemas","Desarrollo de Software","Ciencia de Datos e IA","Ciberseguridad","Diseño UX/UI","Marketing Digital"],
            'A2': ["Medicina","Enfermería","Psicología","Farmacia","Fisioterapia","Nutrición y Dietética"],
            'A3': ["Ingeniería Industrial","Ingeniería Ambiental","Ingeniería Sanitaria","Ingeniería Eléctrica","Ingeniería Mecánica"],
            'A4': ["Contaduría Pública","Administración de Empresas","Negocios Internacionales","Derecho","Economía"],
            'A5': ["Licenciatura en Educación","Trabajo Social","Comunicación Social","Sociología","Filosofía","Antropología","Lingüística","Historia"]
        }
        # Preguntas específicas por carrera para cada área
        self.career_question_prompts = {
            'A1': {
                'Ingeniería de Sistemas':      '¿Te interesa diseñar y mantener arquitecturas de software y bases de datos? (s/n): ',
                'Desarrollo de Software':      '¿Disfrutas escribir y depurar código para crear aplicaciones o sistemas? (s/n): ',
                'Ciencia de Datos e IA':       '¿Te gusta analizar grandes volúmenes de datos y entrenar modelos predictivos? (s/n): ',
                'Ciberseguridad':              '¿Te interesa proteger sistemas y redes de posibles ataques y vulnerabilidades? (s/n): ',
                'Diseño UX/UI':                '¿Te motiva crear interfaces intuitivas y mejorar la experiencia de usuario? (s/n): ',
                'Marketing Digital':           '¿Te gusta planificar campañas online y analizar métricas de rendimiento? (s/n): '
            },
            'A2': {
                'Medicina':                    '¿Te interesa diagnosticar y tratar enfermedades, incluyendo en pacientes infantiles? (s/n): ',
                'Enfermería':                  '¿Disfrutarías asistir en el cuidado directo de pacientes y colaborar en equipos de salud? (s/n): ',
                'Psicología':                  '¿Te interesa entender y ayudar a las personas con sus procesos mentales y emocionales? (s/n): ',
                'Farmacia':                    '¿Te atrae profundizar en cómo funcionan los medicamentos y su desarrollo? (s/n): ',
                'Fisioterapia':                '¿Te motiva ayudar a personas a recuperar movilidad mediante técnicas físicas y ejercicios? (s/n): ',
                'Nutrición y Dietética':       '¿Te apasiona diseñar planes alimenticios para mejorar la salud mediante la nutrición? (s/n): '
            },
            'A3': {
                'Ingeniería Industrial':      '¿Te atrae optimizar procesos productivos y gestionar operaciones eficientes? (s/n): ',
                'Ingeniería Ambiental':       '¿Te interesa diseñar soluciones para reducir el impacto ambiental y conservar recursos? (s/n): ',
                'Ingeniería Sanitaria':       '¿Te gustaría trabajar en proyectos de agua potable y saneamiento básico? (s/n): ',
                'Ingeniería Eléctrica':       '¿Te apasiona diseñar y mantener sistemas eléctricos y circuitos de alta tensión? (s/n): ',
                'Ingeniería Mecánica':        '¿Disfrutas diseñar y analizar mecanismos y sistemas de movimiento? (s/n): '
            },
            'A4': {
                'Contaduría Pública':         '¿Te interesa llevar registros financieros y realizar auditorías contables? (s/n): ',
                'Administración de Empresas': '¿Te motiva coordinar equipos y gestionar recursos para alcanzar metas organizacionales? (s/n): ',
                'Negocios Internacionales':   '¿Te atrae negociar y gestionar operaciones comerciales entre distintos países? (s/n): ',
                'Derecho':                    '¿Te apasiona analizar leyes y representar clientes en asuntos legales? (s/n): ',
                'Economía':                   '¿Te gusta estudiar mercados y políticas para entender la distribución de recursos? (s/n): '
            },
            'A5': {
                'Licenciatura en Educación':  '¿Te interesa planificar y dictar clases para distintos niveles educativos? (s/n): ',
                'Trabajo Social':             '¿Te gustaría intervenir en comunidades para promover el bienestar social? (s/n): ',
                'Comunicación Social':        '¿Te apasiona producir contenidos y estrategias de comunicación masiva? (s/n): ',
                'Sociología':                 '¿Te atrae investigar estructuras sociales y cambios culturales? (s/n): ',
                'Filosofía':                  '¿Disfrutas reflexionar sobre teorías que explican la realidad y el conocimiento? (s/n): ',
                'Antropología':               '¿Te interesa estudiar culturas y prácticas de diferentes comunidades? (s/n): ',
                'Lingüística':                '¿Te apasiona analizar la estructura y evolución de los idiomas? (s/n): ',
                'Historia':                   '¿Te gusta investigar y narrar eventos del pasado y su impacto en el presente? (s/n): '
            }
        }
        # Inferencia proposicional y reglas extras
        self.rules = self.area_rules[:]
        self.symptoms = []
        self.inference_rules = {
            "modus_ponens": self.modus_ponens,
            "de_morgan_law": self.de_morgan_law,
            "and_elimination": self.and_elimination,
            "biconditional_elimination": self.biconditional_elimination,
            "contraposition": self.contraposition
        }

    def evaluate_rules(self, rules, answers):
        scores = {}
        for rule_text in rules:
            antecedent, consequent = rule_text.split('⇒')
            consequent = consequent.strip()
            symbols = [s.strip() for s in antecedent.split('∧')]
            if all(answers.get(sym, False) for sym in symbols):
                scores[consequent] = scores.get(consequent, 0) + 1
        return scores

    def infer_area(self, answers):
        area_scores = self.evaluate_rules(self.area_rules, answers)
        if not area_scores:
            return None, {}
        best_code = max(area_scores, key=area_scores.get)
        return best_code, area_scores

    def infer_career(self, career_answers):
        scores = {c: int(ans) for c, ans in career_answers.items()}
        best = max(scores, key=scores.get) if scores else None
        return best, scores

    # ---------------- Propositional Logic ----------------
    def extract_symbols(self, alpha):
        propositions = [alpha] + self.rules
        symbols = set()
        for sent in propositions:
            for tok in re.split(r"[ ∧∨⇒⇔()]+", sent):
                if tok and tok != '¬':
                    symbols.add(tok)
        return list(symbols)

    def tt_entails(self, alpha):
        return self.tt_check_all(alpha, self.extract_symbols(alpha), {})

    def tt_check_all(self, alpha, symbols, model):
        if not symbols:
            if self.pl_true_kb(model):
                return self.pl_true(alpha, model)
            return True
        p, rest = symbols[0], symbols[1:]
        m_true, m_false = model.copy(), model.copy()
        m_true[p], m_false[p] = True, False
        return self.tt_check_all(alpha, rest, m_true) and self.tt_check_all(alpha, rest, m_false)

    def pl_true_kb(self, model):
        for s in self.rules + self.symptoms:
            if not self.pl_true(s, model): return False
        return True

    def pl_true(self, sentence, model):
        s = sentence.replace(' ', '')
        if s.startswith('¬'): return not self.pl_true(s[1:], model)
        for op, fn in [('⇔', lambda a,b: a==b), ('⇒', lambda a,b: (not a) or b), ('∨', lambda a,b: a or b), ('∧', lambda a,b: a and b)]:
            if op in s:
                l, r = s.split(op,1)
                return fn(self.pl_true(l, model), self.pl_true(r, model))
        return model.get(s, False)

    # --------------- Inference Rules ---------------
    def modus_ponens(self, a, b): return a and ((not a) or b)
    def and_elimination(self, a, b): return a and b
    def biconditional_elimination(self, a, b): return ((not a or b) and (not b or a))
    def contraposition(self, a, b): return b or (not a)
    def de_morgan_law(self, a, b): return (not a) or (not b)

    def apply_rules(self, facts):
        new_facts = set(facts)
        for nm, fn in self.inference_rules.items():
            for x in facts:
                for y in facts:
                    if x!=y and fn(x,y): new_facts.add(f"{nm}({x},{y})")
        return new_facts

# ---- Interacción con usuario ----
def ask_yes_no(prompt):
    while True:
        r = input(prompt).strip().lower()
        if r in ('s','n'): return r=='s'
        print("Respuesta no válida. Ingresa 's' o 'n'.")

def ask_questions(mapping):
    # Asegurar que mapping sea dict, no set
    if not hasattr(mapping, 'items'):
        raise TypeError("ask_questions espera un diccionario de prompts")
    return {k: ask_yes_no(p) for k,p in mapping.items()}

if __name__ == '__main__':
    kb = KnowledgeBase()
    # Fase 1: preguntas generales
    general_prompts = {
        'S1S': '¿Te interesa comprender cómo funcionan los problemas sociales o económicos de tu comunidad? (s/n): ',
        'S2S': '¿Te motiva encontrar soluciones que puedan mejorar la calidad de vida de otras personas? (s/n): ',
        'S3S': '¿Sueles estar pendiente de noticias o tendencias que afectan a muchas personas al mismo tiempo? (s/n): ',
        'S4S': '¿Te interesa saber cómo las decisiones de gobierno o empresas impactan en el día a día de la sociedad? (s/n): ',
        'S5S': '¿Te sientes cómodo trabajando con personas de diferentes contextos sociales o culturales? (s/n): ',
        'S6S': '¿Prefieres actividades que generen impacto visible en otras personas más que resultados individuales? (s/n): ',
        'S7S': '¿Te interesaría trabajar en contextos donde puedas influir en decisiones colectivas? (s/n): ',
        'S8S': '¿Te sientes atraído por temas relacionados con sostenibilidad, medio ambiente o bienestar social? (s/n): ',
        'S9S': '¿Consideras importante que tu trabajo responda a una necesidad real de la sociedad? (s/n): ',
        'S10S': '¿Te gustaría identificar oportunidades de negocio o innovación a partir de necesidades insatisfechas? (s/n): ',
        'P1S': '¿Te consideras una persona más reflexiva que impulsiva? (s/n): ',
        'P2S': '¿Sueles disfrutar de pasar tiempo a solas? (s/n): ',
        'P3S': '¿Te cuesta seguir rutinas estrictas durante largos periodos de tiempo? (s/n): ',
        'P4S': '¿Te adaptas con facilidad a los cambios inesperados? (s/n): ',
        'P5S': '¿Tomas decisiones principalmente basándote en la lógica más que en las emociones? (s/n): ',
        'C1S': '¿Te resulta fácil expresar tus ideas frente a otras personas? (s/n): ',
        'C2S': '¿Prefieres escuchar antes que hablar en una conversación grupal? (s/n): ',
        'C3S': '¿Disfrutas colaborando en equipo más que trabajando por tu cuenta? (s/n): ',
        'C4S': '¿Te motiva ayudar a otras personas a resolver sus problemas? (s/n): ',
        'C5S': '¿Evitas los conflictos, incluso si eso significa no expresar tu opinión? (s/n): ',
        'M1S': '¿Te sientes más motivado(a) cuando tienes un objetivo claro por cumplir? (s/n): ',
        'M2S': '¿Prefieres tareas que implican movimiento y acción a aquellas que requieren estar sentado mucho tiempo? (s/n): ',
        'M3S': '¿Te interesa entender cómo funcionan las cosas a profundidad antes de usarlas? (s/n): ',
        'M4S': '¿Te consideras una persona organizada con tus tiempos y responsabilidades? (s/n): ',
        'M5S': '¿Sientes que necesitas sentir pasión por lo que haces para comprometerte de verdad? (s/n): '
    }
    print("=== Fase 1: Detección de área ===")
    answers = ask_questions(general_prompts)
    area_code, scores_area = kb.infer_area(answers)
    if not area_code:
        print("No se pudo determinar un área.")
        exit(1)
    area_name = kb.area_names[area_code]
    print(f"Área recomendada: {area_name}")

    # Fase 2: preguntas específicas de carrera
    print(f"=== Fase 2: Carreras para {area_name} ===")
    prompts = kb.career_question_prompts.get(area_code)
    career_answers = ask_questions(prompts)
    best_career, scores_career = kb.infer_career(career_answers)
    print(f"Carrera recomendada: {best_career}")
