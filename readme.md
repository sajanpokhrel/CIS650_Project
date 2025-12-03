# Overview
The purpose of this document is to make a Human Resource Screening process. This helps HR administrators to automatically filter applicants before they are reviewed by hiring managers.

# Source
The business example for this exercise was found in:

Powell, A., & Barber, C. S. (2021). Teaching Case: Integrating Systems at We Build Stuff: Analysis and Design Case. *Journal of Information Systems Education*, 32(4), 244–248.

# Contents
Based on an analysis of the requirements, we can work with seven data files to address this user story:

- **Position** – PositionID, JobTitle, JobDescription  
- **Applicant** – ApplicantID, FirstName, LastName, Email  
- **Application** – ApplicationID, SubmissionDate, ApplicationStatus, ApplicantID, PositionID  
- **Job Requirement** – RequirementID, RequirementType, RequirementDescription  
- **Qualification** – QualificationID, QualificationDescription, QualificationType  
- **Applicant Qualification** – ApplicantID, QualificationID  
- **Requirement Qualification** – RequirementID, QualificationID, IsMinimumRequired  

# User story
As an HR administrator, I want to automatically screen out the candidates who lack minimum qualifications so that Seth and managers only review qualified candidates.

# Data model
**Position** – PositionID, JobTitle, JobDescription,**Applicant** – ApplicantID, FirstName, LastName, Email, **Application** – ApplicationID, SubmissionDate, ApplicationStatus, ApplicantID, PositionID, **Job Requirement** – RequirementID, RequirementType, RequirementDescription, **Qualification** – QualificationID, QualificationDescription, QualificationType,
**Applicant Qualification** – ApplicantID, QualificationID,**Requirement Qualification** – RequirementID, QualificationID, IsMinimumRequired  

# Use case analysis

| Use case component | Use case details |
|--------------------|-----------------|
| **User story** | As an HR administrator, I want to automatically screen out the candidates who lack minimum qualifications so that Seth and managers only review qualified candidates. |
| **Use case title** | HR Screening Process |
| **Primary actor** | HR Administrator |
| **Secondary actor** | Hiring Managers (Seth) |
| **Goal** | Screen all the applicants who qualify for a job position |
| **Scope** | Human Resource System |
| **Preconditions** | Applicant data is available |
| | Application data is available |
| | Position data is available |
| | Qualification data is available |
| | Applicant Qualification data is available |
| | Requirement Qualification data is available |
| **Post condition** | Only qualified candidates are identified |
| | Unqualified candidates are filtered out |
| | All results are displayed to the HR administrator |
| **Main success scenario** | 1. HR administrator selects a job position |
| | 2. The system lists all minimum requirements required for that position |
| | 3. The system lists all applicants applying for that position |
| | 4. HR administrators chooses who are qualified |
| | 5. HR administrator forwards the qualified applicants to Seth and hiring managers |
| **Extensions** | 1. No applicants have applied to that position |
| | 2. Position has no minimum qualification defined |
| | 3. Applicant has partial qualifications | |
| | 4. Minimum qualifications need to be updated |
|---|---|
