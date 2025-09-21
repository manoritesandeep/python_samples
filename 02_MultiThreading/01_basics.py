from concurrent.futures import ThreadPoolExecutor

def transformation(input):
    src = input['src']
    dst = input['dst']
    
    print(f"Reading from {src}")
    print(f"Transforming data...")
    print(f"Writing to {dst}\n")
    return f"{src} -> {dst}"
    
sample_arr = [
    {"src": "table1", "dst" : "table1"},
    {"src": "table2", "dst" : "table2"},
    {"src": "table3", "dst" : "table3"},
    {"src": "table4", "dst" : "table4"},
     ]
print(f"Type of array is: {type(sample_arr)}\n")

with ThreadPoolExecutor(max_workers=len(sample_arr)) as executor:
    results = executor.map(transformation, sample_arr)

print(f"\nReturned values are: {list(results)}")