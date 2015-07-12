from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Read audio file
[rate, data] = read("Port_m5.wav")

# Plot all samples
plt.plot(data)

# Label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

# Set the title
plt.title("Flute Sample")

#Display the plot
plt.show()
