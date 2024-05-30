# Importing the necessary libraries
import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

''' Accuracy Test for the numpy.fft package '''

# Computation of Inverse DFT using ifft
xOriginal = np.random.rand(128)
X = fft.fft(xOriginal)
xComputed = fft.ifft(X)

# Plotting of the signals
plt.figure(0)
t = np.linspace(-50,50,129)[:-1]
plt.plot(t,xOriginal,label='Original $x(t)$',lw=2)
plt.plot(t,np.abs(xComputed),label='Computed $x(t)$',lw=1)
plt.legend()
plt.title('Comparision of Original and Computed $x(t)$')
plt.xlabel(r'$t\ \to$')
plt.grid()
plt.show()

# Calculation of Error
rms_error = np.sqrt(np.mean(abs(xComputed - xOriginal)**2))
print("Root Mean Square Error between Original and Computed Values is ",rms_error)