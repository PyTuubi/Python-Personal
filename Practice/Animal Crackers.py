#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(s):
    s = s.split(' ')

    if s[0][0] == s[1][0]:
    
        print("True")

    else:
        
        print("False")
    

animal_crackers('Crazy Kangaroo')


