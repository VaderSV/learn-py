"""
You need to print the dictionary in descending order of the sum of each value.

Example with lambda function.
"""
bigGrams = {"AB": [10, 11, 12], "BC": [5, -5, 8], "CD": [105, 1, 0],
            "DE": [6, 6], "EF": [15, 20, 15], "FG": [22, 11, 32],
            "GH": [20, 20, 20]}
sorter = sorted(bigGrams, key=lambda key: sum(bigGrams[key]), reverse=True)

for key in sorter:
    print(key, bigGrams[key])
