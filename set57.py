    
thha,see=map(int,input().split())
hat=list(map(int,input().split()[:thha]))
cat=0
for i in hat:
   if(i==see):
      cat=cat+1
print(cat) 
