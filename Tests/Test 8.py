st = 'Print every word in this sentence that has an even number of letters'

mylist = st.split(" ")

for item in mylist:
    if len(item) % 2 == 0:
        print(item)