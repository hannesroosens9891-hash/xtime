import re, base64, io, qrcode

with open("index.html", "r") as f:
    html = f.read()

# 1. Haal USDC + EURC secties weg als ze er al in staan
# We knippen alles tussen <section ... USDC en de afsluitende </section> weg
html = re.sub(r'<section[^>]*>.*?USDC — Base.*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<section[^>]*>.*?EURC — Base.*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<section[^>]*>.*?USDT.*?</section>', '', html, flags=re.DOTALL)

# 2. Voeg XMR toe als die er nog niet in staat
if "XMR — Monero" not in html:
    print("XMR ontbreekt, ik voeg hem toe...")
    xmr = input("Plak je VOLLEDIGE XMR adres (85jv...): ").strip()

    def qr_b64(uri):
        qr = qrcode.QRCode(box_size=8, border=2)
        qr.add_data(uri)
        qr.make()
        buf = io.BytesIO()
        qr.make_image(fill_color="black", back_color="white").save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode()

    q = qr_b64(f"monero:{xmr}?tx_description=UBUNITY")

    xmr_section = f"""
<section style="background:#0c2214;border:1px solid #1e4a2e;border-radius:14px;padding:16px;margin:16px 0;text-align:center">
<h2 style="color:#7dff9a">XMR — Monero — Donation Only</h2>
<p style="color:#fff;opacity:.8">Private donatie voor satire / humor. Geen returns. Geen KYC om te ontvangen.</p>
<img src="data:image/png;base64,{q}" style="width:190px;background:white;padding:8px;border-radius:10px">
<p style="word-break:break-all;color:#fff;font-size:13px;background:#05100a;padding:10px;border-radius:8px">{xmr[:10]}...{xmr[-8:]}</p>
<button onclick="navigator.clipboard.writeText('{xmr}');alert('Copied')" style="width:100%;padding:13px;background:#7dff9a;border:0;border-radius:10px;font-weight:700">Copy XMR Address</button>
</section>
"""
    # Zet XMR voor de satire-sectie
    html = html.replace('<section style="background:#111', xmr_section + '<section style="background:#111')
    print("XMR toegevoegd")
else:
    print("XMR staat er al in, ik haal alleen USDC/EURC weg")

with open("index.html", "w") as f:
    f.write(html)
print("Klaar: nu alleen BTC + XMR + Satire link")
