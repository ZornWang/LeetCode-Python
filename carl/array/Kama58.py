def main():
    n = int(input())
    prefix_sum = [0] * n

    s = 0
    for i in range(n):
        value = int(input())
        s += value
        prefix_sum[i] = s
    prefix_sum = [0] + prefix_sum
    while True:
        try:
            nums = input().split()
        except:
            break
        print(prefix_sum[int(nums[1]) + 1] - prefix_sum[int(nums[0])])


if __name__ == "__main__":
    main()
