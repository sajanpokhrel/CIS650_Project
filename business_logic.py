import pprint


def view_applicants(Applicant):
    print("\n=== APPLICANT TABLE ===")
    pprint.pprint(Applicant)
    input("\nPress Enter to continue...")

def view_applications(Application):
    print("\n=== APPLICATION TABLE ===")
    pprint.pprint(Application)
    input("\nPress Enter to continue...")

def view_positions(Position):
    print("\n=== POSITION TABLE ===")
    pprint.pprint(Position)
    input("\nPress Enter to continue...")

def view_qualifications(Qualification):
    print("\n=== QUALIFICATION TABLE ===")
    pprint.pprint(Qualification)
    input("\nPress Enter to continue...")

def view_applicant_qualifications(ApplicantQualification):
    print("\n=== APPLICANT QUALIFICATION TABLE ===")
    pprint.pprint(ApplicantQualification.reset_index())
    input("\nPress Enter to continue...")

def view_job_requirements(JobRequirement):
    print("\n=== JOB REQUIREMENT TABLE ===")
    pprint.pprint(JobRequirement)
    input("\nPress Enter to continue...")

def view_requirement_qualifications(RequirementQualification):
    print("\n=== REQUIREMENT QUALIFICATION TABLE ===")
    pprint.pprint(RequirementQualification)
    input("\nPress Enter to continue...")

def get_position_id(Position):
    print("\nAvailable positions (ID and JobTitle):")
    pprint.pprint(Position[["JobTitle"]])

    position_ids = Position.index.tolist()

    while True:
        pos_id = input("\nSelect a position by its ID (e.g., P001), or 0 to cancel: ").strip()
        if pos_id == "0":
            return None
        if pos_id not in position_ids:
            print("Invalid PositionID, please try again.")
        else:
            print(f"You selected position {pos_id} - {Position.loc[pos_id, 'JobTitle']}")
            return pos_id

def view_applications_by_position(Application, Position, Applicant):
    print("\n=== APPLICATIONS BY POSITION ===")
    for app_id, row in Application.iterrows():
        pos_id = row["PositionID"]
        applicant_id = row["ApplicantID"]

        if pos_id in Position.index:
            pos_title = Position.loc[pos_id, "JobTitle"]
        else:
            pos_title = "(Unknown Position)"

        if applicant_id in Applicant.index:
            applicant_name = f"{Applicant.loc[applicant_id, 'FirstName']} {Applicant.loc[applicant_id, 'LastName']}"
        else:
            applicant_name = "(Unknown Applicant)"

        is_qual = row.get("IsQualified", None)
        if is_qual is True:
            qual_text = "Yes"
        elif is_qual is False:
            qual_text = "No"
        else:
            qual_text = "Not decided"

        print(f"\nApplicationID: {app_id}")
        print(f"  Position   : {pos_id} - {pos_title}")
        print(f"  Applicant  : {applicant_id} - {applicant_name}")
        print(f"  Qualified? : {qual_text}")

    input("\n Press Enter to continue...")

