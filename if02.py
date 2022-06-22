def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer = 0
    if a<b and c>b:
        answer+=a
    if a>b and b<c:
        answer+=b
    if c<a and b>c:
        answer+=c
    return answer
print(main(12,8,21))