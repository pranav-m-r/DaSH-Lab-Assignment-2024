import socket, os, json, time
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

# The server will be hosted on port 65432 of the localhost
SERVER = ('localhost', 65432)

# Create a socket specifying IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the specified port of the host
server_socket.bind(SERVER)
# Listen for requests from clients
server_socket.listen()

while True:
    # Accept incoming requests from clients
    comm_socket, address = server_socket.accept()
    print(f'Connected to {address}')
    data = comm_socket.recv(1024).decode('utf-8')
    if not data:
        break
    # Load the JSON formatted request
    request = json.loads(data)
    # Process the request (API call to LLM)
    response = query_llm(request["Prompt"])
    # Add the client's ID to the response
    response["ClientID"] = request.get("ClientID", "unknown")
    # Send the complete response back to the client
    comm_socket.sendall(json.dumps(response).encode('utf-8'))
