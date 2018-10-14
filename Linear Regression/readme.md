# Linear Regression

 Linear Regression is used to find the relation between dependent variable and independent variable.
 
 * Used to find the relation and based on the relation between them we can predict the outcome.
 * The dependent variable is continuous, independent variable(s) can be continuous or discrete.

It is represented by an equation Y=a+b*X + e, where a is intercept, b is slope of the line and e is error term. This equation can be used to predict the value of target variable based on given predictor variable(s).
 
#### Lets put it in real world scenario.
1. Sharing a Post in social networking, Total Shares (dependent variable) experienced for an item shared on a social network, given the Number of Friends (independent variable) connected to by the original sharer. 


![real-and-predicted-values-bad11](https://user-images.githubusercontent.com/36659683/46913244-480b7a80-cfa7-11e8-901d-1135bdbc6d1a.png)

2. Relation between height and weight can also be predicted using Linear Regression.

![capture](https://user-images.githubusercontent.com/36659683/46913287-d4b63880-cfa7-11e8-9254-aca467bd0deb.PNG)

# Let's Learn Coding:
First let's see the Linear Regression model without training and testing dataset.

Import the necessary Library files.
```
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
```
Pandas - **manipulating DataFrame and datasets**<br>
Sklearn linear_model - **Performing linear Regression**<br>
Matplotlib.pyplot - **Plotting the data**<br>

### open Basic- Linear Regression file
