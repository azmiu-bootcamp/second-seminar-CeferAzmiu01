#CeferMemmedzade  #1citapshiriq
reqem = int(input("reqemi daxil edin: "))
a  = reqem //1000
b = (reqem - a*1000)//100
c = (reqem - a*1000 - b*100)//10
d =reqem - a*1000 - b*100 - c*10
print("Reqemlerin toplami: ", a+b+c+d)
