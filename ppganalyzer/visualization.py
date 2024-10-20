import matplotlib.pyplot as plt

def plot_signal(time, signal):
    """
    Plots the signal over time.

    Args:
        time (array-like): Time values corresponding to the signal.
        signal (array-like): Signal data.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(time, signal, label="Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal Over Time")
    plt.legend()
    plt.show()
