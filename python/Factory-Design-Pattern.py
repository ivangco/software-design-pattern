"""
El patrón de diseño de fábrica es un patrón creacional
que proporciona una interfaz para crear objetos de diferentes tipos, 
pero permite a las clases delegar la responsabilidad de instanciar 
objetos a las subclases. Esto significa que una clase abstracta 
define una interfaz para crear un objeto, pero las subclases 
deciden qué tipo de objeto crear.
"""

#Crear la clase amongus
class Amongus:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
#Crear clase white
class White(Amongus):
    def speak(self):
        return self.__class__.__name__+": I'am Amongus Ally!" + " my head is a "+self.name

#Crear clase red
class Red(Amongus):
    def speak(self):
        return self.__class__.__name__+": I'am Amongus Ally!" + " my head is a "+self.name


#Crear fabrica de amongus white
class AmongusFactory:
    def create_Amongus(self, Amongus_type, name):
        if Amongus_type == "White":
            return White(name)
        elif Amongus_type == "Red":
            return Red(name)
        else:
            return f"Impostor Amongus is '{Amongus_type}'"

# Crear una instancia de la fábrica de Amonguses
Amongus_factory = AmongusFactory()

# Crear instancias de Amonguses utilizando la fábrica de Amonguses
White = Amongus_factory.create_Amongus("White", "egg")
Red = Amongus_factory.create_Amongus("Red", "hat")
Black = Amongus_factory.create_Amongus("Black", "flower")

# Llamar a los métodos speak() de los objetos Amongus
print(White.speak()) # Output: White Amongus Ally!
print(Red.speak()) # Red Amongus Ally!
print(Black) # Output: Impostor Amongus is 'Black'


