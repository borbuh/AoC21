import binascii, sys
import datetime

forward = 0
depth = 0
up = 0
down = 0
aim = 0
moveForward = 0

if(len(sys.argv)>1):
  fns = sys.argv[1:]
else:
  fns=["C:\\Users\\borbu\\Downloads\\log.txt"]
  
for fn in fns:
 if not '.py' in fn:
  with open(fn, "r", encoding='utf-8') as f:
    lines = f.readlines()
    with open(fn+'.txt', "w") as fout:
      for line in lines:
        print("-----------------------")
        if "forward" in line:
         # print(line)
          forward = int(line.split('forward ')[1])
          depth += aim * forward
          moveForward += forward
          print("Forward: ", forward)
          print("Aim: ", aim)
          print( "Depth: ",depth)
        if "down" in line:
         # print(line)
          down -= int(line.split('down ')[1])
          aim += abs(int(line.split('down ')[1]))
          #print("Aim: ", aim)
        if "up" in line:
         # print(line)
          up += int(line.split('up ')[1])
          aim -= abs(int(line.split('up ')[1]))
          #print("Aim: ", aim)
          
print("Final position = ", moveForward * depth )
