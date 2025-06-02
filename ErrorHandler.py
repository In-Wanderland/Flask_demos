def hypergeofunchandler(x, sample, population, successes):
    # error handling for the hypergeometric calculator, due to the nature of 
    # the calculator code, error checking cannot be done within the function
    # and each seperate possible error is checked for here
    order = [x, sample, successes, population]
    return (not order == sorted(order)) or ((population - successes) < (sample - x))
    # if there is an error, returns true
    
