### Pedro Miguel 26/09/2024
### Compulsory 1 - Statistics/Programming

import random

# 1.1|1.2|1.3
def mean(sample):
    """
    Calculate the mean (expectation) of a sample.
    
    :param sample: List of sample data points.
    :return: Mean of the sample.
    """
    return sum(sample) / len(sample)


def variance(sample):
    """
    Calculate the variance of a sample.
    
    :param sample: List of sample data points.
    :return: Variance of the sample.
    """
    n = len(sample)
    if n < 2:
        raise ValueError("Variance requires at least two data points.")
    
    sample_mean = mean(sample)
    return sum((x - sample_mean) ** 2 for x in sample) / (n - 1)


def std_dev(sample):
    """
    Calculate the standard deviation of a sample without using the math library.
    
    :param sample: List of sample data points.
    :return: Standard deviation of the sample.
    """
    return variance(sample) ** 0.5


def confidence_interval(sample):
    """
    Calculate the standard deviation of a sample without using the math library.
    
    :param sample: List of sample data points.
    :return: Lower and upper bounds of sample.
    """    
    n = len(sample)
    
#    if n < 30:
#        print("Sample too small.")
    
    z_value = 1.96
    std_err = std_dev(sample) / n ** 0.5
    margin_error = z_value * std_err
    
    lower_bound = mean(sample) - margin_error
    upper_bound = mean(sample) + margin_error
    
    return lower_bound, upper_bound

def read_sample():
    # Generate random numbers and write them to a file
    sample = [round(random.uniform(1, 10), 2) for i in range(30)]

    
    with open("numerical_data.txt", "w") as file:
        file.write("10\n")
        for number in sample:
            file.write(str(number) + ' ')


    print("Numbers:", sample)
    print("Mean:", mean(sample))
    print("Variance:", variance(sample))
    print("Standard Deviation:", std_dev(sample))
    print("The 95% confidence interval for the population mean is:", confidence_interval(sample))
    
    return sample

read_sample()





























