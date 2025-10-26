# Function to calculate the midpoint of a line segment
def midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)

# Input coordinates of the endpoints
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

# Calculate and display the midpoint
mid = midpoint(x1, y1, x2, y2)
print(f"The midpoint of the line segment is: {mid}")
