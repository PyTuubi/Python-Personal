#MASTER YODA: Given a sentence, return a sentence with the words reversed

#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

def master_yoda(s):
    s2 = s.split(" ")
    s2 = s2[-1::-1]
    output = " ".join(s2)
    return output

print(master_yoda("We are ready"))
    

