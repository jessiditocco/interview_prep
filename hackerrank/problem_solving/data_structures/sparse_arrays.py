def sparse_arrays(strings, queries):
    # make a dictionary with the input strings and their occurances
    # loop through the queries and add that count to a frequency list
    # return the list

    string_count = {}
    frequencies = []

    for string in strings:
        string_count[string] = string_count.get(string, 0) + 1

    for query in queries:
        if query in string_count:
            frequencies.append(string_count[query])
        else:
            frequencies.append(0)

    return frequencies

if __name__ == "__main__":
    strings_count = int(raw_input())
    strings = []
    queries = []

    for n in range(strings_count):
        string = raw_input()
        strings.append(string)

    queries_count = int(raw_input())

    for q in range(queries_count):
        query = raw_input()
        queries.append(query)

    sparse_arrays(strings, queries)