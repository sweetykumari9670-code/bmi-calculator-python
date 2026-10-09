
# BMI Calculator Project

def calculate_bmi(weight, height):
    return weight / (height * height)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 30)
    print("       BMI CALCULATOR")
    print("=" * 30)

    try:
        name = input("Enter your name: ")
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Please enter positive values.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print("\n----- BMI REPORT -----")
        print("Name:", name)
        print("Weight:", weight, "kg")
        print("Height:", height, "m")
        print("Your BMI:", round(bmi, 2))
        print("Category:", category)

        print("----------------------")
        print("Thank you for using BMI Calculator!")

    except ValueError:
        print("Invalid input! Please enter numbers for weight and height.")


if __name__ == "__main__":
    main()
