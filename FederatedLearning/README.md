# Federated Learning Based Systems

## Level 0
Done in the [DevelopmentQuestion directory](../DevelopmentQuestion).

## Level 1

Ran the PyTorch quickstart locally and attached [screenshots](Level1/screenshots) of the same. Prepared a [write-up](Level1/Flower%20Write-up.md) with my understanding of the components of the Flower framework and the FL lifecycle.  
[BONUS] Completed the bonus part as well. Setup and ran flower in both [normal mode](Level1/screenshots/2.png) and [simulation mode](Level1/screenshots/Bonus.png).

## Level 2

Read the FedNTD paper and prepared a [detailed write-up](Level2/FedNTD%20Write-up.md) on the same. Watched the recommended part of the lecture on knowledge distillation.  
Implemented the distillation loss to the best of my knowledge. Modified the client's training loop by making changes to the train function in [task.py](./Level2/dashlab/dashlab/task.py). The losses increase with each round, so there must be mistakes, but I was not able to fix it despite spending a lot of time trying to figure it out. I have understood the working and theory behind the process.

## Level 3
Looked at the official implementation at https://github.com/Lee-Gihun/FedNTD/blob/master/algorithms/fedntd.  
I could not go through it in detail due to lack of time, and can not work on it since I am stuck on the implementation of level-2.  
[BONUS] Read the paper on Mutual Information Driven Federated Learning.
