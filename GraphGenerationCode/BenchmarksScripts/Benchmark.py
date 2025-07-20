from Algorithms.HeapSelect import heapSelect
from Algorithms.QuickSelect import quickSelect
from Algorithms.QuickP3WSelect import quickSelectRandomized
from Algorithms.MedianOfMediansSelect import medianOfMediansSelect

import random
import time
import os
#################################### ! DISCLAIMER ! ###################################################################

# THE FOLLOWING BENCHMARK WAS NOT DESIGNED TO BE EXECUTED ON WINDOWS.
# IT HAS BEEN TESTED ON MACOS AND UBUNTU, THEREFORE WE DO NOT RECOMMEND EXECUTION ON DIFFERENT OPERATING SYSTEMS.
# IN PARTICULAR, THE BENCHMARK EXECUTION TIMES ON WINDOWS CAN BE EXTREMELY HIGHER.
# ADDITIONALLY, THE GRAPH WILL NOT BE GENERATED.

'''
minimumMeasurableTime:
    Returns the minimum measurable time from the time.monotonic() counter.
'''
def minimumMeasurableTime():
    measurementStart = time.monotonic()
    while time.monotonic() == measurementStart:
        pass
    measurementEnd = time.monotonic()
    return measurementEnd - measurementStart


'''
measureTimes:
    1) Accurately measures the execution time of each algorithm in the selectionAlgorithms list.
    2) Guarantees a relative error lower than 1%.
    3) Adds the measured average time to the average time counter of each executed algorithm.
'''
minMeasurableTime = minimumMeasurableTime() * (1 + (1 / 0.01))  # max_rel_error = 1% = 0.01

def measureTimes(array, k, selectionAlgorithms, averageTimes):
    for i, func in enumerate(selectionAlgorithms):
        count = 0
        initialTime = time.monotonic()
        while time.monotonic() - initialTime < minMeasurableTime:
            func(array.copy(), k)
            count += 1
        duration = time.monotonic() - initialTime
        averageTimes[i] += (duration / count)


'''
benchmark:
    1) Measures the average execution time of each algorithm in the selectionAlgorithms list.
    2) Generates sequenceSteps(100) arrays of increasing size following a geometric series.
        The array size ranges from 100 to 100000.
    3) At each step, testsPerN(500) tests are executed with random k to ensure that algorithm execution times are average.
    4) In each test, the array of predetermined size is filled with random values in a range [-1000,1000].
    5) In each test, the execution time is measured.
    6) At the end of the tests, the average times for that sequence step are saved in a list of lists averageTimes.
    7) At each step, after executing testsPerN(500), the size of the array on which that step was executed is saved.
    8) At the end of 100 steps, the average time data is saved in separate files. One for each algorithm.
    9) Finally, the function that draws the graph is called, taking data from the generated files.
'''
# List of selection algorithms
selectionAlgorithms = [quickSelect, quickSelectRandomized, heapSelect, medianOfMediansSelect]
selectionAlgorithmNames = ["QuickSelect", "QuickSelectRandomizedPTW", "HeapSelect", "MedianOfMediansSelect"]


# Initialize lists for average times
averageTimes = [[] for _ in selectionAlgorithms]     # list of as many lists as there are selection algorithms
generatedArraySizes = []

def benchmark():
    A = 100  # Start of geometric series
    B = (100000 / 100) ** (1 / 99)  # Calculation of B to obtain final n of 100000 (99th root)
    sequenceSteps = 100
    testsPerN = 500


    for i in range(sequenceSteps):
        arraySize = int(A * (B ** i))
        print("Executing step {} / {} of sequence \t len(A) : {}".format(i+1, sequenceSteps, arraySize))
        
        # Initialize average times for this array size
        stepAverageTimes = [0] * len(selectionAlgorithms)
    
        for _ in range(testsPerN):
            array = [random.randint(-1000, 1000) for _ in range(arraySize)]
            k = random.randint(1, arraySize)
            measureTimes(array, k, selectionAlgorithms, stepAverageTimes)
            
        for j in range(len(selectionAlgorithms)):
            averageTimes[j].append(stepAverageTimes[j] / testsPerN)

        generatedArraySizes.append(arraySize)


    # Set working directory relative to this file's position
    directoryPath = os.path.join(os.path.dirname(__file__), 'BenchmarkResults')

    # Check if folder exists, otherwise create it
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)

    # Build file paths relative to this directory
    arraySizes_path = os.path.join(directoryPath, 'arraySizes.txt')

    # Write the size of each generated array to a file.
    with open(arraySizes_path, 'w') as f:
        for n in generatedArraySizes:
            f.write(f"{n}\n")

    # Write execution time results to separate text files. One for each algorithm.
    for i, name in enumerate(selectionAlgorithmNames):
        file_path = os.path.join(directoryPath, f'times{name}.txt')
        with open(file_path, 'w') as f:
            for time_val in averageTimes[i]:
                f.write(f"{time_val}\n")

print("Benchmark started")
benchmark()
print("Benchmark completed")