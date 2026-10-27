# Third-party notices

## CPython codec mapping provenance
The BMP mapping distributed with CodecLab is independently generated using Python's standard-library gb18030 codec. CPython is maintained by the Python Software Foundation and its contributors. The Chinese CJK codec implementation credits Hye-Shik Chang; the upstream mapping generator credits Hye-Shik Chang and Donghee Na.

The full CPython v3.13.5 LICENSE is retained at third_party/CPython-3.13.5-LICENSE.txt. This retains the upstream PSF copyright and license terms without substituting the CodecLab MIT license for them.

Transformation summary: enumerate BMP code points through the standard-library encoder; use zero placeholders for surrogates; repack output bytes into 65536 little-endian uint32 entries; embed that generated table as Base64 for the browser application. No Python interpreter, codec C implementation or upstream generation script is distributed in this application.

The original historical table provenance remains unknown; this release adopts the documented independently regenerated equivalent. See SOURCES.md for versions, hashes and reproduction details. No endorsement by Python, PSF or codec contributors is implied.
