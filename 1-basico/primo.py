def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(eh_primo(2))   # True
print(eh_primo(15))  # False
print(eh_primo(17))  # True
