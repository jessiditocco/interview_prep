from collections import Counter
import operator

def can_you_sort(arr):
    """Sort by frequency occurance, than value"""

    counter = Counter(arr)

    custom_sort = []

    sorted_counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))

    for item in sorted_counter:
        for i in range(item[1]):
            custom_sort.append(item[0])
        

    print custom_sort



if __name__ == "__main__":
    num = int(raw_input())

    arr = []

    for i in range(num):
        arr.append(int(raw_input()))

    can_you_sort(arr)



# from collections import Counter
# import operator

# def can_you_sort(arr):
#     """Sort by frequency occurance, than value"""

#     counter = Counter(arr)

#     custom_sort = []

#     sorted_by_value = sorted(counter.items(), key=lambda x: (x[1], x[0]))

#     print(sorted_by_value)

#     for item in sorted_by_value:
#         for i in range(item[1]):
#             custom_sort.append(item[0])
        
#     print(custom_sort)

# if __name__ == "__main__":
#     num = int(input())

#     arr = []

#     for i in range(num):
#         arr.append(int(input()))

#     can_you_sort(arr)