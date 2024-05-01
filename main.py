import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
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
    needed for the dish and each ingredient's cost. After the list include the overall cost compared to the budget.
    Keep in mind if more units of each ingredient must be bought for larger servings.
    Then include the recipe for the chosen dish.
    If it is expected that there are more ingredients left over than what is included in the serving,
    suggest other dishes that can be made with the left over ingredients. 

    Separate the shopping list and cost comparison.
    Do not include any spaces before or after each new line.
    Format the information ordered and divided with dashes into 6 sections like so:
    
        The name of the dish chosen
    --- 
        The amount of servings in parentheses
    ---
        The shopping list with quantities and prices of each individual item (do not add a title)
    ---
        The total cost of the ingredients and the amount of the budget remaining on two different lines
    ---
        The recipe as a numbered list with measurements for the dish chosen (do not add a title)
    ---
        Suggestions for the leftover ingredients
    ---
    '''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": prompt,
            }
        ],

        model="gpt-3.5-turbo",
    )

    list = chat_completion.choices[0].message.content

    return list


@app.route('/test')
@cross_origin()
def hello():
    return "Success"

@app.route('/')
@cross_origin()
def index():
    return render_template('plan.html')

@app.route('/plan.html')
@cross_origin()
def plan():
    return render_template('plan.html')

@app.route('/shop.html')
@cross_origin()
def shop():
    return render_template('shop.html')

@app.route('/cook.html')
@cross_origin()
def cook():
    return render_template('cook.html')

@app.route('/suggestions.html')
@cross_origin()
def suggestions():
    return render_template('suggestions.html')

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    data = request.json

    serving_size = data.get('serving_size')
    diet_details = data.get('diet_details')
    budget = data.get('budget')

    # Process the data and generate a result
    result = gen_list(serving_size, diet_details, budget)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)