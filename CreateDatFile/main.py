import random


def main():
    vehicle_type = ["Bicycle", "Motorcycle", "Car"]

    if random.choice(vehicle_type) == 'Car':
        car_made = ["Ford", "Honda", "Toyota", "Nissan", "Dodge", "Hyundai", "Audi", "Kia", "Volvo"]

        ford_models = {
            'Sedan': ["Fiesta", "Focus", "Fusion", "Taurus"],
            'Truck': ["F150 Regular Cab", "F150 Super Cab", "F150 SuperCrew Cab", "F250 SuperDutyCrew Cab"],
            'SUV': ["EcoSport", "Edge", "Escape", "Expedition", "Explorer", "Flex"],
            'Van': ["Transit 150", "Transit 250", "Transit 350", "Transit 350 HD", "Transit 350 Wagon"]
        }

        honda_models = {
            'Sedan': ["Accord", "Civic", "Fit", "Insight", "Clarity"],
            'Truck': ["Ridge line"],
            'SUV': ["CR-V", "HR-V", "Pilot"],
            'Van': ["Odyssey"]
        }

        toyota_model = {
            'Sedan': ["Avalon", "Camry", "Corolla", "Mirai", "Prius", "Yaris"],
            'Truck': ["Tacoma Access Cab", "Tacoma Double Cab", "Tundra CrewMax", "Tundra Double Cab"],
            'SUV': ["4Runner", "C-HR", "Highlander", "Land Cruiser", "RAV4", "Sequoia"],
            'Van': ["Sienna"]
        }

        nissan_model = {
            'Sedan': ["Altima", "Maxima", "Sentra", "Versa", "Versa Note"],
            'Truck': ["Frontier Crew Cab", "Frontier King Cab", "Titan Crew Cab", "Titan King Cab", "Titan Single Cab",
                      "Titan XD Crew Cab", "Titan XD King Cab", "Titan XD Single Cab"],
            'SUV': ["Armada", "Kicks", "Murano", "Pathfinder", "Rogue", "Rogue Sport"],
            'Van': ["NV1500 Cargo", "NV200", "NV2500 HD cargo", "NV3500 HD Cargo", "NV3500 HD Passenger"]
        }

        dodge_model = {
            'Sedan': ["Charger"],
            'SUV': ["Durango", "Journey"],
            'Van': ["Grand Caravan Passenger"]

        }

        kia_model = {
            'Sedan': ["Cadenza", "Forte", "Optima", "Rio", "Stinger"],
            'SUV': ["Sorento", "Sportage"],
            'Van': ["Sedona"]
        }

        hyundai_model = {
            'Sedan': ["Accent", "Elantra", "Ioniq", "Sonata"],
            'SUV': ["Kona", "Santa Fe", "Santa Fe Sport", "Santa Fe XL", "Tucson"]
        }

        audi_model = {
            'Sedan': ["A3", "A4", "A5", "A6", "A7", "A8", "RS 3", "RS 7", "S3", "S4", "S5", "S6", "S7", "S8"],
            'SUV': ["e-tron", "Q3", "Q4", "Q7", "SQ5"]
        }

        volvo_model = {
            'Sedan': ["S60", "S90"],
            'SUV': ["XC40", "XC60", "XC90"]
        }

    car_color = ["White", "Silver", "Black", "Dark Blue", "Dark Gray", "Red", "Dark Green", "Light Brown"]

    color = random.choice(car_color)
    price = random.randrange(20, 60, 3) * 1000
    mileage = random.randrange(1, 5, 3) * 1000


if __name__ == "__main__":
    main()
