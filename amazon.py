
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return n + recursive_function(n-1)

print(recursive_function(5))