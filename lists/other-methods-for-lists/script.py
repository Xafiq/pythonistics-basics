employees = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
employees.index("Alex")  # 4
employees.count("Max")  # 2
employees.sort()  # Sorts the list in place: ["Alex", "Carlos", "Martine", "Max", "Max", "Patrick"]
sorted(employees)  # Sorts the list but does not modify the original list!
sorted_list = sorted(employees)  # Returns the sorted list in a new list.

numbers = [10, 1, 5, 15]
numbers.reverse()  # Reverses the order of the list: [15, 5, 1, 10]
print(numbers)

