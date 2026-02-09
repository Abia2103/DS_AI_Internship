#Task 1: The Personal Logger (Appending & Modes)
with open("logs",'a') as file:
    log = input("Enter your name and daily goal: ")
    file.write("\n")
    file.write(log)

    
#Task 2: The CSV Student List (Data Ingestion)
import csv
with open("students.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2]=="Pass":
            print(row)
    
    
    
#Task 3: The "Safe Opener" (Error Handling)
file = input("Enter file: ")
try:
    with open(file) as f:
        r = f.read()
        print(r)
except:
    print("Oops! That file doesn't exist yet")