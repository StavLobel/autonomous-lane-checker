### GitHub Issues Task Management Plan (no Projects)

This plan defines how to manage all epics and tasks with plain GitHub Issues only: labels, milestones, assignees, templates, and simple automation. It replaces any usage of GitHub Projects.

---

### Objectives
- Represent every Epic and Task as a GitHub Issue.
- Use labels for Type and Priority; use Milestones for iterations/releases.
- Keep status simple: Open = in-progress/backlog, Closed = done; optionally a status label.
- Link PRs to issues for auto-close on merge.

---

### Labels (create once and reuse)
- Type: `type:epic`, `type:major`, `type:minor`
- Priority: `priority:P0`, `priority:P1`, `priority:P2`, `priority:P3`
- Status (optional): `status:todo`, `status:in-progress`, `status:in-review`, `status:blocked`, `status:done`
- Epic key (optional): `epic:ALC-EP001` .. `epic:ALC-EP007`

Notes:
- Prefer one Status label at a time if you choose to use them; otherwise rely on Open/Closed.
- Keep Priority mandatory on all issues.

---

### Milestones
- Use Milestones as Iterations/Sprints or Releases (e.g., `Sprint 1`, `v0.1`).
- Assign each task to a Milestone during planning; epics may span multiple Milestones.

---

### Issue title conventions
- Epic: `[ALC-EP00X] <Concise epic name>`
- Task: `[ALC-EP00X-MYY] <Concise task name>`

This keeps IDs from `docs/TASKS.md` visible and searchable.

---

### Issue body templates (copy/paste)

Epic template:
```
Summary
-------
<one-paragraph epic goal>

Scope
-----
- <bullet points>

Acceptance
----------
- [ ] Outcome 1
- [ ] Outcome 2

Links
-----
- Child tasks: #<issue>, #<issue>
```

Task template:
```
Context
-------
<why this is needed>

Plan
----
- [ ] Step 1
- [ ] Step 2

Acceptance
----------
- [ ] Checks pass and meets criteria in SRD/STP

Links
-----
- Epic: #<epic-issue>
```

---

### Workflow
1) Create issues for all epics/tasks from `docs/TASKS.md` using the naming and labels above.
2) Set Assignee(s), Milestone, Priority.
3) Optionally add a Status label; otherwise track progress by Open/Closed.
4) Link PRs to issues and use closing keywords in PR descriptions (e.g., `Fixes #123`).
5) Close issues when acceptance is met and PRs are merged.

Saved searches (examples):
- P0 open: `is:issue is:open label:"priority:P0"`
- My tasks this sprint: `is:issue is:open assignee:@me milestone:"Sprint 1"`
- Blocked: `is:issue is:open label:"status:blocked"`

---

### Seeding from `docs/TASKS.md`
Process:
1) Create one issue per Epic (`type:epic`, `priority:<Px>`, optional `epic:ALC-EP00X`).
2) Create one issue per Major/Minor task with title `[ID] Name`, labels `type:<major|minor>`, `priority:<Px>`, and optional `epic:ALC-EP00X`.
3) In each Epic issue, maintain a task list linking child issues: `- [ ] #123`.
4) Assign Milestones and Assignees.

---

### Cadence
- Daily: Update issue descriptions/checklists and labels as progress changes.
- Weekly: Triage new issues, adjust Priority, plan next Milestone.
- At merge: Ensure PR links an issue; let merge auto-close.

---

### Lightweight automation (optional)
- Labeler action to set `type:*` or `priority:*` based on title prefixes like `[ALC-EP...]`.
- Stale bot (optional) for long-idle `status:blocked` issues.

---

### Minimal status without Projects
- If avoiding status labels entirely: use Open (active/backlog) and Closed (done) plus Milestones for timeboxing.
- If using status labels: move items by changing the single status label.



