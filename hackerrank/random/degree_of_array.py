from collections import Counter

def degree_of_array(arr):
    
    counter = Counter(arr)

    max_frequency = 0

    for i in counter:
        if counter[i] > max_frequency:
            max_frequency = counter[i]
                               
    max_frequencies = []

    for item in counter:
        if counter[item] == max_frequency:
            max_frequencies.append(item) 

    a_dict = {}

    # import pdb; pdb.set_trace()

    for i in range(len(arr)):

        if a_dict.get(arr[i]) == None:
            a_dict[arr[i]] = [i, 0]

        counter[arr[i]] -= 1

        if counter[arr[i]] == 0:
            start = a_dict[arr[i]][0]
            a_dict[arr[i]] = [start, i]

    minimum = len(arr)

    for num in max_frequencies:
        if a_dict[num][1] - a_dict[num][0] < minimum:
            minimum = a_dict[num][1] - a_dict[num][0]

    print minimum + 1



if __name__ == "__main__":
    num = int(raw_input())
    arr = []

    for i in range(num):
        arr.append(int(raw_input()))

    degree_of_array(arr)
