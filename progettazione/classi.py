from custom_types import Telefono, Email

class Studente:
        # campi dati 
        _matricola: int  # <imm>, noto alla nascita 
        _nome: str  # noto alla nascita
        _genere: str  # noto alla nascita
        _telefono: set[Telefono]  # noto alla nascita  [1..*]
        _email: set[Email]  # noto alla nascita [0..*]
   
        def matricola(self):
                return self._matricola
        
        def nome(self):
                return self._nome

        def genere(self):
                return self._genere
                
        def telefono(self):
                return frozenset(self._telefono)
        
        # setters
        def set_nome(self, nome: str):
                self._nome = nome

        def set_genere(self, genere: str):
                self._genere = genere
                        
        def add_telefono(self, telefono: Telefono):
                self._telefono.add(telefono)
                
        def remove_telefono(self, telefono: Telefono):
                if len(self.telefono()) > 1:
                        self._telefono.remove(telefono)
                else:
                        raise RuntimeError("Non puoi rimuovere l'ultimo telefono")
        
        def add_email(self, email: Email):
                self._email.add(email)
                
        def remove_email(self, email: Email):
                self._email.remove(email)
        
        
        
studente1 = Studente()
studente1._matricola = 123456
studente1._nome = "Mario Rossi"
studente1._genere = "Maschio"
studente1._telefono = "1234567890"

print(studente1.matricola())  # Output: 123456
print(studente1.nome())  # Output: Mario Rossi
print(studente1.genere())  # Output: Maschio
print(studente1.telefono())  # Output: frozenset()
print(studente1._telefono)  # Output: 1234567890

   
        


