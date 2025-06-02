def factorial(n):
    if n == 0 : return 1
    else : return (factorial(n-1)*n)

def nCkfunc(n, k):
    #function throws an error if n < k
    return factorial(n)/(factorial(k)*factorial(n-k))

def hypergeofunc(X, Sample, Population, Successes):
    #function throws an error if it asks for a negative factorial
    num = nCkfunc(Sample, X)*nCkfunc(Population-Sample, Successes - X)
    den = nCkfunc(Population, Successes)
    return num/den