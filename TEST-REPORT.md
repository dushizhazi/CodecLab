# FXB CodecLab v1.0.0 — Release test record

**Application HTML unchanged from RC3**: SHA-256 `a88f074a8238a84032b1f521c691133b58bbeceb419f8a2228547123765ce80e`.

- 03 RC3 independent Node v24.22.1 script review: 11 targeted checks PASS, including stale candidate callback, file-read race, language conversion persistence, forced charset budget, failed conversion rollback, six GZIP/ZLIB boundary cases. Earlier R01/R02/R05 targeted evidence inherited. Not browser E2E.
- User explicitly confirmed browser main flows manually on 2026-10-27: **PASS (user manual acceptance)**. Exact browser version, download-byte matrix and detailed case logs not provided; no assertion of full browser compatibility.
- RC4 GB18030 mapping: rebuilt independently with Python 3.13.5, 262144 bytes identical, 63488 BMP scalar values and 2048 surrogate entries checked; SHA-256 `a0aae8f074ce932296493ea19d022024fb37973087654a40bfd27ee2a60e2dde`.
- Browser automation: NOT RUN (prior environment access block classified ACTION_PATH_BLOCK). Source review completed by 03; independently regenerated table adopted and upstream license/attribution retained. See SOURCES.md and THIRD-PARTY-NOTICES.md.
- No application HTML changes after RC3 independent code review.

## 03 final checks
- Final application HTML remains byte-identical to reviewed RC3/RC4.
- Generator independently executed with CPython 3.12.14; all 262144 bytes match the embedded data, SHA-256 a0aae8f074ce932296493ea19d022024fb37973087654a40bfd27ee2a60e2dde.
- Current browser main-flow acceptance is recorded by T04 as the user statement: “浏览器主流程是人工验证的，我确认”. This is submitted user-manual acceptance, not a browser run independently performed by 03.
- Browser automation remains NOT RUN; complete download-byte and cross-browser matrices remain outside the established coverage.
