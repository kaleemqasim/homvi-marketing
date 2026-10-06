import sys, pathlib
from playwright.sync_api import sync_playwright

src_dir = pathlib.Path(sys.argv[1])
out_dir = pathlib.Path(sys.argv[2])
names = sys.argv[3:]
out_dir.mkdir(parents=True, exist_ok=True)

FONT_CSS = """
@font-face{font-family:'Inter Tight';src:local('Inter Display ExtraBold'),local('InterDisplay-ExtraBold');font-weight:800}
@font-face{font-family:'Inter Tight';src:local('Inter Display Bold'),local('InterDisplay-Bold');font-weight:700}
@font-face{font-family:'Inter Tight';src:local('Inter Display SemiBold'),local('InterDisplay-SemiBold');font-weight:600}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium" if pathlib.Path("/opt/pw-browsers/chromium").is_file() else None)
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.route("**/*", lambda r: r.abort() if r.request.url.startswith("http") else r.continue_())
    for n in names:
        pg.goto((src_dir / n).resolve().as_uri())
        pg.add_style_tag(content=FONT_CSS)
        pg.wait_for_timeout(400)
        out = out_dir / (n.replace(".dc.html", ".png"))
        pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        print(out)
    b.close()
