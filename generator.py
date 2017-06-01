import search
import random

def main (state,generatorIL):
    result= search.main(state,0,generatorIL)
    print("Generator : 2 is put into position " , result[0][-1])
    return result[0]
#
def randomGenerate():
    state=[0,0,0,0,0,0,0,0,0]
    state [random.randint(0,8)]=2
    return state