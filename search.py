import move

#turn= 1(player),0(generator)
def main (state,turn,IL):
    initialDepth=0 #constant never change
    a=-1 #alfa
    b=2048 #beta
    board=list(state)
    #player
    if turn:
        return max(state,a,b,initialDepth,IL)
    #generator
    else:
        return min(state,a,b,initialDepth,IL)
#
def min (state,a,b,depth,IL):
    depth+=1
    if terminate([0,0,0,0,0,0,0,0],depth,IL):
        return [[],[utility(state)]]
    minChild=[]
    minScore=2048
    children=findMinChildren(state)
    for child in children:
        result=max(child,a,b,depth,IL)
        score=result[1][0]
        if score<minScore:
            minChild=child
            minScore=score
        if minScore<=a:
            break
        if minScore<b:
            b=minScore
    return [minChild,[minScore]]
#
def findMinChildren(state):
    board=list(state)
    while len (board)>9:
        del board[-1]
    minChildren=[]
    for x in getPossiblePositions(board):
        temp=list(state)
        temp[x]=2
        temp.append(x)
        minChildren.append(temp)
    return minChildren
#
def max (state,a,b,depth,IL):
    depth+=1
    if terminate(state,depth,IL):
        return [[],[utility(state)]]
    maxChild=[]
    maxScore=-1
    children=findMaxChildren(state)
    for child in children:
        result=min(child,a,b,depth,IL)
        score=result[1][0]
        if score >maxScore:
            maxChild=child
            maxScore=score
        if maxScore>=b:
            break
        if maxScore>a:
            a=maxScore
    return [maxChild,[maxScore]]
#
def findMaxChildren(state):
    board = list(state)
    maxChildren=[]
    for x in range (1,5):
        temp=move.main(board,x)
        if temp[-1]:
            maxChildren.append(temp)
    return maxChildren
#
def terminate(state,depth,IL):
    board=list(state)
    maxDepth=IL
    if depth<=maxDepth:
        for x in range (0,9):
            if board[x]==0:
                return False
        for x in range(1,5):
            if move.main(board,x)[-1]:
                return False
    return True
#
def utility(state):
    score=0
    for x in range(0,9):
        temp=state[x]
        if temp>score:
            score=temp
    return score
#
def getPossiblePositions(state):
    positions=[]
    for x in range(0,9):
        if state[x]==0:
            positions.append(x)
    return positions