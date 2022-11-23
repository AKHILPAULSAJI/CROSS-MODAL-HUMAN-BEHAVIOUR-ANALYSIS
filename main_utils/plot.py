import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import seaborn
seaborn.set()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	xsmile = np.array([0])
	ysmile = np.array([0])
	try:
		xsmile = np.load('../data_save/a.npy')
		ysmile = np.load('../data_save/b.npy')
		
	except:
		print("No")

	ax1.clear()
	ax1.plot(xsmile,ysmile)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
