import matplotlib.pyplot as plt
import os
from enum import Enum

# ====================================== Config Parameters ======================================
# Graph styling configuration
dotSize = 20  # Size of the scatter plot points
dotZ = 3      # Z-order (layer) for dots - higher value means on top
lineZ = 1     # Z-order for connecting lines - lower value means behind dots

# Directory path configuration
data_DirPath = os.path.join(os.path.dirname(__file__), 'BenchmarkFinalData')  # Path to benchmark data directory
lang_DirPath = os.path.join(os.path.dirname(__file__), 'Languages')           # Path to language files directory

# File path configuration
arraySizeFilePath = os.path.join(data_DirPath, 'ArraySize.txt')    # File containing array sizes for x-axis
valuesOfKFilePath = os.path.join(data_DirPath, 'kValues.txt')      # File containing k values (0 to 1000, step 10)
langFilePath = os.path.join(lang_DirPath, 'eng.txt')               # Language file for labels

# ====================================== Enum & Dictionary ======================================
# Enumeration defining different types of graphs that can be generated
class GraphType(Enum):
    # Individual algorithm performance graphs
    Heap = '_Title_HeapSelect'                             # Heap Select algorithm performance
    Medians = '_Title_MedianOfMediansSelect'               # Medians of Medians Select algorithm performance
    Quick = '_Title_Quick'                                 # Quick Select algorithm performance
    WorstQuick = '_Title_WorstQuick'                       # Worst case Quick Select performance
    WorstQuickP3W = '_Title_WorstQuickPartition3Way'       # Worst case Quick Select with 3-way partitioning
    
    # Comparative graphs with different k values
    WithK10x = '_Title_k=10x'                              # Performance with k as multiples of 10
    WithK1 = '_Title_k=1'                                  # Performance with k=1 (finding minimum)
    WithKLenArray = '_Title_k=lenArray'                    # Performance with k=array_length (finding maximum)
    WithKLenArrayDiv2 = '_Title_k=lenArray//2'             # Performance with k=array_length/2 (finding median)
    
    # Final comparison graphs
    FinalGraph = '_Title_k=random'                         # Final comparison with random k values
    FinalGraphWithP3W = '_Title_k=random_withP3W'                  # Final comparison including 3-way partitioning

# Dictionary containing styling and data information for each algorithm
INFO = {
    GraphType.Heap: {
        'name': 'Heap Select',                                        # Display name for legend
        'dotColor': 'paleturquoise',                                  # Color for scatter plot points
        'lineColor': 'darkturquoise',                                 # Color for connecting lines
        'dataDir': os.path.join(data_DirPath, 'HeapSelectExecTimes')  # Directory containing execution time data
    },
    GraphType.Medians: {
        'name': 'Medians Of Medians Select',
        'dotColor': 'mediumpurple',
        'lineColor': 'blueviolet',
        'dataDir': os.path.join(data_DirPath, 'MediansSelectExecTimes')
    },
    GraphType.WorstQuick: {
        'name': 'Quick Select',
        'dotColor': 'orange',
        'lineColor': 'darkorange',
        'dataDir': os.path.join(data_DirPath, 'QuickSelectExecTimes')
    },
    GraphType.Quick: {
        'name': 'Quick Select',
        'dotColor': 'orange',
        'lineColor': 'darkorange',
        'dataDir': os.path.join(data_DirPath, 'QuickSelectExecTimes')
    },
    GraphType.WorstQuickP3W: {
        'name': 'Quick Select P3W',
        'dotColor': 'red',
        'lineColor': 'red',
        'dataDir': os.path.join(data_DirPath, 'WorstQuickP3WExecTimes')
    }
}

# ====================================== Utility Functions ======================================
def isWhithRandomK(graphEnum: GraphType):
    """
    Determines if the graph type uses random k values for testing.
    
    Args:
        graphEnum (GraphType): The type of graph to check
        
    Returns:
        bool: True if the graph uses random k values, False otherwise
    """
    if graphEnum in {
        GraphType.Heap,
        GraphType.Medians,
        GraphType.Quick,
        GraphType.WorstQuick,
        GraphType.WorstQuickP3W
    }: 
        return True
    return False

def readValues(filePath):
    """
    Reads numerical values from a text file, one value per line.
    
    Args:
        filePath (str): Path to the file containing numerical values
        
    Returns:
        list: List of float values read from the file
    """
    values = []
    with open(filePath, 'r') as file:
        for line in file:
            newValue = float(line.strip())  # Convert string to float and remove whitespace
            values.append(newValue)
    return values
    
