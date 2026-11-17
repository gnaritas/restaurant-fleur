#!/usr/bin/env python3
"""Generate the Restaurant Fleur site (template v2 T1, 2026-11-17).
French-American fine dining opening soon in the restored Justice Building,
101 W Capitol Ave, Little Rock AR. Identity: ivory paper, ink + bordeaux,
hairline gold rules, fleur-de-lis ornament, editorial serif. Zero JS, one
local stylesheet, inline SVG only.
Copy ONLY from verified card facts (t_17752f23):
- Founder announcement jennifermaune.com (updated 2026-09-28): chef Jennifer
  Maune (Arkansas native, MasterChef S13 finalist/runner-up, Ecole Ducasse
  Expert Diploma), co-founder Brian Maune, ground floor + basement of the
  Bob R. Brooks Jr. Justice Building (former Boyle Building, 1909, $35M
  renovation), 101 W Capitol Ave & Main St.
- aymag.com / arktimes.com / arkansasonline.com: elevated French-American
  lunch & dinner, chef's tasting menus, garden-to-table; opening delayed,
  targeted Oct/Nov 2026; 2026-11-12 IG: interviewing leadership, awaiting open.
- Founder IG 2026-09-30: group includes Fleur Pastry & Cafe and Fleur
  Provisions (retail goods, coffee, tea).
NOT published (omitted, never faked): opening date, hours, phone, menu prices.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")
os.makedirs(PUB, exist_ok=True)

ORIGIN = "https://restaurant-fleur-demo.up.railway.app"
NAME = "Restaurant Fleur"
STREET = "101 W Capitol Ave"
CITYZIP = "Little Rock, AR 72201"
NAP = f"{STREET}, {CITYZIP}"
LAT, LON = 34.74419, -92.271868
FB = "https://www.facebook.com/profile.php?id=61578431486949"
IG = "https://www.instagram.com/chefjennifermaune/"
Q = STREET.replace(" ", "%20") + "%2C%20" + CITYZIP.replace(" ", "%20").replace(",", "%2C")
DIR = f"https://www.google.com/maps/dir/?api=1&destination={Q}"
MAPSRC = f"https://www.google.com/maps?q={Q}&amp;output=embed"
OG = ORIGIN + "/og.png"
esc = lambda s: html.escape(s, quote=True)

DESC_HOME = ("Elevated French-American lunch and dinner with chef's tasting menus and "
             "garden-to-table cooking — Chef Jennifer Maune's flagship restaurant, opening "
             "soon in the restored Justice Building at 101 W Capitol Ave, Little Rock AR.")

# ---- fleur-de-lis ornament (hand-built, decorative) ----
def fleur(size, color="#A88A54", cls=""):
    return f'''<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" fill="{color}">
<path d="M12 1.4 C13.4 4.4 14.9 7.1 14.9 9.7 C14.9 11.4 13.6 12.7 12 12.7 C10.4 12.7 9.1 11.4 9.1 9.7 C9.1 7.1 10.6 4.4 12 1.4 Z"/>
<path d="M9.1 6.2 C6.4 6.9 4.4 9 4.1 11.6 C4.05 13.5 5.4 14.9 7.2 14.9 C8.8 14.9 10 14 10.5 12.5 L9.1 6.2 Z"/>
<path d="M14.9 6.2 C17.6 6.9 19.6 9 19.9 11.6 C19.95 13.5 18.6 14.9 16.8 14.9 C15.2 14.9 14 14 13.5 12.5 L14.9 6.2 Z"/>
<rect x="4.6" y="14.3" width="14.8" height="1.7" rx="0.85"/>
<path d="M12 16 C12 18.3 10.7 20 8.7 21 C11.1 21.3 12 22.1 12 22.7 C12 22.1 12.9 21.3 15.3 21 C13.3 20 12 18.3 12 16 Z"/>
</svg>'''

def head(path, title, desc, noindex=False):
    util = path in ("/404", "/thanks")
    canonical = ORIGIN + path if path != "/" else ORIGIN + "/"
    og = "" if util else f'''  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{esc(NAME)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:image" content="{OG}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
'''
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    return f'''<!DOCTYPE html>
<!-- BUILT-2026-11-17 -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">{robots}
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{canonical}">
{og}  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/style.css">
</head>
'''

NAV = f'''  <a class="skip" href="#main">Skip to content</a>
  <header class="site">
    <div class="bar">
      <a class="brand" href="/">{fleur(22, "#A88A54", "ficon")}<span>Restaurant Fleur</span></a>
      <nav aria-label="Main">
        <a href="/menus">Menus</a>
        <a href="/tasting-menu">Tasting Menu</a>
        <a href="/justice-building">The Justice Building</a>
        <a href="/contact">Contact</a>
      </nav>
    </div>
  </header>
'''

FOOTER = f'''  <footer>
    <div class="hair" aria-hidden="true"></div>
    <div class="wrap">
      <div class="fgrid">
        <div>
          <h4>Restaurant Fleur</h4>
          <address class="nap">French-American restaurant · opening soon<br>
          {STREET}<br>{CITYZIP}</address>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="/menus">Menus &amp; Experiences</a></li>
            <li><a href="/tasting-menu">Chef's Tasting Menu</a></li>
            <li><a href="/justice-building">The Justice Building</a></li>
            <li><a href="/contact">Contact &amp; Directions</a></li>
            <li><a href="/privacy">Privacy</a></li>
          </ul>
        </div>
        <div>
          <h4>Find Us</h4>
          <ul>
            <li><a href="{IG}" target="_blank" rel="noopener">@chefjennifermaune on Instagram</a></li>
            <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
            <li><a href="{DIR}" target="_blank" rel="noopener">Get directions</a></li>
          </ul>
        </div>
      </div>
      <div class="footline"><span>© 2026 Restaurant Fleur · {NAP}</span><span>{fleur(14, "#A88A54", "finline")} Opening soon — follow @chefjennifermaune for dates</span></div>
    </div>
  </footer>
</body>
</html>
'''

def ld(blocks):
    return "\n".join(f'  <script type="application/ld+json">\n{json.dumps(b, indent=2, ensure_ascii=False)}\n  </script>' for b in blocks)

ADDR = {"@type": "PostalAddress", "streetAddress": "101 W Capitol Ave",
        "addressLocality": "Little Rock", "addressRegion": "AR",
        "postalCode": "72201", "addressCountry": "US"}
REST = {"@type": "Restaurant", "name": NAME,
        "description": "Elevated French-American restaurant with chef's tasting menus and garden-to-table cooking, opening soon in the restored Justice Building.",
        "servesCuisine": ["French", "American"],
        "address": ADDR,
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
        "hasMap": DIR, "image": OG, "url": ORIGIN + "/", "sameAs": [FB, IG]}

def crumbs(path, name, extra=None):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]
    items.append({"@type": "ListItem", "position": 2, "name": name, "item": ORIGIN + path})
    if extra:
        for i, (n, u) in enumerate(extra, start=3):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": u})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def page(path, title, desc, body, blocks, noindex=False):
    out = head(path, title, desc, noindex) + "\n<body>\n" + NAV + f'<main id="main">\n{body}</main>\n' + FOOTER
    if blocks:
        out = out.replace("</head>", ld(blocks) + "\n</head>")
    open(os.path.join(PUB, "index.html" if path == "/" else path.strip("/") + ".html"),
         "w", encoding="utf-8").write(out)

MAP_HTML = f'''<div class="mapwrap">
  <iframe src="{MAPSRC}" loading="lazy" title="Map — Restaurant Fleur at {STREET}, {CITYZIP}" referrerpolicy="no-referrer-when-downgrade"></iframe>
  <p class="small">At Capitol Avenue and Main Street, downtown Little Rock · <a href="{DIR}" target="_blank" rel="noopener">Get directions</a></p>
</div>'''

# ---------------- HOME ----------------
faq_items = [
    ("When does Restaurant Fleur open?",
     "Opening soon. Opening dates and reservation details will be announced on the restaurant's Instagram, <a href=\"" + IG + "\" target=\"_blank\" rel=\"noopener\">@chefjennifermaune</a>, and on this page."
     ),
    ("Where exactly is it?",
     "On the ground floor and basement of the Bob R. Brooks Jr. Justice Building — the former Boyle Building at 101 W Capitol Ave at Main Street, Little Rock, AR 72201."
     ),
    ("What kind of food?",
     "Elevated French-American lunch and dinner, chef's tasting menus, and garden-to-table cooking from Chef Jennifer Maune's kitchen."
     ),
    ("Is there a full menu yet?",
     "The menu has not been published yet — follow <a href=\"" + IG + "\" target=\"_blank\" rel=\"noopener\">@chefjennifermaune</a> for the first look."
     ),
    ("What else is part of the Fleur group?",
     "Fleur Pastry &amp; Café and Fleur Provisions — retail goods, coffee, and tea — open alongside the restaurant."
     ),
]
faq_html = "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq_items)
FAQ_SCHEMA = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", html.unescape(a)).strip()}}
                             for q, a in faq_items]}

home_body = f'''  <section class="hero">
    <div class="wrap narrow">
      {fleur(64, "#A88A54", "fhero")}
      <p class="eyebrow">Opening soon · Downtown Little Rock</p>
      <h1><span class="fleur">Restaurant</span> Fleur</h1>
      <p class="lede">Elevated French-American lunch &amp; dinner, chef's tasting menus, and garden-to-table cooking in the restored Justice Building at Capitol Avenue and Main Street.</p>
      <p class="cta-row"><a class="btn" href="/contact">Get in touch</a> <a class="btn ghost" href="/menus">Menus &amp; Experiences</a></p>
    </div>
  </section>
  <section class="band">
    <div class="wrap">
      <div class="rule" aria-hidden="true"></div>
      <div class="cols">
        <div>
          <p class="eyebrow">Le Concept</p>
          <h2>A French-trained kitchen, Arkansas-grown</h2>
          <p>Chef Jennifer Maune — an Arkansas native, a <em>MasterChef</em> Season 13 finalist, and an École Ducasse Expert Diploma holder — is opening her flagship restaurant with her husband and co-founder Brian Maune. Expect elevated French-American cooking for lunch and dinner, chef's tasting menus, and produce-driven, garden-to-table plates.</p>
          <p><a class="btn" href="/tasting-menu">The chef's tasting menu</a></p>
        </div>
        <div>
          <p class="eyebrow">La Maison</p>
          <h2>The restored Justice Building</h2>
          <p>Fleur takes over the ground floor and basement of the Bob R. Brooks Jr. Justice Building — the former Boyle Building, built in 1909 and brought back through a $35M renovation — at 101 W Capitol Ave, the corner of Capitol Avenue and Main Street.</p>
          <p><a class="btn ghost" href="/justice-building">The building story</a></p>
        </div>
      </div>
    </div>
  </section>
  <section class="group">
    <div class="wrap">
      <div class="rule" aria-hidden="true"></div>
      <p class="eyebrow center">Le Groupe</p>
      <h2 class="center">One roof, three doors</h2>
      <p class="center lede">The Fleur group opens together in the Justice Building: the restaurant, a pastry counter and café, and a retail shop.</p>
      <div class="cols">
        <div class="card">
          {fleur(34, "#7A2E3F")}
          <h3>Fleur Pastry &amp; Café</h3>
          <p>Pastries and a café — part of the Fleur group, opening alongside the restaurant.</p>
        </div>
        <div class="card">
          {fleur(34, "#7A2E3F")}
          <h3>Fleur Provisions</h3>
          <p>Retail goods, coffee, and tea to take home — part of the Fleur group, opening alongside the restaurant.</p>
        </div>
      </div>
      <p class="center"><a class="btn ghost" href="/menus">All menus &amp; experiences</a></p>
    </div>
  </section>
  <section class="faq">
    <div class="wrap narrow">
      <div class="rule" aria-hidden="true"></div>
      <p class="eyebrow center">Good to Know</p>
      <h2 class="center">Before you visit</h2>
      <div class="faqlist">
{faq_html}
      </div>
    </div>
  </section>
  <section class="find">
    <div class="wrap">
      <div class="rule" aria-hidden="true"></div>
      <p class="eyebrow center">Find Fleur</p>
      <h2 class="center">101 W Capitol Ave, Little Rock</h2>
      <p class="center">Questions while we finish getting ready? <a href="/contact">Send the shop a note</a> — and follow <a href="{IG}" target="_blank" rel="noopener">@chefjennifermaune</a> for opening dates.</p>
{MAP_HTML}
    </div>
  </section>
'''
page("/", "Restaurant Fleur — French-American Restaurant, Little Rock AR", DESC_HOME, home_body,
     [{"@context": "https://schema.org", "@graph": [REST,
        {"@type": "WebPage", "url": ORIGIN + "/", "name": "Restaurant Fleur — French-American Restaurant, Little Rock AR", "inLanguage": "en-US", "about": REST}]},
      FAQ_SCHEMA,
      crumbs("/", "Home")])

# ---------------- MENUS (hub) ----------------
menus_body = f'''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Menus &amp; Experiences</p>
      <h1>The table, taking shape</h1>
      <p class="lede">Restaurant Fleur is opening soon, so nothing is printed yet — but the cooking is set: elevated French-American lunch and dinner, chef's tasting menus, and garden-to-table plates, with a pastry counter and a retail shop under the same 1909 roof.</p>
    </div>
  </section>
  <section class="cards">
    <div class="wrap">
      <div class="rule" aria-hidden="true"></div>
      <div class="cols three">
        <div class="card">
          <h3>Lunch &amp; Dinner</h3>
          <p>Elevated French-American service for lunch and dinner — composed plates built on garden-to-table sourcing from Arkansas growers and purveyors.</p>
          <p class="soon">Menu published at opening · follow @chefjennifermaune</p>
        </div>
        <div class="card">
          <h3>Chef's Tasting Menus</h3>
          <p>A multi-course table composed by Chef Jennifer Maune — French technique, Arkansas ingredients, the kitchen's clearest voice.</p>
          <p><a class="btn ghost" href="/tasting-menu">Read more</a></p>
        </div>
        <div class="card">
          <h3>Pastry, Café &amp; Provisions</h3>
          <p>Fleur Pastry &amp; Café and Fleur Provisions — pastries, coffee, tea, and retail goods — open alongside the restaurant.</p>
          <p class="soon">Details at opening</p>
        </div>
      </div>
      <p class="center"><a class="btn" href="/contact">Ask us anything</a></p>
    </div>
  </section>
'''
service_node = lambda n, d: {"@context": "https://schema.org", "@type": "Service", "name": n,
                             "description": d,
                             "areaServed": {"@type": "City", "name": "Little Rock", "addressRegion": "AR"},
                             "provider": {"@type": "Restaurant", "name": NAME, "address": ADDR, "url": ORIGIN + "/"}}
page("/menus", "Menus & Experiences — Restaurant Fleur, Little Rock AR",
     "What Restaurant Fleur will serve in downtown Little Rock: elevated French-American lunch and dinner, chef's tasting menus, plus Fleur Pastry & Café and Fleur Provisions.",
     menus_body,
     [{"@context": "https://schema.org", "@type": "ItemList", "name": "Menus &amp; Experiences — Restaurant Fleur",
       "itemListElement": [{"@type": "ListItem", "position": 1, "item": service_node("Lunch & Dinner — Restaurant Fleur", "Elevated French-American lunch and dinner with garden-to-table sourcing.")},
                            {"@type": "ListItem", "position": 2, "item": service_node("Chef's Tasting Menu — Restaurant Fleur", "Multi-course chef's tasting menus by Chef Jennifer Maune.")},
                            {"@type": "ListItem", "position": 3, "item": service_node("Fleur Pastry & Café", "Pastries and a café, part of the Fleur group in the Justice Building.")}]},
      crumbs("/menus", "Menus & Experiences")])

# ---------------- TASTING MENU (detail) ----------------
tasting_body = f'''  <section class="pagehead">
    <div class="wrap narrow">
      {fleur(44, "#A88A54", "fhero")}
      <p class="eyebrow">Chef's Tasting Menu</p>
      <h1>The long table</h1>
      <p class="lede">At the center of Restaurant Fleur: chef's tasting menus composed by Jennifer Maune — courses that follow her training at the École Ducasse and her Arkansas garden sourcing, from the kitchen of her flagship restaurant.</p>
    </div>
  </section>
  <section class="prose">
    <div class="wrap narrow">
      <div class="rule" aria-hidden="true"></div>
      <h2>Who is composing it</h2>
      <p>Chef Jennifer Maune grew up in Arkansas, finished as the runner-up of <em>MasterChef</em> Season 13, and earned an Expert Diploma at the École Ducasse — the French hospitality school founded by Alain Ducasse. Restaurant Fleur, opened with co-founder Brian Maune, is where that cooking comes home: French technique applied to ingredients grown and raised in Arkansas, served as chef's tasting menus alongside à la carte lunch and dinner.</p>
      <h2>What to expect</h2>
      <p>A composed, multi-course menu that changes with the garden. The full course list has not been published yet — opening dates and the first menu reveal will come through the restaurant's channels as the kitchen readies the dining room.</p>
      <p class="small">Follow <a href="{IG}" target="_blank" rel="noopener">@chefjennifermaune</a> for the first look · questions welcome: <a href="/contact">contact page</a>.</p>
      {MAP_HTML}
    </div>
  </section>
'''
page("/tasting-menu", "Chef's Tasting Menu — Restaurant Fleur, Little Rock AR",
     "Chef's tasting menus by Chef Jennifer Maune at Restaurant Fleur — French technique, Arkansas garden sourcing, downtown Little Rock. Menu published at opening.",
     tasting_body,
     [{"@context": "https://schema.org", "@type": "Service", "name": "Chef's Tasting Menu — Restaurant Fleur",
       "description": "Multi-course chef's tasting menus composed by Chef Jennifer Maune, served at Restaurant Fleur in the Justice Building, 101 W Capitol Ave, Little Rock AR.",
       "audience": {"@type": "Audience", "name": "Diners in Little Rock"},
       "areaServed": {"@type": "City", "name": "Little Rock", "addressRegion": "AR"},
       "provider": REST},
      crumbs("/tasting-menu", "Chef's Tasting Menu",
             [("Menus & Experiences", ORIGIN + "/menus")])])

# ---------------- JUSTICE BUILDING (detail) ----------------
building_body = f'''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">La Maison · 101 W Capitol Ave</p>
      <h1>A 1909 landmark, restored</h1>
      <p class="lede">Restaurant Fleur takes the ground floor and basement of the Bob R. Brooks Jr. Justice Building — the former Boyle Building at Capitol Avenue and Main Street, back in service after a $35M renovation.</p>
    </div>
  </section>
  <section class="prose">
    <div class="wrap narrow">
      <div class="rule" aria-hidden="true"></div>
      <h2>The building</h2>
      <p>The Boyle Building rose in 1909 and spent decades as one of downtown Little Rock's landmarks. After a $35M renovation, it returns as the Bob R. Brooks Jr. Justice Building — and the ground floor and basement become home to Restaurant Fleur, Fleur Pastry &amp; Café, and Fleur Provisions.</p>
      <h2>The corner</h2>
      <p>Fleur sits at 101 W Capitol Ave, at Capitol Avenue and Main Street — downtown's spine, a few blocks from the state capitol. Directions, and answers to any question you have while the dining room takes shape, are on the <a href="/contact">contact page</a>.</p>
{MAP_HTML}
    </div>
  </section>
'''
page("/justice-building", "The Justice Building — Restaurant Fleur at 101 W Capitol Ave, Little Rock AR",
     "Restaurant Fleur opens on the ground floor and basement of the Bob R. Brooks Jr. Justice Building — the restored 1909 Boyle Building at 101 W Capitol Ave, Little Rock AR.",
     building_body,
     [{"@context": "https://schema.org", "@type": "Place", "name": "Restaurant Fleur — Justice Building",
       "description": "Restaurant Fleur, Fleur Pastry & Café, and Fleur Provisions in the Bob R. Brooks Jr. Justice Building (former Boyle Building, 1909), 101 W Capitol Ave at Main St, Little Rock AR.",
       "address": ADDR,
       "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
       "containedInPlace": {"@type": "AdministrativeArea", "name": "Downtown Little Rock"},
       "image": OG, "url": ORIGIN + "/justice-building"},
      crumbs("/justice-building", "The Justice Building")])

# ---------------- CONTACT ----------------
contact_body = f'''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Contact &amp; Directions</p>
      <h1>Send the shop a note</h1>
      <p class="lede">Restaurant Fleur is not open yet. The team is finishing the dining room of the Justice Building — press releases, opening dates, and the first menus will be announced on <a href="{IG}" target="_blank" rel="noopener">@chefjennifermaune</a>. Meanwhile, anything you'd like to ask goes straight through this form.</p>
    </div>
  </section>
  <section class="two">
    <div class="wrap">
      <div class="rule" aria-hidden="true"></div>
      <div class="cols">
        <div>
          <form class="cform" method="post" action="/contact">
            <div>
              <label for="f-name">Your name</label>
              <input id="f-name" name="name" autocomplete="name" required>
            </div>
            <div class="row">
              <div>
                <label for="f-phone">Phone (optional)</label>
                <input id="f-phone" name="phone" type="tel" autocomplete="tel">
              </div>
              <div>
                <label for="f-email">Email</label>
                <input id="f-email" name="email" type="email" autocomplete="email">
              </div>
            </div>
            <div>
              <label for="f-message">Your message</label>
              <textarea id="f-message" name="message" required placeholder="Opening-date questions, press, private dining ideas — anything at all."></textarea>
            </div>
            <button class="btn" type="submit">Send the shop a note</button>
            <p class="small">We answer as fast as we can between build-out and interviews.</p>
          </form>
        </div>
        <div>
          <h3>The address</h3>
          <address class="addr">Restaurant Fleur<br>{STREET}<br>{CITYZIP}</address>
          <p>At Capitol Avenue and Main Street, in the Bob R. Brooks Jr. Justice Building.</p>
{MAP_HTML}
          <h3>Elsewhere</h3>
          <ul class="plain">
            <li><a href="{IG}" target="_blank" rel="noopener">Instagram · @chefjennifermaune</a></li>
            <li><a href="{FB}" target="_blank" rel="noopener">Facebook · Restaurant Fleur | Little Rock AR</a></li>
          </ul>
        </div>
      </div>
    </div>
  </section>
'''
page("/contact", "Contact & Directions — Restaurant Fleur, Little Rock AR",
     "Contact Restaurant Fleur while it opens in the Justice Building: send a note, get directions to 101 W Capitol Ave, or follow @chefjennifermaune for opening dates.",
     contact_body,
     [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact — Restaurant Fleur",
       "url": ORIGIN + "/contact", "about": {"@type": "Organization", "name": NAME, "address": ADDR}},
      crumbs("/contact", "Contact")])

# ---------------- PRIVACY ----------------
privacy_body = f'''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Privacy</p>
      <h1>How this site treats your information</h1>
    </div>
  </section>
  <section class="prose">
    <div class="wrap narrow">
      <div class="rule" aria-hidden="true"></div>
      <h2>Who runs this site</h2>
      <p>This website represents Restaurant Fleur, opening soon at 101 W Capitol Ave, Little Rock, AR 72201. It carries no advertising and no analytics.</p>
      <h2>The contact form</h2>
      <p>If you use the contact form, you send us your name, an optional phone number, an optional email address, and your message. We use it only to answer you, and we keep it only as long as needed to do that. We do not sell it, and we do not add you to marketing lists.</p>
      <h2>No trackers, no third-party scripts</h2>
      <p>This site sets no cookies and loads no third-party JavaScript or tracking pixels. Styles and icons are served by the site itself. On pages that show the location map, the embedded map (Google Maps) may set its own cookies under Google's privacy policy once it loads.</p>
      <h2>Your choices</h2>
      <p>Ask us to delete or correct anything you sent through the form the same way — through the <a href="/contact">contact form</a>. If this policy changes, the change appears on this page.</p>
      <p class="small">© 2026 Restaurant Fleur · {NAP}</p>
    </div>
  </section>
'''
page("/privacy", "Privacy Policy — Restaurant Fleur, Little Rock AR",
     "Privacy policy for the Restaurant Fleur website: one contact form, no cookies, no trackers, no third-party scripts, and no advertising.",
     privacy_body,
     [{"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy Policy — Restaurant Fleur", "url": ORIGIN + "/privacy"},
      crumbs("/privacy", "Privacy")])

# ---------------- THANKS / 404 ----------------
thanks_body = f'''  <section class="pagehead tall">
    <div class="wrap narrow">
      {fleur(52, "#A88A54", "fhero")}
      <p class="eyebrow">Message sent</p>
      <h1>Thank you</h1>
      <p class="lede">Your note is on its way to the restaurant. We will answer as soon as we can — and for opening dates, follow <a href="{IG}" target="_blank" rel="noopener">@chefjennifermaune</a>.</p>
      <p class="cta-row"><a class="btn" href="/">Back to the front page</a></p>
    </div>
  </section>
'''
page("/thanks", "Thank You — Restaurant Fleur, Little Rock AR",
     "Thank you — your message has been sent to Restaurant Fleur in downtown Little Rock.", thanks_body, [], noindex=True)

nf_body = f'''  <section class="pagehead tall">
    <div class="wrap narrow">
      {fleur(52, "#A88A54", "fhero")}
      <p class="eyebrow">404</p>
      <h1>That page isn't here</h1>
      <p class="lede">The dining room is still being finished — some pages haven't been set yet. Start from the front and find your way.</p>
      <p class="cta-row"><a class="btn" href="/">Front page</a> <a class="btn ghost" href="/contact">Contact</a></p>
    </div>
  </section>
'''
page("/404", "Page Not Found — Restaurant Fleur, Little Rock AR",
     "The page you were looking for isn't here — Restaurant Fleur is opening soon in downtown Little Rock.", nf_body, [], noindex=True)

# ---------------- sitemap / robots / favicon ----------------
core = ["/", "/menus", "/tasting-menu", "/justice-building", "/contact", "/privacy"]
urls = "\n".join(f"  <url><loc>{ORIGIN}{u if u != '/' else '/'}</loc><lastmod>2026-11-17</lastmod></url>" for u in core)
open(os.path.join(PUB, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
open(os.path.join(PUB, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nDisallow: /thanks\nDisallow: /404\n\nSitemap: " + ORIGIN + "/sitemap.xml\n")
open(os.path.join(PUB, "favicon.svg"), "w", encoding="utf-8").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="4" fill="#201C23"/>'
    + fleur(24, "#A88A54").replace(f'class="" ', "").replace(' class=""', "") + '</svg>\n')

# ---------------- stylesheet ----------------
CSS = ''':root{
  --ink:#201C23; --ink2:#3A333C; --paper:#FBF7EF; --paper2:#F1EADB;
  --wine:#7A2E3F; --gold:#A88A54; --gold-d:#8F7443; --sage:#5F6F5A; --line:#D9CFBC;
  --serif:"Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--wine)}
a:hover{color:var(--gold-d)}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:var(--ink);color:var(--paper);padding:8px 14px;z-index:9}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px}
.wrap.narrow{max-width:760px}
header.site{background:var(--paper);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:8}
.bar{max-width:1080px;margin:0 auto;padding:10px 22px;display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-size:20px;letter-spacing:.06em;font-weight:700}
.brand .ficon{flex:none}
nav{margin-left:auto;display:flex;flex-wrap:wrap;gap:4px}
nav a{color:var(--ink2);text-decoration:none;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;padding:8px 10px;border-radius:2px}
nav a:hover{color:var(--wine);background:var(--paper2)}
.eyebrow{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-d);margin:0 0 12px}
.center{text-align:center}
h1{font-size:clamp(38px,6.4vw,64px);line-height:1.08;font-weight:400;letter-spacing:.01em;margin:6px 0 18px}
h1 .fleur{display:block;font-size:.44em;letter-spacing:.32em;text-transform:uppercase;color:var(--wine);font-style:italic;margin-bottom:8px}
h2{font-size:clamp(24px,3.4vw,32px);font-weight:400;line-height:1.2;margin:0 0 14px}
h3{font-size:20px;font-weight:700;margin:0 0 10px}
.lede{font-size:clamp(18px,2.3vw,22px);color:var(--ink2);max-width:62ch}
section{padding:56px 0}
.rule{border-top:3px double var(--gold);width:180px;margin:0 auto 34px;height:0}
section.band,section.group{background:var(--paper2)}
.hero{padding:84px 0 72px;text-align:center;background:
  radial-gradient(ellipse 60% 46% at 50% -8%, rgba(122,46,63,.14), transparent 68%),
  radial-gradient(ellipse 42% 34% at 50% 108%, rgba(168,138,84,.16), transparent 70%), var(--paper)}
.fhero{display:block;margin:0 auto 18px}
.cta-row{margin-top:26px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-block;background:var(--wine);color:#FDF9F0;text-decoration:none;font-size:14px;letter-spacing:.12em;text-transform:uppercase;padding:13px 26px;border-radius:2px;border:1px solid var(--wine)}
.btn:hover{background:#652333;color:#FDF9F0}
.btn.ghost{background:transparent;color:var(--wine)}
.btn.ghost:hover{background:var(--paper);border-color:var(--gold);color:var(--gold-d)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:10px}
.cols.three{grid-template-columns:1fr 1fr 1fr;gap:26px}
.card{background:var(--paper);border:1px solid var(--line);border-top:3px solid var(--gold);padding:26px 24px;border-radius:2px}
.group .card{text-align:center}
.group .card svg{display:block;margin:0 auto 12px}
.soon{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--sage)}
.pagehead{padding:72px 0 40px;text-align:center}
.pagehead.tall{padding:88px 0 64px}
.prose{padding:10px 0 60px}
.prose h2{margin-top:26px}
.prose p{margin:0 0 16px;max-width:66ch}
.faqlist details{border-bottom:1px solid var(--line);padding:14px 4px}
.faqlist summary{cursor:pointer;font-size:19px;list-style-position:inside}
.faqlist summary:hover{color:var(--wine)}
.faqlist p{margin:10px 0 4px;color:var(--ink2)}
.mapwrap{margin-top:26px}
.mapwrap iframe{width:100%;height:340px;border:1px solid var(--line);border-radius:2px;display:block;filter:sepia(.18) saturate(.9)}
.mapwrap .small{margin-top:10px}
.small{font-size:14px;color:var(--ink2)}
.two .cols{align-items:start}
.cform{background:var(--paper);border:1px solid var(--line);border-top:3px solid var(--gold);padding:26px;border-radius:2px}
.cform label{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin:0 0 6px}
.cform input,.cform textarea{width:100%;padding:11px 12px;font:inherit;font-size:16px;border:1px solid var(--line);border-radius:2px;background:#fff;color:var(--ink)}
.cform textarea{min-height:130px}
.cform .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.cform>div{margin-bottom:16px}
.cform button{margin-top:4px}
.addr{font-style:normal;line-height:1.5;margin:0 0 14px}
ul.plain{list-style:none}
ul.plain li{margin:0 0 8px}
footer{background:var(--ink);color:#E8E1D2;padding:0 0 30px;margin-top:20px}
footer .hair{border-top:3px double var(--gold);height:0;width:180px;margin:0 auto}
.fgrid{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:40px;padding:44px 0 26px}
footer h4{color:var(--gold);font-size:13px;letter-spacing:.2em;text-transform:uppercase;margin:0 0 12px;font-weight:400}
footer .nap{font-style:normal;line-height:1.7}
footer ul{list-style:none}
footer li{margin:0 0 8px}
footer a{color:#E8E1D2;text-decoration:underline;text-decoration-color:rgba(168,138,84,.6);text-underline-offset:3px}
footer a:hover{color:#fff}
.footline{border-top:1px solid rgba(232,225,210,.18);padding-top:16px;display:flex;gap:16px;justify-content:space-between;flex-wrap:wrap;font-size:13.5px;color:#B8AF9E}
.finline{vertical-align:-2px;margin-right:4px}
@media (max-width:820px){
  .cols,.cols.three,.fgrid,.cform .row{grid-template-columns:1fr}
  .cols.three{gap:22px}
  nav{margin-left:0;width:100%}
  section{padding:44px 0}
  .hero{padding:64px 0 54px}
  h1{font-size:40px}
}
/* paragraph-junction rhythm (fixes 0px glue under the margin reset; matches .prose p 16px / .mapwrap 26px) */
main p + p{margin-top:16px}
main .cols + p{margin-top:26px}
.cform p.small{margin-top:12px}
.mapwrap + h3{margin-top:26px}
'''
open(os.path.join(PUB, "style.css"), "w", encoding="utf-8").write(CSS)

print("pages generated:", sorted(os.listdir(PUB)))
