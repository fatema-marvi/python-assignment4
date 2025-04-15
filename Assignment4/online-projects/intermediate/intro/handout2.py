# Gravitational constants relative to Earth's gravity
PLANET_MULTIPLIERS = {
    "mercury": 0.38,
    "venus": 0.91,
    "earth": 1.00,
    "moon": 0.165,
    "mars": 0.378,
    "jupiter": 2.34,
    "saturn": 1.06,
    "uranus": 0.92,
    "neptune": 1.19,
    "pluto": 0.06
}

def main():
    # Step 1: Get user's Earth weight
    earth_weight_str = input("Enter your weight on Earth: ")
    earth_weight = float(earth_weight_str)

    # Step 2: Ask for a planet
    print("Choose a celestial body from the list below:")
    for planet in PLANET_MULTIPLIERS:
        print(" -", planet.capitalize())
        
    chosen_planet = input("Which planet/moon would you like to know your weight on?: ").strip().lower()

    # Step 3: Check if the planet is valid
    if chosen_planet in PLANET_MULTIPLIERS:
        multiplier = PLANET_MULTIPLIERS[chosen_planet]
        planet_weight = earth_weight * multiplier
        rounded_weight = round(planet_weight, 2)
        print(f"Your weight on {chosen_planet.capitalize()} would be: {rounded_weight}")
    else:
        print("Sorry, that is not a valid planet or moon from our list.")

# Run the program
if __name__ == '__main__':
    main()