def getTitle(graphEnum: GraphType) -> str:
    """
    Retrieves the localized title for a specific graph type from the language file.
    
    Args:
        graphEnum (GraphType): The type of graph to get the title for
        
    Returns:
        str: Localized title string, or error message if not found
    """
    key = graphEnum.value  # Get the enum value (e.g., '_Title_HeapSelect')
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]  # Read all non-empty lines
    
    # Search for the key and return the next line as the title
    for i in range(len(righe) - 1):
        if righe[i] == key:
            return righe[i + 1]  
    return f"Title not found {key}"

def getLinear() -> str:
    """
    Retrieves the localized label for linear trend lines from the language file.
    
    Returns:
        str: Localized linear trend label, or error message if not found
    """
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]
    
    # Search for the '_Linear' key
    for i in range(len(righe) - 1):
        if righe[i] == '_Linear':
            return righe[i + 1] 
    return f"_Linear not found"

def getXTag(graphEnum: GraphType) -> str:
    """
    Retrieves the appropriate X-axis label for a specific graph type.
    
    Args:
        graphEnum (GraphType): The type of graph to get the X-axis label for
        
    Returns:
        str: Localized X-axis label, or error message if not found
    """
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    # Use special X-axis label for k=10x graphs, general label for others
    if graphEnum == GraphType.WithK10x:
        key = '_X_k=10x'    
    else:
        key = '_X'   

    # Search for the appropriate key
    for i in range(len(righe) - 1):
        if righe[i] == key:
            return righe[i + 1] 
    return f"_X not found"

def getYTag() -> str:
    """
    Retrieves the Y-axis label from the language file.
    
    Returns:
        str: Localized Y-axis label, or error message if not found
    """
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]
    
    # Search for the '_Y' key
    for i in range(len(righe) - 1):
        if righe[i] == '_Y':
            return righe[i + 1] 
    return f"_Y not found"

# ====================================== Plotting Functions ======================================

def addPlottedGraph(graph: GraphType, kType, ax):
    """
    Adds a single algorithm's performance data to the current plot.
    
    Args:
        graph (GraphType): The algorithm type to plot
        kType (str): The type of k values used ('kIsRandom', 'kIs1', etc.)
        ax: The matplotlib axes object to plot on
    """
    # Get algorithm information (colors, name, data directory)
    algorithm = INFO[graph]
    ExecTimePathFile = os.path.join(algorithm['dataDir'], kType + '.txt')

    # Determine X-axis values based on the type of test
    if kType == 'kIs10x':
        # For k=10x tests, X-axis represents k values (0, 10, 20, ..., 1000)
        xValues = readValues(valuesOfKFilePath)
        yValues = readValues(ExecTimePathFile)  # Use averaged execution times
    else:
        # For other tests, X-axis represents array sizes
        xValues = readValues(arraySizeFilePath)
        yValues = readValues(ExecTimePathFile)
    
    # Create scatter plot points
    plt.scatter(xValues, yValues, color=algorithm['dotColor'], label=algorithm['name'], zorder=dotZ, s=dotSize)
    
    # Draw connecting lines between points
    ax.plot(xValues, yValues, '-', color=algorithm['lineColor'], zorder=lineZ)
    
    # Add linear trend line for non-k10x graphs
    if kType != 'kIs10x':
        # Calculate linear trend: y = kx (where k is the slope)
        k = yValues[0] / xValues[0]  # Calculate slope from first data point
        linearTrend = [(k * x) for x in xValues]  # Generate linear trend line
        ax.plot(xValues, linearTrend, '--', color=algorithm['lineColor'], label=getLinear(), zorder=2)

