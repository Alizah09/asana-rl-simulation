def generate_sections(conn):
    sections = [
        ("sec_1", "proj_1", "To Do", 1),
        ("sec_2", "proj_1", "In Progress", 2),
        ("sec_3", "proj_1", "Done", 3),
    ]

    for sid, pid, name, pos in sections:
        conn.execute("""
            INSERT INTO sections (section_id, project_id, name, position)
            VALUES (?, ?, ?, ?)
        """, (sid, pid, name, pos))

    conn.commit()
