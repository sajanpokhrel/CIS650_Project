import os
import pandas as pd
import json

pd.set_option('display.max.rows', None)
pd.set_option('display.max.columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

def read_data():
    subfolder_path = "Data"

    Applicant = pd.read_json(os.path.join(subfolder_path, "Applicant.json"))
    Applicant.set_index('ApplicantID', inplace= True)

    Application = pd.read_json(os.path.join(subfolder_path, "Application.json"))
    Application.set_index('ApplicationID', inplace= True)

    JobRequirement = pd.read_json(os.path.join(subfolder_path, "JobRequirement.json"))
    JobRequirement.set_index('RequirementID', inplace= True)
    
    Position = pd.read_json(os.path.join(subfolder_path, "Position.json"))
    Position.set_index('PositionID', inplace= True)

    Qualification = pd.read_json(os.path.join(subfolder_path, "Qualification.json"))
    Qualification.set_index('QualificationID', inplace= True)

    ApplicantQualification = pd.read_json(os.path.join(subfolder_path, "ApplicantQualification.json"))
    ApplicantQualification.set_index(['ApplicantID','QualificationID'], inplace= True)
    
    RequirementQualification = pd.read_json(os.path.join(subfolder_path, "RequirementQualification.json"))
    RequirementQualification.set_index(['RequirementID','QualificationID'], inplace= True)



    return(Applicant, Application, JobRequirement, Position, Qualification, ApplicantQualification, RequirementQualification)

def show_data():
    Applicant, Application, JobRequirement, Position, Qualification, ApplicantQualification, RequirementQualification = read_data()
    
    print("\n========== Applicant Table==========")
    print(Applicant.head())
    print("\nData Types:")
    print(Applicant.dtypes)
    print("_" * 80)

    
    print("\n========== Application Table==========")
    print(Application.head())
    print("\nData Types:")
    print(Application.dtypes)
    print("_" * 80)

    print("\n========== JobRequirement Table==========")
    print(JobRequirement.head())
    print("\nData Types:")
    print(JobRequirement.dtypes)
    print("_" * 80)

    print("\n========== Position Table==========")
    print(Position.head())
    print("\nData Types:")
    print(Position.dtypes)
    print("_" * 80)

    print("\n========== Qualification Table==========")
    print(Qualification.head())
    print("\nData Types:")
    print(Qualification.dtypes)
    print("_" * 80)
    
    print("\n========== ApplicantQualification Table==========")
    print(ApplicantQualification.head())
    print("\nData Types:")
    print(ApplicantQualification.dtypes)
    print("_" * 80)

    print("\n========== RequirementQualification Table==========")
    print(RequirementQualification.head())
    print("\nData Types:")
    print(RequirementQualification.dtypes)
    print("_" * 80)


    print("\n All tables displayed successfully!!")

if __name__ =="__main__":
    show_data()
    



