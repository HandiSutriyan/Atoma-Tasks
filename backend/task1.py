def binary_gap(n):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while n > 0 and n % 2 == 0:
        n //= 2

    while n > 0:
        remainder = n % 2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        n //= 2
    print (max_gap)

x = int(input(''))
binary_gap(int(x))
