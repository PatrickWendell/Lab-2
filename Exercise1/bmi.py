def calculate_bmi (height, weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print(bmi)
    if (bmi<18.5) :
        print("underweight")
    elif (bmi>=18.5):
        print("normal")
    elif (bmi>25.0) :
        print("overweight")





calculate_bmi(weight=57,height=1.73)