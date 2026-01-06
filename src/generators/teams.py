def generate_teams(conn):
    teams = [
        ("team_eng", "org_1", "Payments Platform", "Engineering"),
        ("team_prod", "org_1", "Core Product", "Product"),
        ("team_mkt", "org_1", "Growth Marketing", "Marketing"),
        ("team_ops", "org_1", "Business Operations", "Operations"),
        ("team_sales", "org_1", "Sales Ops – EMEA", "Sales Ops"),
    ]

    for team in teams:
        conn.execute("""
            INSERT INTO teams (team_id, org_id, name, function, created_at)
            VALUES (?, ?, ?, ?, datetime('now', '-6 years'))
        """, team)

    conn.commit()
