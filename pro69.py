bhh,sbt=map(str,input().split("|"))
cct=input()
if  len(bhh)>len(sbt):
    if len(bhh)==len(sbt)+len(cct):
        print(bhh+"|"+sbt+cct)
elif len(bhh)<len(sbt):
     if len(sbt)==len(bhh)+len(cct):
        print(bhh+cct+"|"+sbt)
elif len(bhh)==len(sbt) and len(cct)>1 or (len(sbt) or len(bhh)):
    print("impossible")
