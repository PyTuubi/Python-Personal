#BLACKJACK: Given three integers between 1 and 11, 
# if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, 
# reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(x,y,z):
    if x + y + z >= 21 and (x == 11 or y == 11 or z == 11):
        return (x + y + z) - 10
    
    elif x + y + z >= 21:
        return "Bust"
    
    elif x + y + z <= 21:
        return x + y + z
    



result = blackjack(9,9,11)

print(result)
