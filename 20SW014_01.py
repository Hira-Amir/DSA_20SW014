
#TASK1

name = "Hira"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

"""TASK2"""

string = "hello"
capitalized_string = string.capitalize()
print(capitalized_string)

string = "smile anyway"
count = string.count("y")
print(count)

string = "sad day "
replaced_string = string.replace("happy", "day")
print(replaced_string)

"""TASK3"""

month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num_days = days_in_month[month - 1]
print(num_days)

"""TASK4"""

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003', 'March 29, 2006', 'August 1, 2008',
 'July 22, 2009', 'July 11, 2010', 'November 13, 2012', 'March 20, 2015', 'March 9, 2016']

recent_dates = eclipse_dates[-3:]
print(recent_dates)

"""TASK5"""

students = {
    "John": {
        "age": 18,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    },
    "Emily": {
        "age": 17,
        "grade": "B",
        "subjects": ["History", "Geography", "Art"]
    },
    "Michael": {
        "age": 19,
        "grade": "A+",
        "subjects": ["Physics", "Chemistry", "Biology"]
    }
}

# Accessing student data
print(students["John"]["age"])  # Output: 18
print(students["Emily"]["subjects"])  # Output: ['History', 'Geography', 'Art']
print(students["Michael"]["grade"])  # Output: A+