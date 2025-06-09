""" def dict_converter(lst: list[tuple]) -> dict:
    result = {}
    
    for key, value in lst: 
        if key in result: 
            result[key] += value
        else: 
            result[key] = value 
    return result

print(dict_converter([(1, 2), (3, 4), (5, 6)]))
"""
""" def neg_pos(numbers: list) -> dict: 
    dizionario: dict = {"positivi": [] , "negativi": [] }
    
    for elem in numbers: 
        if elem >= 0: 
            dizionario["positivi"].append(elem) 
        else: 
            dizionario["negativi"].append(elem) 
    
    return dizionario

print(neg_pos([10, -5, 3, -8, 7, -2, 0, 15, -20, 1]))          """       

""" def price(dizionario: dict) -> dict: 
    
    newdict = {}  
    
    for key, value in dizionario.items(): 
        if value < 50:
            newdict[key] = round(value * 0.10, 2)
            
    return newdict
    
print(price({
    "Maglietta": 45.0,
    "Jeans": 60.0,
    "Cintura": 25.5,
    "Cappello": 15.99,
    "Giacca": 120.0
})) """

class ContactManager:
    
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}
        
    def create_contact(self, name: str, phone_numbers: list[str]): 
        
        if name in self.contacts:
            raise ValueError("Errore. Il contatto esiste già!")
        else: 
            self.contacts[name] = phone_numbers 
            print("Contatto aggiunto!")
            
            return {name: phone_numbers} 
        
    def add_phone_number(self, contact_name: str, phone_number: str): 
                
        if contact_name not in self.contacts: 
            raise ValueError("Errore: Il contatto non esiste.")
        
        elif phone_number in self.contacts: 
            raise ValueError("Errore. Il numero di telefono esiste già.")
        
        else : 

            self.contacts[contact_name].append(phone_number)
            print("Numero aggiunto al contatto!")
            return {contact_name: self.contacts[contact_name] }  

    def remove_phone_number(self, contact_name: str, phone_number: str): 
                
        if contact_name not in self.contacts: 
            raise ValueError("Errore. Il contatto non esiste.")
        
        elif phone_number not in self.contacts: 
            raise ValueError("Errore. Il numero di telefono non è presente.")
        
        else: 
            self.contacts[contact_name].remove(phone_number) 
            return { contact_name: self.contacts[contact_name] } 
            
            
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number:str):
        
        if contact_name not in self.contacts:
            raise ValueError("Errore. Il Contatto non esiste.")
        
        elif old_phone_number not in self.contacts[contact_name] : 
            raise ValueError("Errore. Il nuemro di telefono non è presente.")
        
        else: 
            indice = self.contacts[contact_name].index(old_phone_number)
            self.contacts[contact_name][indice] = new_phone_number
            
            return { contact_name: self.contacts[contact_name] } 
        
    def list_contacts(self):
        
        return list(self.contacts.keys())
    
    def  list_phone_numbers(self, contact_name: str):
        
        if contact_name not in self.contacts:
            raise ValueError("Errore. Il contatto non esiste.")
        
        else: 
            return self.contacts[contact_name] 
        
    def search_contact_by_phone_number(self, phone_number: str): 
        
        contacts_list: list[str] = []
        
        for contacts, list_contacts in self.contacts.items():
            
            if phone_number in list_contacts: 
                
                contacts_list.append(contacts)
            
            if contacts_list == []:
                raise Exception("Errore. Nessun contatto trovato con questo numero di telefono.")   
            
            return contacts_list
        
    

        
         