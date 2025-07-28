def bmi_calculator():
    print("You have entered the Bmi calculator.")
    while True:
        print("To [e]xit")
        try:
            height = input("Enter your height: ")
            if height.lower() == "e":
                break
            unit_height = input("[I]nches, [C]m: ").lower()
            if unit_height == "e":
                break
            weight = input("Enter your weight: ")
            if weight.lower() == "e":
                break
            unit_weight = input("[K]g or [L]bs: ").lower()
            if unit_weight == "e":
                break
            height = float(height)
            weight = float(weight)
            if unit_height == "i":
                height = height/39.37
            elif unit_height == "c":
                height = height/100
            else:
                print("Invalid unit!")
            if unit_weight == "l":
                weight = weight/2.205
            elif unit_weight == "k":
                weight = weight
            else:
                print("Invalid unit!")
            bmi = weight/(height*height)
            if bmi < 18.5:
                bmi_word = "Underweight"
            elif bmi >= 18.5 and bmi <= 24.9:
                bmi_word = "Healthy"
            elif bmi >= 25.0 and bmi <= 29.9:
                bmi_word = "Overweight"
            else:
                bmi_word = "Obesity"
            print(f"Your BMI is: {bmi}")
            print("You are " + bmi_word)
        except ValueError:
            print("Please enter valid numbers in numeric form!")
    print("BMI Calculator exited")


bmi_calculator()
