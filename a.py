
try:
    import Queue as Q
except ImportError:
    import queue as Q

import helper
from strategy import UCS, IDS


N, ARRAY, GOAL = helper.input('input1.txt')


def UCS(init):
    PQ = Q.PriorityQueue()

    visited = [False for i in range(N*N)]
    listExpanded = []
    path = [-1 for i in range(N*N)]

    PQ.put([0, init])

    # loop
    while not PQ.empty():
        pathCost, currentNode = PQ.get()
        listExpanded.append(currentNode)
        visited[currentNode] = True

        if currentNode == GOAL:
            pathReturn = [GOAL]
            tmp = GOAL
            while not init in pathReturn:
                pathReturn.append(path[tmp])
                tmp = path[tmp]
            pathReturn.reverse()
            return (len(listExpanded)-1, listExpanded, pathReturn)

        for nodeExpand in ARRAY[currentNode]:
            if not visited[nodeExpand]:
                # PQ.put(pathCost+1, nodeExpand)
                path[nodeExpand] = currentNode
                tmpCost = pathCost+1
                tmpPQ = Q.PriorityQueue()
                duplicate = False
                for i in range(PQ.qsize()):
                    tmpValue = PQ.get()
                    if tmpValue[1] == nodeExpand:
                        if (tmpCost < tmpValue[0]):
                            tmpValue[0] = tmpCost
                        duplicate = True
                    tmpPQ.put(tmpValue)

                for i in range(tmpPQ.qsize()):
                    PQ.put(tmpPQ.get())
                if not duplicate:
                    PQ.put([pathCost+1, nodeExpand])
    return (len(listExpanded)-1, listExpanded, [])


print(UCS(0))
