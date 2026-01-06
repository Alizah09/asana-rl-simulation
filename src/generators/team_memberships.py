def generate_team_memberships(conn):
    """
    Insert minimal but realistic team memberships.
    Demonstrates:
    - many-to-many user–team relationship
    - cross-functional collaboration
    """

    memberships = [
        # Engineering
        ("team_eng", "u1"),
        ("team_eng", "u3"),

        # Product
        ("team_prod", "u2"),

        # Marketing
        ("team_mkt", "u4"),

        # Operations
        ("team_ops", "u5"),

        # Cross-team membership (manager in sales ops + eng)
        ("team_sales", "u3"),
    ]

    for team_id, user_id in memberships:
        conn.execute(
            """
            INSERT INTO team_memberships (team_id, user_id, joined_at)
            VALUES (?, ?, datetime('now', '-4 years'))
            """,
            (team_id, user_id),
        )

    conn.commit()
