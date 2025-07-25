# Dictionaries (dict)
# A dictionary is a collection of key-value pairs
# It is mutable and unordered
# It is indexed by keys
# It is defined by using curly braces {}

a = {"name": "bhaskar", "age": 22, "place": "hyderabad"}

# Adding / Updating
a["name"] = "bhaskar rao"
a["age"] = 23
a["place"] = "hyderabad, india"
print(a)

# Removing
del a["place"]
print(a)

# Accessing
print(a["name"])
print(a["age"])

# Iterating
# Iterating over keys
for key in a:
    print("Key:", key, "Value:", a[key])

# Or use items() to iterate over key-value pairs
for key, value in a.items():
    print(f"{key} : {value}")

