# this file will import the functions form the 2 files randomOddNums.py and triangle.py

import triangle
import randomOddNums

x = randomOddNums.generateNumber()

triangle.trianglePrint(x)
print("length = " + str(x))

# x > 63 seems to be the limit based on terminal dimensions otherwise triangle comes out weird