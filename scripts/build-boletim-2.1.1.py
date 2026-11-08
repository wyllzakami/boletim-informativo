import base64
import subprocess
import sys
import zlib

PATCH = "eNqNVF1uGzcQft9TDJQCsaHdleTEaNNahpVqjQqwI0Fy85pQy1HElEtuSe7GTmAgQK/QA7ToQ9ACeQp6gr1JT9IhV7EF/zTVA7UkZ4Yz3/fNJEkCFk2NJn1to263u7U7OoLkyeCb+Gvotn9HRxFcxjDYf9Hv93fTShlc7ex+F0H02UsK61DtzKbzsxh+mC5o3dmF4SG8ixKAXCurJaZSv9p5+ZS+nChgolbaFMyJWsNeOkgHwIUttWo+1ihBMSi1cQy+eueDXqYv6b3u/wr1KO1/ORTcCDUWBl3zyQgNHEEU7BUq+y25/Dg7mY7GL8aT+WUKWREKFs0Hbcmfdr7ugnkfZn6uKAELuGr+KtDoGGhTlVIzbkE1f2iwemmwFjUWwMCgUCIXTIq3rPnQ/I22x5GsL+xdCT58FgL4Bc/FUnBGCRjkqCiEsCGBHK3VoOhV8rDpQx/lkpaEuC6rpRR5TyiO5+naFTJwfvvUc7/vmd/f8A5wUCCBp1iBw04t8I0Hs+OTI8bdsPNGcLcecqorxyRsYqDKHFWW2JxJHA7SfufwZiS3xgKTXEtttoI9GPT3lvtPbptztLkRpRNabZnPmFDEsFDWCVfldMmkh4KoqQhcxjc0baDxfkZLOgbc1O6hJ0ypJijRrIRM6W2S7AEFlHh4r1gPeq2B1+R/2pIar2x9TVKon4h7OexYdyHRrhEJzTV11LDTC0dpbq0H4KC3Rsb9x1Lzi8NA4zwbjU+ztOCBvuudp20QP4auX4i25AHcnc5e1L3vijL1Hf0lTFvABDFgFIu34WWVZyXATueMJEpoW7DVaxSOPprfgJVG15sQ91LgA2lDbcE1tZwlDTR/QkVdRpMmdIAXe2nQ0mutc88h9WHcdpm3FEUp2efb27VQFrwKdymV7IE9ySajhLB05y5Au71vwR30Pbq0enifTk+ys8kpTJ4dT+eno7PJ82kL7t0XAdrhnT8P+fNsvmh+mUaQhF+UUCgaYv+8/xVQ1e1Imo2PA0TX0iYA1wJNmDthAo14QY1HoNOlgZkRNBtKJqPkxhVaWGBeKd78TvPOxlAw308UkYbKqlLtNAJ+DXiQfBp12+Hq87qdTrydDbt6j8QVVKJWgqTW8kG5SpJEZVgcdddk5gdvHs6Ri83zCCSFICBWM8opNDPlWJCbTINSs/nxZAHjDEbfZ4vFFX7Xv+hf5OJXMg=="
raw = zlib.decompress(base64.b64decode(PATCH))
result = subprocess.run(
    ["patch", "-p0", "--batch", "--forward"],
    cwd=sys.argv[1], input=raw, stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT, check=False,
)
print(result.stdout.decode("utf-8", errors="replace"))
if result.returncode != 0:
    raise SystemExit(result.returncode)
print("Applied Boletim Informativo 2.3.0 presentation-label polish.")
