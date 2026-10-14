from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria",100,15)
    goblin = Character("Goblin",30,5)
    
    knight = Character("Knight", 60,10)
    orc = Character("Orc", 45, 8)
    
    for round_number in range(1,4):
        print(f"\n----Round {round_number} -----")
        
        knight.attack(orc)
        orc.attack(knight)
        
        print(knight.describe())
        print(orc.describe())
        
        
    print(hero.describe())
    print(goblin.describe())
    
    
    hero.heal(20)
    print(hero.describe())
    
    
    hero.attack(goblin)
    print(goblin.describe())
    