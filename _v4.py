# -*- coding: utf-8 -*-
import io, re, os
os.chdir(r"C:\Users\suminlee\_ghwork\easycopilotlab-2026")
s = io.open("index.html", encoding="utf-8").read()
for t in ["div", "table", "section", "details", "ol", "ul", "pre"]:
    o = len(re.findall(r"<%s[ >]" % t, s))
    c = len(re.findall(r"</%s>" % t, s))
    print(t, o, c, "OK" if o == c else "MISMATCH")
imgs = re.findall(r'src="(ecl-[^"]+)"', s)
print("images", len(imgs), "missing", sorted(i for i in set(imgs) if not os.path.exists(i)))
used = set(os.path.basename(i) for i in imgs)
print("unused:", [f for f in sorted(os.listdir("ecl-shots")) if f not in used])
