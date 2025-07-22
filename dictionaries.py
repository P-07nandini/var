#dictionaries(dict)
#a dictionary is a collectionof key-value pairs
#it is mutable and unordered
#it is indexed by keys
#it is defined by using curly braces{}
a={"name":"bhaskar","age":22,"place":"hyderabad"}
#adding /updating
a["name"]="bhaskar rao"
a["age"]=23
a["place"]="hyderabad, india "
#removing
del a["place"]
print(a)
#accessing
print(a["name"])
print(a["age"])
#iterating