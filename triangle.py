
def trianglePrint(Oddnumber):
    for row in range(Oddnumber):
        for coloumn in range(row +1): #  +1 will need to print an extra last star in last coloumn for every row
            # deciding which row and coloumn entries will get a * - all perimeter points

            if row==coloumn or row==Oddnumber -1 or coloumn==0:
                print('*', end =" ") #end keeps on the same line 
            else:
                print(" ", end =" ")

        print() #prevents a linear printout


