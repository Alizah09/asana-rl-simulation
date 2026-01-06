def generate_attachments(conn):
    """
    Insert minimal attachments linked to tasks.
    Demonstrates sparse attachment usage.
    """

    attachments = [
        ("att_1", "t1", "pdf"),
        ("att_2", "t2", "png"),
    ]

    for attachment_id, task_id, file_type in attachments:
        conn.execute(
            """
            INSERT INTO attachments (attachment_id, task_id, file_type, created_at)
            VALUES (?, ?, ?, datetime('now', '-3 days'))
            """,
            (attachment_id, task_id, file_type)
        )

    conn.commit()
