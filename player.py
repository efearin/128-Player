import search

def main (state, playerIL) :
    result=search.main(state,1,playerIL)
    move=result[0][-1]
    if move==1:
        print("Player : Up is played")
    elif move==2:
        print("Player : Down is played")
    elif move==3:
        print("Player : Left is played")
    elif move==4 :
        print("Player : Right is played")
    else:
        print(move)
    return result[0]