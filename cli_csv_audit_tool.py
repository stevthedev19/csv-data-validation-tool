"""
CSV Data Validation Tool

Validates structured CSV files against required fields
and parameter constraints using defensive programming.
"""

import csv

required_fields = ["sample_id", "concentration"]


def required_field_check(fields, req_fields):

    missing_para = []

    for para in req_fields:
        if not para in fields:
            missing_para.append(para)

    if missing_para:
        print(f"Required parameters missing: {missing_para}")
        exit()

def required_field_value_check(row,req_fields):


    for r in req_fields:

        v = row.get(r)
        if v == None:
            return False
        v = v.strip().capitalize()      #checks for empty values for required parameters
        if not v or v== "Na":
            return False

    return True


def parameter_check(row):

    for p,v in row.items():

        if p == "concentration":  #required row
            try:
                v = float(v)
            except ValueError:
                return False
            if v < 0:
                return False


        elif p == "temp":

            v = v.strip().capitalize()
            if v == "" or v == "Na":
                continue

            else:
                try:
                    v = float(v)
                except ValueError:
                    return False
                if v > 30 or v < 20:
                    return False



    return True




def main():

    flagged = []
    errors = 0

    with open("file.csv","r") as file:
        csv_file = csv.DictReader(file)
        required_field_check(csv_file.fieldnames, required_fields)

        for row in csv_file:
            if required_field_value_check(row,required_fields) == False or parameter_check(row) == False:
                errors += 1

    print(f"Errors present: {errors}")

main()