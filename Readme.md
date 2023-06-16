# OpenAI's Function calling capability in the Chat Completions API - Sample

This project demonstrates a simple example of using the Function calling feature of OpenAI API

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/home-automation.git

2. Create .env file and add your OpenAI API Key

3. Run Startup.bat


## About Function calling 
Developers can now describe functions to gpt-4-0613 and gpt-3.5-turbo-0613, and have the model intelligently choose to output a JSON object containing arguments to call those functions. This is a new way to more reliably connect GPT's capabilities with external tools and APIs.

These models have been fine-tuned to both detect when a function needs to be called (depending on the user’s input) and to respond with JSON that adheres to the function signature. Function calling allows developers to more reliably get structured data back from the model. For example, developers can:

Create chatbots that answer questions by calling external tools (e.g., like ChatGPT Plugins)
Convert queries such as “Email Anya to see if she wants to get coffee next Friday” to a function call like send_email(to: string, body: string), or “What’s the weather like in Boston?” to get_current_weather(location: string, unit: 'celsius' | 'fahrenheit').

Convert natural language into API calls or database queries
Convert “Who are my top ten customers this month?” to an internal API call such as get_customers_by_revenue(start_date: string, end_date: string, limit: int), or “How many orders did Acme, Inc. place last month?” to a SQL query using sql_query(query: string).

Extract structured data from text
Define a function called extract_people_data(people: [{name: string, birthday: string, location: string}]), to extract all people mentioned in a Wikipedia article.

These use cases are enabled by new API parameters in our /v1/chat/completions endpoint, functions and function_call, that allow developers to describe functions to the model via JSON Schema, and optionally ask it to call a specific function. Get started with our developer documentation and add evals if you find cases where function calling could be improved


https://openai.com/blog/function-calling-and-other-api-updates?ref=upstract.com
