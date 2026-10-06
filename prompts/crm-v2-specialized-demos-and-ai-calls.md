# Prompt: Specialized demo sites + AI phone outreach (ELGE CRM v2)

> Written from Landyn's request on 2026-10-06, cleaned up for a coding agent.
> Repos: `LandynG10/lg-crm` (Next.js 16 + Drizzle + Supabase, deployed on
> Vercel at crm.elgestudio.net) and `LandynG10/ELGELLC` (marketing site,
> Vite + React, GitHub Pages at elgestudio.net).

## Goal

ELGE Studio sells two things to local businesses in Houston:
1. **Websites** (and booking sites) for businesses with no site or a weak one.
2. **AI phone receptionists** that answer every call, take orders, book
   appointments and text back missed calls, **in English and the caller's
   language** (Spanish first, then Vietnamese and Chinese).

The CRM's "Find clients" flow currently only targets #1 and generates one
generic demo site. Make it sell both, and make the demo sites feel built
for that specific kind of business.

## Part 1 — Industry demo templates with real visual polish

The public demo at `/preview/[id]` is what prospects see first. Replace the
single generic layout with **industry templates**, chosen automatically from
the business's Google category:

| Template | Categories (match on category text) | Feel |
| --- | --- | --- |
| **Trades** | plumbing, HVAC, roofing, electrical, construction, contractors, landscaping, cleaning, pest, movers | Bold and trustworthy. Heavy condensed type, dark background with a strong accent colour, big "Call now" CTA, emergency strip |
| **Auto** | auto repair, tire shops, body shops, detailing, mechanics | Garage/industrial. Dark steel, red or yellow accent, checkered/stripe motif |
| **Food & sellers** | restaurants, food trucks, taquerías, bakeries, cafés, shops that sell goods | Warm and playful. Rounded display type, menu-board layout, "Order by phone" CTA |
| **Barber & beauty** | barbers, salons, nails, lashes, spas, tattoo | Stylish. Black and gold or barber-pole motif, elegant serif, "Book now" CTA |
| **Health** | dentists, clinics, chiropractors, therapy, vets | Calm and clean. Soft teal, lots of white space |
| **Default** | anything else | Modern and neutral |

Every template must have **effects that stand out** and work on phones:
an animated hero (gradient or motif), scroll-reveal sections, hover lift on
cards, a sticky mobile call bar, and at least one signature motif per
template (for example an animated barber-pole stripe, or a scrolling marquee).
Respect `prefers-reduced-motion`. No heavy libraries: CSS animations plus
one small client component for scroll reveal.

Add an **English/Español toggle** on every demo. In Houston that alone
impresses owners.

Honesty rules (keep these):
- Only show facts from the Google listing: name, phone, address, hours,
  rating and review count.
- Generic copy stays labeled as sample text.
- Never invent reviews, prices, licences or years in business.

## Part 2 — Two prospecting modes in Find clients

Split Find clients into two modes with tabs: **Website leads** and
**AI phone leads**.

- **Website leads** = current behaviour: no website or website gaps, ranked
  by the existing opportunity score.
- **AI phone leads** = businesses that live on the phone: restaurants and
  takeout, auto shops, salons, trades and clinics. Rank them with a new
  **AI phone score**:
  - Has a phone number (required).
  - Call-driven category (orders or appointments by phone).
  - Busy: high review count, which means more calls and more missed calls.
  - Good rating.
  - **Likely serves Spanish-, Vietnamese- or Chinese-speaking customers**,
    inferred only from the business's name and category (for example
    "taquería", "llantera", "taller", "pho", "dim sum"). Phrase this as the
    customers the business serves. Never claim anything about the owner's
    English or ethnicity.
- The search form gets a mode switch with mode-specific quick picks. AI mode
  examples: Taquerías, Mexican restaurants, Chinese restaurants, Pho &
  Vietnamese, Tire shops, Auto repair, Nail salons, HVAC, Dentists. AI mode
  doesn't apply the "no website only" filter.
- Store the mode in the existing `discovered_businesses.search_query` JSON.
  No migration.

## Part 3 — AI phone outreach kit

For AI phone leads, "Reach out" opens an AI-specific kit:
- Call, text, walk-in and email scripts about missed calls and phone orders,
  using sourced, conditional numbers: 62% of small-business calls go
  unanswered and most callers don't leave a voicemail. Never quote a number
  about *their* business.
- **Spanish versions** of the call, text and walk-in scripts when the
  language signal is Spanish. Short Vietnamese and Chinese text messages
  when those signals fire, flagged "have a native speaker check before
  sending".
- A **demo link** to `/preview/[id]?offer=ai`: the business's demo page with
  an animated sample call transcript showing the AI answering as that
  business, in English and Spanish, clearly labeled as a sample.
- The same one-tap logging and follow-ups as the website kit.

## Part 4 — Marketing site

On elgestudio.net, add "Answers in English, Spanish and more" to the AI
Receptionist package, then redeploy.

## Done means
- `tsc`, `eslint` and `vitest` pass, with new unit tests for template
  selection, the AI phone score, language signals and the AI kit.
- `next build` passes.
- Every template is checked visually at phone and desktop widths, with
  screenshots.
- PR opened, review-bot findings addressed, merged, and Vercel deploy
  confirmed green.
