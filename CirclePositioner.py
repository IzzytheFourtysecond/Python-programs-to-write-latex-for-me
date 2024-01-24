
def circlePositioner(radius, numNodes, startAngle = 90, **kwargs):
   strToReturn = ""
   dAngle = 360 / numNodes
   for num in range(numNodes):
      angle = ((dAngle * num) // 1) + startAngle
      strToReturn += "\\node[<AAAAdevtext_to_replaceAAAA>] (" + str(num) + ") at (" + str(angle) + ":" + str(radius) + ") {}"

      if num != 0:
         strToReturn += "\n\tedge[<BBBBdevtext_to_replaceBBBB>] (" + str(num - 1) + ")"
         if num == numNodes - 1:
            strToReturn += " edge[<BBBBdevtext_to_replaceBBBB>] (0)"

      strToReturn += ";\n"

   return strToReturn

if __name__ == "__main__":
   print(circlePositioner(5, 7))