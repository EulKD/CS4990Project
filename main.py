import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

load_dotenv()
app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def gen_list(serving_size, diet_details, budget):
    prompt = f'''
    Create a grocery shopping list for a breakfast with serving sizes for {serving_size}.
    The meal must be {diet_details}.
    The budget for the ingredients is {budget}.
    With this information, choose an appropriate dish and make one shopping list that shows each ingredient
    needed for the dish , each ingredient's cost, and the overall cost compared to the budget.
    Keep in mind if more units of each ingredient must be bought for larger servings.
    Then include the recipe for the chosen dish.
    If it is expected that there are more ingredients left over than what is included in the serving,
    suggest other dishes that can be made with the left over ingredients. 

    Format the information using JSON lists in an order like so:

    The dish chosen (the amount of servings)

    The shopping list with quantities and prices

    The total cost of the ingredients and the amount of the budget remaining

    The recipe with measurements for the dish chosen

    Suggestions for the leftover ingredients
    '''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": prompt,
            }
        ],

        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
    )

    list = chat_completion.choices[0].message.content

    return list


@app.route('/test')
@cross_origin()
def hello():
    return "Success"

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    data = request.json

    data = {
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

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)