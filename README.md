# csv-filter-challenge-azra-gallano

## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```
## How-To
Clone this repository and run it in any text-editor that can run Python. Answer the prompts in the command-line in order to test the functionality of the program. If you would like to test a different CSV file than the one provided, please put it in the 'records' folder. 

## Assumptions 
1. The file provided will always be a CSV file
2. CSV file to read exists within a folder the program can easily access- in this case, records folder 
3. CSV file will always contain a header column 
4. CSV file will not contain any empty columns
5. Records must be an exact match to the value provided as input on the filter 
6. The filtered results are returned from the filter_data function, but are printed for visibility 
