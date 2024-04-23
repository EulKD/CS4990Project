from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from main import gen_list

app = Flask(__name__)

@app.route('/test')
@cross_origin()
def hello():
    return "success"

@app.route('/generate', methods=['GET', 'POST'])
@cross_origin()
def generate():
    data = request.get_json  # Get the data sent in the POST request
    
    # Extract the inputs for the gen_list method from the data
    serving_size = data.get('serving_size')
    diet_details = data.get('diet_details')
    budget = data.get('budget')

    # Call your function with the data
    result = gen_list(serving_size, diet_details, budget)

    result = {
        "dish": "Oatmeal with Fruit Toppings (4 servings)",
        "shopping_list": [
            {
                "ingredient": "Rolled oats",
                "quantity": "2 cups",
                "price_per_unit": "$2",
                "total_price": "$4"
            },
            {
                "ingredient": "Milk (or alternative)",
                "quantity": "2 cups",
                "price_per_unit": "$3",
                "total_price": "$6"
            },
            {
                "ingredient": "Banana",
                "quantity": "2",
                "price_per_unit": "$0.50",
                "total_price": "$1"
            },
            {
                "ingredient": "Berries (e.g. blueberries, strawberries)",
                "quantity": "1 cup",
                "price_per_unit": "$3",
                "total_price": "$3"
            },
            {
                "ingredient": "Honey",
                "quantity": "2 tbsp",
                "price_per_unit": "$1",
                "total_price": "$1"
            }
        ],
        "total_cost": "$15",
        "budget_remaining": "$10",
        "recipe": "1. In a saucepan, combine rolled oats and milk. Cook over medium heat until oats are creamy.\n2. Slice the banana and wash the berries.\n3. Serve the oatmeal in bowls, top with banana slices, berries, and a drizzle of honey.",
        "leftover_suggestions": [
            "Make smoothies with leftover berries, bananas, and milk.",
            "Use leftover oats to make oatmeal cookies or granola bars."
        ]
    }

    return result  # Return the result as JSON

if __name__ == '__main__':
    app.run(debug=True)
