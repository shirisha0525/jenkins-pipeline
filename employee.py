# Employee Management Demo Script for Jenkins CI/CD

# Initial employee data
employees = {
    101: {"name": "Arun", "role": "DevOps Engineer", "salary": 6000},
    102: {"name": "Kiran", "role": "Python Developer", "salary": 5000},
    103: {"name": "Meena", "role": "QA Engineer", "salary": 4500}
}

print("===================================")
print("📊 Employee Details (Before Update)")
print("===================================")

def display_employees():
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Role: {details['role']}")
        print(f"Salary: {details['salary']}")
        print("-----------------------------------")

display_employees()

# -------------------------------
# Update employee details
# -------------------------------
print("\n🔄 Updating Employee Details...\n")

# Example updates
employees[102]["salary"] = 5500
employees[103]["role"] = "Senior QA Engineer"

# Adding a new employee
employees[104] = {"name": "Ravi", "role": "Cloud Engineer", "salary": 6500}

print("===================================")
print("📊 Employee Details (After Update)")
print("===================================")

display_employees()

print("✔ Employee update completed successfully for CI/CD pipeline")
