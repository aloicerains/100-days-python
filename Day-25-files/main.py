# Handling csv files
# this is basic method
# data = []
# with open('weather_data.csv', 'r') as f:
#     for line in f: # you can also use readlines function instead
#         data.append(line.strip()) # strip removes the white spaces including the newline character
# print(data)

# There is inbuilt library for handling csv data files
# import csv
#
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file) # csv reader object that can be looped through
#     temperatures = [int(row[1]) for row in data if row[1].isnumeric()]
#     print(temperatures)

# using pandas library
import pandas as pd

data = pd.read_csv('weather_data.csv')
temperatures = data.temp
# print(temperatures)
# Getting dictionary data
data_dict = data.to_dict()
# print(data_dict)

# Getting a list of temperatures
list_temp = data.temp.to_list() # works for series data
# print(list_temp)

# Getting avarage temperature
avg = round(data.temp.mean(), 2)
# print(avg)

# Getting max temp
max_temp = data.temp.max()
# print(max_temp)

# Getting row data with max temperature of the week
day = data[data['temp'] == data.temp.max()]

# Getting Monday temperature in farenheight
monday = data[data.day == 'Monday']
fahrenheit = round(monday.temp * 9 / 5 + 32, 2)
# print(fahrenheit)

# Creating a data frame from dictionary
student_score = {
    'students': ['Akyi', 'Milan', 'Okot', 'Martin'],
    'scores': [56, 67, 89, 54]
}

students = pd.DataFrame(student_score)
# print(students)

def grading(row):
    """Function transforms the dataset"""
    if row.scores > 80:
        row['Grade'] = 'A'
    elif row.scores > 60:
        row['Grade'] = 'B'
    elif row.scores > 55:
        row['Grade'] = 'C'
    else:
        row['Grade'] = 'Fail'
    return row


# axis column implies grading function will work on the rows,
# axis index would imply that the function would work on columns
student_grades = students.apply(grading, axis='columns')
# print(student_grades)

# Saving the data to csv file
student_grades.to_csv('students_grade.csv')

# ANALYSIS OF SQUIRREL DATA
# Obj: Create a data frame based on the number of squirrel colors

dataset = pd.read_csv('squirrel data.csv')

fur_dataset = dataset['Primary Fur Color'].value_counts() # Generates series data where the index is the
# is the unique color and the values are the total counts
squirrel_fur = pd.DataFrame({
    'Fur color': fur_dataset.index,
    'Count': fur_dataset.values
})
print(squirrel_fur.head())
# loading data to csv
squirrel_fur.to_csv('squirrel_color_count.csv')

