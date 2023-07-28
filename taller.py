def who_is_taller(X, Y):
    if X < Y:
        return 'B'
    else:
        return 'A'

# Input
T = int(input().strip())

# Process each test case
for _ in range(T):
    X, Y = map(int, input().strip().split())

    # Output
    print(who_is_taller(X, Y))
