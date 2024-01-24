
def circlePositioner(radius, numNodes, startAngle = 90, **kwargs):
   strToReturn = ""
   dAngle = 360 // numNodes
   for num in range(numNodes):
      angle = (dAngle * num) + startAngle
      strToReturn += "\\node[<AAAAdevtext_to_replaceAAAA>] (" + str(num) + ") at (" + str(angle) + ":" + str(radius) + ") {};\n"
   
   return strToReturn

if __name__ == "__main__":
   print(circlePositioner(8, 13))