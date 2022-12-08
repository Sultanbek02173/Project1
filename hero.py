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

hero = SuperHero("Bruce Wayne", "Batman", "Ninjutsu", 100, "I'm whatever Gotham needs me to be")
hero.nameHero()
hero.myltyhealth_points()
print(hero)
print(len(hero))


 
# dsfsd