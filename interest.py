# Program to compute Simple Interest

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

# Compute simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print(f"Simple Interest = {simple_interest}")
