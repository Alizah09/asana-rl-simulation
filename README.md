# Asana RL Simulation

## Overview
This repository contains a high-fidelity simulated Asana workspace designed for evaluating and fine-tuning reinforcement learning (RL) agents on enterprise project management workflows.

The simulation emphasizes realistic data behavior rather than scale, modeling incomplete information, uneven activity, task hierarchies, and evolving workflows commonly observed in real organizations.

---

## Simulation Context
The simulated workspace represents a late-stage B2B SaaS company (~7,500 employees) using Asana across multiple functions:
- Engineering
- Product Management
- Marketing
- Operations
- Sales Operations

The simulation spans a six-month activity window and intentionally includes:
- Active, completed, and archived projects
- Parent tasks and subtasks
- Unassigned and overdue tasks
- Sparse comments, tags, attachments, and custom fields
- Cross-functional team memberships

This design avoids clean or uniform synthetic data to prevent shortcut learning by AI agents.

---

## Project Structure
```text
asana-rl-simulation/
├── schema.sql                  # SQLite schema definition
├── src/
│   ├── main.py                 # Entry point
│   ├── generators/             # Seed data generators (per entity)
│   └── utils/                  # Database and helper utilities
└── output/
    └── asana_simulation.sqlite # Generated SQLite database
