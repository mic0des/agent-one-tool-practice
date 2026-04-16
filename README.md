In this task, you'll build your first real tool for an AI agent: `get_ticket`.

You'll implement a tool that fetches a ticket by ID from a GitHub Issues database and returns structured JSON.

👩‍💻 Workflow at a glance
1. Set up your environment
2. Implement `get_ticket`
3. Test the tool
4. Create one additional tool
5. Check your work
6. Submit

Let's go!

## 1. Set up your environment

Once you log in to your GitHub account, the repository for this task will be added automatically.

1. Confirm that `agent-one-tool-practice` appears in your GitHub account.
2. Clone it and open it in your editor.
3. Check that you have Python 3.9+ installed: `python --version`.
4. Install the GitHub CLI if you don't have it: [GitHub CLI](https://cli.github.com/).

> **Tickets database**: This repo's GitHub Issues act as the ticket database: 
[GitHub Issues](https://github.com/nebius-academy-templates/issue-examples/issues)
> 

### Repository layout

```
agent-one-tool-practice/
├── skills/
│   └── get_ticket/       ← implement your tool here
│       └── get_ticket.py
├── output/
│   └── ticket.json       ← your tool writes here
└── README.md
```

## 2. Implement `get_ticket`

Create `skills/get_ticket/get_ticket.py`.

The tool should fetch a ticket by ID from GitHub Issues in this repository: [`issue-examples`](https://github.com/nebius-academy-templates/issue-examples/issues).

Write the result to `output/ticket.json`.

#### **Requirements**

| **Requirement** | **Detail** |
| --- | --- |
| Input | `ticket_id` — a GitHub issue number (string or int) |
| Source | GitHub Issues in [**this repo**](https://github.com/nebius-academy-templates/issue-examples/issues) |
| Output | JSON written to `output/ticket.json` |

#### Required JSON shape

```
{
  "ticket_id":"3",
  "title":"Add Observability",
  "description":"Full issue body text...",
  "comments": ["comment 1 body","comment 2 body"]
}
```

#### **Tips**

1. Field names must match exactly — the verifier checks them.
2. The GitHub Issues API is public for public repos — no token needed.
3. If you want a quick path, install `requests` with `pip install requests` and use it to call the GitHub API.
4. Comments are available via a separate endpoint: `GET /repos/{owner}/{repo}/issues/{issue_number}/comments`

### 🚀 Speed up with a prompt (optional)

You can use AI to generate a first implementation of the tool.

#### Prompt

Before you run it, replace `<your-github-username>` with your actual username.

```
Create a Python script called get_ticket.py.
It must define a function get_ticket(ticket_id: str) -> dict.
Use the GitHub REST API (no authentication needed for public repos) to fetch
issue number `ticket_id` from the repo `<your-github-username>/agent-one-tool-practice`.
Also fetch its comments.
Return a dict with keys: ticket_id, title, description, comments (list of comment bodies).
At the bottom of the script, when run directly:
  - Call get_ticket with the ticket_id passed as a CLI argument (sys.argv[1])
  - Write the result as pretty-printed JSON to output/ticket.json
  - Print the JSON to stdout as well
```

## 3. Test the tool

Fetch the ticket titled "Add Observability" (issue #3):

```
python skills/get_ticket/get_ticket.py #3
```

Verify that `output/ticket.json` was created and looks correct.

## 4. Add one more tool of your choice

1. Create one additional tool of your choice. Examples: `search_specs`, `post_comment`, `find_related_tickets`.
2. Run it once and save evidence of the result — for example, a screenshot or a JSON output file.

## 5. Check your work

Before submitting, test your solution locally and review the submission checklist. 

### ✅ Submission checklist

- [ ]  `skills/get_ticket/get_ticket.py` exists
- [ ]  One extra tool has been created, and evidence of the result is submitted
- [ ]  `get_ticket(ticket_id)` returns JSON with `ticket_id`, `title`, `description`, `comments`
- [ ]  `output/ticket.json` contains the result for ticket #3 — Add Observability
- [ ]  Local verifier passes
- [ ]  Changes are committed and pushed to `main`

## 6. Submit **your task**

1. Commit your changes.
2. Push to GitHub.
3. Return to the lesson and click "Submit."
