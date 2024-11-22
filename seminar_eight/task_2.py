import csv
import glob, json

dir ='/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_eight'




def unite_jsons(dir):
    files = glob.glob('/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_eight/*.json')

with (
    open('employees1.json', 'r') as emp_1,
        open('employees2.json', 'r') as emp_2,
            open('employees3.json', 'r') as emp_3,
                open('all_employees.json', 'w') as all_emp
):
    file_1 = json.load(emp_1)
    file_2 = json.load(emp_2)
    file_3 = json.load(emp_3)
    all_employees = []
    all_employees.extend(file_1)
    all_employees.extend(file_2)
    all_employees.extend(file_3)
    json.dump(all_employees, all_emp, indent=2)

if __name__ == "__main__":
    unite_jsons()