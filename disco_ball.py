import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import threading
from pygame import mixer

# sucks for u, you will have to listen to the entire song or kill your terminal


# Function to play music
def play_music():
    mixer.init()
    mixer.music.load("./party4u.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # Wait for music to finish playing
        time.sleep(1)


# Create a dark-themed figure
fig = plt.figure()
fig.patch.set_facecolor("#222222")  # Set background color to dark gray
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("#222222")  # Set plot background color to dark gray

# Remove axes for a clean disco ball effect
ax.set_axis_off()

# Sphere parameters
center = (0, 0, 0)
radius = 1
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

# Create a mesh grid for the sphere
phi, theta = np.meshgrid(phi, theta)
x = center[0] + radius * np.sin(phi) * np.cos(theta)
y = center[1] + radius * np.sin(phi) * np.sin(theta)
z = center[2] + radius * np.cos(phi)

# Plot the sphere with interesting color
ax.plot_surface(x, y, z, color="#C7C1C0", alpha=0.8)  # Disco ball grayish color

# Create and start a thread for music playback
music_thread = threading.Thread(target=play_music)
music_thread.start()

# Show the plot (this will continue to run while music plays in the background)
plt.show()

# Wait for the music thread to finish (optional if you want to wait for music to finish before closing)
music_thread.join()
