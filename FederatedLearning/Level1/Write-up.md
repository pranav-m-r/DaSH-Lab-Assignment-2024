# Level 1 Write-up

## Server
The server is the central aggregator of the federated learning system. It sends updated models to the clients after aggregating the training results from the clients which are picked for training on their local data.  
  
In the flower framework, the server app is initialized using a server function callback. The function contains all the information required to create and return the required ServerAppComponents object. This usually includes the server configuration (with fields like the number of server rounds) and a training strategy (the guide uses the FedAvg strategy).

## Client
The clients are the devices or simulated partitions which contain local data which the FL model can train on. The clients use the model for their purposes and additionally train and test updated models using local data (without exposing the actual data) when requested by the server.  
  
In the flower framework, the client app is created using a client function call back, just like the server app. The client function returns a flower client (the guide used a client which was extended from flower's NumPy client). The flower client class contains a constructor, and majorly a fit method and evaluate method. The fit method is used to train an updated model, by first setting the local model's weights to be the same as the global model's and then training it on its local data, and then sending the updated model parameters to the server. In flower we simulate the existence of multiple clients with their own local data on a single machine or a small set of machines by partitioning the data using in-built methods.

## Strategy
The strategy defined in for a flower workflow allows the customization of the federated learning process.  
We can use and build upon popular algorithms such as FedAvg (which is the strategy used in the guide). My explanations for the server and clients is also partially derived from the FedAvg strategy because I have only interacted with this type of model.

## FL Lifecycle
FedAvg or the Federated Averaging algorithm works in this way:
1. There is a global model initialized on the server.
2. In each round of training, the server selects a subset of available clients to participate in the training process.
3. These clients get the global parameters and train the model on their local data.
4. The updated parameters are sent back to the server, which aggregates them and updates the global model with the new parameters.
  
The strategy can be customized by changing parameters like fraction fit (fraction of available clients used for training), fraction_evaluate (fraction of available clients used for testing), initial parameters (initial parameters for the global model), minimum available clients (minimum available clients for the learning process to start), etc.