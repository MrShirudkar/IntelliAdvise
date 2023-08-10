from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# List of diamond shapes and metals
diamond_shapes = ["Round Brilliant","Princess Cut", "Cushion Cut", "Emerald Cut", "Asscher Cut", "Oval Cut", "Marquise Cut", "Pear Shape", "Heart Shape","Radiant Cut"]
metals = ["Gold", "Platinum", "Silver"]

# Function to filter diamonds based on user's shape, metal, and budget preferences
def map_parameters(shape, metal, budget):
    diamonds_data = pd.read_csv('diamonds.csv')  # Replace with your actual data loading code
    
    # Filtering diamonds based on shape, metal, and budget
    filtered_diamonds = diamonds_data[
        (diamonds_data['Shape'] == shape) &
        (diamonds_data['Metal'] == metal) &
        (diamonds_data['Price'] <= budget)
    ]
    
    return filtered_diamonds

# Function to calculate similarity score between user input and a diamond
def calculate_similarity(user_input, diamond):
    # Extracting attributes from user input and diamond data
    user_attributes = np.array([
        user_input['budget'],
        user_input['carat_weight'],
        user_input['color_value'],
        user_input['clarity_value']
    ])
    
    diamond_attributes = np.array([
        diamond['Price'],
        diamond['Carat Weight'],
        diamond['Color Value'],
        diamond['Clarity Value']
    ])

    # Mapping color and clarity values to numerical values
    color_mapping = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5}
    clarity_mapping = {'IF': 1, 'VVS1': 2, 'VVS2': 3, 'VS1': 4, 'VS2': 5, 'SI1': 6, 'SI2': 7}

    user_attributes[2] = color_mapping.get(user_attributes[2], 0)
    user_attributes[3] = clarity_mapping.get(user_attributes[3], 0)
    
    diamond_attributes[2] = color_mapping.get(diamond_attributes[2], 0)
    diamond_attributes[3] = clarity_mapping.get(diamond_attributes[3], 0)

    # Converting attributes to appropriate data types
    user_attributes = user_attributes.astype(float)
    diamond_attributes = diamond_attributes.astype(float)
    
    # Calculating similarity score using Euclidean distance
    similarity_score = np.linalg.norm(user_attributes - diamond_attributes)
    
    return similarity_score

# Function to generate top diamond recommendations based on similarity
def generate_recommendations(user_input, filtered_diamonds, num_recommendations=5):
    recommendations = []

    # Calculating similarity scores for each diamond and storing in recommendations list
    for idx, diamond in filtered_diamonds.iterrows():
        similarity_score = calculate_similarity(user_input, diamond)
        recommendations.append((idx, similarity_score))

    # Sorting recommendations by similarity score
    recommendations.sort(key=lambda x: x[1])
    top_recommendations = recommendations[:num_recommendations]
    
    return top_recommendations

# Function to generate recommendation details for display
def generate_recommendation_details(filtered_diamonds, top_recommendations):
    recommendation_details = []

    # Creating recommendation details dictionary for each top diamond recommendation
    for idx, similarity_score in top_recommendations:
        diamond = filtered_diamonds.loc[idx]
        
        recommendation = {
            'Price Range': f"${diamond['Price'] - 500} - ${diamond['Price'] + 500}",
            'Carat Weight': diamond['Carat Weight'],
            'Color': diamond['Color Value'],
            'Clarity': diamond['Clarity Value']
        }
        
        recommendation_details.append(recommendation)
    
    return recommendation_details

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation_details = []

    if request.method == 'POST':
        # Extracting user input from the form
        shape = request.form.get('shape')
        metal = request.form.get('metal')
        budget = float(request.form.get('budget'))
        
        # Filtering diamonds based on user input
        filtered_diamonds = map_parameters(shape, metal, budget)
        
        # Creating a sample user input for similarity calculation
        user_input = {
            'budget': budget,
            'carat_weight': 0.8,
            'color_value': 'D',
            'clarity_value': 'VVS2'
        }
        
        # Generating top diamond recommendations
        top_recommendations = generate_recommendations(user_input, filtered_diamonds)
        recommendation_details = generate_recommendation_details(filtered_diamonds, top_recommendations)

    # Rendering the template with necessary data
    return render_template('index.html', diamond_shapes=diamond_shapes, metals=metals, recommendations=recommendation_details)

if __name__ == '__main__':
    app.run(debug= True)