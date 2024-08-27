import os, json, time
from dotenv import load_dotenv
from groq import Groq

# Load the env variable containing the API key
load_dotenv()

# Initialize the client using our Groq API key
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

"""
Send an API call to Groq with the prompt (parameter) and return a dictionary with the required values
"""
def query_llm(prompt):
    # Record the UNIX timestamp when the request is sent
    time_sent = time.time()
    # Store the response in a variable
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # We are using the llama3-8b model
        model = "llama3-8b-8192",
    )
    # Record the UNIX timestamp when the response is received
    time_recvd = time.time()
    # Create a dictionary with the required fields
    ret_dict = {
        "Prompt": prompt,
        "Message": chat_completion.choices[0].message.content,
        "TimeSent": round(time_sent),
        "TimeRecvd": round(time_recvd),
        "Source": "Groq"
    }
    # Return the dictionary
    return ret_dict

# Open the text file "input.txt" with the prompts
with open('input.txt', 'r') as file:
    output = []
    # Read the prompts line-by-line and retrieve the responses
    for line in file:
        # Add each response to a list
        output.append(query_llm(line.strip()))

# Output the list of dictionaries as a JSON array in "output.json"
with open('output.json', 'w') as json_file:
    json.dump(output, json_file, indent=4)