# QUESTION 1 : Create a text file that has your full name, and write code to read it and extract firstname,surname, and lastname
#1: Write the full name to a text file
with open ("myFullName.txt","w") as name:
    name.write("Akinyemi Ogunleye")

#2: Read the full name
with open ("myFullName.txt","r") as name:
    fullName = name.read()
print(fullName)

#3: Exract First Name and Last Name
nameParts = fullName.split()
firstName = nameParts[0]
lastName = nameParts[1]
print(f"First Name: {firstName}")
print(f"Last Name: {lastName}")

# QUESTION 2: Using the library os, print your local file path on screen
import os

myLocalFilePath = os.getcwd()
print(myLocalFilePath)

# QUESTION 3:Extraction of baby name from file using regex not using built-in libraries, create a sort algorithm, implement binary search.

#1. Extract Baby Names Using Regex (Without Built-In Libraries)

def extract_names(text):
    name_pattern = "[A-Za-z]+"  # Simplified pattern for names
    names = []
    i = 0
    while i < len(text):
        if 'A' <= text[i] <= 'Z':  # Names start with an uppercase letter
            j = i
            while j < len(text) and ('a' <= text[j] <= 'z' or 'A' <= text[j] <= 'Z'):
                j += 1
            names.append(text[i:j])
            i = j
        else:
            i += 1
    return names

# Sample text extracted from the html source code for 20 Names in the Popularity in 2008 table

text = """
<tr align="right"><td>1</td><td>Jacob</td><td>Emma</td></tr>
<tr align="right"><td>2</td><td>Michael</td><td>Isabella</td></tr>
<tr align="right"><td>3</td><td>Ethan</td><td>Emily</td></tr>
<tr align="right"><td>4</td><td>Joshua</td><td>Madison</td></tr>
<tr align="right"><td>5</td><td>Daniel</td><td>Ava</td></tr>
<tr align="right"><td>6</td><td>Alexander</td><td>Olivia</td></tr>
<tr align="right"><td>7</td><td>Anthony</td><td>Sophia</td></tr>
<tr align="right"><td>8</td><td>William</td><td>Abigail</td></tr>
<tr align="right"><td>9</td><td>Christopher</td><td>Elizabeth</td></tr>
<tr align="right"><td>10</td><td>Matthew</td><td>Chloe</td></tr>
<tr align="right"><td>11</td><td>Jayden</td><td>Samantha</td></tr>
<tr align="right"><td>12</td><td>Andrew</td><td>Addison</td></tr>
<tr align="right"><td>13</td><td>Joseph</td><td>Natalie</td></tr>
<tr align="right"><td>14</td><td>David</td><td>Mia</td></tr>
<tr align="right"><td>15</td><td>Noah</td><td>Alexis</td></tr>
<tr align="right"><td>16</td><td>Aiden</td><td>Alyssa</td></tr>
<tr align="right"><td>17</td><td>James</td><td>Hannah</td></tr>
<tr align="right"><td>18</td><td>Ryan</td><td>Ashley</td></tr>
<tr align="right"><td>19</td><td>Logan</td><td>Ella</td></tr>
<tr align="right"><td>20</td><td>John</td><td>Sarah</td></tr>
"""
names = extract_names(text)
print("Names: ",names)

# 2. Create a Sort Algorithm

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_names = selection_sort(names)
print("Sorted Names:", sorted_names)

#3. Implement Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

name_to_search = "Emma"
index = binary_search(sorted_names, name_to_search)
if index != -1:
    print(f"Name '{name_to_search}' found at index {index}.")
else:
    print(f"Name '{name_to_search}' not found.")