def show_requirements_and_qualifications(
    position_id,
    applicant_id,
    Applicant,
    JobRequirement,
    Qualification,
    ApplicantQualification,
):

    print("\n================ APPLICANT INFO ================")
    if applicant_id in Applicant.index:
        a = Applicant.loc[applicant_id]
        full_name = f"{a.get('FirstName', '')} {a.get('LastName', '')}".strip()
        print(f"ApplicantID : {applicant_id}")
        print(f"Name        : {full_name}")
        if "Phone" in a:
            print(f"Phone       : {a['Phone']}")
        if "Email" in a:
            print(f"Email       : {a['Email']}")
    else:
        print(f"ApplicantID : {applicant_id}")
        print("Name        : (Unknown Applicant)")

    print("\n------------- Applicant's Qualifications -------------")
    aq = ApplicantQualification.reset_index() 
    aq_rows = aq[aq["ApplicantID"] == applicant_id]

    if aq_rows.empty:
        print("  (No qualifications found for this applicant.)")
    else:
        for _, aqr in aq_rows.iterrows():
            qid = aqr["QualificationID"]
            if qid in Qualification.index:
                q_row = Qualification.loc[qid]
                q_desc = q_row.get("QualificationDescription", "")
                q_type = q_row.get("QualificationType", "")
                print(f"  - {qid}: {q_desc} [{q_type}]")
            else:
                print(f"  - {qid}: (Unknown qualification)")

    print("\n------------- Job Requirements for this Position -------------")
    req_for_pos = JobRequirement[JobRequirement["PositionID"] == position_id]

    if req_for_pos.empty:
        print("  (No requirements found for this position.)")
    else:
        for req_id, row in req_for_pos.iterrows():
            r_type = row.get("RequirementType", "")
            r_desc = row.get("Requirementdescription", "")
            print(f"RequirementID : {req_id}")
            print(f"  Type        : {r_type}")
            print(f"  Description : {r_desc}")
            print("")

def manual_screening(Applicant,
                     Application,
                     JobRequirement,
                     Position,
                     Qualification,
                     ApplicantQualification):

    pos_id = get_position_id(Position)
    if pos_id is None:
        print("Manual screening cancelled.")
        return

    print(f"\n=== MANUAL SCREENING FOR POSITION {pos_id} ===")

    apps_for_pos = Application[Application["PositionID"] == pos_id]

    if apps_for_pos.empty:
        print("No applications found for this position.")
        return

    pending_apps = apps_for_pos[(apps_for_pos["IsQualified"].isna()) |
                                (apps_for_pos["IsQualified"] != "Yes")]

    if pending_apps.empty:
        print("No pending applicants. All applicants for this position are already qualified.")
        return

    print("\nApplicants who applied for this position (pending or not qualified):")
    available_applicant_ids = []

    for app_id, row in pending_apps.iterrows():
        applicant_id = row["ApplicantID"]
        if applicant_id in Applicant.index:
            a = Applicant.loc[applicant_id]
            name = f"{a['FirstName']} {a['LastName']}"
        else:
            name = "(Unknown Applicant)"

        is_qual = row.get("IsQualified", None)
        if is_qual is "Yes":
            qual_text = "Yes"
        elif is_qual is "No":
            qual_text = "No"
        else:
            qual_text = "Not decided"

        print(f"- ApplicantID: {applicant_id} | Name: {name} | ApplicationID: {app_id} | Qualified? {qual_text}")

        if applicant_id not in available_applicant_ids:
            available_applicant_ids.append(applicant_id)

    if not available_applicant_ids:
        print("\nNo available applicants to review.")
        return

    while True:
        selected_id = input(
            "\nType an ApplicantID from the list above to review (or 0 to cancel): "
        ).strip()
        if selected_id == "0":
            print("Manual screening cancelled.")
            return
        if selected_id not in available_applicant_ids:
            print("Invalid ApplicantID. Please choose from the list shown.")
        else:
            break

    selected_row = pending_apps[pending_apps["ApplicantID"] == selected_id]
    if selected_row.empty:
        print("No matching application found for that applicant and position.")
        return

    app_id = selected_row.index[0]

    show_requirements_and_qualifications(
        pos_id,
        selected_id,
        Applicant,
        JobRequirement,
        Qualification,
        ApplicantQualification,
    )

    while True:
        decision = input("\nIs this applicant qualified? (yes/no): ").strip().lower()
        if decision in ("yes", "y"):
            Application.at[app_id, "IsQualified"] = True
            print("\nResult: Qualified: Yes. (Will not show again for this position.)")
            break
        elif decision in ("no", "n"):
            Application.at[app_id, "IsQualified"] = False
            print("\nResult: Qualified: No. (They may appear again if you run screening again.)")
            break
        else:
            print("Please type 'yes' or 'no'.")
