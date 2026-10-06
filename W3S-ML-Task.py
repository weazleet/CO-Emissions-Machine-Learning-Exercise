import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


scale = StandardScaler()
# Pandas reads the dataframe of the given dataset. Dataset from the guide is not accurate and so predictions will provide false results. To counter this, I corrected the inaccuracies as well as added more entries for testing purposes.  
dataPath = Path(__file__).parent / "data.csv"
df = pandas.read_csv(dataPath)



X = df[['Weight', 'Volume']]
y = df['CO2']


# Scaled method of model fitting does not produce same results as guide. As so, I have commented out the scaling mehod, and instead used the multiple regression method to better fit the data with the model. 

# scaledX = scale.fit_transform(X)
# regr.fit(scaledX, y)
# scaled = scale.transform([[2300, 1.3]])
# predictedCO2 = regr.predict([scaled[0]])
# print(scaledX)

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[2300, 1300]])

# Print shows the two values of the prediction within the console.
print(predictedCO2)
print(regr.coef_)

#Building the dataset for graph from the data.csv file.
x2 = df['Weight']
y2 = df['Volume']
z = df['CO2']


# 3D plotted graph to show Co2 emission levels for each vehicle in the dataset.

# Creating figure
fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")

# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.3, 
        alpha = 0.2) 


# Creating color map
my_cmap = plt.get_cmap('hsv')


# Original (c) value was 'c = (x2 + y2 + z)', this provided an unclear map of results, changing this to only provide colour for the amount of Co2 produced made the graph much clearer and easier to understand.
# Creating plot
sctt = ax.scatter3D(x2, y2, z,
                    alpha = 0.8,
                    c = (z), 
                    cmap = my_cmap, 
                    marker ='^')

plt.title("3D graph showing level of Co2 emissions, given the weight of vehicle and volume of engine.")
ax.set_xlabel('Vehicle Weight (kg)', fontweight ='bold') 
ax.set_ylabel('Engine Displacement (cm3)', fontweight ='bold') 
ax.set_zlabel('Co2 Emissions (p/Km)', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)

# Show plot
plt.show()