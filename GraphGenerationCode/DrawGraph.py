import matplotlib.pyplot as plt
import os
from enum import Enum

'''global var'''
dotSize=20
dotZ=3
lineZ=1 #so the line is under the dot
'''dirs'''
dataDirPath = os.path.join(os.path.dirname(__file__), 'BenchmarkFinalData')
execTimeDirPath = os.path.join(dataDirPath, 'ExecutionTimes')
langDirPath = os.path.join(os.path.dirname(__file__), 'Languages')
'''files'''
arraySizeFilePath = os.path.join(dataDirPath, 'ArraySize.txt')
valuesOfKFilePath = os.path.join(dataDirPath, 'ValuesOfK.txt') #for k=10x
langFilePath = os.path.join(langDirPath, 'ita.txt')

class GraphType(Enum):
    Heap = '_Title_HeapSelect'
    Medians = '_Title_MedianOfMediansSelect'
    Quick = '_Title_Quick'
    WorstQuick = '_Title_WorstQuick'
    WorstQuickP3W ='_Title_WorstQuickPartition3Way'
    WithVariableK = '_Title_k=10x'
    WithK1 ='_Title_k=1'
    WithKLenArray = '_Title_k=lenArray'
    WithKLenArrayDiv2 = '_Title_k=lenArray//2'
    FinalGraph = '_Title_End_Graph'
    FinalGraphWithP3W = '_Title_End_Graph'

INFO = {
    GraphType.Heap: {
        'name': 'Heap Select',
        'dotColor': 'paleturquoise',
        'lineColor': 'darkturquoise',
        'execTimesPath': os.path.join(execTimeDirPath, 'HeapSelect.txt')
    },
    GraphType.Medians: {
        'name': 'Medians Of Medians Select',
        'dotColor': 'mediumpurple',
        'lineColor': 'blueviolet',
        'execTimesPath': os.path.join(execTimeDirPath, 'MedianOfMediansSelect.txt')
    },
    GraphType.Quick: {
        'name': 'Quick Select',
        'dotColor': 'orange',
        'lineColor': 'darkorange',
        'execTimesPath': os.path.join(execTimeDirPath, 'QuickSelect.txt')
    }
}

def isSingleGraph(graphEnum: GraphType):
    if graphEnum in {
    GraphType.Heap,
    GraphType.Medians,
    GraphType.Quick}: 
        return True
    return False

def readValues(filePath):
    values = []
    with open(filePath, 'r') as file:
        for line in file:
            newValue = float(line.strip())
            values.append(newValue)
    return values

def getTitle(graphEnum: GraphType) -> str:
    chiave_cercata = graphEnum.value

    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    for i in range(len(righe) - 1):
        if righe[i] == chiave_cercata:
            return righe[i + 1]  

    return f"Title not found {chiave_cercata}"

def getLinear():
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    for i in range(len(righe) - 1):
        if righe[i] == '_Linear':
            return righe[i + 1] 

    return f"_Linear not found"

def getXTag():
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    for i in range(len(righe) - 1):
        if righe[i] == '_X':
            return righe[i + 1] 

    return f"_X not found"

def getYTag():
    with open(langFilePath, 'r', encoding='utf-8') as file:
        righe = [line.strip() for line in file if line.strip()]

    for i in range(len(righe) - 1):
        if righe[i] == '_Y':
            return righe[i + 1] 

    return f"_Y not found"

def addPlottedGraph(graph: GraphType, superGraph: GraphType, ax):
    algorithm = INFO[graph]
    if superGraph != GraphType.WithVariableK:
        xValues = readValues(arraySizeFilePath)
    else:
        xValues = readValues(valuesOfKFilePath)
    yValues = readValues(algorithm['execTimesPath'])
   
    'dots'
    plt.scatter(xValues , yValues, color = algorithm['dotColor'], label = algorithm['name'], zorder=dotZ, s=dotSize)
    'lines'
    ax.plot(xValues, yValues, '-', color=algorithm['lineColor'], zorder=lineZ)

    k = yValues[0] / xValues[0]
    linearTrend = [(k * x) for x in xValues]
    ax.plot(xValues, linearTrend, '--', color=algorithm['lineColor'], label = getLinear(), zorder=2)


def DrawGraph(graphEnum: GraphType, isLog: bool):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(getTitle(graphEnum), fontsize = 15, fontweight = 'bold')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(labelsize=12)

    if isSingleGraph(graphEnum):
        addPlottedGraph(graphEnum, None, ax)
    elif graphEnum==(GraphType.FinalGraph or GraphType.FinalGraphWithP3W):
        addPlottedGraph(GraphType.Heap, GraphType.FinalGraph, ax)
        addPlottedGraph(GraphType.Medians, GraphType.FinalGraph, ax)
        addPlottedGraph(GraphType.Quick, GraphType.FinalGraph, ax)
        if graphEnum==GraphType.FinalGraphWithP3W:
            addPlottedGraph(GraphType.WorstQuickP3W, GraphType.FinalGraph, ax)

    if isLog:
        plt.xscale('log')
        plt.yscale('log')

    #Imposta la legenda
    ax.legend(loc='upper left', fontsize=10)

    #Imposta le etichette sugli assi x,y
    ax.set_xlabel(getXTag(), fontsize=11, fontweight = 'bold')
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
DrawGraph(GraphType.Heap, False)
DrawGraph(GraphType.WithVariableK, False)
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
DrawGraph(GraphType.FinalGraphWithP3W, False)
'''
