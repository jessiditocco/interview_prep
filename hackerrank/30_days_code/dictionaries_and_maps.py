# Enter your code here. Read input from STDIN. Print output to STDOUT

phonebook_entries = []
phonebook = {}

for i in range(int(raw_input())):
    s = raw_input()

    phonebook_entries.append(s)
    
for phonebook_entry in phonebook_entries:
    name, number = phonebook_entry.split()
    phonebook[name] = number

while True:
        search = raw_input()

        if search == "":
            break
        else:
            if search in phonebook:
                print "{}={}".format(search, phonebook[search])
            else:
                print "Not found"