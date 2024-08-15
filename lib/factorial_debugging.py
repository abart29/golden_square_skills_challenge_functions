def factorial(n):
    product = 1
    print(f"at the start product is {product}")
    while n > 1:
        print(f"* Starting Loop")
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")
        n -= 1
        print(f"now 'n' is: {n}")
    print(f"* Now n is 1 > exit loop")

    return product

print(f"""
  Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

print(f"""
  Running: factorial(6)
Expected: 720
  Actual: {factorial(6)}
""")

print(f"""
  Running: factorial(3)
Expected: 6
  Actual: {factorial(3)}
""")

print(f"""
  Running: factorial(7)
Expected: 5040
  Actual: {factorial(7)}
""")
