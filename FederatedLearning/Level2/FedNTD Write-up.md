# Level 2 Write-up

#### I prepared this write-up as I was going through the paper for the first time so that I can create a detailed summary of the research. It will also serve as revision material if I need to refer back to this paper anytime while completing the module.

The paper starts out by pointing out a major problem in federated learning, even while using the FedAvg algorithm which works well in most cases, which is the data heterogeneity problem. As clients generate the data that the model is trained on, the local data usually differs a lot from the global distribution, reducing the performance of FL algorithms. Solving this problem would prove helpful in reducing communication cost and training time due to faster convergence.  

This problem also exists in continual learning and causes the model to forget previously learnt attributes while trying to learn the new trends, which is not desirable for the global model. The model might give inconsistent predictions and do worse in predicting classes that the previous model predicted well. The global knowledge which corresponds to the region outside the local distribution is prone to be forgotten.  

The research group primarily:
1. conducts a systematic study on forgetting in FL.
2. proposes the FedNTD algorithm to prevent forgetting without compromising data privacy or communication costs.
3. analyzes how the proposed algorithm benefits FL.

## Forgetting in Federated Learning

As expected, the observation from experiments was that the models trained on locals with independent and identically distibuted data predicted classes evenly after each communication round, while the non-IID case showed significant inconsistency and forgetting. So, forgetting is a real issue in federated learning.  

Since the distribution of classes across clients may differ greatly, the study formulates in-local distribution and out-local distribution (assigns higher proportion to classes with fewer samples in local data). After training, the local model was well-fitted towards in-local distribution and the global model also performs well on it. As hypothesized, the local model performs poorly on out-local distribution, also degrading the global model's performance on the same.  
  
An intriguing property of knowledge preservation on out-local distribution is that it corrects the local
gradients towards the global direction.

## FedNTD: Federated Not-True Distillation

The core idea of FedNTD is to preserve the global knowledge for not-true classes. It conducts local-side distillation using a linear combination of the cross-entropy loss and the not-true distillation loss.
The hyperparameter beta (β) stands for the strength of knowledge preservation on the out-local distribution.  
  
The not-true distillation loss function helps the model learn new knowledge on in-local distribution by following true-class signals from the data using the cross-entropy loss function, while also preserving previous knowledge on out-local distribution by following the global model's perspective corresponsing to not-true class signals using the not-true distillation loss function.  
β controls the trade-off between learning on new knowledge and preserving previous knowledge.  
  
The experiments showed that the new FedNTD algorithm had state-of-the-art accuracies for many of the setups.

## Experiment

The tests were conducted on MNIST, CIFAR-10, CIFAR 100, and CINIC-10.  
Two NIID partition strategies were used:
1. Sharding: Dividing the data into same-sized shards after sorting by label and controlling the statistical heterogeneity by the number of shards per user.
2. LDA (Latent Dirichlet Allocation): Assigns partition of a class by sampling. Here, both the distribution and dataset size vary for each client.  
  
The experiments show that FedNTD performs much better in terms of forgetting, resulting in better accuracies. This shows that performance in FL is closely related to forgetting.

Prior works also often require statefulness (the clients must be repeatedly sampled with identification), additional communication cost or auxiliary data. FedNTD neither compromises data privacy nor requires additional communication burden.  

## Knowledge Preservation of FedNTD

Both FedAvg and FedNTD show only slight differences in local accuracy on in-local distribution but FedNTD shows significantly higher local accuracy on out-local distribution, implying that it prevents forgetting. The test accuracy of the global model also increases greatly. The gaps are enlarged with further rounds of training as expected because heterogeneity spoils the FedAvg model as more and more training is performed on local data.  
  
#### Weight Alignment: How much the semantics of each weight is preserved?  

Matching the semantic alignment across local models plays an important role in global convergence.
To analyze semantic alignment of each parameter, the study identifies each neuron's class preference by which class has the largest activation range on average. The alignment for a layer is measured between two models as the proportion of neurons that the class preference is matched for each other.  
There is little difference in the IID case but FedNTD significantly enhances alignment for NIID cases.

#### Weight Divergence: How far the local weights drift from the global model?

Knowledge preservation by FedNTD leads the global model to predict each class more evenly. This even prediction performance stabilizes weight divergance.

## Conclusion & Impact

FL is an important learning paradigm that enables privacy-preserving ML. FedNTD solves a major issue with FL frameworks, which is the impact of heterogeneity in data on the global model, focusing on the issue of forgetting. It does this without compromising the data privacy and without incurring extra communication losses.

Possible issue: If the global model is biased, the trained local models are more prone to have a similar tendency due to the preservation of knowledge outside of the local distribution in the global model.