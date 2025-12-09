from flask import Flask

from abc import ABC

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float ):
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    def species(self):
        pass

    def daily_food_grams(self):
        pass

    def info(self):
        return { "id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg}

    def bmi_like(self):
        return self.weight_kg / (self.age_years + 1)

class Dog(Animal):

    def __init__(self, id, name, age_years, weight_kg, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "Dog"

    def daily_food_grams(self):
        return 200 + self.age_years * 50

    def info(self):
        return { "id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg, "breed": self.breed, "is_trained": self.is_trained}

class Cat(Animal):

    def __init__(self, id, name, age_years, weight_kg, favourite_toy: str, indoor_only: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.favourite_toy = favourite_toy
        self.indoor_only = indoor_only

    def species(self):
        return "Cat"

    def daily_food_grams(self):
        return 100 + self.age_years * 30

    def info(self):
        return {"id": self.id, "name": self.name, "species": self.species(), "age_years": self.age_years, "weight_kg": self.weight_kg, "favourite_toy": self.favourite_toy, "indoor_only": self.indoor_only}

class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = {}
        self.adoptions: dict[str, str] = {}

    def add(self, animal):
        if animal.id in self.animals:
            print("animale gia presente")
        else:
            self.animals[animal.id] = animal

    def get_animal(self, animal_id):
        if animal_id not in self.animals:
            return None
        else:
            return self.animals[animal_id]

    def list_all(self):
        for animal in self.animals.values():
            print(animal.info())

    def is_adopted(self, animal_id):
        if animal_id in self.adoptions:
            return True
        else: return False

    def set_adopted(self, animal_id, adopter_name):
        if animal_id in self.adoptions:
            print("adozione gia registrata")
        else:
            self.adoptions[animal_id] = adopter_name

shelter = Shelter()
shelter.add(Dog("d1", "Fido", 3, 15.0, "Labrador", True))
shelter.add(Cat("c1", "Whiskers", 2, 4.5, "Ball", True))
shelter.add(Dog("d2", "Rex", 5, 20.0, "German Shepherd", False))

from flask import Flask, jsonify, url_for
from abc import ABC

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float):
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    def species(self):
        pass

    def daily_food_grams(self):
        pass

    def info(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg
        }

class Dog(Animal):
    def __init__(self, id, name, age_years, weight_kg, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "Dog"

    def daily_food_grams(self):
        return 200 + self.age_years * 50

    def info(self):
        data = super().info()
        data.update({"breed": self.breed, "is_trained": self.is_trained})
        return data

class Cat(Animal):
    def __init__(self, id, name, age_years, weight_kg, favourite_toy: str, indoor_only: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.favourite_toy = favourite_toy
        self.indoor_only = indoor_only

    def species(self):
        return "Cat"

    def daily_food_grams(self):
        return 100 + self.age_years * 30

    def info(self):
        data = super().info()
        data.update({"favourite_toy": self.favourite_toy, "indoor_only": self.indoor_only})
        return data

class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = {}
        self.adoptions: dict[str, str] = {}

    def add(self, animal):
        self.animals[animal.id] = animal

    def get_animal(self, animal_id):
        return self.animals.get(animal_id, None)

    def list_animals(self):
        return list(self.animals.values())

    def is_adopted(self, animal_id):
        return animal_id in self.adoptions

    def set_adopted(self, animal_id, adopter_name):
        self.adoptions[animal_id] = adopter_name


shelter = Shelter()
shelter.add(Dog("d1", "Fido", 3, 15.0, "Labrador", True))
shelter.add(Cat("c1", "Whiskers", 2, 4.5, "Ball", True))
shelter.add(Dog("d2", "Rex", 5, 20.0, "German Shepherd", False))

app = Flask(__name__)

@app.route("/")
def home():

    links = {"list_animals": url_for("list_animals", _external=True)}
    for animal in shelter.list_animals():
        links[f"{animal.id}_info"] = url_for("get_animal", animal_id=animal.id, _external=True)
        links[f"{animal.id}_food"] = url_for("get_animal_food", animal_id=animal.id, _external=True)
        links[f"{animal.id}_adoption"] = url_for("get_animal_adoption", animal_id=animal.id, _external=True)

    return jsonify({
        "message": "Welcome to Animal Shelter API",
        "links": links
    })

@app.route("/animals")
def list_animals():
    return jsonify({"animals": [a.info() for a in shelter.list_animals()]})

@app.route("/animals/<animal_id>")
def get_animal(animal_id):
    animal = shelter.get_animal(animal_id)
    if animal:
        return jsonify(animal.info())
    return jsonify({"error": "Animal not found"}), 404

@app.route("/animals/<animal_id>/food")
def get_animal_food(animal_id):
    animal = shelter.get_animal(animal_id)
    if animal:
        return jsonify({"animal_id": animal.id, "daily_food_grams": animal.daily_food_grams()})
    return jsonify({"error": "Animal not found"}), 404

@app.route("/animals/<animal_id>/adoption")
def get_animal_adoption(animal_id):
    animal = shelter.get_animal(animal_id)
    if animal:
        return jsonify({"animal_id": animal.id, "adopted": shelter.is_adopted(animal_id)})
    return jsonify({"error": "Animal not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)





