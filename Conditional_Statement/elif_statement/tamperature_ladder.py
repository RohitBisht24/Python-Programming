temperature = int(input("Enter your Temperature : "))

if temperature >= -5 and temperature <= 5:
    print("Frzzing cold")
elif temperature >= 6 and temperature <= 18:
    print("cold")
elif temperature >= 19 and temperature <= 30:
    print("Hot")
else:
    print("Very Hot")