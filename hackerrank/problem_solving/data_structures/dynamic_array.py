def dynamic_array(n, q):

    seq_list = []

    for i in range(n):
        seq_list.append([])

    last_answer = 0

    for i in range(q):
        query = raw_input().split()
        query_type = int(query[0])
        x = int(query[1])
        y = int(query[2])

        if query_type == 1:
            index = ((x ^ last_answer) % n)
            seq = seq_list[index]
            seq.append(y)

        elif query_type == 2:
            index = ((x ^ last_answer) % n)
            seq = seq_list[index]
            last_answer = seq[y % len(seq)]
            print last_answer


if __name__ == "__main__":
    line1 = raw_input().split()
    n = int(line1[0])
    q = int(line1[1])

    dynamic_array(n, q)




