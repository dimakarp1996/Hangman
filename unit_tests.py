
from Hangman import loss
assert loss(5,7)=='You won!'
assert loss(7,7)=='You lost!'
assert loss(9,7)=='You lost!'
from Hangman import check
from Hangman import DICT
alph='abcdefghijklmnopqrstuvwxyz'
for i in range(5):
    for word in DICT:
        for letter in alph:
            if letter not in word:
                assert check(letter,'*****',word,i)==('*****',word,i+1)
    assert check('e','*****',"hello",i)==('*e***',"hello",i)
    assert check('e','*****',"smell",i)==('**e**',"smell",i)
    assert check('l','**e**',"smell",i)==('**ell',"smell",i)
    assert check('e','*****',"apple",i)==('****e',"apple",i)
    assert check('e','*****',"phone",i)==('****e',"phone",i)
    assert check('r','*****',"brink",i)==('*r***',"brink",i)