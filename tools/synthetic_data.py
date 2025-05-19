import ollama
from tool_calling import get_stock_price

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'What is the current price of AAPL?'
        }
    ],
    tools=[get_stock_price]
)

print(dict(response))

avaialble_functions = {
    'get_stock_price': get_stock_price
}

for tool in response.message.tool_calls  or []:
    function_to_call  = avaialble_functions.get(tool.function.name)

    if function_to_call:
        print('Aruguments: ',tool.function.arguments)
        print('Function Output: ',function_to_call(**tool.function.arguments))

    else:
        print('Function not found: ',  tool.function.name)
