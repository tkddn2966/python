import os 
import pickle

def save(n):
    with open(n,mode="wb")as file:
        print("[점수 입력]")
        a = 1
        scores = []
        while True:
            score = int(input(f"#{a}? "))
            if score >= 0:
                scores.append(score)
                a += 1
            else:
                break
        pickle.dump(len(scores), file)  
        for s in scores:
            pickle.dump(s, file)
        
    
def load(n):
    with open(n,mode="rb")as file:
        print("[점수 출력]")
        print(f"개인점수: ",end = "")
        b = 0
        c = pickle.load(file)
        for i in range(c):
            scores = pickle.load(file)
            print(scores,end =" ")
            b += scores
        print(f"\n평균: {b//c}")
        

s = "score.bin"

if os.path.exists(s):
    print("[파일 읽기]")
    print()
    pass
else:
    save(s)

load(s)
