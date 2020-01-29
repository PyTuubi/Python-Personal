#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

def almost_there(n):
    list1 = [90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210]
    if n in list1:
        print("True")
    else:
        print("False")

almost_there(209)

