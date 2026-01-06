def generate_projects(conn):
    projects = [
        ("proj_1", "team_eng", "Q3 Payments Sprint", "engineering_sprint", "active"),
        ("proj_2", "team_mkt", "Website Redesign Campaign", "marketing_campaign", "completed"),
        ("proj_3", "team_ops", "Hiring Pipeline", "operations_workflow", "archived"),
    ]

    for pid, team_id, name, ptype, status in projects:
        conn.execute("""
            INSERT INTO projects (project_id, team_id, name, project_type, status, start_date)
            VALUES (?, ?, ?, ?, ?, date('now', '-90 days'))
        """, (pid, team_id, name, ptype, status))

    conn.commit()
