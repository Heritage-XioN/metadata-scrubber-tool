# 🔒 Metadata Scrubber

A privacy-focused CLI tool that removes sensitive metadata from files. Supports images, PDFs, and Microsoft Office documents. Perfect for protecting your privacy before sharing files online.

[![Tests](https://github.com/Heritage-XioN/metadata-scrubber-tool/actions/workflows/test.yml/badge.svg)](https://github.com/Heritage-XioN/metadata-scrubber-tool/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

- **Multi-format support** - Images (JPEG, PNG), PDFs, and Office docs (Word, Excel, PowerPoint)
- **Concurrent processing** - Process 1000+ files efficiently with ThreadPoolExecutor
- **Dry-run mode** - Preview what would be scrubbed without making changes
- **Smart format detection** - Uses library-level format detection, not just file extensions
- **Beautiful CLI** - Rich progress bars and formatted output
- **Privacy-first** - Removes GPS coordinates, author info, timestamps, camera data

## 📁 Supported Formats

| Category | Extensions | Metadata Removed |
|----------|------------|------------------|
| **Images** | `.jpg`, `.jpeg`, `.png` | EXIF, GPS, camera info, timestamps |
| **PDF** | `.pdf` | Author, creator, producer, dates |
| **Word** | `.docx` | Author, title, comments, keywords |
| **Excel** | `.xlsx`, `.xlsm`, `.xltx`, `.xltm` | Author, title, company, comments |
| **PowerPoint** | `.pptx`, `.pptm`, `.potx`, `.potm` | Author, title, comments, keywords |

## 🚀 Quick Start

### Installation

```bash
# Using uv (recommended)
uv pip install metadata-scrubber

# Or clone and install locally
git clone https://github.com/Heritage-XioN/metadata-scrubber-tool.git
cd metadata-scrubber-tool
uv sync
```

### Basic Usage

```bash
# Read metadata from a file
mst read document.pdf

# Scrub metadata and save to output folder
mst scrub photo.jpg --output ./cleaned

# Batch process entire folder
mst scrub ./documents -r -ext docx --output ./cleaned
```

## 📖 Commands

### `mst read` - View Metadata

```bash
mst read photo.jpg                      # Single file
mst read report.pdf                     # PDF file
mst read ./docs -r -ext docx            # All Word docs recursively
```

### `mst scrub` - Remove Metadata

```bash
mst scrub photo.jpg --output ./out      # Single file
mst scrub ./photos -r -ext jpg -o ./out # All JPEGs in directory
mst scrub ./docs -r -ext pdf --dry-run  # Preview PDF scrubbing
mst scrub ./files -r -ext xlsx -w 8     # 8 concurrent workers
```

### CLI Options

| Option | Description |
|--------|-------------|
| `-r`, `--recursive` | Process directories recursively |
| `-ext`, `--extension` | Filter by file extension |
| `-o`, `--output` | Output directory for cleaned files |
| `-d`, `--dry-run` | Preview without making changes |
| `-w`, `--workers` | Number of concurrent workers |
| `-V`, `--verbose` | Show detailed debug logs |
| `-v`, `--version` | Show version |

## 🛠️ Development

### Setup

```bash
git clone https://github.com/Heritage-XioN/metadata-scrubber-tool.git
cd metadata-scrubber-tool

# Install with dev dependencies
uv sync --all-extras

# Run tests
pytest

# Run linting
ruff check .

# Run type checking
mypy src
```

### Project Structure

```
src/
├── main.py                 # CLI entry point (Typer app)
├── commands/
│   ├── read.py             # Read metadata command
│   └── scrub.py            # Scrub metadata command
├── services/
│   ├── metadata_factory.py # Factory for creating handlers
│   ├── metadata_handler.py # Abstract base class
│   ├── image_handler.py    # JPEG/PNG handler
│   ├── pdf_handler.py      # PDF handler
│   ├── excel_handler.py    # Excel handler
│   ├── powerpoint_handler.py # PowerPoint handler
│   ├── worddoc_handler.py  # Word document handler
│   └── batch_processor.py  # Concurrent batch processing
└── core/
    ├── jpeg_metadata.py    # JPEG EXIF processor
    └── png_metadata.py     # PNG metadata processor
```

## ⚠️ Security Considerations

- **Original files are never modified** - processed copies are created
- **Use `--dry-run`** to preview changes before committing
- **GPS coordinates** are completely stripped for privacy
- **Author information** is removed from all supported formats
- **Always backup files** before scrubbing in production

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

Made with ❤️ for privacy