def DrawGraph(graphEnum: GraphType, isLog: bool):
    """
    Main function to generate and display a complete graph based on the specified type.
    
    Args:
        graphEnum (GraphType): The type of graph to generate
        isLog (bool): Whether to use logarithmic scaling for both axes
    """
    # Initialize matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(getTitle(graphEnum), fontsize=15, fontweight='bold')  # Set localized title
    ax.grid(True, linestyle='--', alpha=0.7)  # Add grid for better readability
    ax.tick_params(labelsize=12)  # Set tick label font size

    # Determine which algorithms to plot based on graph type
    if isWhithRandomK(graphEnum):
        # Single algorithm with random k values
        if graphEnum == GraphType.WorstQuick:
            addPlottedGraph(graphEnum, 'kIsRandom_Worst', ax)
        else:
            addPlottedGraph(graphEnum, 'kIsRandom', ax)
    elif graphEnum == (GraphType.FinalGraph or GraphType.FinalGraphWithP3W):
        # Comparison of all algorithms
        addPlottedGraph(GraphType.Heap, 'kIsRandom', ax)
        addPlottedGraph(GraphType.Medians, 'kIsRandom', ax)
        addPlottedGraph(GraphType.Quick, 'kIsRandom', ax)
        if graphEnum == GraphType.FinalGraphWithP3W:
            # Include 3-way partitioning variant if specified
            addPlottedGraph(GraphType.WorstQuickP3W, 'kIsRandom', ax)
    elif graphEnum == (GraphType.WithK1):
        # Comparison with k=1 (finding minimum element)
        addPlottedGraph(GraphType.Heap, 'kIs1', ax)
        addPlottedGraph(GraphType.Medians, 'kIs1', ax)
        addPlottedGraph(GraphType.Quick, 'kIs1', ax)
    elif graphEnum == (GraphType.WithKLenArray):
        # Comparison with k=array_length (finding maximum element)
        addPlottedGraph(GraphType.Heap, 'kIsLenArray', ax)
        addPlottedGraph(GraphType.Medians, 'kIsLenArray', ax)
        addPlottedGraph(GraphType.Quick, 'kIsLenArray', ax)
    elif graphEnum == (GraphType.WithKLenArrayDiv2):
        # Comparison with k=array_length/2 (finding median element)
        addPlottedGraph(GraphType.Heap, 'kIsLenArrayDiv2', ax)
        addPlottedGraph(GraphType.Medians, 'kIsLenArrayDiv2', ax)
        addPlottedGraph(GraphType.Quick, 'kIsLenArrayDiv2', ax)
    elif graphEnum == (GraphType.WithK10x):
        # Comparison with k as multiples of 10
        addPlottedGraph(GraphType.Heap, 'kIs10x', ax)
        addPlottedGraph(GraphType.Medians, 'kIs10x', ax)
        addPlottedGraph(GraphType.Quick, 'kIs10x', ax)
    
    # Apply logarithmic scaling if requested
    if isLog:
        plt.xscale('log')  # Logarithmic X-axis
        plt.yscale('log')  # Logarithmic Y-axis

    # Configure plot appearance
    ax.legend(loc='upper left', fontsize=10)  # Add legend in upper left corner
    ax.set_xlabel(getXTag(graphEnum), fontsize=11, fontweight='bold')  # Set X-axis label
    ax.set_ylabel(getYTag(), fontsize=11, fontweight='bold')  # Set Y-axis label

    # Display the completed graph
    plt.show()

# ================================================================================================
# Main execution: Generate all graphs used in the report
# ================================================================================================
'''
# Individual algorithm performance graphs (both linear and logarithmic scales)
DrawGraph(GraphType.Quick, True)           # Quick Select - logarithmic scale
DrawGraph(GraphType.Quick, False)          # Quick Select - linear scale
DrawGraph(GraphType.Medians, True)         # Medians of Medians - logarithmic scale
DrawGraph(GraphType.Medians, False)        # Medians of Medians - linear scale
DrawGraph(GraphType.Heap, True)            # Heap Select - logarithmic scale
DrawGraph(GraphType.Heap, False)           # Heap Select - linear scale

# Performance comparison with varying k values
DrawGraph(GraphType.WithK10x, False)       # Performance vs k (multiples of 10)

# Performance comparison with specific k values
DrawGraph(GraphType.WithK1, True)          # k=1 comparison - logarithmic scale
DrawGraph(GraphType.WithK1, False)         # k=1 comparison - linear scale
DrawGraph(GraphType.WithKLenArray, True)   # k=array_length comparison - logarithmic scale
DrawGraph(GraphType.WithKLenArray, False)  # k=array_length comparison - linear scale

DrawGraph(GraphType.WithKLenArrayDiv2, True)   # k=array_length/2 comparison - logarithmic scale
DrawGraph(GraphType.WithKLenArrayDiv2, False)  # k=array_length/2 comparison - linear scale

# Worst-case performance analysis
DrawGraph(GraphType.WorstQuick, True)      # Worst-case Quick Select - logarithmic scale
DrawGraph(GraphType.WorstQuick, False)     # Worst-case Quick Select - linear scale
DrawGraph(GraphType.WorstQuickP3W, True)   # Worst-case Quick Select 3-way - logarithmic scale
DrawGraph(GraphType.WorstQuickP3W, False)  # Worst-case Quick Select 3-way - linear scale

# Final comparison graphs
DrawGraph(GraphType.FinalGraph, True)      # Final comparison - logarithmic scale
DrawGraph(GraphType.FinalGraph, False)     # Final comparison - linear scale
'''
DrawGraph(GraphType.FinalGraphWithP3W, True)   # Final comparison with 3-way - logarithmic scale
DrawGraph(GraphType.FinalGraphWithP3W, False)  # Final comparison with 3-way - linear scale 
