st = 'Print only the words that start with s in this sentence'

mylist = st.split(" ")

for item in mylist:
    if item[0] == "s":
        print(item)