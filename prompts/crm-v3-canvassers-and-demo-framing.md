# CRM v3: target door-to-door companies, and frame every demo as a first draft

Owner's request (paraphrased): target companies that solicit a lot (window
cleaning, roof cleaning, solar, and similar) for both the website and the AI
receptionist offers, because their customers look them up after a knock or a
door hanger. Make sure prospects understand the demo is only a quick first
draft that gets much better once Landyn learns what they want, so nobody
thinks "this is so simple, how does this help me?" Research how to find these
companies and put it in Find clients.

## Context
- Repo: `lg-crm` (Next.js 16, see AGENTS.md). Outreach copy lives in
  `lib/outreach-kit.ts` (website) and `lib/ai-phone.ts` (AI receptionist),
  shared voice in `lib/voice.ts`, industry detection in `lib/industry.ts`,
  quick-pick niches in `components/discovery/search-filters-bar.tsx`, the
  public demo page in `app/preview/[id]/page.tsx`.
- All copy follows `SIDE-GIG/playbook/voice.md` (I'm Landyn → local Houston →
  found you → noticed something → made something for y'all → want to see it?).
  No stats, no invented facts.

## Tasks
1. **Door-to-door niche.** Add `isCanvasser(name, category)` to
   `lib/industry.ts` (solar, roofing, roof/window/gutter cleaning, pest
   control, home security/alarm, pressure washing, lawn/landscaping, pool,
   siding/windows, tree service, water treatment, internet/fiber). Solar,
   security, gutter, siding, tree and water treatment must classify as
   `trades` so they get the trades demo theme.
2. **Find clients.** Add a "Door-to-door companies" quick-pick row to the
   search form in both modes (Solar, Roofing, Roof cleaning, Window cleaning,
   Pest control, Home security, Pressure washing, Gutter cleaning, Lawn care).
   Show a one-line why under it. Score canvassers higher in AI phone mode
   (reason: "Door-to-door sales").
3. **Canvasser angle in copy.** For canvassers, the website email adds one
   plain sentence: people who get a knock or a door hanger usually look the
   company up first, so it helps to have something to point them to. The AI
   receptionist copy says it answers calls from door hangers, flyers and yard
   signs and sets up estimates while the crew is out. No stats.
4. **Demo = first draft, everywhere.**
   - Email, link text, walk-in and the follow-up that carries the link say,
     in Landyn's voice, that it's just a quick demo to get the idea and the
     real one gets built around what they want. Spanish versions too.
   - Demo page: the ribbon says "Quick demo made for X" and a section before
     the footer explains what the real version includes (their photos, real
     services and prices, colors and logo, booking or quote forms; for the AI
     offer: trained on their services, hours, prices and how they want calls
     handled). English and Spanish.
5. **Research note.** `SIDE-GIG/RESEARCH-CANVASSERS.md`: which industries
   canvass (sourced), why they're a fit for each offer, the exact Find
   clients searches to run in Houston, and in-person tips. Only sourced or
   clearly-labelled-as-advice claims.
6. **Verify.** Unit tests for `isCanvasser`, canvasser copy and the demo
   framing; tsc, eslint, vitest, next build; screenshot the demo page and the
   new quick-pick row at phone width. Open a PR, address review bots, merge.

## Don't
- Don't promise features the demo doesn't have. Don't add stats to first
  touches. Don't change how sending works (owner is happy with it).
