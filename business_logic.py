import pprint



def view_applicants(Applicant):
    """Show all applicants."""
    print("\n=== APPLICANT TABLE ===")
    pprint.pprint(Applicant)
    input("\nPress Enter to continue...")


def view_positions(Position):
    """Show all positions."""
    print("\n=== POSITION TABLE ===")
    pprint.pprint(Position)
    input("\nPress Enter to continue...")


def view_applications(Application):
    """Show all applications."""
    print("\n=== APPLICATION TABLE ===")
    pprint.pprint(Application)
    input("\nPress Enter to continue...")


def view_job_requirements(JobRequirement):
    """Show all job requirements."""
    print("\n=== JOB REQUIREMENT TABLE ===")
    pprint.pprint(JobRequirement)
    input("\nPress Enter to continue...")


def view_qualifications(Qualification):
    """Show all qualifications."""
    print("\n=== QUALIFICATION TABLE ===")
    pprint.pprint(Qualification)
    input("\nPress Enter to continue...")


def view_applicant_qualifications(ApplicantQualification):
    """Show the ApplicantQualification table."""
    print("\n=== APPLICANT QUALIFICATION TABLE ===")
    pprint.pprint(ApplicantQualification)
    input("\nPress Enter to continue...")


def view_requirement_qualifications(RequirementQualification):
    """Show the RequirementQualification table."""
    print("\n=== REQUIREMENT QUALIFICATION TABLE ===")
    pprint.pprint(RequirementQualification)
    input("\nPress Enter to continue...")



def get_position_id(Position):
    """Let the user choose a PositionID (e.g., P001)."""
    print("\nAvailable positions (ID and JobTitle):")
    
    pprint.pprint(Position[["JobTitle"]])

    position_ids = Position.index.tolist()

    while True:
        pos_id = input("\nSelect a position by its ID (e.g., P001): ").strip()
        if pos_id not in position_ids:
            print("Invalid PositionID, please try again.")
        else:
            print(f"You selected position {pos_id} - {Position.loc[pos_id, 'JobTitle']}")
            return pos_id


def get_applicant_id(Applicant):
    """Let the user choose an ApplicantID (if needed)."""
    print("\nAvailable applicants (ID and name):")
    names = Applicant[["FirstName", "LastName"]]
    pprint.pprint(names)

    applicant_ids = Applicant.index.tolist()

    while True:
        a_id = input("\nSelect an Applicant ID (e.g., A001): ").strip()
        if a_id not in applicant_ids:
            print("Invalid ApplicantID, please try again.")
        else:
            full_name = f"{Applicant.loc[a_id, 'FirstName']} {Applicant.loc[a_id, 'LastName']}"
            print(f"You selected applicant {a_id} - {full_name}")
            return a_id



def view_requirements_for_position(JobRequirement,
                                   RequirementQualification,
                                   Qualification,
                                   position_id):
    """
    Show all job requirements and linked qualifications
    for one position.
    """
    print(f"\n=== REQUIREMENTS FOR POSITION {position_id} ===")

    
    req_for_pos = JobRequirement[JobRequirement["PositionID"] == position_id]

    if req_for_pos.empty:
        print("No requirements found for this position.")
        return

   
    rq = RequirementQualification.reset_index()  

    for req_id, row in req_for_pos.iterrows():
        print(f"\nRequirementID: {req_id}")
        print(f"  RequirementType       : {row['RequirementType']}")
        print(f"  Requirementdescription: {row['Requirementdescription']}")

        
        rq_rows = rq[rq["RequirementID"] == req_id]

        if rq_rows.empty:
            print("  No linked qualifications.")
        else:
            print("  Linked qualifications:")
            for _, rq_row in rq_rows.iterrows():
                qid = rq_row["QualificationID"]
                is_min = rq_row["IsMinimumRequired"]
                q_desc = Qualification.loc[qid, "QualificationDescription"]
                q_type = Qualification.loc[qid, "QualificationType"]
                min_tag = " (MINIMUM)" if is_min else ""
                print(f"    - {qid}: {q_desc} [{q_type}]{min_tag}")




