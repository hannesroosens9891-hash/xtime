with open("index.html", "r") as f:
    html = f.read()

# Don't add it twice
if "ubunity-quantum-parody" in html:
    print("Link already there, skipping")
else:
    section = """
<section style="background:#111;border:1px solid #333;border-radius:14px;padding:16px;margin:16px 0;text-align:center;font-family:system-ui">
<h2 style="color:#fff;margin:0">QUANTOMICS — SATIRE / PARODY</h2>
<p style="color:#fff;opacity:.8">Personally created satire. Not news. Not financial advice. Story + code.</p>
<a href="https://ubunity-quantum-parody.vercel.app/" style="display:inline-block;padding:13px 20px;background:#fff;color:#000;border-radius:10px;font-weight:700;text-decoration:none">Enter the Parody →</a>
<p style="font-size:12px;color:#fff;opacity:.6">Each issue hides a clue. Find them all to mine the block.<br>UBUNITY — XTIME</p>
</section>
"""
    html = html.replace("</div></body></html>", section + "</div></body></html>")
    with open("index.html", "w") as f:
        f.write(html)
    print("Satire link added")
