import csv
import random

# Lists of possible attributes for diamonds
shapes = ["Round Brilliant","Princess Cut", "Cushion Cut", "Emerald Cut", "Asscher Cut", "Oval Cut", "Marquise Cut", "Pear Shape", "Heart Shape","Radiant Cut"]
metals = ["Gold", "Platinum", "Silver"]
color_values = ["D", "E", "F", "G", "H"]
clarity_values = ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]

# Empty list to store generated diamond data
diamonds = []

# Generate 100 random diamond data entries
for _ in range(200):
    shape = random.choice(shapes)
    metal = random.choice(metals)
    price = random.randint(1000, 100000)
    carat_weight = round(random.uniform(0.3, 2.5), 2)
    color_value = random.choice(color_values)
    clarity_value = random.choice(clarity_values)
    diamonds.append([shape, metal, price, carat_weight, color_value, clarity_value])

# Define the CSV file path
csv_file_path = "diamonds.csv"

# Write the generated diamond data to a CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header row
    csv_writer.writerow(["Shape", "Metal", "Price", "Carat Weight", "Color Value", "Clarity Value"])
    # Write data rows
    csv_writer.writerows(diamonds)

# Print a message indicating successful file creation
print(f"Generated 200 random diamond data entries and saved to {csv_file_path}")
