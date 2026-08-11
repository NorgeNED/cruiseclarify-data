"""Publish the six public dataset files to Hugging Face.

Run by .github/workflows/sync-huggingface.yml. Needs HF_TOKEN in the
environment (a Hugging Face WRITE token, stored as a GitHub repository secret).

Why this is a script and not a command line
-------------------------------------------
This step used to shell out to `huggingface-cli upload`. Hugging Face renamed
that tool to `hf` and changed its arguments, and because the workflow installs
the latest library on every run, the command broke underneath a workflow that
had been working. Worse, it broke silently: Hugging Face simply stopped
receiving updates for three weeks in August 2026 and nothing announced it.

The Python API is the stable interface — it does not get renamed between
releases the way the command-line tool did. One call, one commit, and a real
error message if anything goes wrong.

Never publish anything beyond PUBLIC_FILES. The builder, the roadmap and the
international backlog are internal and must stay in the GitHub repository only.
"""

import os
import sys

from huggingface_hub import HfApi

REPO_ID = "CruiseClarify/cruise-costs"

PUBLIC_FILES = [
    "cruise-costs.csv",
    "cruise-costs.json",
    "cruise-packages.csv",
    "cruise-gratuities-tiers.csv",
    "README.md",
    "LICENSE",
]


def main() -> int:
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("::error::HF_TOKEN is not set.")
        return 1

    missing = [f for f in PUBLIC_FILES if not os.path.isfile(f)]
    if missing:
        print(f"::error::Expected files are missing from the checkout: {missing}")
        return 1

    api = HfApi(token=token)

    # Authenticate first, so a token problem reports as a token problem rather
    # than as a failed upload.
    try:
        who = api.whoami()
    except Exception as exc:
        print(f"::error::HF_TOKEN did not authenticate: {exc}")
        print("Check it is a WRITE token on the account that owns " + REPO_ID)
        return 1
    print(f"Authenticated as: {who.get('name')}")

    sha = os.environ.get("GITHUB_SHA", "local")
    try:
        api.upload_folder(
            folder_path=".",
            repo_id=REPO_ID,
            repo_type="dataset",
            allow_patterns=PUBLIC_FILES,
            commit_message=f"Sync from GitHub {sha}",
        )
    except Exception as exc:
        print(f"::error::Upload failed: {exc}")
        return 1

    print(f"Published {len(PUBLIC_FILES)} files to {REPO_ID}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
