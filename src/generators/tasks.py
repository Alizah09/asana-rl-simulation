def generate_tasks(conn):
    tasks = [
        ("t1", "proj_1", "sec_1", None, "Payment API refactor", "Refactor legacy payment service", "u1", "2026-01-10", 0),
        ("t2", "proj_1", "sec_2", None, "Fix webhook retries", None, "u2", "2026-01-05", 1),
        ("t3", "proj_1", "sec_2", "t1", "Update unit tests", None, None, None, 0),
    ]

    for task in tasks:
        conn.execute("""
            INSERT INTO tasks
            (task_id, project_id, section_id, parent_task_id, name, description, assignee_id, due_date, completed, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now', '-14 days'))
        """, task)

    conn.commit()
