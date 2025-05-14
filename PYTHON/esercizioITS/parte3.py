# Copia qui di seguito il codice di Realizzazione e Gestione Corsi ITS - Parte 1 
class Room:
    def __init__(self, id:str, floor:int, seats:int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats*2
        
    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area

class Building:
    def __init__(self, name:str, address:str, floors:tuple):
        self.name = name
        self.address= address
        self.floors = floors
        self.rooms = []
        
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room):
        floor = room.get_floor()
        if self.floors[0] <=floor <=self.floors[1]:
            for exist_room in self.rooms:
                if exist_room.get_id()==room.get_id():
                    return
            self.rooms.append(room)   
        else: 
            return 
        
    def area(self):
        return sum(room.get_area() for room in self.rooms)

# Copia qui di seguito il codice di Realizzazione e Gestione Corsi ITS - Parte 2
class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf, name, surname, age, group = None):
        super().__init__(cf, name, surname, age)
        self.group = group
    
    def set_group(self, group):
        self.group = group

class Lecturer(Person):
     def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name: str, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        return 1 if len(self.students) < 10 else len(self.students) // 10
    
    def add_student(self, student):
        if self.limit > len(self.students):
            self.students.append(student)
    
    def add_lecturer(self, lecturer):
        
        limit = self.get_limit_lecturers()
        if limit > len(self.lecturers):
            self.lecturers.append(lecturer)

class Course:
    def __init__(self, name: str):
        self.name = name
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def get_groups(self):
        return self.groups

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                return
