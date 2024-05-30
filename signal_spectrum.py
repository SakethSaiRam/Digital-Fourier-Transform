# Importing the necessary libraries
import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

''' Generic function to plot the spectrum of a signal with sampling frequency, coordinates range as its arguments '''
def spectrum(func,sampling_freq,coord_range):
    s,e = coord_range

    # Time axis
    t = np.linspace(s,e,sampling_freq + 1)[:-1]
    y = func(t)

    # DFT Computation
    Y = fft.fftshift(fft.fft(y)) / sampling_freq
    Ymag = np.abs(Y)
    Yphase = np.angle(Y)

    # Checking the frequencies which are present in the signal
    presentFreqs = np.where(Ymag > 1e-10)

    left_xlimit = (np.array(presentFreqs[0]-(sampling_freq/2))[0]) / ((e - s) / (2 * np.pi))
    right_xlimit = (np.array(presentFreqs[0]-(sampling_freq/2))[-1]) / ((e - s) / (2 * np.pi))

    # Setting up the frequency axis with zero frequency at the center
    w = (np.array(list(range(sampling_freq))) - (sampling_freq / 2)) / ((e - s) / (2 * np.pi))

    fig1 = plt.figure(0)

    # Plotting of Magnitude plot
    plt.suptitle("Spectrum of the Signal")
    plt.subplot(2,1,1)
    plt.plot(w,Ymag,'b-',lw=1)
    plt.ylabel(r"$|Y|$")
    plt.xlim([2*left_xlimit,2*right_xlimit])
    plt.grid()

    # Plotting of Phase Plot
    plt.subplot(2,1,2)
    plt.plot(w[presentFreqs],Yphase[presentFreqs],'ro-',lw=0.5)
    plt.ylabel(r"$\angle Y$")
    plt.xlabel(r"$\omega$")
    plt.xlim([2*left_xlimit,2*right_xlimit])
    plt.grid()

    plt.show()

# Defining functions for a few continuous signals
def f1(t):
    return np.sin(5*t)
def f2(t):
    return (1 + 0.1*np.cos(t)) * np.cos(10*t)
def f3(t):
    return (np.sin(t)) ** 3
def f4(t):
    return (np.cos(t)) ** 3
def f5(t):
    return np.cos((20*t) + (5*np.cos(t)))
def f6(t):
    return fft.ifftshift(np.exp(-(t ** 2)/2)) * 8
def f7(t):
    return np.cos(10 * t) + np.sin(20 * t)

# Example
spectrum(f1,128,[0*np.pi,4*np.pi])
spectrum(f2,512,[-4*np.pi,4*np.pi])
spectrum(f3,512,[-4*np.pi,4*np.pi])
spectrum(f4,512,[-4*np.pi,4*np.pi])
spectrum(f5,512,[-4*np.pi,4*np.pi])
spectrum(f6,512,[-8*np.pi,8*np.pi])
spectrum(f7,1024,[-10*np.pi,10*np.pi])