from read_data import read_data, save_application
from business_logic import (
    view_applicants,
    view_applications,
    view_positions,
    view_qualifications,
    view_applicant_qualifications,
    view_job_requirements,
    view_requirement_qualifications,
    view_applications_by_position,
    manual_screening,
)


def main():
    print("Welcome to the We Build Stuff HR System")
    print("User Story: Manual screening with manager Yes/No decision\n")

    (
        Applicant,
        Application,
        JobRequirement,
        Position,
        Qualification,
        ApplicantQualification,
        RequirementQualification,
    ) = read_data()

    while True:
        print("""
==================== HRS MENU ====================
1. View Applicants
2. View Applications
3. View Positions
4. View Qualifications
5. View ApplicantQualification
6. View Job Requirements
7. View RequirementQualification
8. View Applications by Position
9. Manual Screening for a Position
0. Exit
=================================================
""")

        choice = input("Enter your choice (0-9): ").strip()

        if choice == "1":
            view_applicants(Applicant)

        elif choice == "2":
            view_applications(Application)

        elif choice == "3":
            view_positions(Position)

        elif choice == "4":
            view_qualifications(Qualification)

        elif choice == "5":
            view_applicant_qualifications(ApplicantQualification)

        elif choice == "6":
            view_job_requirements(JobRequirement)

        elif choice == "7":
            view_requirement_qualifications(RequirementQualification)

        elif choice == "8":
            view_applications_by_position(Application, Position, Applicant)

        elif choice == "9":
            # Manual screening (position -> applicant -> yes/no)
            manual_screening(
                Applicant,
                Application,
                JobRequirement,
                Position,
                Qualification,
                ApplicantQualification,
            )
            # Save Application changes (IsQualified) to JSON
            save_application(Application)

        elif choice == "0":
            print("Exiting HR System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 9.")


if __name__ == "__main__":
    main()
