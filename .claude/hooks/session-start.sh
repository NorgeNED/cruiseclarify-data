#!/bin/bash
# Installs huggingface_hub so upload_to_hf.py can be imported and run in
# Claude Code on the web sessions. Local (Mac) sessions are left alone.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

python3 -m pip install --quiet --disable-pip-version-check --root-user-action=ignore huggingface_hub
