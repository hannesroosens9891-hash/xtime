import base64, io, qrcode

print("Paste BTC 1 (full, starts with bc1q3j...):")
btc1 = input("BTC 1: ").strip()
print("Paste BTC 3 (full, starts with bc1q38...):")
btc3 = input("BTC 3: ").strip()

def qr_b64(uri):
    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(uri)
    qr.make()
    buf = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

q1 = qr_b64(f"bitcoin:{btc1}?label=UBUNITY-1")
q3 = qr_b64(f"bitcoin:{btc3}?label=UBUNITY-3")

def section(title, addr, qr):
    return f"""
<section style="background:#0c2214;border:1px solid #1e4a2e;border-radius:14px;padding:16px;margin:16px 0;text-align:center;font-family:system-ui">
<h2 style="color:#7dff9a;margin:0">{title} — Donation Only</h2>
<p style="color:#fff;opacity:.8;font-size:13px">Scan or copy. This address only accepts donations. It does not ask for anything.</p>
<img src="data:image/png;base64,{qr}" style="width:190px;background:white;padding:8px;border-radius:10px">
<p style="word-break:break-all;color:#fff;font-size:13px;background:#05100a;padding:10px;border-radius:8px">{addr[:10]}...{addr[-8:]}</p>
<button onclick="navigator.clipboard.writeText('{addr}');alert('Copied')" style="width:100%;padding:13px;background:#7dff9a;border:0;border-radius:10px;font-weight:700;cursor:pointer">Copy Address</button>
<a href="bitcoin:{addr}" style="display:block;margin-top:10px;color:#7dff9a;text-decoration:none">Open in Bitcoin Wallet →</a>
</section>
"""

html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UBUNITY - XTIME</title></head>
<body style="margin:0;background:#05100a;color:#fff;font-family:system-ui"><div style="max-width:620px;margin:0 auto;padding:18px 16px 40px;text-align:center">
<h1 style="color:#7dff9a;letter-spacing:2px">UBUNITY</h1>
<p>AI for I. I for AI. — All for 1, 1 for All</p>
<p style="color:#7dff9a"><b>I am, so we are energy.</b></p>
{section("BTC 1", btc1, q1)}
{section("BTC 3", btc3, q3)}
<p style="font-size:12px;opacity:.6">EVERYTHING IS UBUNITY — XTIME<br>Donations are irreversible. Verify first 10 / last 8 chars before sending.</p>
</div></body></html>"""

with open("xtime_main.html","w",encoding="utf-8") as f:
    f.write(html)
print("Built FULL xtime_main.html")
