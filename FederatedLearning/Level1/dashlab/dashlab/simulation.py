import flwr as fl

# from dashlab.server_app import app as server
# from dashlab.client_app import app as client

from dashlab.client_app import client_fn
from dashlab.server_app import parameters
from flwr.server import ServerConfig

strategy = fl.server.strategy.FedAvg(
    fraction_fit=1.0,
    fraction_evaluate=1.0,
    min_available_clients=2,
    initial_parameters=parameters
)

#fl.simulation.run_simulation(server_app=server, client_app=client, num_supernodes=4)
history = fl.simulation.start_simulation(
    client_fn = client_fn,
    num_clients = 4,
    config = ServerConfig(num_rounds=3),
    strategy = strategy,
    # client_resources = {"num_cpus": 1},
)