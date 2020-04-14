# code_kes2020


### Paper Name
1. Cloud Resources Prediction Using Meta-heuristics And Convolutional Neural Network 
2. Forecasting Cloud Resources Using Hybrid Convolutional Neural Network 
3. Applying The State-Of-The-Art Meta-heuristics and Convolutional Neural Network For Forecasting Cloud Resources
 

# Traditional 
1. MLNN
2. RNN
3. LSTM
4. GRU
5. CNN

# Evolutionary 
1. GA-CNN

# Swarm 
1. WOA-CNN  (Whale)

# Physics 
1. Multi-Verse Optimizer (MVO) - 2016 - MVO-CNN
2. EO 

# Bio 
1. Satin Bowerbird Optimizer (SBO) - 2017 - SBO-CNN

# Human (Our proposed)
1. Social Ski-Driver Optimization (SSDO) - 2019 - SSDO-CNN
2. Life Choice-Based Optimizer (LCBO) - 2019 - LCBO-CNN

# System
1. AEO 

### Weights of Hybrid-CNN
* sliding windows: 2h is the best - 24


## Final comparison between
1. RNN
2. LSTM
3. GRU
4. CNN
5. WOA-CNN  (Whale)
6. Multi-Verse Optimizer (MVO) - 2016 - MVO-CNN
7. Satin Bowerbird Optimizer (SBO) - 2017 - SBO-CNN
8. Life Choice-Based Optimizer (LCBO) - 2019 - LCBO-CNN
9. Life Choice-Based Optimizer (LCBO) - 2019 - LCBO-CNN
10. AEO-CNN (Our proposed)


* Kernel size changed:
```code 
- 4 - 2 - 2
  
  43
  63
  103
  
  
- 8
  
  75
  115
  195
  
  
- 16 - 2 - 2
  
  139
  219
  379
  
  
- 32 
  
  267
  427
  747
  
  
- 64 
  
  3 - 523
  6 - 843
  10 - 1483


```
### Results from test4 proved : elu-elu or relu-relu is the best
- ('tanh', 'elu'), ('relu', 'elu'), ('elu', 'elu'), ('tanh', 'relu'), ('elu', 'relu'), ('relu', 'relu'), 
('tanh', 'signmoid'), ('relu', 'sigmoid'), ('elu', 'sigmoid')


https://blog.coast.ai/lets-evolve-a-neural-network-with-a-genetic-algorithm-code-included-8809bece164
https://github.com/harvitronix/neural-network-genetic-algorithm
https://github.com/jliphard/DeepEvolve
