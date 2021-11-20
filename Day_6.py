T = int(input()) #berapa kali input data 

for i in range(0, T):
    S = input()
    print(S[0::2] + " " + S[1::2])