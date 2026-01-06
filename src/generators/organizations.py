def generate_organization(conn):
    conn.execute("""
        INSERT INTO organizations (org_id, name, created_at)
        VALUES (?, ?, datetime('now', '-9 years'))
    """, (
        "org_1",
        "Acme Analytics Inc"
    ))
    conn.commit()
