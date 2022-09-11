import numpy as np
import matplotlib.pyplot as plt

mydata = np.array([15, 20, 35, 15])

plt.pie(mydata,labels=['Series 1','Series 2','Series 3','Series 4'],colors=['red','darkgreen','skyblue','yellow'])
plt.title("My Pie Plot")
plt.show()