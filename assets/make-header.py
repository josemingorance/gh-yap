# Regenerates the README headers (run from the repo root): python3 assets/make-header.py [social-preview.svg]
import sys
TEXT = {
 "en": ("A social network for your terminal.", "Posts are issues. Likes are reactions.", "GitHub is the backend.", ["0 servers", "0 databases", "$0 / month", "just gh"], "anyone else's CI green on the first try?", "shipping on a friday ", "hello world", "yapped "),
 "es": ("Una red social para tu terminal.", "Los posts son issues. Los likes, reacciones.", "GitHub es el backend.", ["0 servidores", "0 bases de datos", "0 € / mes", "solo gh"], "¿a alguien más le pasa el CI a la primera?", "desplegando en viernes ", "hola mundo", "publicado "),
}
themes = {
 "dark": dict(bg1="#0d1117", bg2="#161b22", dot="#21262d", win="#010409", winstroke="#30363d", bar="#161b22",
              fg="#e6edf3", dim="#7d8590", num="#6e7681", user="#e3b341", mention="#d2a8ff", tag="#79c0ff",
              heart="#ff7b72", ok="#3fb950", prompt="#d2a8ff", tagline="#adbac7", chip="#21262d", chipfg="#adbac7", chipstroke="#30363d"),
 "light": dict(bg1="#ffffff", bg2="#f6f8fa", dot="#d0d7de", win="#0d1117", winstroke="#d0d7de", bar="#161b22",
              fg="#e6edf3", dim="#7d8590", num="#6e7681", user="#e3b341", mention="#d2a8ff", tag="#79c0ff",
              heart="#ff7b72", ok="#3fb950", prompt="#d2a8ff", tagline="#424a53", chip="#f6f8fa", chipfg="#424a53", chipstroke="#d0d7de"),
}
def svg(t, lang, rx=18):
    T = TEXT[lang]
    c = themes[t]
    mono = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
    sans = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    wordfill = "#1f2328" if t == "light" else "#f0f6fc"
    lines = []
    y = 236
    def L(parts, dy=27):
        nonlocal y
        spans = "".join(f'<tspan fill="{col}"{" font-weight=\"700\"" if b else ""}>{txt}</tspan>' for txt, col, b in parts)
        lines.append(f'<text x="712" y="{y}" xml:space="preserve">{spans}</text>')
        y += dy
    L([("$ ", c["prompt"], True), ("gh yap", c["fg"], True)], 38)
    L([("#41 ", c["num"], False), ("@octocat", c["user"], True), (" · 3h", c["dim"], False)])
    L([("    " + T[4], c["fg"], False)])
    L([("    ♥ 4  💬 2", c["dim"], False)], 38)
    L([("#42 ", c["num"], False), ("@you", c["user"], True), (" · now", c["dim"], False)])
    L([("    " + T[5], c["fg"], False), ("#yolo", c["tag"], False), (" cc ", c["fg"], False), ("@octocat", c["mention"], False)])
    L([("    ", c["dim"], False), ("♥ 12", c["heart"], False), ("  💬 3", c["dim"], False)], 38)
    L([("$ ", c["prompt"], True), (f'gh yap post "{T[6]}"', c["fg"], False)])
    L([("✓ ", c["ok"], True), (T[7], c["fg"], False), ("#43", c["dim"], False)], 27)
    term = "\n    ".join(lines)
    chips = []
    x = 80
    for label in T[3]:
        w = 22 + len(label) * 10.2
        chips.append(f'<rect x="{x}" y="470" width="{w:.0f}" height="38" rx="19" fill="{c["chip"]}" stroke="{c["chipstroke"]}"/>'
                     f'<text x="{x + w/2:.0f}" y="495" text-anchor="middle" font-family="{mono}" font-size="17" fill="{c["chipfg"]}">{label}</text>')
        x += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c["bg1"]}"/><stop offset="1" stop-color="{c["bg2"]}"/>
    </linearGradient>
    <linearGradient id="word" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#d2a8ff"/><stop offset="0.5" stop-color="#ff7eb6"/><stop offset="1" stop-color="#ffa657"/>
    </linearGradient>
    <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.4" fill="{c["dot"]}"/>
    </pattern>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ff7eb6" stop-opacity="0.28"/><stop offset="1" stop-color="#ff7eb6" stop-opacity="0"/>
    </radialGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity="{0.45 if t == "dark" else 0.22}"/>
    </filter>
  </defs>
  <rect width="1280" height="640" rx="{rx}" fill="url(#bg)"/>
  <rect width="1280" height="640" rx="{rx}" fill="url(#dots)"/>
  <ellipse cx="930" cy="330" rx="420" ry="300" fill="url(#glow)"/>

  <text x="80" y="255" font-family="{mono}" font-size="116" font-weight="800" letter-spacing="-4">
    <tspan fill="{wordfill}">gh</tspan><tspan fill="url(#word)" dx="26">yap</tspan>
  </text>
  <text x="84" y="322" font-family="{sans}" font-size="34" font-weight="600" fill="{wordfill}">{T[0]}</text>
  <text x="84" y="368" font-family="{sans}" font-size="25" fill="{c["tagline"]}">{T[1]}</text>
  <text x="84" y="402" font-family="{sans}" font-size="25" fill="{c["tagline"]}">{T[2]}</text>
  {"".join(chips)}

  <g filter="url(#shadow)">
    <rect x="680" y="150" width="540" height="390" rx="14" fill="{c["win"]}" stroke="{c["winstroke"]}"/>
  </g>
  <path d="M680 164 a14 14 0 0 1 14 -14 h512 a14 14 0 0 1 14 14 v26 h-540 z" fill="{c["bar"]}"/>
  <circle cx="706" cy="171" r="7" fill="#ff5f57"/><circle cx="730" cy="171" r="7" fill="#febc2e"/><circle cx="754" cy="171" r="7" fill="#28c840"/>
  <text x="950" y="177" text-anchor="middle" font-family="{mono}" font-size="15" fill="{c["dim"]}">~ zsh</text>
  <g font-family="{mono}" font-size="18">
    {term}
  </g>
  <text x="712" y="{y + 11}" font-family="{mono}" font-size="18" font-weight="700" fill="{c["prompt"]}">$</text>
  <rect x="734" y="{y - 6}" width="11" height="22" fill="{c["fg"]}" opacity="0.85"/>
</svg>
'''
for t in themes:
    open(f"assets/header-{t}.svg", "w").write(svg(t, "en"))
    open(f"assets/header-{t}.es.svg", "w").write(svg(t, "es"))
import sys
if len(sys.argv) > 1:  # square-cornered copy for the 1280x640 social preview
    open(sys.argv[1], "w").write(svg("dark", "en", rx=0))
