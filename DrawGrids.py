

def DrawGrids(start, vSize, hSize):
   outputStr = [""]  # Its in a list because otherwise
                     # the string is passed by value.
   def addLine(text, thing=outputStr):
      thing[0] += "\t" + text + "\n"
   

   

   addLine("hello")
   return outputStr[0]




if __name__ == "__main__":
   print(DrawGrids())