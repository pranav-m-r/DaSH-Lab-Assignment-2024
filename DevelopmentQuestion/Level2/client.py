import socket, os, json, uuid

# The server will be hosted on port 65432 of the localhost
SERVER = ('localhost', 65432)

"""
Send a request to the server with the prompt and the client's unique ID
"""
def send_request(prompt, client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the client socket to the server
    client_socket.connect(SERVER)
    request = json.dumps({"Prompt": prompt, "ClientID": client_id})
    # Send the request to the server
    client_socket.sendall(request.encode('utf-8'))
    # Receive the response from the server
    response = client_socket.recv(4096).decode('utf-8')
    client_socket.close()
    return json.loads(response)

client_id = str(uuid.uuid4())  # Create a unique ID for each client
input_file = 'input.txt' # The input text file with the prompts
output_file = f'output_{client_id}.json' # The output json file for the response

# Variables to mark the prompts allotted to each client
start_line = int(os.environ.get("START_LINE", 0))
end_line = int(os.environ.get("END_LINE", 4))

# Open the text file "input.txt" with the prompts
with open(input_file, 'r') as file:
    output = []
    lines = file.readlines()[start_line:end_line]
    # Read the prompts line-by-line and retrieve the responses
    for line in lines:
        response = send_request(line.strip(), client_id)
        # If the client receives a response for a prompt it did not send,
        # then set the Source to 'user'
        if response["ClientID"] != client_id:
            response["Source"] = "user"
        # Add each response to a list
        output.append(response)

# Output the list of dictionaries as a JSON array in "output.json"
with open(output_file, 'w') as json_file:
    json.dump(output, json_file, indent=4)