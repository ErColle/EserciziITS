class Room:
    def __init__(self, id, floor, seats):
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
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room):
        floor = room.get_floor()
        if self.floors[0] <=floor <=self.floors[1]:
            self.rooms.append(room)
        else: 
            print(f"L'aula è al piano{floor}, si trova fuori dall'intervallo: {self.floors}")
            
    def area(self):
        return sum(room.get_area() for room in self.rooms)

        