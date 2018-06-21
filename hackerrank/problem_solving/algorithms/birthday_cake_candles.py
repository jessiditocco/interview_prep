def birthdayCakeCandles(ar):
    maximim = max(ar)

    print ar.count(maximim)

if __name__ == "__main__":
    ar_count = int(input())

    ar = list(map(int, raw_input().rstrip().split()))

    birthdayCakeCandles(ar)