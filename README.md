# SIDE-GIG: Local Website Sprint

**The plan:** sell simple, professional websites to local businesses that
don't have one. Claude builds the sites. You find the businesses and close the
deals. Why this gig beat KDP, YouTube, dropshipping and the rest:
[`RESEARCH.md`](RESEARCH.md).

## How it works

```
You find a business with good reviews and no website (Google Maps)
  → paste its details to Claude
  → Claude builds a demo site in ~1 minute
  → you put it online for free (Netlify)
  → you show the owner: walk in, call, or text
  → they pay a 50% deposit → Claude finishes it → they pay the rest
```

## Faster path: use ELGE CRM

Once the `lg-crm` update is merged and deployed, the CRM does most of this
for you. **Find clients** searches Google for businesses with no website and
ranks them. **Reach out** opens call, text, walk-in and email scripts, plus
a ready-made demo site link (`crm.elgestudio.net/preview/...`) you can text
right away. No Netlify step needed. One tap on "Called / Texted / Visited"
logs it and schedules the follow-up. The steps below still work without the
CRM.

## Your first 7 days

**Day 1: Set up (about 1 hour)**
1. Create free accounts: [Netlify](https://www.netlify.com) (hosting) and
   [Stripe](https://stripe.com) or [Square](https://squareup.com) (to get paid).
2. Pick 2–3 niches from `playbook/scripts.md` (plumbers, barbers, cleaners…).
3. Open Google Maps and search "[niche] near [your city]". Find **10 businesses
   with 4.3★+ reviews and no website**. Add them to `tracker/leads.csv`.

**Day 2: Build demos**
4. For each business, tell Claude:
   > Make a demo site for: [business name], [city], [phone], [address],
   > [hours], services: [list], and these reviews: [copy 2–3 real ones from Google]
5. Claude creates `sites/configs/<name>.json` and builds
   `sites/out/<name>/index.html`. Drag that folder into Netlify, and you get a
   link like `rivera-plumbing.netlify.app`.

**Days 3–7: Outreach (2–3 hours a day, this is the job)**
6. **10+ contacts a day.** Walk-ins first (they close best), then calls with a
   texted link, then DMs. Scripts: `playbook/scripts.md`.
7. Follow up on day 2, day 5 and day 10. Most sales happen on a follow-up.
8. When someone says yes: send the agreement and the deposit link
   (`playbook/offer-and-pricing.md`). Then tell Claude what to change and
   connect their domain.
9. Every evening, update `tracker/leads.csv` and build 5 more demos.

**Goal for week 1:** 50 contacts, 1–2 deposits. The full road to $20k and
honest expectations are in [`playbook/money-math.md`](playbook/money-math.md).

## Need cash before the first client pays?

Run one of these alongside the website business: flipping free items from
Facebook Marketplace's "Free" section, or a few delivery shifts (DoorDash,
Instacart). Both can pay within days. See `RESEARCH.md`.

## What's in here

| Path | What |
| --- | --- |
| `RESEARCH.md` | Side gig comparison and sources |
| `playbook/scripts.md` | Walk-in, call, text, email scripts, follow-ups, objections |
| `playbook/offer-and-pricing.md` | Packages, deposits, agreement, hosting, taxes |
| `playbook/money-math.md` | How many contacts and sales $20k takes |
| `tracker/leads.csv` | Your pipeline. One row per business |
| `tools/make_site.py` | Builds a site from a JSON config (Python 3, no installs) |
| `sites/_template/` | The website template |
| `sites/configs/` | One JSON per business |
| `.claude/skills/` | Claude's skills: `local-site-sprint` (this workflow), `prospecting`, `cold-email`, `copywriting`, `offers`, `pricing`, `sales-enablement`, `seo-audit`, `social`, `marketing-psychology`, and the 11 `replica-*` app-building skills |

Plugins registered in `.claude/settings.json`:
[oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) (multi-agent
orchestration), plus the full [replica-skill](https://github.com/Jakeschincariol/replica-skill)
and [marketingskills](https://github.com/coreyhaines31/marketingskills) marketplaces.
