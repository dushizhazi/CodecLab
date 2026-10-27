"""Rebuild CodecLab BMP GB18030 map using Python standard-library codec.
65536 little-endian uint32; big-endian encoded byte sequence packed in integer.
Surrogates map to 0; ASCII NUL also maps to 0 and is handled separately by app.
"""
import struct,hashlib,sys
from pathlib import Path
out=bytearray()
for cp in range(65536):
    b=b'' if 0xD800<=cp<=0xDFFF else chr(cp).encode('gb18030')
    out.extend(struct.pack('<I',int.from_bytes(b,'big')))
Path('GB18030-BMP-map.bin').write_bytes(out)
print(sys.version)
print(len(out),hashlib.sha256(out).hexdigest())
