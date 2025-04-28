class Persona:
    # i dati di persona sono vuoti
    def __init__(self, name, surname, age):
        self.name = name
        self.lastname = surname
        self.age = age

    def display_data(self):
        print(f'Name: {self.name}, LastName: {self.lastname}, age: {self.age}') 
    
    # funzioni con set prendono paremetri in input 
    def set_name(self, name):
        self.name = name
       
    def set_lastname(self, lastname: str):
        self.lastname = lastname
    
    def set_age(self, age: str):
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
    # non ha nessu input ma ritorna un valore
    def get_name(self) -> str:
        return self.name
    
    def get_lastname(self) -> str:
        return self.lastname
    

    def get_age(self) -> int:
        return self.age
    
    def speak(self) -> None:

        print(f'Hello my name is {self.get_name()}!')

    def __str__(self) -> str:
        return f'Ciao mi chiamo {self.get_name()} {self.get_lastname()} ho {self.get_age()} anni!'