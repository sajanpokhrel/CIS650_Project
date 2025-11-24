from read_data import read_data
from business_logic import (
    view_applicants,
    view_positions,
    view_applications,
    view_job_requirements,
    view_qualifications,
    view_applicant_qualifications,
    view_requirement_qualifications,
    get_position_id,
    view_requirements_for_position,
    view_applicants_and_qualifications,
    screen_applicants_for_position,
)


def main():
    print("Welcome to the We Build Stuff HR Screening System")
    print("User Story 5: Automatically screen out unqualified applicants\n")

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
================ HRS MENU ================
1. View Applicants
2. View Positions
3. View Applications
4. View Job Requirements
5. View Qualifications
6. View ApplicantQualification table
7. View RequirementQualification table
8. View Requirements for a Position
9. View Applicants & Their Qualifications
10. Screen Applicants for a Position
0. Exit
==========================================
""")

        choice = input("Enter your choice (0–10): ").strip()

        if choice == "1":
            view_applicants(Applicant)

        elif choice == "2":
            view_positions(Position)

        elif choice == "3":
            view_applications(Application)

        elif choice == "4":
            view_job_requirements(JobRequirement)

        elif choice == "5":
            view_qualifications(Qualification)

        elif choice == "6":
            view_applicant_qualifications(ApplicantQualification)

        elif choice == "7":
            view_requirement_qualifications(RequirementQualification)

        elif choice == "8":
            # Pick a position, then show its requirements + linked qualifications
            pos_id = get_position_id(Position)
            view_requirements_for_position(
                JobRequirement,
                RequirementQualification,
                Qualification,
                pos_id,
            )

        elif choice == "9":
            # Show each applicant + their qualifications
            view_applicants_and_qualifications(
                Applicant,
                ApplicantQualification,
                Qualification,
            )

        elif choice == "10":
            # Main user story: automatic screening by minimum qualifications
            pos_id = get_position_id(Position)
            screen_applicants_for_position(
                pos_id,
                Applicant,
                Application,
                JobRequirement,
                Qualification,
                ApplicantQualification,
                RequirementQualification,
            )

        elif choice == "0":
            print("Exiting HR Screening System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 10.")


if __name__ == "__main__":
    main()
