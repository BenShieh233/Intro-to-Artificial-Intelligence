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
    # Set a dictionary with keys from A-Z
    X = {char: 0 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    
    # Opening the file
    with open('letter.txt', encoding='utf-8') as f:
        text = f.read()
        # Update the counts based on the characters in the text
        for char in text:
            if char.isalpha(): # Keep only letters in each line
                char = char.upper() # Case-folding
                if char in X:
                    X[char] += 1
    return X

# Calculate x1*loge1 and x1*logs1
def cal_x1_logs(X, e, s):
    x1 = X[0]
    x1_log_e1 = round(x1 * math.log(e[0]), 4)
    x1_log_s1 = round(x1 * math.log(s[0]), 4)
    return x1_log_e1, x1_log_s1

# Calculate F(Spanish) and F(English)
def cal_F(X, e, s):
    global PEng, PSpan
    xilogei, xilogsi = 0, 0
    for i in range(len(X)):
        xilogei += X[i] * math.log(e[i])
        xilogsi += X[i] * math.log(s[i])
    FEng = round(xilogei+math.log(PEng) ,4)
    FSpan = round(xilogsi+math.log(PSpan), 4)
    return FEng, FSpan

def cal_prob_ENG(FEng, FSpan):
    if FSpan - FEng >= 100:
        Prob_Eng_ = 0
    elif FSpan - FEng <= -100:
        Prob_Eng = 1
    else:
        Prob_Eng = 1/(1 + math.exp(FSpan - FEng))
    return round(Prob_Eng, 4)

# Q1: Character counts
X = list(shred().values())
print("Q1")
for char, count in shred().items():
    print(f"{char} {count}")

#Q2: x1*loge1 and x1*logs1
e, s = get_parameter_vectors()[0], get_parameter_vectors()[1]
x1loge1, x1logs1 = cal_x1_logs(X, e, s)
print("Q2")
print(x1loge1)
print(x1logs1)

#Q3: F(English) and F(Spanish)
PEng = 0.6
PSpan = 0.4
FEng, FSpan = cal_F(X, e, s)
print("Q3")
print(FEng)
print(FSpan)

#Q4: Prob(Y=English | X)
Prob_Eng = cal_prob_ENG(FEng, FSpan)
print("Q4")
print(Prob_Eng)




