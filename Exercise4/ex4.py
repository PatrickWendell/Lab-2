def calc_average_temp():
    x = [5,6,7,9]
    sumOftemps = sum(x)
    count = len(x)
    average = sumOftemps/count
    print("The average temperature is", average)

calc_average_temp()

def calc_min_max_temperature():
    x = [5,6,7,9,10,8,20,1]
    print(min(x))
    print(max(x))

calc_min_max_temperature()