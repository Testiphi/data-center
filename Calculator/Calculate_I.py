while True:
    T = float(input("Enter the time period (T) in seconds: "))
    M = float(input("Enter the mass (M) in kilograms: "))
    g = 9.81
    d = float(input("Enter the distance (d) from the pivot point in meters: "))
    pi =3.141592653589793

    I_pivot = (T * T * M * g * d) / (4 * pi * pi)
    I_cm = I_pivot - M * d * d
    print("The moment of inertia of the pivot point is:", I_pivot, "kg m^2")
    print("The moment of inertia of the center of mass is:", I_cm, "kg m^2")
    cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if cont != 'yes':
        break