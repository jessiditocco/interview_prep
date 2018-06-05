def print_even_odd(s1):

    even_index_letters = []
    odd_index_letters = []

    for i in range(len(s1)):
        if i % 2 == 0:
            even_index_letters.append(s1[i])
        else:
            odd_index_letters.append(s1[i])

    return "".join(even_index_letters) + " " + "".join(odd_index_letters)


print print_even_odd("Hacker")


# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(raw_input())):
    s = raw_input()
    
    even_index_letters = []
    odd_index_letters = []
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_index_letters.append(s[i])
        else:
            odd_index_letters.append(s[i])
            
    print "".join(even_index_letters) + " " + "".join(odd_index_letters)


# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(raw_input())):
    s = raw_input()
    
    print s[::2] + " " + s[1::2]
