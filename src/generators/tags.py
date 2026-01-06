def generate_tags(conn):
    """
    Insert minimal but realistic tags and task-tag relationships.
    """

    # Insert tags
    tags = [
        ("tag_blocked", "blocked"),
        ("tag_urgent", "urgent"),
        ("tag_customer", "customer-facing"),
    ]

    for tag_id, name in tags:
        conn.execute(
            """
            INSERT INTO tags (tag_id, name)
            VALUES (?, ?)
            """,
            (tag_id, name)
        )

    # Assign tags to tasks (sparse, realistic)
    task_tags = [
        ("t1", "tag_urgent"),
        ("t2", "tag_blocked"),
    ]

    for task_id, tag_id in task_tags:
        conn.execute(
            """
            INSERT INTO task_tags (task_id, tag_id)
            VALUES (?, ?)
            """,
            (task_id, tag_id)
        )

    conn.commit()
