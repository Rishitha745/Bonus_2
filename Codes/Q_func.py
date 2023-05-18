import scipy.special

def q_function(z):
    return 0.5 * scipy.special.erfc(z / (2**0.5))

# Example usage:
z = float(input("Give the value of Z-score "))
q = q_function(z)
print(f"Q({z})= {q}")
