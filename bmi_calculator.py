def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("="*35)
    print("      BMI CALCULATOR")
    print("="*35)
    
    while True:
        try:
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and Height must be positive numbers. Try again.\n")
                continue
            
            bmi = weight / (height ** 2)
            category = get_bmi_category(bmi)
            
            print("\n" + "-"*35)
            print(f"Your BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("-"*35 + "\n")
            
            again = input("Calculate again? (y/n): ").lower()
            if again != 'y':
                print("Thank you! Stay healthy 💪")
                break
                
        except ValueError:
            print("Error: Please enter only numbers. No text allowed.\n")

if __name__ == "__main__":
    main()