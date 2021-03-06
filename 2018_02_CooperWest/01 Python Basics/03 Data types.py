
# Data Types

# String, can be in double or single quotes:
name = "Andy"
print(name)
# ...because you might need quotes within a string:
phrase = 'Andy says, "hello!"'
print(phrase)

# Integer, and floating point number "float"
print(25 / 3)

# List data type:
days = ["Monday", "Tuesday", 24, "Wednesday", "Thursday"]
print(days)
# Call out one item from the list, counting starts from zero:
print( days[2] )
print( len(days) )
totalItems = len(days)
print(totalItems)
days.sort()
print(days)

print(days + ["Friday"])
print(days)
days = days + ["Friday"]
print(days)

# List index:
print( days[-3:] )
# 0   1         2           3          4           5         6
# [24, 'Monday', 'Thursday', 'Tuesday', 'Wednesday', 'Friday']
    #    -5        -4          -3         -2            -1   

days.pop(2)
print(days)