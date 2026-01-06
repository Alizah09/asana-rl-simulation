CREATE TABLE IF NOT EXISTS organizations (
  org_id TEXT PRIMARY KEY,
  name TEXT,
  created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS teams (
  team_id TEXT PRIMARY KEY,
  org_id TEXT,
  name TEXT,
  function TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

CREATE TABLE IF NOT EXISTS users (
  user_id TEXT PRIMARY KEY,
  org_id TEXT,
  full_name TEXT,
  email TEXT,
  role TEXT,
  seniority TEXT,
  region TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

CREATE TABLE IF NOT EXISTS team_memberships (
  team_id TEXT,
  user_id TEXT,
  joined_at TIMESTAMP,
  PRIMARY KEY (team_id, user_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS projects (
  project_id TEXT PRIMARY KEY,
  team_id TEXT,
  name TEXT,
  project_type TEXT,
  status TEXT,
  start_date DATE,
  end_date DATE,
  FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS sections (
  section_id TEXT PRIMARY KEY,
  project_id TEXT,
  name TEXT,
  position INTEGER,
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS tasks (
  task_id TEXT PRIMARY KEY,
  project_id TEXT,
  section_id TEXT,
  parent_task_id TEXT,
  name TEXT,
  description TEXT,
  assignee_id TEXT,
  due_date DATE,
  completed BOOLEAN,
  created_at TIMESTAMP,
  completed_at TIMESTAMP,
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id),
  FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS comments (
  comment_id TEXT PRIMARY KEY,
  task_id TEXT,
  author_id TEXT,
  body TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (author_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS custom_field_definitions (
  field_id TEXT PRIMARY KEY,
  project_id TEXT,
  name TEXT,
  field_type TEXT,
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS custom_field_values (
  task_id TEXT,
  field_id TEXT,
  value TEXT,
  PRIMARY KEY (task_id, field_id),
  FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

CREATE TABLE IF NOT EXISTS tags (
  tag_id TEXT PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS task_tags (
  task_id TEXT,
  tag_id TEXT,
  PRIMARY KEY (task_id, tag_id),
  FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

CREATE TABLE IF NOT EXISTS attachments (
  attachment_id TEXT PRIMARY KEY,
  task_id TEXT,
  file_type TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);
