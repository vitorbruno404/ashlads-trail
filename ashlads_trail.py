import random
import time

def print_slow(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

E_WASTE_ITEMS = [
    "Swollen Powerbank",
    "Fried Microprocessor",
    "Single AirPod Pro (Left)",
    "Frayed USB-C Cable",
    "Scrapped E-Scooter Motor",
    "Broken VR Headset",
    "Cracked iPhone 6",
    "Glitching LED Panel",
    "Discarded Raspberry Pi 4",
    "Old Tesla Battery Cell"
]

STRANGERS_DATABASE = [
    {"name": "Birger the E-Bike Mechanic", "perk": "fixed your gear"},
    {"name": "Kari the Ultralight Hiker", "perk": "shared real freeze-dried stew"},
    {"name": "Morten the Råner", "perk": "gave you a lift and a Monster Energy"},
    {"name": "Astrid the NTNU Tech Student", "perk": "soldered your electronic junk"},
    {"name": "Svein the Retired Electrician", "perk": "taught you safe wiring"},
    {"name": "Linn the Vipps Enthusiast", "perk": "Vipps'd you 100 NOK for snacks"}
]

def main():
    print_slow("==================================================================")
    print_slow("   THE MODERN ASHLAD'S TRAIL: HIGH-TECH JOURNEY TO THE CAPITAL    ")
    print_slow("==================================================================")
    print_slow("You are Espen Askeladd in modern Norway. While your brothers Per and Pål")
    print_slow("drive leased Teslas, you set off on foot with a backpack, hunting")
    print_slow("for EE-avfall (e-waste) and making genuine friends along the way.")
    print_slow("------------------------------------------------------------------")

    km_traveled = 0
    total_km = 400
    food_rations = 80
    energy = 100
    day = 1
    inventory = ["Old USB-A Cable"]
    friends = []

    alive = True
    won = False

    while alive and not won:
        friend_names = [f["name"] for f in friends]
        
        print(f"\n--- Day {day} ---")
        print(f"Distance to Capital: {km_traveled} / {total_km} km")
        print(f"Supplies (Lefse & Drinks): {food_rations} units")
        print(f"Stamina: {energy}%")
        print(f"E-Waste Pocket: {', '.join(inventory) if inventory else 'Empty'}")
        print(f"Friends Made ({len(friends)}): {', '.join(friend_names) if friends else 'None yet'}")
        print("-----------------")

        print("Actions:")
        print("1. Trudge Ahead (Hike kilometers along the E6/fjords)")
        print("2. Search EE-Avfall (Rummage through electronic waste bins)")
        print("3. Greet & Chat with Strangers (Make new friends)")
        print("4. Rest at a DNT Cabin / Gas Station (Recover energy)")
        print("5. Buy Grandiosa & Lefse (Replenish supplies via Vipps)")
        print("6. Give Up & Take the Bus Home")

        choice = input("What will Espen do? (1-6): ")

        if choice == '1':
            dist = random.randint(20, 45)
            food_used = random.randint(10, 18)
            km_traveled += dist
            food_rations -= food_used
            energy -= random.randint(8, 15)
            day += random.randint(1, 2)
            print_slow(f"You hiked {dist} km through Norwegian nature, consuming {food_used} food/drink units.")

        elif choice == '2':
            day += 1
            energy -= 5
            available_items = [i for i in E_WASTE_ITEMS if i not in inventory]
            if available_items:
                found_item = random.choice(available_items)
                inventory.append(found_item)
                print_slow(f"⚡ 'I found a thing!' Espen cheers as he pulls a [{found_item}] from an EE-avfall container!")
            else:
                print_slow("You checked the e-waste bin, but your pockets are crammed with circuit boards already!")

        elif choice == '3':
            day += 1
            energy = min(100, energy + 10)
            available_strangers = [s for s in STRANGERS_DATABASE if s not in friends]
            if available_strangers:
                new_friend = random.choice(available_strangers)
                friends.append(new_friend)
                print_slow(f"👋 You sat down and struck up a warm conversation with {new_friend['name']}.")
                print_slow(f"You hit it off! They became your friend and {new_friend['perk']} (+10% stamina)!")
            else:
                print_slow("You met a fellow hiker on the trail, shared some coffee, and had a great laugh!")

        elif choice == '4':
            energy_gain = random.randint(25, 40)
            food_used = random.randint(12, 22)
            energy = min(100, energy + energy_gain)
            food_rations -= food_used
            day += random.randint(1, 2)
            print_slow(f"You rested inside a warm cabin with waffles and coffee (+{energy_gain}% energy, -{food_used} food).")

        elif choice == '5':
            food_bought = random.randint(25, 45)
            food_rations += food_bought
            day += 1
            print_slow(f"You Vipps'd some NOK at a Circle K for Grandiosa, lefse, and Monster energy (+{food_bought} supplies).")

        elif choice == '6':
            print_slow("Espen gave up, caught the Vy express bus home, and sat by the fireplace. Game Over.")
            break

        else:
            print("Invalid choice. Per and Pål shake their heads at you from their Teslas.")
            continue

        if choice in ['1', '2', '3'] and random.random() < 0.45:
            encounter = random.choice(["cyber_troll", "scooter_breakdown", "rain_storm", "friend_visit"])

            if encounter == "cyber_troll":
                print_slow("\n👹 A Modern Cyber-Troll blocks a fjord bridge, demanding an innovation toll!")
                if inventory:
                    used_item = inventory.pop(0)
                    print_slow(f"Espen pulls out [{used_item}] from his e-waste collection!")
                    print_slow(f"The Troll is fascinated by the gadget: 'Incredible tech scrap! You may pass!'")
                elif friends:
                    helper = random.choice(friends)
                    print_slow(f"Your friend {helper['name']} steps up and negotiates with the troll on your behalf! You pass safely.")
                else:
                    loss = random.randint(20, 35)
                    energy -= loss
                    print_slow(f"You had no e-waste and no friends to help! You had to argue with the troll and lost {loss}% stamina.")

            elif encounter == "scooter_breakdown":
                print_slow("\n⚡ You find a stranded tourist with a broken electric scooter on a mountain trail.")
                if "Frayed USB-C Cable" in inventory or "Old Tesla Battery Cell" in inventory:
                    print_slow("Using your electronic junk, you hotwired a quick fix for their scooter!")
                    print_slow("In gratitude, they transferred some funds via Vipps for your snacks (+20 supplies).")
                    food_rations += 20
                else:
                    print_slow("You wished them luck and kept walking, losing a bit of time.")
                    day += 1

            elif encounter == "rain_storm":
                print_slow("\n🌧️ Classic Norwegian torrential rain pours down!")
                if friends:
                    pal = random.choice(friends)
                    print_slow(f"Luckily, your friend {pal['name']} lives nearby and invites you inside until the storm passes!")
                else:
                    energy -= 15
                    print_slow("You got soaked to the bone and lost 15% stamina.")

            elif encounter == "friend_visit":
                if friends:
                    pal = random.choice(friends)
                    print_slow(f"\n🎉 Surprise! {pal['name']} catches up to you on the trail to share homemade lefse!")
                    food_rations += 15

        if energy <= 0:
            alive = False
            print_slow("\n💀 You ran out of stamina and fell asleep on a bench outside a 7-Eleven.")
        elif food_rations <= 0:
            alive = False
            print_slow("\n💀 You ran out of supplies. Per and Pål won the kingdom.")
        elif km_traveled >= total_km:
            won = True
            print_slow(f"\n🏰 CONGRATULATIONS! Espen reached the Capital in {day} days!")
            print_slow(f"With {len(friends)} true friends and pockets full of e-waste, he pitched a green tech startup to the King!")
            print_slow("He won half the tech company and the Princess's partnership!")

    print_slow("\n--- Final Journey Summary ---")
    print(f"Total Days: {day}")
    print(f"Distance Covered: {km_traveled} km")
    print(f"Remaining Supplies: {max(0, food_rations)}")
    print(f"E-Waste Left: {', '.join(inventory) if inventory else 'None'}")
    print(f"Friends Made: {', '.join([f['name'] for f in friends]) if friends else 'None'}")

if __name__ == "__main__":
    main()
