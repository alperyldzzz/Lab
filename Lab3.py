def babylonian_sqrt(S, x0, tol, max_steps):
    if S < 0:
        print("S must be non-negative.")
        return

    x = x0

    print("\n*** BABYLONIAN METHOD ***\n")

    for step in range(1, max_steps + 1):
        if x == 0:
            print("Division by zero error!")
            return

        x_new = 0.5 * (x + S / x)
        print(f"Iteration-{step}, x = {x_new:.10f}")

        if abs(x_new - x) < tol:
            x = x_new
            break

        x = x_new

    real = S ** 0.5

    print(f"\nRequired root is: {x:.10f}")

    if x > real:
        print("Overestimate")
    elif x < real:
        print("Underestimate")
    else:
        print("Exact result")


S = float(input("Enter S value: "))
x0 = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance error: "))
max_steps = int(input("Enter maximum steps: "))

babylonian_sqrt(S, x0, tol, max_steps)