import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ['orders', 'products', 'customers', 'reviews', 'cancels']

def my_func(i):
    wait = random.randint(1,10)
    time.sleep(wait)
    print(f"Finished {i} after {wait} seconds")

# for i in tables:
#     my_func(i)
# Output using for loop
# Finished orders after 3 seconds
# Finished products after 9 seconds
# Finished customers after 9 seconds
# Finished reviews after 9 seconds
# Finished cancels after 9 seconds

with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    # futures = executor.map(my_func, tables)
    
    ## method 2: using loops in parallel
    for i in tables:
        future = executor.submit(my_func, i)


# Output using for Threads
# Finished products after 1 seconds
# Finished customers after 3 seconds
# Finished orders after 6 seconds
# Finished reviews after 6 seconds
# Finished cancels after 6 seconds

# Output using for Threads and loops
# Finished orders after 1 seconds
# Finished reviews after 2 seconds
# Finished products after 3 seconds
# Finished customers after 6 seconds
# Finished cancels after 6 seconds
