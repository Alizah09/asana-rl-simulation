def generate_comments(conn):
    conn.execute("""
        INSERT INTO comments (comment_id, task_id, author_id, body, created_at)
        VALUES (?, ?, ?, ?, datetime('now', '-5 days'))
    """, (
        "c1",
        "t2",
        "u3",
        "Fix deployed, monitoring retries."
    ))

    conn.commit()
