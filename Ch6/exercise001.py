def animalSound():
    animal, sound = input('Enter an animal and its corresponding sound: ').split()
    return animal, sound

def oldMacDonald(animal_sound):
    animal = animal_sound[0]
    sound  = animal_sound[1]
    print(
        """
        Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
        And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!
        With a {1}, {1} here and a {1} {1} there.
        Here a {1}, there a {1}, everywhere a {1} {1}.
        Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!""".format(animal, sound)
        )
             
animal_sounds = []
for i in range(5):
    animal_sounds.append(animalSound())

for animal_sound in animal_sounds:
    oldMacDonald(animal_sound)
    
