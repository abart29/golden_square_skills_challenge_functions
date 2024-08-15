def get_most_common_letter(text):
    counter = {}
    print(f"This is counter at line 3: {counter}\n")
    for char in text:
        if char not in ["!", ",", " "]:
            counter[char] = counter.get(char, 0) + 1

    print(f"This is counter at line 8: {counter}\n")

    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0] # pulling out the number in the tuple instead of the 
    
    print(f"This is counter.items at line 12: {counter.items()}\n") #turns into tuple

    print(f"This is sorted counter.items at line 14: {sorted(counter.items())}\n") #sorts allphabetically

    print(f"This is sorted counter.items with key at line 16: {sorted(counter.items(), key=lambda item: item[1])}\n") #sorts in order numerically

    print(f"This is the desired item at line 18: {sorted(counter.items(), key=lambda item: item[1])[-1]}\n") #testing which one it returns 

    print(f"This is the desired 1th index value of the desired item at line 22: {sorted(counter.items(), key=lambda item: item[1])[-1][0]}\n") #

    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
