def isHappy(n: int) -> bool:
    seen = set()
    current = str(n)
    while current not in seen:
        seen.add(current)
        sum = 0

        for digit in current:
            digit = int(digit)
            sum += digit ** 2

        if sum == 1:
            return True
        current = str(sum)
    return False

