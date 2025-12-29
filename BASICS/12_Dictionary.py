# Dictionary = a built-in, mutable data structure that stores collections of data in key-value pairs. key = name , value = "mayank"

student = {
    "name": "Mayank",
    "age": 20,
    "course": "BTech",
    "semester": 4
}

print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Course:", student["course"])

# Updating value
student["age"] = 21
print("Updated age:", student["age"])

# Adding new key-value pair
student["college"] = "ABC Institute"
print("After adding college:", student)

# Removing a key-value pair
student.pop("semester")
print("After removing semester:", student)