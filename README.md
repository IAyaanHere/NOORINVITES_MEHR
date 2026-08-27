# NOORINVITES_MEHR

A customized and fully localized web invitation for Zoya & Zaid.

## Customizations Made

1. **Content & Names:**
   - Groom: Shaikh Zaid (Short: Zaid)
   - Bride: Zoya Khan (Short: Zoya)
   - Title & Meta tags updated to "Zoya & Zaid — Nikah Invitation"
   - Venue: Noor Invites, Mahal, Nagpur
   - Custom `setName` and `setCoupleNames` logic correctly handles short names.

2. **Frontend Asset Recovery & Localization:**
   - Downloaded and preserved original directory structure (`assets/css`, `assets/js`, `assets/images`, `media`).
   - Converted all external resource paths (including Google Fonts) to use local files.
   - Hosted Google Fonts offline via `assets/css/fonts.css`.

3. **UI Cleanup:**
   - Completely removed "Demo Version" badge and "Create Yours" CTA buttons.
   - Stripped out associated modal HTML and JavaScript to prevent console errors.

4. **Audio Fix:**
   - Default intro video now explicitly forced to `muted = true` and `volume = 0` via JS to prevent baked-in audio from playing on mobile devices.
   - Music updated to use the provided local `bismillah.mp3`.
