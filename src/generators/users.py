def generate_users(conn):
    users = [
        ("u1", "Alice Johnson", "IC", "Senior", "North America"),
        ("u2", "Bob Smith", "IC", "Mid", "Europe"),
        ("u3", "Carlos Mehta", "Manager", "Senior", "India"),
        ("u4", "Diana Lee", "IC", "Junior", "North America"),
        ("u5", "Evan Brown", "IC", "Mid", "Europe"),
    ]

    for uid, name, role, seniority, region in users:
        email = name.lower().replace(" ", ".") + "@acme.com"
        conn.execute("""
            INSERT INTO users (user_id, org_id, full_name, email, role, seniority, region, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now', '-5 years'))
        """, (uid, "org_1", name, email, role, seniority, region))

    conn.commit()
