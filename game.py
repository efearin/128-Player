import generator
import player
import search
import move
import time

def main():

    #written by Efe Arın and Cem Recai Çırak 03.2017
    print("written by Efe Arın and Cem Recai Çırak 03.2017")
    print("")
    print("This mini program plays 128 by itself, using minimax algoritm with alpha beta pruning and configurable independent player-generator intelligence level which adjusts how many future steps could be handled by both opponents")
    print("")
    print("program throws result.txt file so make sure that you have write permition in working directory if not copying the program to another folder then running may help")
    print("")
    print("Play with intelligence levels and see differences. Higher then 10 could take a while. To see 128 on the board player intelligence may set over 15")
    print("")
    generatorIL=int(input("enter intelligence level of generator (ex: 5): "))
    playerIL=int(input("enter intelligence level of player (ex: 10): "))
    # generatorIL=1
    # playerIL=1
    print("")

    #
    def terminate (state):
        for x in range (1,5):
            if move.main(state,x)[-1]:
                return False
        return True
    #
    def show(state):
        print(state[0],state[1],state[2])
        print(state[3],state[4],state[5])
        print(state[6],state[7],state[8])
        print("")
    #
    
    resultFile = open("result.txt", "w")
    resultFile.write("player intelligence: "+str(playerIL)+"\n")
    resultFile.write("generator intelligence: "+str(generatorIL)+"\n")

    state = generator.randomGenerate()
    print("Board is randomly initialized by generator")
    show(state)
    resultFile.write("initial board: "+str(state).strip("[]")+"\n")
   
    turnNumber=0
    start=time.time()
    
    resultFile.write("actions taken by player (1:up, 2:down, 3:left, 4:right) and generator (position of 2 (from position 0 to 8 on the board) in play order starting from player: \n")

    while not terminate(state) :
        turnNumber+=1
        print("turn number ",turnNumber)
        state = player.main(state, playerIL)
        resultFile.write(str(state[-1])+" ")
        show(state)
        state = generator.main(state, generatorIL)
        resultFile.write(str(state[-1])+" ")
        show(state)
    
    stop=time.time()
    totalTime=stop-start

    score = search.utility(state)

    resultFile.write("\nfinal board is: "+str(state).strip("[]")+"\n")
    resultFile.write("score: "+str(score)+"\n")
    resultFile.write("turn number: "+str(turnNumber)+"\n")
    resultFile.write("total time: "+str(totalTime)+"\n")
    resultFile.write("time per turn: "+str(totalTime/turnNumber))
    resultFile.close()

    print("Game is over at score ",score," in ",turnNumber," turns and total time spend is ",totalTime," (apprx. ",totalTime/turnNumber," for each turn).")
    print("")
    print("Result file is created under working directory named as result.txt")
    print("")
    print("Press any key to exit")
    input()
#
if __name__== "__main__":
    logicLevel=10
    main()


