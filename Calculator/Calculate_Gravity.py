while(True):
    L = float(0.28002)
    x = float(input("Enter Width: "))
    T = float(input("Enter Time Period: "))
    pi = 3.14159
    g = ((1/12 * L * L + x * x) / (x)) * (4 * pi * pi / (T * T))
    E = abs(g - 9.81) / 9.81 * 100
    print("Error: ", E, "%")
    print("Gravity: ", g)
    cont = input("Do you want to calculate again? (yes/no): ")
    if cont.lower() != 'yes':
        break