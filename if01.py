def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer = 0
    if a>b and a>c:
        answer += a
    if b>a and b>c:
        answer += a
    if c>b and c>a:
        answer += c
    return answer
print(main(12,8,2))
    