import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

serving_size = '''
3 teens
'''

diet_details = '''
peanut-free and have a vegetarian option
'''
budget = '''
$50
'''
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

print(chat_completion.choices[0].message.content)