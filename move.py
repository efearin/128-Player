# 1 up 2 down 3 left 4 right 
# 012
# 345
# 678
#last bit is check if movement is proper 1 if not 0 decode it from other functions if there is deleted here

def main (state,movement):
    while len(state)>9:
        del state[-1]
    board=list(state)
    move(board,movement)
    if state==board:
        board.append(0)
        return board
    else:
        board.append(movement)
        return board
#
def move(board,movement):
    for x in range(0,3):
        #initiation
        if movement==1:
            a=board[x]
            b=board[x+3]
            c=board[x+6]
        if movement==2:
            c=board[x]
            b=board[x+3]
            a=board[x+6]
        if movement==3:
            a=board[3*x]
            b=board[3*x+1]
            c=board[3*x+2]
        if movement==4:
            c=board[3*x]
            b=board[3*x+1]
            a=board[3*x+2]
        #shift
        if a==0:
            a=b
            b=c
            c=0
            if a==0:
                a=b
                b=0
        else:
            if b==0:
                b=c
                c=0
        #sum
        if a!=0:
            if a==b:
                a=a+b
                b=c
                c=0
            else:
                if b==c:
                    b=b+c
                    c=0
        #reverse initiation
        if movement==1:
            board[x]=a
            board[x+3]=b
            board[x+6]=c
        if movement==2:
            board[x]=c
            board[x+3]=b
            board[x+6]=a
        if movement==3:
            board[3*x]=a
            board[3*x+1]=b
            board[3*x+2]=c
        if movement==4:
            board[3*x]=c
            board[3*x+1]=b
            board[3*x+2]=a

