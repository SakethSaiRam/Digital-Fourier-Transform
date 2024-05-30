# Importing the necessary library
import scipy.fftpack as fft

''' Generic function to compute N point DFTs of a signal'''
def dft(signal,N):
    length = len(signal)
    if length > N:
        sys.exit("Length of the signal is greater than N")
    else:
        newSignal = list(signal) + [0 for _ in range(N - length)]
        return fft.fft(newSignal)

# Example
signal = [-2,-1,0,1,2]
print(dft(signal,10))