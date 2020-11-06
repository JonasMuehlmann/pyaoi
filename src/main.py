from src import std
print(std.all_of([1, 2, 3, 4, 5], lambda x: x < 6))
print(std.all_of([1, 2, 3, 4, 5], lambda x: x > 6))
print(std.all_of(1, print))
