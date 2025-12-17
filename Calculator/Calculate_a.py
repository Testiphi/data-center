while True:
    T1 = float(input("Enter the first number: "))
    T2 = float(input("Enter the second number: "))
    T3 = float(input("Enter the third number: "))
    T4 = float(input("Enter the fourth number: "))
    x_0 = float(input("Enter the x_0 value: "))
    x_t = float(input("Enter the x_t value: "))
    a = ((8 / (T4 - T3)**2 -(8 / (T2 - T1)**2)) / (2 * (x_t - x_0)))
    print("The calculated acceleration (a) is:", a, "m/s^2")