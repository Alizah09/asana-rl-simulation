def generate_custom_fields(conn):
    """
    Insert minimal custom field definitions and values.
    Kept intentionally small for seed data.
    """

    # Custom field definitions
    conn.execute("""
        INSERT INTO custom_field_definitions (field_id, project_id, name, field_type)
        VALUES (?, ?, ?, ?)
    """, ("cf_priority", "proj_1", "Priority", "enum"))

    # Custom field value
    conn.execute("""
        INSERT INTO custom_field_values (task_id, field_id, value)
        VALUES (?, ?, ?)
    """, ("t1", "cf_priority", "High"))

    conn.commit()
