chat,chet=map(int,input().split())
law=list(map(int,input().split()))
chat=[]
law.insert(0,0)
for p in range(chet):
     vim=[]
     sha=0
     but,zee=map(int,input().split())
     for i in range(but,zee+1):         
         sha^=law[i]     
     chat.append(sha)
for p in chat:
     print(p)
