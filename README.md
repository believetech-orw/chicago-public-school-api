# Chicago Public Schools Information for Parents

## What is this?
This is a script uses publicly available software - made available by the Chicago Public Schools system - to pull information about public schools in  the city of Chicago.

## How do I use it?
Running this script will generate a CSV file that you can open in any spreadsheet program.  Currently, the file is set to filter for:

- High schools
- With Graduation Stats
- With Graduation Rates above 80%
- With College Enrollment Stats
- With College Enrollment Rates above 75%
- With Swim Teams

In order to run this script, you will need:
- The Python language runtime installed on your computer (http://www.python.org)

To get started:

1. download the script file named: `get_cps_info.py`

2. Open a terminal or command prompt and go to the directory where you placed the file.

3. Run the following command `python get_cps_info.py`, you should see the following output:

```
High Schools: 173
With Grad Rate Data: 136
Grad Rate > 80%: 90
With College Enrollment Data: 89
College Enrollment Rate > 75%: 25
With Swim Program: 13
got here
```
If you see the above output, you should also be able to open a newly-created file named `cps_qualifying_list.csv`.

The CSV file contains a list of schools that match the criteria specified by each filter in the Python script.

Not being from Chicago, we found this very helpful in whittling down the list of CPS high schools that would be a good match for our kid.  If you look at all the data returned, you can tweak the python script to filter on all kinds of information about the schools.

Hope this helps other parents discovering the Chicago Public Schools system