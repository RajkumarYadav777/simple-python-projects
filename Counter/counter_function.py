
# we are making a counter app using functions
# here we manage states using closures and nonlocal


def make_counter(start = 0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def reset():
        nonlocal count
        count = start
        return count

    
    return increment, decrement, reset

inc, dec, reset = make_counter(5)
print(inc())
print(inc())
print(dec())
print(reset())
