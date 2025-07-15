import matplotlib.pyplot as plt
import os
from enum import Enum

'''Graph Info''' 
dotSize=20
dotZ=3
lineZ=1 

'''Directory Paths'''
data_DirPath = os.path.join(os.path.dirname(__file__), 'BenchmarkFinalData')
lang_DirPath = os.path.join(os.path.dirname(__file__), 'Languages')

'''File Paths'''
arraySizeFilePath = os.path.join(data_DirPath, 'ArraySize.txt')
valuesOfKFilePath = os.path.join(data_DirPath, 'kValues.txt')
langFilePath = os.path.join(lang_DirPath, 'ita.txt')

'''Type of Graphs'''
class GraphType(Enum):
    Heap = '_Title_HeapSelect'
    Medians = '_Title_MedianOfMediansSelect'
    Quick = '_Title_Quick'
    WorstQuick = '_Title_WorstQuick'
    WorstQuickP3W ='_Title_WorstQuickPartition3Way'
    WithK10x = '_Title_k=10x'
    WithK1 ='_Title_k=1'
    WithKLenArray = '_Title_k=lenArray'
    WithKLenArrayDiv2 = '_Title_k=lenArray//2'
    FinalGraph = '_Title_k=random'
    FinalGraphWithP3W = '_Title_k=random'

'''Useful Info For Each Graph''' #(name, color of the dot, color of the line connecting the dots, execution times file path)
INFO = {
    GraphType.Heap: {
        'name': 'Heap Select',
        'dotColor': 'paleturquoise',
        'lineColor': 'darkturquoise',
        'dataDir': os.path.join(data_DirPath, 'HeapSelectExecTimes')
    },
    GraphType.Medians: {
        'name': 'Medians Of Medians Select',
        'dotColor': 'mediumpurple',
        'lineColor': 'blueviolet',
        'dataDir': os.path.join(data_DirPath, 'MediansSelectExecTimes')
    },
    GraphType.Quick: {
        'name': 'Quick Select',
        'dotColor': 'orange',
        'lineColor': 'darkorange',
        'dataDir': os.path.join(data_DirPath, 'QuickSelectExecTimes')
    },
    GraphType.WorstQuickP3W: {
        'name': 'Quick Select',
        'dotColor': 'red',
        'lineColor': 'red',
        'dataDir': os.path.join(data_DirPath, 'WorstQuickP3WExecTimes')
    }
}

#--------------------------------------Utility Functions--------------------------------------#
def isWhithRandomK(graphEnum: GraphType):
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
    values = []
    with open(filePath, 'r') as file:
        for line in file:
            newValue = float(line.strip())
            values.append(newValue)
    return values

def readValues_kIs10x(filePath):
    values = []
    with open(filePath, 'r') as file:
        for line in file:
            values.append(float(line.strip()))
    
    averaged = []
    for i in range(0, len(values), 5):
        block = values[i:i + 5]
        if len(block) == 5:
            media = sum(block) / 5
            averaged.append(media)
    return averaged
    
def getTitle(graphEnum: GraphType) -> str:
    key = graphEnum.value
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]
    for i in range(len(righe) - 1):
        if righe[i] == key:
            return righe[i + 1]  
    return f"Title not found {key}"

def getLinear() -> str:
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]
    for i in range(len(righe) - 1):
        if righe[i] == '_Linear':
            return righe[i + 1] 
    return f"_Linear not found"

def getXTag(graphEnum: GraphType) -> str:
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    if graphEnum==GraphType.WithK10x:
        key='_X_k=10x'    
    else:
        key='_X'   

    for i in range(len(righe) - 1):
        if righe[i] == key:
            return righe[i + 1] 
    return f"_X not found"

def getYTag() -> str:
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]
    for i in range(len(righe) - 1):
        if righe[i] == '_Y':
            return righe[i + 1] 
    return f"_Y not found"

#--------------------------------------Plotting Functions--------------------------------------#
def addPlottedGraph(graph: GraphType, kType, ax):
    #Get the correct exec times based on kType
    algorithm = INFO[graph]
    ExecTimePathFile = os.path.join(algorithm['dataDir'], kType + '.txt')

    #Get the correct x values based on kType (the value of k for 'kIs10', the array size for the other ones)
    if kType=='kIs10x_5values':
        xValues = readValues(valuesOfKFilePath)
        yValues = readValues_kIs10x(ExecTimePathFile)
    else:
        xValues = readValues(arraySizeFilePath)
        yValues = readValues(ExecTimePathFile)

    print(ExecTimePathFile)
    print(valuesOfKFilePath) 
    print(len(xValues), len(yValues))
    #Dots 
    plt.scatter(xValues , yValues, color = algorithm['dotColor'], label = algorithm['name'], zorder=dotZ, s=dotSize)
    #Line connecting the dots
    ax.plot(xValues, yValues, '-', color=algorithm['lineColor'], zorder=lineZ)
    
    #Linear trend graph
    k = yValues[0] / xValues[0]
    linearTrend = [(k * x) for x in xValues]
    ax.plot(xValues, linearTrend, '--', color=algorithm['lineColor'], label = getLinear(), zorder=2)

