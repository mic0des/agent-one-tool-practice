import json
import os
import sys
import urllib.request
from pathlib import Path


def post_comment(ticket_id: str) -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable is not set")

    base = "https://api.github.com/repos/mic0des/agent-one-tool-practice/issues"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }

    def fetch(url: str) -> dict | list:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    def post(url: str, payload: dict) -> dict:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            url,
            data=data,
            headers={**headers, "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    issue = fetch(f"{base}/{ticket_id}")

    comment_body = (
        f"Automated summary for '{issue['title']}':\n\n"
        f"{issue['body'] or '(no description provided)'}\n\n"
        f"---\n_Posted by post_comment skill._"
    )

    post(f"{base}/{ticket_id}/comments", {"body": comment_body})
    raw_comments = fetch(f"{base}/{ticket_id}/comments")

    return {
        "ticket_id": ticket_id,
        "title": issue["title"],
        "description": issue["body"] or "",
        "comments": [c["body"] for c in reversed(raw_comments)],
    }


if __name__ == "__main__":
    result = post_comment(sys.argv[1].lstrip("#"))
    output = json.dumps(result, indent=2)

    out_path = Path(__file__).parent.parent.parent / "output" / "post_comment.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output)

    print(output)
