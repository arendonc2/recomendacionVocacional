from agent import DiagnosisAgent

class DoInferencias:
    def __init__(self):
        self.agent = DiagnosisAgent()

    def extract_symbols(self, KB, alpha): # La función extract simbolos nos permite extraer los simbolos relevantes del conocimiento base y de alpha
        propotitions=[]
        propotitions.append(alpha)
        for i in self.agent.kb.rules:
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


    def tt_entails(self, KB, alpha):
        """Verifica si KB lógicamente implica alpha usando la enumeración de la tabla de verdad"""
        symbols = self.extract_symbols(KB, alpha)  # Extraer los símbolos del KB y alpha
        print(symbols)
        return self.tt_check_all(KB, alpha, symbols, {})

    def tt_check_all(self, KB, alpha, symbols, model):
        """Función recursiva que evalúa si el modelo satisface el KB y alpha."""
        if not symbols: #en caso de que ya se halla asignado valor True o False a todos los simbolos
            print("Probar con", model)
            if self.pl_true_kb(KB, model): #ver si el modelo satisface el KB
                print("Es el modelo de prueba que cumple con KB: ", model)
                print("Esto es alpha: ", alpha)
                print("Esto es el resultado de alpha en el modelo: ", self.pl_true(alpha, model))
                print("-------------------------------------------------------------------")
                return self.pl_true(alpha, model)
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
            return self.tt_check_all(KB, alpha, rest, model_true) and self.tt_check_all(KB, alpha, rest, model_false)



    def pl_true_kb(self, KB, model):
        rules_symptoms = KB.rules + KB.symptoms
        #Evalúa si todo el conocimiento base es verdadero en un modelo dado.
        for sentence in rules_symptoms:
            print("resultado de evaluación de kb en el modelo: ", self.pl_true(sentence, model))
            if not self.pl_true(sentence, model):
                return False  # Si alguna oración es falsa, todo el KB es falso
        return True  # Si todas las oraciones son verdaderas, el KB es verdadero

    def pl_true(self, sentence, model):
        # Elimina espacios para simplificar
        sentence = sentence.replace(")", "").replace("(", "").replace(" ","")

        # Caso para la negación (¬)
        if sentence.startswith("¬"):
            return not self.pl_true(sentence[1:], model)

        # Caso para la bicondicional (⇔)
        if "⇔" in sentence:
            lhs, rhs = sentence.split("⇔")
            #print("xxx: ", pl_true(lhs, model))
            #print("yyy: ", pl_true(rhs, model))
            return self.pl_true(lhs, model) == self.pl_true(rhs, model)

        # Caso para el condicional (⇒)
        if "⇒" in sentence:
            lhs, rhs = sentence.split("⇒")
            return not self.pl_true(lhs, model) or self.pl_true(rhs, model)

        # Caso para la disyunción (∨)
        if "∨" in sentence:
          if len(sentence.split("∨"))==2:
            lhs, rhs = sentence.split("∨")
            #print("esto es lhs: ", lhs)
            #print("esto es rhs: ", rhs)
            return self.pl_true(lhs, model) or self.pl_true(rhs, model)
          else:
            lhs, rhs, ohs = sentence.split("∨")
            return self.pl_true(lhs, model) or self.pl_true(rhs, model) or self.pl_true(ohs, model)

        # Caso para la conjunción (∧)
        if "∧" in sentence:
            lhs, rhs = sentence.split("∧")
            return self.pl_true(lhs, model) and self.pl_true(rhs, model)

        # Si es una proposición atómica, busca en el modelo
        if sentence in model:
            return model[sentence]

        # Retorna False si no encuentra la proposición en el modelo
        return False