---
name: local-site-sprint
description: Run this repo's business, which is selling one-page websites to local businesses. Use when the user names a business to build a demo for ("make a demo site for…", "new lead", pastes a Google Maps listing), wants to edit or launch a client site, wants outreach messages for a specific lead, or asks what to do next or how the pipeline is going.
---

# Local Site Sprint

The business: find local businesses with good Google reviews and no website,
build them a demo site first, show it to the owner, collect a 50% deposit, and
launch. Read `README.md` and `playbook/` for the full plan.

## New lead → demo site

1. Collect: business name, city, phone, address, hours, services, 2–3 **real**
   reviews (copied from their Google/Yelp listing, with author first name),
   and a brand colour if they have one. If something is missing, ask, or
   leave it out. **Never invent reviews, licences, years in business or
   claims.** Only use badges the listing supports.
2. Write `sites/configs/<slug>.json` in the format of
   `sites/configs/example-plumber.json`. Write the headline and subheadline
   specific to their trade and city (use the `copywriting` skill's
   principles: plain, concrete, benefit first).
3. Run `python3 tools/make_site.py sites/configs/<slug>.json`.
4. If Playwright/Chromium is available, screenshot at 390px and 1280px and
   check it.
5. Add or update the row in `tracker/leads.csv` (status `demo_built`).
6. Hand the user: the folder to drop into Netlify, plus a filled-in outreach
   message from `playbook/scripts.md` for this lead.

## Client said yes

- Confirm the deposit is paid before doing more than small demo edits.
- Apply their changes to the config and rebuild. For more than one page,
  extend the template carefully, keeping it a static site with no build step.
- Walk the user through connecting their domain in Netlify
  (Domain settings → Add a domain → follow the DNS records shown).
- Update the tracker status to `won` with price and care plan.

## Pipeline check-in

Read `tracker/leads.csv` and report: contacts this week, demos built,
follow-ups due today (by `next_followup`), deals won, and revenue. Compare
against `playbook/money-math.md` targets and say plainly what to do today.

## Rules

- Honest numbers only. Don't promise the user or their clients income or results.
- Real reviews and owner-approved photos only.
- Outreach email stays within CAN-SPAM. Stop contacting anyone who says no.
