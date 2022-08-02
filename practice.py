a=[{"question":"Correct extansion of python file?","answer":"py","explaintion":""},
   {"question":"what is django?","answer":"django is framework","explaintion":"django is used to create web-app"},
   {"question":"who is the pm of our country?","answer":"N.Modi","explaintion":""},
   {"question":"what is your name","answer":"my name is noah","explaintion":"noah is also a frictional charchter"},
   {"question":"is set ordered?","answer":"no","explaintion":"since set has no indexing its unordered"},
   {"question":"what is python","answer":"python is a programming langauge","explaintion":""},
   {"question":"Correct extansion of python file?","answer":"py","explaintion":""},
   {"question":"what is django","answer":"django is framework","explaintion":"django is used ton create web-app"},
   {"question":"what is immutable?","answer":"somemthing that can'nt be changed","explaintion":""},
   {"question":"what is mutable","answer":"something that can be change after their creation","explaintion":""}]
k=1
for z in range(len(a)):
    print(k,":-",a[z]["question"])
    print("Ans:", a[z]["answer"])
    k+=1
    
print("explaintions:-")
z=1
for i in range(len(a)):
    b=a[i]["explaintion"]
    if b=="":
        pass
    else:
        print(z,":-",b)
    z+=1
    