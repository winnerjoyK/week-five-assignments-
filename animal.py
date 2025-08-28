 def move(self):
        self._energy -= 8
        self._coils -= 1
        return f"{self.name} is slithering with {self._coils} coils remaining "
    
    def shed_skin(self):
        self._coils = 3
        return "New skin revealed"

def animal_parade():
    creatures = [
        Bird("Golden Eagle", "Mountains", 2.3),
        Fish("Clownfish", "Coral Reef", "Pectoral"),
        Snake("King Cobra", "Jungle", 3.8)
    ]
    
    for animal in creatures:
        print(f"\n=== {animal} ===")
        print(animal.move())
        print(animal.get_energy())
        if isinstance(animal, Bird):
            print(animal.chirp())
        elif isinstance(animal, Fish):
            print(animal.bubble())
        elif isinstance(animal, Snake):
            print(animal.shed_skin())

if __name__ == "__main__":
    animal_parade()