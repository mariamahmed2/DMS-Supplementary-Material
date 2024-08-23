write your code here
--------------------
import numpy as np
import matplotlib.pyplot as plt
# Generate data for sine and cosine waves
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Create a plot
plt.figure(figsize=(10, 6))
# Plot the sine wave
plt.plot(x, y_sin, label='Sine wave', color='b', linestyle='-')
# Plot the cosine wave
plt.plot(x, y_cos, label='Cosine wave', color='r', linestyle='--')
# Add title and labels
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
# Add a legend
plt.legend()
# Display the plot
plt.show()
