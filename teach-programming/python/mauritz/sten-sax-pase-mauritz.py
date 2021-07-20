import random

ALTERNATIV = ["sten", "sax", "påse"]
dator = 0
användare = 0
for i in [ 1, 2, 3, 4, 5]:
  val=input("sten,sax eller påse ")
  datorval=random.choice(ALTERNATIV)

  print(f"val={val} datorval={datorval}")

  if val == "sten" and datorval == "sax":
    print("du vann")
    användare = användare + 1
  elif val == "påse" and datorval =="sten":
    print ("du vann")
    användare = användare + 1
  elif val == "sax" and datorval =="påse":
    print  ("du vann")
    användare = användare + 1
  elif val == "påse" and datorval =="påse":
    print  ("oavgjort")
  elif val == "sax" and datorval =="sax":
    print ("oavgjort")
  elif val =="sten" and datorval =="sten":
    print ("oavgjort")
  else:
    print ("du förlora")
    dator = dator + 1
