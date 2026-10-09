"""
BMI Calculator - Python Project

Features:
- Calculate Body Mass Index (BMI)
- Categorize BMI results
- Validate user input
- Display health suggestions
- Calculate BMI for multiple users
- Maintain session history
"""

from datetime import datetime


class BMICalculator:
    """A simple class-based BMI calculator."""

    def __init__(self):
        self.history = []

    def calculate_bmi(self, weight, height):
        """Calculate BMI using weight in kg and height in meters."""
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")

        return weight / (height ** 2)

    def get_category(self, bmi):
        """Return the BMI category for adults."""
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def get_suggestion(self, category):
        """Return general educational guidance."""
        suggestions = {
            "Underweight":
                "Consider balanced nutrition and seek advice if concerned.",
            "Normal weight":
                "Maintain balanced eating habits and regular activity.",
            "Overweight":
                "Consider sustainable lifestyle habits and regular activity.",
            "Obesity":
                "Consider discussing your health goals with a healthcare professional."
        }

        return suggestions.get(
            category,
            "Consult a qualified healthcare professional for guidance."
        )

    def get_valid_number(self, prompt):
        """Keep asking until the user enters a positive number."""
        while True:
            try:
                value = float(input(prompt))

                if value <= 0:
                    print("Please enter a number greater than zero.")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_person_details(self):
        """Collect the user's basic details."""
        name = input("Enter your name: ").strip()

        if not name:
            name = "User"

        weight = self.get_valid_number("Enter weight in kilograms: ")
        height_cm = self.get_valid_number("Enter height in centimeters: ")

        height_m = height_cm / 100

        return name, weight, height_m

    def display_result(self, name, weight, height, bmi):
        """Display the BMI calculation and its category."""
        category = self.get_category(bmi)
        suggestion = self.get_suggestion(category)

        print("\n" + "=" * 45)
        print("             BMI CALCULATION")
        print("=" * 45)
        print(f"Name          : {name}")
        print(f"Weight        : {weight:.2f} kg")
        print(f"Height        : {height * 100:.2f} cm")
        print(f"BMI           : {bmi:.2f}")
        print(f"Category      : {category}")
        print(f"Suggestion    : {suggestion}")
        print("=" * 45)
        print("BMI is a screening measure, not a diagnosis.")

        record = {
            "name": name,
            "weight": weight,
            "height_cm": height * 100,
            "bmi": round(bmi, 2),
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.history.append(record)

    def calculate_for_one_person(self):
        """Calculate BMI for one person."""
        name, weight, height = self.get_person_details()
        bmi = self.calculate_bmi(weight, height)
        self.display_result(name, weight, height, bmi)

    def calculate_for_multiple_people(self):
        """Calculate BMI for multiple people in one session."""
        while True:
            self.calculate_for_one_person()

            again = input(
                "\nCalculate BMI for another person? (y/n): "
            ).strip().lower()

            if again != "y":
                break

    def show_history(self):
        """Display calculations made during this session."""
        print("\n" + "=" * 45)
        print("              BMI HISTORY")
        print("=" * 45)

        if not self.history:
            print("No calculations have been made yet.")
            return

        for index, record in enumerate(self.history, start=1):
            print(f"\nRecord {index}")
            print(f"Name     : {record['name']}")
            print(f"BMI      : {record['bmi']}")
            print(f"Category : {record['category']}")
            print(f"Date     : {record['date']}")

    def show_menu(self):
        """Display the application menu."""
        print("\n" + "=" * 45)
        print("          BMI CALCULATOR")
        print("=" * 45)
        print("1. Calculate BMI")
        print("2. Calculate BMI for multiple people")
        print("3. View session history")
        print("4. Exit")
        print("=" * 45)

    def run(self):
        """Run the BMI calculator application."""
        print("Welcome to the BMI Calculator!")

        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ").strip()

            try:
                if choice == "1":
                    self.calculate_for_one_person()

                elif choice == "2":
                    self.calculate_for_multiple_people()

                elif choice == "3":
                    self.show_history()

                elif choice == "4":
                    print("Thank you for using BMI Calculator!")
                    break

                else:
                    print("Invalid choice. Please select 1, 2, 3, or 4.")

            except (ValueError, ZeroDivisionError) as error:
                print(f"Unable to calculate BMI: {error}")


def main():
    """Application entry point."""
    calculator = BMICalculator()
    calculator.run()


if __name__ == "__main__":
    main()
