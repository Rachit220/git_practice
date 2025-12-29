import json
with open("data.json", "r") as file:
    data = json.load(file)

print("Company Name:", data["company"]["name"])

print("\nEmployees:")
for dept in data["company"]["departments"]:
    for emp in dept["employees"]:
        print(f"- {emp['name']} ({dept['name']})")
for dept in data["company"]["departments"]:
    for emp in dept["employees"]:
        if emp["name"] == "Rachit":
            emp["salary"] = int(emp["salary"] * 1.10)
new_employee = {
    "id": 103,
    "name": "Kunal",
    "skills": ["JavaScript", "React"],
    "salary": 50000
}

for dept in data["company"]["departments"]:
    if dept["name"] == "Engineering":
        dept["employees"].append(new_employee)
with open("data_updated.json", "w") as file:
    json.dump(data, file, indent=4)

print("\n JSON file updated successfully!")
