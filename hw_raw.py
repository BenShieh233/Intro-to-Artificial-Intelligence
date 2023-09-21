import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred():
    X = {char: 0 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    with open('letter.txt', encoding='utf-8') as f:
        text = f.read()
        # Update the counts based on the characters in the text
        for char in text:
            if char.isalpha():
                char = char.upper()
                if char in X:
                    X[char] += 1
    return X


print("Q1")
for char, count in shred().items():
    print(f"{char} {count}")


print("Q2")
X = list(shred().values())
e, s = get_parameter_vectors()[0], get_parameter_vectors()[1]
x1loge1 = round(X[0] * math.log(e[0]), 4)
x1logs1 = round(X[0] * math.log(s[0]), 4)
print(x1loge1)
print(x1logs1)

print("Q3")
PEng = 0.6
PSpan = 0.4
Xilogei, Xilogsi = 0, 0
for i in range(len(X)):
    Xilogei += X[i] * math.log(e[i])
    Xilogsi += X[i] * math.log(s[i])
FEng = round(Xilogei+math.log(PEng) ,4)
FSpan = round(Xilogsi+math.log(PSpan), 4)

print(FEng)
print(FSpan)

print("Q4")
Prob_Eng = 0
if FSpan - FEng >= 100:
    Prob_Eng_ = 0
elif FSpan - FEng <= -100:
    Prob_Eng = 1
else:
    Prob_Eng = 1/(1 + math.exp(FSpan - FEng))
print(round(Prob_Eng, 4))
