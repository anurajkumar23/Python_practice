with open("file1.txt") as file1:
    file1_data = file1.readlines()
with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
# Write your code above 👆

print(result)