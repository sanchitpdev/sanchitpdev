"""Render the GitHub contribution calendar as an animated isometric
Minecraft world: blocks drop out of the sky column by column while a
pixel miner walks the front edge. Pure-stdlib; takes the GraphQL
contributionCalendar JSON as input.

Usage: python3 generate_minecraft_graph.py contrib.json out.svg
"""
import json
import sys

TW, TH = 14, 7          # iso tile top: width, height
CH = 8                  # cube side height
PAD = 16
TITLE_H = 42
GROUND_EXTRA = 46       # room below front edge for the miner + legend

# block palettes: (top, left, right)
DIRT = ("#8a5a32", "#6b4423", "#57371c")
GRASS = ("#7cbd56", "#6b4423", "#57371c")
GRASS_HI = ("#94d160", "#6b4423", "#57371c")
EMERALD = ("#3ddc84", "#1e9e5c", "#157a46")
DIAMOND = ("#7fdbff", "#3aa8d8", "#2b86b0")


def level(c):
    if c == 0:
        return 0
    if c <= 2:
        return 1
    if c <= 5:
        return 2
    if c <= 9:
        return 3
    return 4


def cube(x, y, pal, w=TW, h=TH, ch=CH):
    """One iso cube whose top-face front vertex sits at (x, y)."""
    top = f'<polygon points="{x},{y} {x+w/2},{y-h/2} {x},{y-h} {x-w/2},{y-h/2}" fill="{pal[0]}"/>'
    left = f'<polygon points="{x-w/2},{y-h/2} {x},{y} {x},{y+ch} {x-w/2},{y-h/2+ch}" fill="{pal[1]}"/>'
    right = f'<polygon points="{x},{y} {x+w/2},{y-h/2} {x+w/2},{y-h/2+ch} {x},{y+ch}" fill="{pal[2]}"/>'
    return left + right + top


def px_rects(pixels, s):
    return "".join(
        f'<rect x="{c*s}" y="{r*s}" width="{n*s}" height="{s}" fill="{col}"/>'
        for r, c, n, col in pixels
    )


def miner(s=2.6):
    """Pixel miner, feet at local (0,0), drawn upward. Two leg frames."""
    HAIR, SKIN, EYE, SHIRT, PANT, BOOT, WOOD, IRON = (
        "#3b2c20", "#c99b6f", "#4a3ba8", "#00a8a8", "#3f51b5", "#555a5e",
        "#8a5a32", "#c0c8cc")
    body = [
        (-16, -3, 6, HAIR), (-15, -3, 6, HAIR),
        (-14, -3, 6, SKIN), (-13, -3, 6, SKIN),
        (-13, -2, 1, EYE), (-13, 1, 1, EYE),
        (-12, -3, 6, SKIN), (-11, -2, 4, HAIR),
        (-10, -3, 6, SHIRT), (-9, -3, 6, SHIRT), (-8, -3, 6, SHIRT),
        (-7, -3, 6, SHIRT), (-6, -3, 6, PANT), (-5, -3, 6, PANT),
        # pickaxe over the shoulder
        (-17, 3, 4, IRON), (-16, 5, 2, IRON),
        (-15, 4, 1, WOOD), (-14, 3, 1, WOOD), (-13, 2, 1, WOOD),
    ]
    legs_a = [(-4, -3, 2, PANT), (-3, -3, 2, PANT), (-2, -3, 2, BOOT), (-1, -3, 2, BOOT),
              (-4, 1, 2, PANT), (-3, 1, 2, PANT), (-2, 1, 2, BOOT), (-1, 1, 2, BOOT)]
    legs_b = [(-4, -4, 2, PANT), (-3, -4, 2, PANT), (-2, -4, 2, BOOT), (-1, -4, 2, BOOT),
              (-4, 2, 2, PANT), (-3, 2, 2, PANT), (-2, 2, 2, BOOT), (-1, 2, 2, BOOT)]
    return (
        f'<g>{px_rects(body, s)}'
        f'<g>{px_rects(legs_a, s)}'
        f'<animate attributeName="opacity" values="1;0;1" dur="0.36s" calcMode="discrete" repeatCount="indefinite"/></g>'
        f'<g opacity="0">{px_rects(legs_b, s)}'
        f'<animate attributeName="opacity" values="0;1;0" dur="0.36s" calcMode="discrete" repeatCount="indefinite"/></g>'
        f'</g>'
    )


