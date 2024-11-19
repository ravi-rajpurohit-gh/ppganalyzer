from scipy.signal import butter, filtfilt

def apply_filter(signal, filter_type='lowpass', cutoff=2.5, fs=100, order=5):
    """
    Applies a specified filter to the signal.

    Args:
        signal (array-like): The signal to filter.
        filter_type (str): Type of filter ('lowpass', 'highpass', 'bandpass').
        cutoff (float or list): Cutoff frequency/frequencies.
        fs (float): Sampling rate of the signal.
        order (int): The order of the filter.

    Returns:
        array-like: The filtered signal.
    """
    nyquist = 0.5 * fs
    if isinstance(cutoff, list):
        normal_cutoff = [c / nyquist for c in cutoff]
    else:
        normal_cutoff = cutoff / nyquist
    
    b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
    return filtfilt(b, a, signal)
 