def DrawGraph(graphEnum: GraphType, isLog: bool):
    #Matplotlib config for the title
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(getTitle(graphEnum), fontsize = 15, fontweight = 'bold')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(labelsize=12)

    if isWhithRandomK(graphEnum):                                           #k=random
        addPlottedGraph(graphEnum, 'kIsRandom', ax)
    elif graphEnum==(GraphType.FinalGraph or GraphType.FinalGraphWithP3W):#End Graph
        addPlottedGraph(GraphType.Heap, 'kIsRandom', ax)
        addPlottedGraph(GraphType.Medians, 'kIsRandom', ax)
        addPlottedGraph(GraphType.Quick, 'kIsRandom', ax)
        if graphEnum==GraphType.FinalGraphWithP3W:                        #End Graph w/ QP3W
            addPlottedGraph(GraphType.WorstQuickP3W, 'kIsRandom', ax)
    elif graphEnum==(GraphType.WithK1):
        addPlottedGraph(GraphType.Heap, 'kIs1', ax)
        addPlottedGraph(GraphType.Medians, 'kIs1', ax)
        addPlottedGraph(GraphType.Quick, 'kIs1', ax)
    elif graphEnum==(GraphType.WithKLenArray):
        addPlottedGraph(GraphType.Heap, 'kIsLenArray', ax)
        addPlottedGraph(GraphType.Medians, 'kIsLenArray', ax)
        addPlottedGraph(GraphType.Quick, 'kIsLenArray', ax)
    elif graphEnum==(GraphType.WithKLenArrayDiv2):
        addPlottedGraph(GraphType.Heap, 'kIsLenArrayDiv2', ax)
        addPlottedGraph(GraphType.Medians, 'kIsLenArrayDiv2', ax)
        addPlottedGraph(GraphType.Quick, 'kIsLenArrayDiv2', ax)
    elif graphEnum==(GraphType.WithK10x):
        addPlottedGraph(GraphType.Heap, 'kIs10x_5values', ax)
        addPlottedGraph(GraphType.Medians,'kIs10x_5values', ax)
        addPlottedGraph(GraphType.Quick, 'kIs10x_5values', ax)
    
    if isLog:
        plt.xscale('log')
        plt.yscale('log')

    #Imposta la legenda
    ax.legend(loc='upper left', fontsize=10)

    #Imposta le etichette sugli assi x,y
    ax.set_xlabel(getXTag(graphEnum), fontsize=11, fontweight = 'bold')
    ax.set_ylabel(getYTag(), fontsize=11, fontweight = 'bold')

    #Mostra il grafico
    plt.show()

#--------------------------------------------------------------------------------------------------#
#Graph used in the report:
'''
DrawGraph(GraphType.Quick, True)
DrawGraph(GraphType.Quick, False)
DrawGraph(GraphType.Medians, True)
DrawGraph(GraphType.Medians, False)
DrawGraph(GraphType.Heap, True)
DrawGraph(GraphType.Heap, False)'''
#DrawGraph(GraphType.WithK10x, False)
'''
DrawGraph(GraphType.WithK1, True)
DrawGraph(GraphType.WithK1, False)
DrawGraph(GraphType.WithKLenArray, True)
DrawGraph(GraphType.WithKLenArray, False)
DrawGraph(GraphType.WithKLenArrayDiv2, True)
DrawGraph(GraphType.WithKLenArrayDiv2, False)
DrawGraph(GraphType.WorstQuick, True)
DrawGraph(GraphType.WorstQuick, False)
DrawGraph(GraphType.WorstQuickP3W, True)
DrawGraph(GraphType.WorstQuickP3W, False)
DrawGraph(GraphType.FinalGraph, True)
DrawGraph(GraphType.FinalGraph, False)
DrawGraph(GraphType.FinalGraphWithP3W, True)
DrawGraph(GraphType.FinalGraphWithP3W, False)'''

