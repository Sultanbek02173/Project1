class SuperHero:
    people='people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def nameHero(self):
        print("Name hero is", self.name)
    
    def myltyhealth_points(self):
        print("Health_points: ",self.health_points * 2)

    def __str__(self) -> str:
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}"
        
    def __len__(self):
        return len(self.catchphrase)

# hero = SuperHero("Bruce Wayne", "Batman", "Ninjutsu", 100, "I'm whatever Gotham needs me to be")
# hero.nameHero()
# hero.myltyhealth_points()
# print(hero)
# print(len(hero))

# Воздушный герой

class AirHero(SuperHero):
    people = "AirHero"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
    def myltyhealth_points(self):
        print("Health_points: ",self.health_points ** 2)
    def flying(self):
        self.fly = True
        print("Fly in the True_phrase: ", self.fly)
    
    
# Земной герой

class EarthlyHero(SuperHero):
    people = "EarthlyHero"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
    def myltyhealth_points(self):
        print("Health_points: ",self.health_points ** 2)
    def flying(self):
        self.fly = False
        print("Fly in the True_phrase: ", self.fly)
        
# Космический герой

class SpaceHero(SuperHero):
    people = "SpaceHero"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
    def myltyhealth_points(self):
        print("Health_points: ",self.health_points ** 2)
    def flying(self):
        self.fly = True
        print("Fly in the True_phrase: ", self.fly)
    


hero = AirHero("Tony Stark", "Iron Man", "Engineer", 150, "I don't paint")
hero.nameHero()
hero.myltyhealth_points()
print(hero)
print(len(hero))
hero.flying()
print()

hero = EarthlyHero("Bruce Wayne", "Batman", "Ninjutsu", 100, "I'm whatever Gotham needs me to be")
hero.nameHero()
hero.myltyhealth_points()
print(hero)
print(len(hero))
hero.flying()
print()

hero = SpaceHero("Peter Jason Quill", "Star Lord", "strategist and melee expert", 130, "Sometimes what we are looking for all our lives... all the time at our side, but we do not notice")
hero.nameHero()
hero.myltyhealth_points()
print(hero)
print(len(hero))
hero.flying()