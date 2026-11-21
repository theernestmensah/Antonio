# Launch status

The redesigned site is local and has not been deployed. It retains supplied photographs and introduces a stronger green/red campaign presentation. Campaign approval and image permissions are pending.

## New donation experience

Donate buttons now appear in the desktop/mobile header and hero. A sticky mobile shortcut appears after the hero and hides while the donation section is visible. The dedicated donation section clearly states that payments are not open; the user has not chosen a destination.

To activate a real hosted payment page, set `donationUrl` in `assets/campaign-config.js` to the campaign-approved HTTPS link. The page keeps payments disabled for missing, invalid or non-HTTPS configuration. No card information, personal data or donations are collected by this site. Do not enter private API keys into that public configuration file. Update the privacy notice to name the selected payment service before activation.

## Upload package

Run `python tools/package.py` after any domain or source updates. Upload the contents of `publish/`, or extract `campaign-site.zip` into the public site root. The package excludes backups, development tools and unused legacy bundles.

## Completed

- Responsive navigation with an accessible mobile toggle, Escape handling, visible focus and a no-JavaScript fallback.
- Simplified campaign presentation, source-linked biography, genuine supplied images, reduced-motion support and local fonts.
- Removed the demo participation form, draft policies, unsupported ballot number, countdown and placeholder contact details.
- Added privacy information, custom 404, Person structured data, social metadata, robots.txt and optional hosting security headers.
- Replaced the loaded animation bundle with a small navigation and share script.

## Before release

1. Confirm campaign approval, public contact information, social profile ownership and image permissions. The current social preview is the supplied og.jpg; branding approval is pending.
2. Run `python tools/configure-domain.py https://APPROVED-DOMAIN` with the real HTTPS origin. This creates sitemap.xml and sets canonical, Open Graph URL and absolute social image URLs. No domain is fabricated in the current files.
3. Confirm the hosting provider’s request logging and retention; complete the privacy notice with operator contact details.
4. Deploy only public HTML, assets, img, og.jpg, robots.txt, generated sitemap.xml and applicable host configuration. Do not publish tools, documentation or .impeccable. Backups are in tools.
5. Configure the host to return the custom 404 with HTTP status 404. `_headers` is supported by some static hosts; configure equivalent headers elsewhere. Enable HTTPS at the host.
6. Verify 360px mobile, tablet and desktop layouts, keyboard and screen reader navigation, touch targets, computed contrast, all external links, image permissions and appearance, share/cancel/fallback behavior, and no console errors.
7. Verify social previews with the real public URL and approved artwork; measure LCP, INP and CLS in production. Targets are LCP ≤2.5s, INP ≤200ms, CLS ≤0.1.

## Verification

`python tools/check.py` passes local fragment, asset, H1, duplicate ID, image alt, structured data and placeholder checks. `node --check assets/site.js` passes. Independent source review fixes were applied. The browser preview could not reach the local server; visual checks, interaction tests, social crawls, WCAG conformance and production deployment are not certified.