def view_applicants_and_qualifications(Applicant,
                                       ApplicantQualification,
                                       Qualification):
    """
    Show each applicant with all their qualifications.
    """
    print("\n=== APPLICANTS AND THEIR QUALIFICATIONS ===")

    
    aq = ApplicantQualification.reset_index() 

    for applicant_id, a_row in Applicant.iterrows():
        print(f"\nApplicantID: {applicant_id}")
        print(f"  Name : {a_row['FirstName']} {a_row['LastName']}")
        print(f"  Email: {a_row['Email']}")

        aq_rows = aq[aq["ApplicantID"] == applicant_id]

        if aq_rows.empty:
            print("  Qualifications: None")
        else:
            print("  Qualifications:")
            for _, aq_row in aq_rows.iterrows():
                qid = aq_row["QualificationID"]
                q_desc = Qualification.loc[qid, "QualificationDescription"]
                q_type = Qualification.loc[qid, "QualificationType"]
                print(f"    - {qid}: {q_desc} [{q_type}]")

    input("\nPress Enter to continue...")




def screen_applicants_for_position(position_id,
                                   Applicant,
                                   Application,
                                   JobRequirement,
                                   Qualification,
                                   ApplicantQualification,
                                   RequirementQualification):
    """
    Implements the user story:

    As an HR administrator, I want to automatically screen out the candidates
    who lack minimum qualifications so that Seth and managers only review
    qualified candidates.
    """

    print(f"\n=== SCREENING APPLICANTS FOR POSITION {position_id} ===")

    # 1. Get all job requirements for this position
    req_for_pos = JobRequirement[JobRequirement["PositionID"] == position_id]

    if req_for_pos.empty:
        print("No job requirements found for this position.")
        return

    # 2. Collect all minimum qualification IDs (IsMinimumRequired = True)
    rq = RequirementQualification.reset_index()
    min_qual_ids = set()

    for req_id in req_for_pos.index:
        rows = rq[(rq["RequirementID"] == req_id) &
                  (rq["IsMinimumRequired"] == True)]
        for _, r in rows.iterrows():
            min_qual_ids.add(r["QualificationID"])

    if not min_qual_ids:
        print("No minimum qualifications defined. Cannot screen automatically.")
        return

    print("\nMinimum qualifications required (must have ALL):")
    for qid in min_qual_ids:
        q_desc = Qualification.loc[qid, "QualificationDescription"]
        q_type = Qualification.loc[qid, "QualificationType"]
        print(f"  - {qid}: {q_desc} [{q_type}]")

    # 3. Find all applicants who applied to this position (from Application table)
    apps_for_pos = Application[Application["PositionID"] == position_id]

    if apps_for_pos.empty:
        print("\nNo applications found for this position.")
        return

    applicant_ids = apps_for_pos["ApplicantID"].unique()

    # 4. For each applicant, check if they have ALL min qualifications
    aq = ApplicantQualification.reset_index()  
    qualified_applicants = []

    for a_id in applicant_ids:
        a_rows = aq[aq["ApplicantID"] == a_id]
        applicant_qids = set(a_rows["QualificationID"])

        if min_qual_ids.issubset(applicant_qids):
            qualified_applicants.append(a_id)

    
    print("\n=== QUALIFIED APPLICANTS ===")
    if not qualified_applicants:
        print("No applicants meet all minimum qualifications.")
        return

    for a_id in qualified_applicants:
        a = Applicant.loc[a_id]
        print(f"\nApplicantID: {a_id}")
        print(f"  Name : {a['FirstName']} {a['LastName']}")
        print(f"  Email: {a['Email']}")

    print("\nThese are the applicants Seth and the managers should review.")
