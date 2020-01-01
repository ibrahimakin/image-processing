# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[78]:


class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=5, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)                    
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        sayac_1 = 0
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)   
                sayac_1 += 1
            print(self.weights)
        print("Dongu sayisi", sayac_1)


# In[79]:


import numpy as np
training_inputs= []
labels = []

training_inputs.append(np.array([1,1]))
training_inputs.append(np.array([1,0]))
training_inputs.append(np.array([0,1]))
training_inputs.append(np.array([0,0]))

labels = np.array([1,0,0,0])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

inputs = np.array([1,1])
perceptron.predict(inputs)


# In[72]:


inputs = np.array([1,0])
perceptron.predict(inputs)


# In[73]:


inputs = np.array([0,0])
perceptron.predict(inputs)


# In[74]:


inputs = np.array([0,1])
perceptron.predict(inputs)


# In[75]:


perceptron.train(training_inputs,labels)


# In[ ]:




