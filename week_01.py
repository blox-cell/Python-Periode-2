print("Hello Periode 2!")

# Stap 1 - De speler aanmaken
player_name = input("Wat is jouw naam? ")
player_gold = 100
inventory = []

print(f"Welkom, {player_name}! Je hebt {player_gold} gold om te besteden.")

# Stap 2 - De winkelvoorraad
items = ["Sword", "Shield", "Potion", "Bow"]

print("\nDit is de winkelvoorraad:")
for item in items:
    print(f"- {item}")

# Functie om items te kopen (maakt de code lekker makkelijk)
def koop_item(item_naam, prijs):
    global player_gold
    if player_gold >= prijs:
        player_gold -= prijs
        inventory.append(item_naam)
        print(f"Je hebt een {item_naam} gekocht!")
        print(f"Je hebt nu nog {player_gold} gold over.")
    else:
        print(f"Je hebt niet genoeg gold om een {item_naam} te kopen!")

# Stap 3 & 4 - Het winkelmenu en items kopen
while True:
    print("n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")
    
    keuze = input("What would you like to do? ")
    
    match keuze:
        case "1":
            koop_item("Sword", 50)
        case "2":
            koop_item("Shield", 40)
        case "3":
            koop_item("Potion", 20)
        case "4":
            koop_item("Bow", 60)
            
        # Stap 5 - Inventory bekijken
        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Jouw inventory:")
                for item in inventory:
                    print(f"- {item}")
                    
        # Stap 6 - De winkel verlaten
        case "6":
            print("Bedankt voor het winkelen en tot ziens!")
            print(f"Je hebt nog {player_gold} gold over.")
            break
            
        case _:
            print("Ongeldige keuze, kies een getal tussen 1 en 6.")