def main():
    static = "--static" in sys.argv
    cal = json.load(open(sys.argv[1]))
    if "data" in cal:
        cal = cal["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    total = cal["totalContributions"]
    n = len(weeks)

    ox = PAD + 6 * TW / 2 + TW / 2
    oy = TITLE_H + TH * 3
    W = int(ox + n * TW / 2 + TW / 2 + PAD)

    def pos(i, j):
        return ox + (i - j) * TW / 2, oy + (i + j) * TH / 2

    front_y = oy + (n - 1 + 6) * TH / 2 + CH
    H = int(front_y + GROUND_EXTRA)

    build_dur = 6.0
    stagger = build_dur / n

    cols = []
    sparkles = []
    for i, w in enumerate(weeks):
        blocks = []
        for j, day in enumerate(w["contributionDays"]):
            x, y = pos(i, j)
            lv = level(day["contributionCount"])
            blocks.append(cube(x, y, DIRT))  # base terrain layer
            for k in range(lv):
                pal = (GRASS if k < 1 else GRASS_HI) if lv <= 2 else (
                    EMERALD if lv == 3 else DIAMOND)
                blocks.append(cube(x, y - (k + 1) * CH, pal))
            if lv == 4:
                sparkles.append((x, y - 4 * CH - TH / 2))
        begin = round(i * stagger, 2)
        if static:
            cols.append(f"<g>{''.join(blocks)}</g>")
            continue
        cols.append(
            f'<g opacity="0" transform="translate(0,-70)">'
            f'<animate attributeName="opacity" to="1" dur="0.05s" begin="{begin}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 -70" to="0 0" '
            f'dur="0.45s" begin="{begin}s" fill="freeze" calcMode="spline" '
            f'keySplines="0.3 0 0.7 1.4" keyTimes="0;1"/>'
            f'{"".join(blocks)}</g>'
        )

    spark_svg = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.6" fill="#e8fbff" opacity="0">'
        f'<animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="{build_dur + 0.3 * k}s" '
        f'repeatCount="indefinite"/></circle>'
        for k, (x, y) in enumerate(sparkles[:12])
    )

    # miner walks the front edge, then idles at the right
    sx, sy = pos(0, 6)
    ex, ey = pos(n - 1, 6)
    if static:
        walk = f'<g transform="translate({ex + 30},{ey + CH})">{miner()}</g>'
    else:
        walk = (
        f'<g transform="translate({sx - 26},{sy + CH})">'
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="{sx - 26} {sy + CH}" to="{ex + 30} {ey + CH}" dur="{build_dur}s" fill="freeze"/>'
        f'<g><animateTransform attributeName="transform" type="translate" additive="sum" '
        f'values="0 0;0 -1.5;0 0" dur="0.36s" repeatCount="indefinite"/>'
        f'{miner()}</g></g>'
    )

    legend_y = H - 12
    legend = (
        f'<g font-size="10" fill="#8b949e">'
        f'{cube(PAD + 8, legend_y, DIRT, 10, 5, 5)}<text x="{PAD + 18}" y="{legend_y + 3}">0</text>'
        f'{cube(PAD + 48, legend_y, GRASS, 10, 5, 5)}<text x="{PAD + 58}" y="{legend_y + 3}">1–5</text>'
        f'{cube(PAD + 98, legend_y, EMERALD, 10, 5, 5)}<text x="{PAD + 108}" y="{legend_y + 3}">6–9</text>'
        f'{cube(PAD + 148, legend_y, DIAMOND, 10, 5, 5)}<text x="{PAD + 158}" y="{legend_y + 3}">10+</text>'
        f'</g>'
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'SF Mono','Fira Code',Consolas,monospace">
  <rect width="{W}" height="{H}" rx="12" fill="#0d1117" stroke="#30363d"/>
  <text x="{PAD}" y="26" fill="#7cbd56" font-size="14" font-weight="bold">⛏ {total} blocks mined in the last year</text>
  <text x="{W - PAD}" y="26" text-anchor="end" fill="#8b949e" font-size="11">@sanchitpdev</text>
  {"".join(cols)}
  {spark_svg}
  {walk}
  {legend}
</svg>'''
    open(sys.argv[2], "w").write(svg)
    print(f"wrote {sys.argv[2]}  {len(svg)/1024:.0f}KB  {W}x{H}")


if __name__ == "__main__":
    main()
