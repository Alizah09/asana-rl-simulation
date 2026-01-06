from utils.db import init_db

from generators.organizations import generate_organization
from generators.teams import generate_teams
from generators.users import generate_users
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.comments import generate_comments
from generators.custom_fields import generate_custom_fields
from generators.tags import generate_tags
from generators.attachments import generate_attachments

DB_PATH = "output/asana_simulation.sqlite"
SCHEMA_PATH = "schema.sql"

def main():
    conn = init_db(DB_PATH, SCHEMA_PATH)

    generate_organization(conn)
    generate_teams(conn)
    generate_users(conn)
    generate_team_memberships(conn)
    generate_projects(conn)
    generate_sections(conn)
    generate_tasks(conn)
    generate_comments(conn)
    generate_custom_fields(conn)
    generate_tags(conn)
    generate_attachments(conn)

    print("✅ Minimal Asana simulation data generated successfully.")
    conn.close()

if __name__ == "__main__":
    main()
