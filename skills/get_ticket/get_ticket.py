import json
import sys
import urllib.request
from pathlib import Path


def get_ticket(ticket_id: str) -> dict:
    base = "https://api.github.com/repos/mic0des/agent-one-tool-practice/issues"
    headers = {"Accept": "application/vnd.github+json"}

    def fetch(url: str) -> dict | list:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    issue = fetch(f"{base}/{ticket_id}")
    raw_comments = fetch(f"{base}/{ticket_id}/comments")

    return {
        "ticket_id": ticket_id,
        "title": issue["title"],
        "description": issue["body"] or "",
        "comments": [c["body"] for c in raw_comments],
    }


if __name__ == "__main__":
    result = get_ticket(sys.argv[1].lstrip("#"))
    output = json.dumps(result, indent=2)

    out_path = Path(__file__).parent.parent.parent / "output" / "ticket.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output)

    print(output)
