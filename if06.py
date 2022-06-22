from operator import index


def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    s = 0
    a = n%10
    n//=10   
    if s<a:
        s = 1
    b = n%10
    n//=10
    if s<b:
        s = 2
    c = n%10
    n//=10
    if s<c:
        s = 3
    d = n%10
    n//=10
    if s<d:
        s = 4
    e = n%10
    n//=10
    if s<e:
        s = 5
    return s
print(main(25698))

    