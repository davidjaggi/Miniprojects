# https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/

# Importing matplotlib
from matplotlib import pyplot as plt

# Plotting to our canvas
plt.plot([1,2,3],[4,5,1])
# Show what we plotted
plt.show()

# add title

x = [5,8,10]
y = [12,16,6]
plt.plot(x,y)
plt.title('Epic title')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()