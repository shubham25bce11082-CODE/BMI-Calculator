def reference_chart():
    headers = ["BMI Range", "Category", "Health Risk"]
    data = [
        ["Below 18.5", "Underweight", "Malnutrition risk"],
        ["18.5 - 24.9", "Normal weight", "Low risk"],
        ["25.0 - 29.9", "Overweight", "Enhanced risk"],
        ["30.0 - 34.9", "Obese Class I", "Medium risk"],
        ["35.0 - 39.9", "Obese Class II", "High risk"],
        ["Above 40", "Obese Class III", "Very high risk"]
    ]

    col_widths = []
    for i in range(len(headers)):
        max_width = len(headers[i])
        for row in data:
            if len(row[i]) > max_width:
                max_width = len(row[i])
        col_widths.append(max_width + 2)

    print("Here You can take the reference chart\n")

    print("+" + "+".join(["-" * width for width in col_widths]) + "+")

    header_str = "|"
    for i, header in enumerate(headers):
        header_str += " " + header.ljust(col_widths[i] - 1) + "|"
    print(header_str)

    print("+" + "+".join(["=" * width for width in col_widths]) + "+")

    for row in data:
        row_str = "|"
        for i in range(len(row)):
            row_str += " " + row[i].ljust(col_widths[i] - 1) + "|"
        print(row_str)
        print("+" + "+".join(["-" * width for width in col_widths]) + "+")


def calculate_bmi(height, weight):
    if height <= 0:
        return None

    bmi = weight / (height * height)
    bmi = int(bmi * 100 + 0.5) / 100
    return bmi


def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."


def main():
    print("="*50)
    print("       BMI CALCULATOR")
    print("="*50)
    print()

    reference_chart()
    print()

    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        result = interpret_bmi(bmi)

        print()
        print("="*50)
        print(result)
        print("="*50)

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()
