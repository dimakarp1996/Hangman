
import random#calculate random numbers
DICT = ['hello', 'apple', 'phone', 'smell', 'brink']
def loss(attempts, num):#calculate loss
    if attempts >= num:
        return 'You lost!'
    return 'You won!'
def check(INP,GUESS,LETTER,ATTEMPTS):
    INP=INP[0]
    N=len(LETTER)
    if INP in LETTER:
        for j in range(N):
            if LETTER[j] == INP:
                GUESS = GUESS[:j]+INP+GUESS[j+1:]
        print('Hit!')
        print('The word: '+GUESS)
    else:
        ATTEMPTS += 1
        print('Nussed, mistake %d out of %d'% (ATTEMPTS, N))
    return GUESS,LETTER,ATTEMPTS
def play():
    random.seed(0)
    i = random.randint(0, 4)
    print("GUESS a LETTER:")
    LETTER = DICT[i]
    N = len(LETTER)
    GUESS = '*'*N
    REQUESTS = []
    ATTEMPTS = 0
    while ATTEMPTS < N:
        INP = input()
        REQUESTS.append(INP[0])
        INP = INP[0]
        GUESS,LETTER,ATTEMPTS=check(INP,GUESS,LETTER,ATTEMPTS)
        if GUESS == LETTER:
                break
    print(loss(ATTEMPTS, N)+'\n')
