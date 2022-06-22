from operator import index


def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n%10
    n//=10   

    b = n%10
    n//=10

    c = n%10
    n//=10

    d = n%10
    n//=10

    e = n%10
    n//=10
    if a>b and a>c and a>d and a>e:
        answer = a
    if b>a and b>c and b>d and b>e:
        answer = b
    if c>a and c>b and c>d and c>e:
        answer = c
    if d>a and d>b and d>c and d>e:
        answer = d
    if e>a and e>b and e>c and e>d:
        answer+=e
    return 5
print(main(25689))