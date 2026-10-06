---
name: cleanup-pass
description: Post-feature cleanup. Finds and removes dead code, unused files, components, exports and dependencies, duplicate logic and needless complexity, then proves nothing broke. Use after finishing any feature and before opening its PR, or when the user says "clean up", "find dead code", "remove unused", "deduplicate", "simplify what you just added" or "what mess did that feature leave".
---

# Cleanup pass

Building features is the fun part; every feature also leaves a little mess
(an unused file, a duplicated helper, a function nobody calls). Run this pass
after **every** feature, before the PR. Deleting is the default; refactoring
is only for real duplication.

## Which repo
The commands below are for **lg-crm** (Next.js), which has `knip.json` and
`npm run cleanup:scan`. For **ELGELLC** (Vite/React) run
`npx -y knip@5` and `npx -y jscpd@4 src --min-lines 8 --min-tokens 70`, then
`npm run build`. For this repo (SIDE-GIG, Python standard library), read
`tools/` for unused functions and run `python3 tools/make_site.py` on a
config to prove it still builds.

## 1. Scope
- What did this feature touch? `git diff --stat origin/main...HEAD` (or the
  working tree). Read every changed file once, fully.
- Then scan the whole repo, because a feature often orphans *old* code (a
  component it replaced, a helper it superseded).

## 2. Automated scan
Run `npm run cleanup:scan` (knip + jscpd; config in `knip.json`). knip needs
`DATABASE_URL`/`DIRECT_URL` set to anything if `.env.local` is missing.
- **knip**: unused files, unused dependencies, unused exports.
- **jscpd**: copy-pasted blocks (8+ lines).
- `npx eslint .` for unused imports/vars, `npx tsc --noEmit`.

## 3. Read the diff for what tools miss
- A new helper that duplicates an existing one (grep for the idea, not the name).
- Props, params, state or branches nothing uses; feature flags never toggled.
- Two components that render the same thing with small differences: make one
  take a prop.
- Comments that restate the code or describe old behavior; leftover
  `console.log`, TODOs, commented-out code.
- Abstractions with one caller, wrappers that only forward arguments.
- Copy in two places that must stay in sync (move it to one constant).

## 4. Verify every finding before deleting
- `grep -rn` the name across app, components, lib, scripts **and tests**.
- Entry points look unused but aren't: Next.js `page/layout/route/loading/
  error` files, `middleware`/proxy, server actions passed to `<form action>`,
  config files, seed/migration scripts.
- Used only inside its own file means un-export it, not delete it.
- shadcn/ui primitives export more parts than we use; that's fine. Delete a
  whole `components/ui/*` file only when nothing imports it.

## 5. Fix
- Delete dead files, functions, constants and dependencies
  (`npm uninstall <pkg>` so the lockfile updates; never edit it by hand).
- Merge real duplicates into one shared piece only when it stays simple.
  Bigger refactors (e.g. two similar forms) go in the report as follow-ups.
- Keep behavior identical. No new features in a cleanup.

## 6. Prove nothing broke
`npx tsc --noEmit`, `npx eslint .`, `npx vitest run`, `npx next build`, then
click through any screen whose code you touched (Playwright at 390px and
1280px, no console errors). `npm run cleanup:scan` should come back clean.

## 7. Report
Lines deleted, what was removed and why, duplicates merged, and follow-ups
you deliberately left (with file names), in plain language.

## Related tools
- `/simplify` (built in): reuse, simplification and efficiency fixes on the
  current diff.
- `/code-review`: correctness bugs in the current diff.
- `oh-my-claudecode:ai-slop-cleaner`: deletion-first cleanup of AI-generated
  code with regression checks.
Use them alongside this pass. This skill adds the repo-wide scan (knip,
jscpd), the verification rules and the "run it after every feature" habit.
