import csv
import os
import datetime

min_year = 1000;
max_year = int(datetime.datetime.now().strftime("%Y"));
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = ""
filter_type = ""
filter_input = ""
data = []

def set_file():
    global filename
    
    filename = str(input("Enter in name of file to be read:\n"))
    
def read_file():
    global data
    path = os.path.join(ROOT_DIR, "records", filename)
    
    try: 
        with open(path, "r") as file:
            data_list = csv.reader(file, delimiter=",")
            data = list(data_list)[1:]
    except IOError:
        print("Error: File does not exist. Please try again.")
        set_file();
    
def set_filter_type():
    global filter_type
    
    filter_type = str(input("Enter in filter method (first_name, last_name, birth_year):\n")).lower()
    
    while filter_type != "first_name" and filter_type != "last_name" and filter_type != "birth_year":
        print("Not a valid filter option. Please try again.")
        filter_type = str(input("Enter in filter method:\n")).lower()
    
def set_filter_input():
    global filter_input
    
    if filter_type == "first_name" or filter_type == "last_name":
        filter_input = str(input("Enter in the exact name you wish to filter on:\n"))
    elif filter_type == "birth_year":
        set_birth_date()

def set_birth_date():
    global filter_input
    
    filter_input = int(input("Enter in the year you wish to filter on: \n"))
    while filter_input > max_year or filter_input < min_year:
        print("Not a valid year. Please try again.")
        filter_input = int(input("Enter in the year you wish to filter on: \n"))

def filter_data():
    global data
    
    if filter_type == "first_name":
        data = list(filter(lambda x: x[0] == filter_input, data))
    elif filter_type == "last_name":
        data = list(filter(lambda x: x[1] == filter_input, data))
    elif filter_type == "birth_year":
        data = list(filter(lambda x: x[2][0:4] == str(filter_input), data))
    
    if not data:
        return ("No matching records found")
    else:
        return data

def init():
    set_file()
    read_file()
    set_filter_type()
    set_filter_input()
    print(filter_data())
    
init()