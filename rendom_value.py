import csv
import random

# List of possible values for different fields
shapes = ["Round", "Princess", "Oval", "Pear", "Emerald"]
metals = ["Gold", "Platinum", "Silver"]
color_values = ["D", "E", "F", "G", "H"]
clarity_values = ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]

# Generating 100 random diamond data entries
diamonds = []
for _ in range(100):
    shape = random.choice(shapes)
    metal = random.choice(metals)
    price = random.randint(1500, 100000)
    carat_weight = round(random.uniform(0.3, 2.5), 2)
    color_value = random.choice(color_values)
    clarity_value = random.choice(clarity_values)
    diamonds.append([shape, metal, price, carat_weight, color_value, clarity_value])

# Writing the data to a CSV file
csv_file_path = "diamonds.csv"
with open(csv_file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Shape", "Metal", "Price", "Carat Weight", "Color Value", "Clarity Value"])  # Writing header
    csv_writer.writerows(diamonds)  # Writing data rows

print(f"Generated 100 random diamond data entries and saved to {csv_file_path}")
