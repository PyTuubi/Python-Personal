#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(s):
    result = ''

    for l in s:
        result += l*3
    
    return result


print(paper_doll("Hello"))

