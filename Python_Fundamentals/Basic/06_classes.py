class Empty:
    pass

class Person:
    def __init__(self,name,surname, alias = "sin alias"):
        self.__name = name #PROPIEDAD PRIVADA
        self.surname = surname
        self.full_name = f"{name} {surname} {alias}"
    def get_name(self):
        return self.__name
    def walk(self):
        print(f"{self.full_name} esta caminando") 
        
           
my_person = Person("Hernan", "ESQ")
print(f"{my_person.get_name()} {my_person.surname}")
my_person.walk()
print(f"My name is: {my_person.get_name()}")

my_other_person = Person("Lucas", "More", "lol")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "lucas more (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)


my_other_person = Person("Matias", "Core")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Matias Core (chiquito)"
print(my_other_person.full_name)