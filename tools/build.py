"""Builds one privacy policy page per app (plus an index) for GitHub Pages.

Run from the repository root:  python3 tools/build.py
Edit APPS or the shared text below, rebuild, commit, push. Pages serve the repo root.
"""
import html
import os

DEVELOPER = "Warriani Entertainment"
LEGAL_ENTITY = "NGUYEN THE HUNG (Vietnam)"
EMAIL = "kelynback@gmail.com"
WEBSITE = "https://iyeahent.com"
UPDATED = "October 29, 2026"

# slug, app name as on Google Play, package, extra features that touch data
APPS = [
    ("blender", "Blender Sounds – White Noise", "com.iYeahEntertainment.Blender", []),
    ("vacuum-cleaner-sounds", "Vacuum Cleaner Sounds", "com.iYeahEntertainment.VacuumCleanerSounds", []),
    ("hair-dryer", "Hair Dryer Sounds: White Noise", "com.iYeahEntertainment.HairDryer", []),
    ("tivi-sounds", "Tivi Sounds – TV White Noise", "com.iYeahEntertainment.TiviSounds", []),
    ("baby-sleep", "White Noise: Baby Sleep Sounds", "com.iYeahEntertainment.SleepBaby", ["parents"]),
    ("circular-saw", "Circular Saw Simulator Prank", "com.iYeahEntertainment.CircularSaw", ["camera", "vibration"]),
    ("fidget-spinner", "Fidget Spinner Hands – Spin", "com.BestAppsTNeX.FidgetSpinner", ["camera"]),
    ("vacuum-cleaner-prank", "Vacuum Cleaner Simulator Prank", "com.iYeahEntertainmet.vacuumcleaner", ["camera", "vibration"]),
    ("dog-and-cat-on-screen", "Dog and Cat on Screen", "com.iYeahEntertainment.SnakeOnScreen", ["overlay", "photo", "notifications"]),
]

FEATURES = {
    "camera": (
        "Camera",
        "If you allow it, the app shows the live view of your rear camera behind the on-screen effect. "
        "The picture is only displayed on your screen while you use the app. The app does not take photos, "
        "record video, store camera images or send them anywhere. You can refuse or withdraw the camera "
        "permission at any time in Android settings; the app still works without it.",
    ),
    "vibration": (
        "Vibration",
        "The app vibrates your phone as part of the effect. This uses no personal data.",
    ),
    "overlay": (
        "Display over other apps",
        "With the “Display over other apps” permission, the app draws animated animals, or the "
        "companion you placed, on top of other apps. It does not read, capture or record what is on your "
        "screen. You can remove the animals from the notification or in the app, and revoke the permission "
        "in Android settings.",
    ),
    "photo": (
        "Your photo",
        "If you choose to use your own photo as the on-screen companion, you pick it with the Android "
        "photo picker, which gives the app access to that one image only. The app keeps a resized copy in "
        "its private storage on your device so it can show it. The photo is never uploaded or shared. "
        "Choosing another photo replaces it, and uninstalling the app deletes it.",
    ),
    "notifications": (
        "Notifications",
        "While the animals are on screen the app shows an ongoing notification with a button to remove "
        "them. Notifications contain no personal data.",
    ),
    "parents": (
        "Audience",
        "The app is meant to be used by parents and other adults to play soothing sounds. It is not "
        "designed to be operated by children, does not provide medical advice and makes no health claims.",
    ),
}

CSS = """
:root{--ink:#1f1b16;--muted:#5b5248;--bg:#fbf8f3;--card:#fff;--line:#e6ddd0;--accent:#2e6b34}
@media (prefers-color-scheme:dark){:root{--ink:#f1ece4;--muted:#c3b8aa;--bg:#17140f;--card:#211d17;--line:#3a332a;--accent:#8fd18f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 16px 64px}h1{font-size:28px;line-height:1.25;margin:0 0 8px}
h2{font-size:19px;margin:32px 0 8px}p,li{color:var(--ink)}.muted{color:var(--muted)}a{color:var(--accent)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:16px 0}
dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 16px;margin:0}dt{color:var(--muted)}dd{margin:0;overflow-wrap:anywhere}
ul{padding-left:20px}footer{margin-top:40px;font-size:14px;color:var(--muted)}
"""


