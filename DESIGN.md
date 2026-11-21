---
name: Antonio Edem Asinyo campaign
description: Bold campaign typography and a source-linked record.
colors:
  green: "#005236"
  deep: "#003b29"
  red: "#c92437"
  paper: "#f6f4ec"
  ink: "#102a21"
  line: "#ccd3c9"
  white: "#fff"
  focus: "#f4bc45"
typography:
  display:
    fontFamily: "Campaign, Arial, sans-serif"
    fontSize: "clamp(64px,7.4vw,112px)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Campaign, Arial, sans-serif"
    fontSize: "clamp(42px,4.8vw,72px)"
    fontWeight: 750
    lineHeight: 1.06
    letterSpacing: "-0.035em"
  emphasis:
    fontFamily: "Editorial, Georgia, serif"
    fontWeight: 400
  body:
    fontFamily: "Campaign, Arial, sans-serif"
    fontSize: "17px"
    lineHeight: 1.65
  label:
    fontFamily: "Campaign, Arial, sans-serif"
    fontSize: "14px"
rounded:
  control: "4px"
  donation-panel: "12px"
spacing:
  gutter: "clamp(24px,5.2vw,84px)"
  section: "100px"
  mobile-section: "60px"
components:
  button-red:
    backgroundColor: "{colors.red}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: "14px 24px"
  button-dark:
    backgroundColor: "{colors.green}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: "14px 24px"
---

# Design System: Antonio Edem Asinyo campaign

## Overview

**Creative North Star: "A record you can explore"**

This documents the implemented redesign: bold campaign typography, italic serif emphasis, green surfaces, red actions and supplied photographs. The portrait, typographic signature and campaign ribbon establish identity; reporting supports the biography.

Donate was requested by the user. Its pending state is intentional because the destination is unknown. Campaign approval and image permissions remain pending. Review was source-only: browser connections failed. No screenshots, rendered layouts, browser interaction or measured contrast QA is claimed. Domain, operator contact and hosting privacy practices require confirmation before release; see LAUNCH.md.

**Key Characteristics:**

- Bold headlines with serif emphasis.
- Green, red and warm paper surfaces.
- Supplied photography and linked references.
- Honest pending donation availability.

## Colors

### Primary

Green anchors hero and donation sections. Deep green anchors navigation, milestone and footer.

### Secondary

Red identifies donation actions, ribbon and signature. Gold identifies keyboard focus. Red hover uses #a51b2b; green hover uses the deep token.

### Neutral

Paper separates reading sections; ink carries text. The line token separates experience and stories. Supporting light-surface text uses #466052; dark surfaces use white and pale green. These are source values, not measured contrast findings.

## Typography

Campaign is the local alias for Schibsted Grotesk Variable, weights 400–900, with Arial/sans-serif fallbacks. Editorial is local DM Serif Display, normal and italic at weight 400, with Georgia/serif fallbacks. Local WOFF2 files use font-display: swap.

Hero bank uses Editorial at 1.13em. Lead text scales from 23px to 33px. Record titles use 21px and descriptions 16px with a 65ch maximum measure. Functional metadata, references, status, captions and footer use a 14px floor. Small branding has an 11px floor. Component-specific mobile overrides supplement these roles.

## Layout

The homepage loads assets/campaign.css directly, not the former bundled CSS/refinement cascade. Desktop generally uses two columns and 6–9vw gaps. Section padding is 100px, becoming 80px below 1150px and 65px below 900px.

Navigation collapses at 900px; Menu is hidden above that width. At 600px content grids stack, sections use 60px by 24px padding, dates and sources move above record descriptions, and footer metadata stacks. The milestone photo follows its text.

Desktop hero has a 730px minimum, viewport-derived height and 940px maximum with an absolutely positioned portrait. Mobile uses a 960px minimum and 440px portrait stage. The first hero line break remains visible and italic emphasis loses its left margin below 600px. A specific narrow-screen header adjustment handles 320px. These are source rules, not tested render outcomes. Anchor offsets are 100px and 90px on mobile. The Chevening image has its actual 460 by 478 intrinsic dimensions.

## Elevation & Depth

Most surfaces are flat and separated by color changes or thin rules. The portrait signature rotates negative four degrees. The visible mobile donation action uses 0 5px 22px #001e2240; no broader shadow system is implied.

## Shapes

Controls use compact corners; the donation panel uses the larger frontmatter radius. Photos remain rectangular. Supplied logo geometry and photographs are identity assets. Inline SVG hearts, arrows and stars are geometric accents.

## Components

### Buttons

Red donation and green declaration actions use 15px bold type and a 52px minimum height. Background hover transitions take 0.2 seconds. Keyboard focus uses a 3px gold outline offset by 5px. Pending donation is disabled with explicit unavailable copy and a muted green-gray surface.

### Navigation

Sticky deep-green navigation includes branding, section links and Donate. Hover reveals an underline. Mobile expansion uses aria-expanded and aria-controls. Escape closes and focuses Menu; outside clicks and link activation close it. Links remain visible without JavaScript. A skip link appears on focus. IntersectionObserver progressively enhances active-section indication.

### Record and stories

Native details/summary exposes the record, open by default. Each entry links to published evidence; one featured entry has a pale-green wash. News combines outlet, date, title and an underlined read action.

### Donation

Header, hero, footer and mobile Donate actions lead to the donation section. campaign-config.js currently sets donationUrl to null. Payment navigation stays hidden, the opening-soon control stays disabled and Awaiting confirmation remains visible. A configured absolute HTTPS destination reveals hosted-payment navigation and updates copy. Missing, invalid and non-HTTPS values preserve the pending state. No payment form or card-data collection exists here.

Below 600px the sticky Donate action appears after the hero leaves view and while donation is outside view. This depends on IntersectionObserver; normal donation links remain available without it. Activation requires an approved destination, not invented configuration.

### Sharing and motion

Sharing uses native sharing, clipboard or a textual address fallback. A polite live region reports results; the control disables during the attempt. Reduced motion disables transitions, animations and smooth scrolling. Content remains visible without animation initialization.

## Do's and Don'ts

### Do:

- **Do** preserve supplied photos, local fonts and campaign colors.
- **Do** tie donation availability to an approved HTTPS destination.
- **Do** retain references, native disclosure and visible keyboard focus.
- **Do** verify actual renders before claiming visual QA.

### Don't:

- **Don't** invent payment details, ballot positions, contacts or approvals.
- **Don't** add payment fields, tracking or embeds without updating privacy handling.
- **Don't** treat source rules as evidence of tested mobile layouts.
