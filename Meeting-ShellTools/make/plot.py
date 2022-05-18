import matplotlib.pyplot as plt
import sys
import numpy as np

DATA_FILE = sys.argv[1]
IMAGE_FILE = sys.argv[2]

data = np.loadtxt(DATA_FILE)
plt.plot(data[:, 0], data[:, 1])
plt.savefig(IMAGE_FILE)
