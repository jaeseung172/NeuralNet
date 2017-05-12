# NeuralNet
Just For Fun to make Neural Network Library. 

Also my chromebook could not run tensorflow library too

Feel Free To Use My library, Now It's Supports Some common activation Function and Single Layer Perceptron.

I'll Support for Multiple Layer Perceptron As soon as possible, Thanks.

(It'll Support OpenCL As well, firstly I need to Learn how to use Opencl Programming & GPU I/O Basics)

### Brief Information About This Module

- Supported Activation Function
  
  - Identy Function
  
  - TanH Function
  
  - Binary Function
  
  - Logistic Function
  
  - Relu Function
  
### Code Example (for Single Layer Perceptron)

```python3
from NeuralNetwork import *
X1 = [1, 0, 1]
_W = NN.GetWeights('rand', len(X)) ## Return Array to variable '_W'
_b = 1 ## Set Bias Variable
_Y1 = prop.Relu(NN.Proc(X1, _W, _b))
print(_Y1)
```

### Requirements

> Python3 & Not at all!
