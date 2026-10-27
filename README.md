# FXB CodecLab v1.0.0

A browser-based, offline-first encoding exploration and conversion utility. / 纯静态、离线优先的编码探索与转换工具。

## Use / 使用

- **Online / 在线**: https://dushizhazi.github.io/CodecLab/ (available after GitHub Pages is enabled)
- **Offline / 离线**: Download `index.html` and open it in a modern browser.
- Paste text or choose a local file, run automatic exploration, select a candidate, and optionally convert/export the result.

## Features / 功能

- Multi-layer encoding exploration, candidate ranking, and manual charset selection
- Common text and binary encodings, including UTF-8 and Chinese legacy encodings
- File inspection, copy/export, bilingual UI, dark/light themes, mobile-friendly layout
- Single-file distribution: no server-side processing required

## Privacy / 隐私

The application processes content locally in the browser. No upload server is required. Avoid submitting sensitive information to third-party websites when sharing results.

## Limitations / 限制

Automatic encoding detection is heuristic and may be wrong. Verify output before replacing original files. Browser support for some APIs and legacy encodings varies. The project is provided as-is.

## License

Application code: MIT — see [LICENSE](LICENSE). Mapping provenance and retained upstream terms: [SOURCES.md](SOURCES.md) and [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). FXB branding rights remain separate.

## Release

v1.0.0 — user-approved release baseline. Full cross-browser automated regression coverage has not been established.
