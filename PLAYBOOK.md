# Homvi LinkedIn Playbook

Instructions for the scheduled runs that manage the Homvi LinkedIn company page. Read this whole file before doing anything.

## The product

Homvi is an AI-powered home maintenance app for Android, coming soon to Google Play. Launch date: not set yet. Until Kaleem gives a date, every post says "Coming soon to Google Play".

Features, all shown in the original designs:
- **Dashboard:** a Home Health Score, plus counts of overdue, due-soon and healthy assets, and upcoming tasks.
- **AI appliance scan:** photograph a nameplate, and Homvi AI fills in the brand, model and specs, then sets up reminders.
- **Service schedules:** every asset (AC/HVAC, water purifier/RO, car or EV, solar panels, generator) gets its own reminders.
- **AI assistant:** a chat that answers home maintenance questions and gives budget estimates per quarter.
- **Document vault:** warranties, receipts and invoices, linked to their assets, with alerts before a warranty expires.
- **Budget insights:** a monthly maintenance cost chart.

The founder is Kaleem, a full-stack developer building Homvi.

## Audience and timing

- Audience: US homeowners, plus people interested in proptech, AI and startups. Use USD.
- Post times are 9:00 America/New_York on Mon, Wed, Thu and Sat.
- The Monday run creates the whole week. The Wed, Thu and Sat runs only publish what's already planned.

## Content mix per week, rotating so nothing repeats two weeks running

1. Feature spotlight: one feature, built around a concrete moment from daily life.
2. Problem → solution: a relatable home pain point, then how Homvi handles it.
3. Practical home tip: a genuinely useful maintenance tip, such as a seasonal checklist or how often to change filters, with a light Homvi tie-in.
4. Founder / build-in-public: why Homvi exists, a design decision, a lesson from building it, or a launch countdown. Write in first person as Kaleem, honestly and without hype.

Seasonality matters. Fall means HVAC servicing before winter, gutters and the furnace; winter means pipes and the generator; spring means AC prep; summer means AC load and solar.

## Writing rules

- **Hook:** the first two lines must earn the "see more" click, using a surprising truth, a relatable pain, or a crisp claim. Never open with "Excited to announce".
- **Length:** 600 to 1,300 characters. Use short paragraphs with blank lines between them.
- **Keywords:** work natural search phrases into the body, such as home maintenance app, appliance warranty tracker, HVAC maintenance and homeowner checklist.
- **Ending:** end with a question or a soft call to action ("Follow the page to get launch news").
- **Hashtags:** exactly 3 to 5, on the last line. Always include #HomeMaintenance, then pick from #Homeowners #PropTech #SmartHome #AIApps #HomeImprovement #BuildInPublic #StartupJourney #MobileApp #PersonalFinance #ArtificialIntelligence.
- **Emoji:** at most 1 per post.
- **Parentheses:** don't use them. LinkedIn's API treats ( ) as reserved characters, so use commas or dashes instead.
- **Facts:** never invent statistics, user numbers, testimonials, prices or a launch date. Don't claim savings figures. Don't mention competitors.

## Graphics

- Each post gets one portrait graphic, 1080x1350, in the Homvi style. See `templates/*.dc.html` for the four reference layouts and reuse their structure.
- **Colors:** navy #1E3A8A, blue #2563EB/#1D4ED8, light ground #EEF2FB, dark ground #0B1220. Status colors are red #B91C1C, amber #B45309 and green #047857. Purple #6D28D9 is for the vault only.
- **Type:** 'Inter Tight' 800 for headlines with tight letter-spacing, Inter for everything else.
- **Layout:** a letter-spaced eyebrow label, a big headline with one colored phrase, a visual made of app-style UI cards, then the standard navy footer bar: house icon, "Homvi", "AI-powered home maintenance" and a "Coming soon · Google Play" pill. Copy the footer exactly from a template.
- No emoji in graphics, no fake phone status bars, no invented numbers beyond the example app data in the templates.
- Vary the background across the week, mixing light, dark, lavender and navy.

## Weekly creation (Monday run)

1. Check posting history in `posts/*/plan.json` so you don't repeat topics.
2. Write 4 posts in the content mix above. Slot them on Mon, Wed, Thu and Sat of this week; this week's folder is named for the Monday date, YYYY-MM-DD.
3. Build each graphic as a `.dc.html` file using the templates' structure. Also publish them to a new Claude Design canvas titled "Homvi LinkedIn Week of <Mon date>", using the Design artifact type, so Kaleem can view and edit them.
4. Render them to PNG with `python3 -I tools/render.py <dir with .dc.html> posts/<monday>/ <files...>`. Look at each PNG and fix overflow, wrapping or clipping before continuing.
5. Write `posts/<monday>/plan.json`, using the format below. Commit and push to `main`.
6. Publish today's (Monday's) slot, then mark it posted in plan.json and push again.

## Publishing a slot

Use Zapier → LinkedIn:
- `selected_api`: `LinkedInCLIAPI`
- `action`: `create_company_update`
- `company_id`: `144576993`, the Homvi page
- `comment`: the caption
- `image_type`: `post_media`
- `image`: `https://raw.githubusercontent.com/kaleemqasim/homvi-marketing/main/posts/<monday>/<file>.png`
- `allow_reserved_characters`: `false`

Rules:
- Before publishing, check that the slot's `posted` value is false, so you never double-post. After a success, set `posted: true` and record `posted_at`, then push.
- If publishing fails, retry once. If it fails again, leave the slot unposted, add an `error` field, push, and stop. Do not try other posting routes.

## plan.json format

```json
{
  "week_of": "2026-10-05",
  "slots": [
    {"date": "2026-10-06", "theme": "Introducing Homvi", "image": "Main.png", "caption": "...", "posted": false}
  ]
}
```
