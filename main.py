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
        self.symptoms = []

    def tell(self, symptom):
        self.symptoms.append(symptom)

    def ask(self):
        diagnoses = set()
        for symptom in self.symptoms:
            if symptom in self.rules:
                diagnoses.update(self.rules[symptom].split("∨"))
        return diagnoses if diagnoses else {"Sin diagnóstico"}


class DiagnosisAgent:
    def __init__(self):
        self.kb = KnowledgeBase()

    def perceive_symptoms(self, symptoms):
        for symptom in symptoms:
            self.kb.tell(symptom)

    def diagnose(self):
        return self.kb.ask()


def extract_symbols(KB,alpha): # La función extract simbolos nos permite extraer los simbolos relevantes del conocimiento base y de alpha
    propotitions=[]
    propotitions.append(alpha)
    for i in agent.kb.rules:
        if "Executed" not in i:
            if type(i)==tuple and len(i[0])!=0:
                print(i[0])
                propotitions.append(str(i[0][0]))
            elif (type(i)!=tuple): propotitions.append(i)
    symbols = set()
    print(propotitions)
    for sentence in propotitions:
        # Divide y extrae las partes de la oración, aquí se hace de manera simplificada
        for symbol in sentence.replace("(", "").replace(")", "").replace("⇔", "").replace("¬", "").split():
            if symbol not in ["∨", "∧", "⇒"]:
                symbols.add(symbol)
    return(list(symbols))


def tt_entails(KB, alpha):
    """Verifica si KB lógicamente implica alpha usando la enumeración de la tabla de verdad"""
    symbols = extract_symbols(KB, alpha)  # Extraer los símbolos del KB y alpha
    print(symbols)
    return tt_check_all(KB, alpha, symbols, {})

def tt_check_all(KB, alpha, symbols, model):
    """Función recursiva que evalúa si el modelo satisface el KB y alpha."""
    if not symbols: #en caso de que ya se halla asignado valor True o False a todos los simbolos
        print("Probar con", model)
        if pl_true_kb(KB, model): #ver si el modelo satisface el KB
            print("Es el modelo de prueba que cumple con KB: ", model)
            print("Esto es alpha: ", alpha)
            print("Esto es el resultado de alpha en el modelo: ", pl_true(alpha, model))
            print("-------------------------------------------------------------------")
            return pl_true(alpha, model)
        else:
            return True  # Si KB es falso en el modelo, no importa alpha
    else:
        P = symbols[0]  # El primer simbolo
        #print(P)
        rest = symbols[1:]  # Los simbolos restantes
        # Probar con P verdadero
        model_true = model.copy()
        model_true[P] = True
        # Probar con P falso
        model_false = model.copy()
        model_false[P] = False
        #print("Probar con P False", model_false)
        # Evaluar recursivamente ambos casos
        return tt_check_all(KB, alpha, rest, model_true) and tt_check_all(KB, alpha, rest, model_false)



def pl_true_kb(KB, model):
    rules_symptoms = KB.rules + KB.symptoms
    #Evalúa si todo el conocimiento base es verdadero en un modelo dado.
    for sentence in rules_symptoms:
        print("resultado de evaluación de kb en el modelo: ", pl_true(sentence, model))
        if not pl_true(sentence, model):
            return False  # Si alguna oración es falsa, todo el KB es falso
    return True  # Si todas las oraciones son verdaderas, el KB es verdadero

def pl_true(sentence, model):
    # Elimina espacios para simplificar
    sentence = sentence.replace(")", "").replace("(", "").replace(" ","")

    # Caso para la negación (¬)
    if sentence.startswith("¬"):
        return not pl_true(sentence[1:], model)

    # Caso para la bicondicional (⇔)
    if "⇔" in sentence:
        lhs, rhs = sentence.split("⇔")
        #print("xxx: ", pl_true(lhs, model))
        #print("yyy: ", pl_true(rhs, model))
        return pl_true(lhs, model) == pl_true(rhs, model)

    # Caso para el condicional (⇒)
    if "⇒" in sentence:
        lhs, rhs = sentence.split("⇒")
        return not pl_true(lhs, model) or pl_true(rhs, model)

    # Caso para la disyunción (∨)
    if "∨" in sentence:
      if len(sentence.split("∨"))==2:
        lhs, rhs = sentence.split("∨")
        #print("esto es lhs: ", lhs)
        #print("esto es rhs: ", rhs)
        return pl_true(lhs, model) or pl_true(rhs, model)
      else:
        lhs, rhs, ohs = sentence.split("∨")
        return pl_true(lhs, model) or pl_true(rhs, model) or pl_true(ohs, model)

    # Caso para la conjunción (∧)
    if "∧" in sentence:
        lhs, rhs = sentence.split("∧")
        return pl_true(lhs, model) and pl_true(rhs, model)

    # Si es una proposición atómica, busca en el modelo
    if sentence in model:
        return model[sentence]

    # Retorna False si no encuentra la proposición en el modelo
    return False

# Simulación
patients = [["S2"],
            ["S1", "S4"],
            ["S2", "S3"]]  # Paciente 1: Fiebre y Tos

inferencias = []

for i, patient in enumerate(patients, 1):
    agent = DiagnosisAgent()
    agent.perceive_symptoms(patient)
    alpha = "E1"

    inferencias.append(f'¿KB implica el diagnóstico alpha? para el paciente {i}: , {tt_entails(agent.kb, alpha)}')

for i in inferencias:
    print(i)