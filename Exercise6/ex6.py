def calc_median_temperature():
    # Ask the user for input and create a list of temperatures
    temperatures = []
    while True:
        try:
            temperature = input("Enter a temperature (or 'done' to finish): ")
            if temperature.lower() == 'done':
                break
            temperatures.append(float(temperature))
        except ValueError:
            print("Please enter a valid temperature or 'done' to finish.")

    # Sort the list of temperatures
    temperatures.sort()

    # Calculate the median
    length = len(temperatures)
    if length % 2 == 0:
        # For an even number of temperatures, average the middle two
        mid = length // 2
        median = (temperatures[mid - 1] + temperatures[mid]) / 2
    else:
        # For an odd number of temperatures, pick the middle one
        median = temperatures[length // 2]

    return median

# Example usage
median_temp = calc_median_temperature()
print(f"The median temperature is: {median_temp}")