def page(title, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
{body}
<footer>{html.escape(DEVELOPER)} · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</main>
</body>
</html>
"""


def policy(name, package, features):
    e = html.escape
    extra = "".join(f"<h2>{e(FEATURES[f][0])}</h2>\n<p>{e(FEATURES[f][1])}</p>\n" for f in features)
    body = f"""
<h1>Privacy Policy for {e(name)}</h1>
<p class="muted">Last updated: {UPDATED}</p>

<div class="card"><dl>
<dt>App</dt><dd>{e(name)}</dd>
<dt>Package name</dt><dd>{e(package)}</dd>
<dt>Developer</dt><dd>{e(DEVELOPER)} (as shown on Google Play)</dd>
<dt>Legal entity</dt><dd>{e(LEGAL_ENTITY)}</dd>
<dt>Contact</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
</dl></div>

<p>This policy explains what data the Android app <strong>{e(name)}</strong> ({e(package)}), published on
Google Play by <strong>{e(DEVELOPER)}</strong>, collects, how it is used and the choices you have.</p>

<h2>Summary</h2>
<ul>
<li>The app has no sign-in and no accounts. We do not ask for your name, email, phone number or contacts.</li>
<li>Your settings (for example the chosen sound, timer or animal) are stored only on your device.</li>
<li>The app shows ads from Google AdMob. Google may collect some device data for advertising, analytics and fraud prevention, as described below.</li>
<li>We do not sell personal data.</li>
</ul>

<h2>Data collected through advertising</h2>
<p>The app uses the Google Mobile Ads SDK (AdMob) and Google's User Messaging Platform (UMP). Depending on your
consent choices and region, the SDK may automatically collect and share with Google:</p>
<ul>
<li>Device and account identifiers, such as the Android advertising ID and app set ID;</li>
<li>Approximate location derived from your IP address;</li>
<li>Product interactions, such as app launches, taps and ad views;</li>
<li>Diagnostic information, such as app launch time and performance.</li>
</ul>
<p>This data is used for advertising (including ad personalization where you allow it), analytics and fraud
prevention, and is encrypted in transit. In the European Economic Area, the UK and Switzerland the app asks for
your consent before personalized ads, and you can change your choice later from the app's menu
(Privacy settings). You can reset or delete your advertising ID, or opt out of ad personalization, in
Android Settings &gt; Privacy &gt; Ads.</p>
<p>Learn more: <a href="https://policies.google.com/privacy">Google Privacy Policy</a> ·
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its services</a> ·
<a href="https://support.google.com/admob/answer/6128543">AdMob and user data</a>.</p>

{extra}
<h2>Permissions</h2>
<p>Internet and network state are used to load ads. Any other permission is described above and is used only
for the feature it belongs to.</p>

<h2>Data retention and deletion</h2>
<p>We do not store your data on our servers. Settings and any files the app keeps stay on your device and are
deleted when you clear the app's data or uninstall it. Data collected by Google through ads is handled under
Google's policies; you can manage it through your Google account and Android ad settings. You may also email us
with any request about your data and we will reply within 30 days.</p>

<h2>Children</h2>
<p>The app is not directed to children under 13 and we do not knowingly collect personal information from
children. If you believe a child has provided personal information, contact us and we will help remove it.</p>

<h2>Security</h2>
<p>Data sent by the advertising SDK is encrypted in transit (TLS). The app does not transmit other data.</p>

<h2>Changes to this policy</h2>
<p>We may update this policy when the app changes. The new version will be posted on this page with a new
"Last updated" date.</p>

<h2>Contact</h2>
<p>{e(DEVELOPER)}, {e(LEGAL_ENTITY)} — <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    return page(f"Privacy Policy – {name}", body)


def index():
    items = "".join(
        f'<li><a href="{slug}/">{html.escape(name)}</a> <span class="muted">({html.escape(pkg)})</span></li>\n'
        for slug, name, pkg, _ in APPS
    )
    body = f"""
<h1>{html.escape(DEVELOPER)} – Privacy Policies</h1>
<p class="muted">Last updated: {UPDATED}</p>
<p>Privacy policies for the Android apps published on Google Play by {html.escape(DEVELOPER)}
({html.escape(LEGAL_ENTITY)}).</p>
<ul>
{items}</ul>
"""
    return page(f"{DEVELOPER} – Privacy Policies", body)


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as f:
        f.write(index())
    for slug, name, pkg, features in APPS:
        os.makedirs(os.path.join(root, slug), exist_ok=True)
        with open(os.path.join(root, slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(policy(name, pkg, features))
    # Serve files as-is on GitHub Pages (no Jekyll processing).
    open(os.path.join(root, ".nojekyll"), "w").close()
    print("built", len(APPS), "policies")


main()
