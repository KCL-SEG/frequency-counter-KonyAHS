"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for value in items:
        #converts value to Strings
        val = str(value)
        
        #decides if to increment or add new element
        if val in frequencies.keys():
            frequencies[val] += 1
        else: 
            frequencies[val] = 1
    return frequencies
