#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(s):
    for l in s:
        print(l * 3)


paper_doll("Hello")

