import json

with open("Data/Applicant.json") as f:
    applicant = json.load(f)
with open("Data/Application.json") as f:
    application = json.load(f)
with open("Data/JobRequirement.json") as f:
    jobrequirement = json.load(f)
with open("Data/Position.json") as f:
    position = json.load(f)
with open("Data/Qualification.json") as f:
    qualification = json.load(f) 

merged_data = {
    "Applicant" : applicant,
    "Application": application,
    "JobRequirement": jobrequirement,
    "Position": position,
    "Qualification" : qualification,
    }

with open("masterdata.json", "w") as f:
    json.dump(merged_data, f, indent = 4)

print("Merged into masterdata.json successfully!")