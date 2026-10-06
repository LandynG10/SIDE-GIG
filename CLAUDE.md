# SIDE-GIG

A business repo, not a software product. The business: build and sell
one-page websites to local businesses with no website (see `README.md`,
`RESEARCH.md`, `playbook/`).

- For anything to do with leads, demo sites, client edits or pipeline status,
  use the `local-site-sprint` skill.
- Sites: `sites/configs/<slug>.json` → `python3 tools/make_site.py <config>` →
  `sites/out/<slug>/index.html` (gitignored; rebuild from config). Python
  standard library only; keep it that way.
- Pipeline lives in `tracker/leads.csv`.
- The owner is not a developer. Give step-by-step, plain-language
  instructions: where to click and what to paste.
- All outreach (email, text, call, in person) follows `playbook/voice.md`.
- Owner's working style: rewrite each request into a clear coding-agent
  prompt, save it under `prompts/`, then carry it out.
- Never invent reviews, testimonials, credentials or income claims.
- After finishing any feature in any repo, run the `cleanup-pass` skill
  before opening the PR.
