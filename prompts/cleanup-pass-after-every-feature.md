# Cleanup pass after every feature

Owner's request (paraphrased): every feature leaves a mess behind (unused
files, duplicate functions, code nobody understands). After finishing a
feature, find and remove dead code, duplicate logic, unused components and
unnecessary complexity. Make it a permanent skill, check whether a skill for
this already exists, and run it now across the projects.

## Tasks
1. Check existing skills: built-in `/simplify` and `/code-review`, and
   `oh-my-claudecode:ai-slop-cleaner`. Say how they relate.
2. Add a `cleanup-pass` skill (lg-crm and SIDE-GIG): scope the diff, run
   knip + jscpd, read for what tools miss, verify every finding (grep
   including tests, Next.js entry points, server actions), delete first,
   merge real duplicates only when simple, prove nothing broke (tsc, eslint,
   vitest, next build, click-through), report with follow-ups.
3. Make it a habit: lg-crm `CLAUDE.md` says to run it after every feature;
   add `knip.json` and `npm run cleanup:scan`.
4. Run it now on lg-crm and ELGELLC. Delete unused files, deps and
   functions; merge the duplicated ELGE Bot panel into `BotInsights`.
   List bigger duplicates as follow-ups rather than refactoring tonight.
5. Verify, open PRs, handle review bots, merge.
