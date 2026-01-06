# 🔒 Metadata Scrubber Tool

A privacy-focused CLI tool that removes sensitive metadata (EXIF, GPS, author info) from image files. Perfect for protecting your privacy before sharing photos online.

## ✨ Features

- **Multi-format support** - JPEG, PNG (with PDF/Office planned)
- **Concurrent processing** - Process 1000+ files efficiently with ThreadPoolExecutor
- **Dry-run mode** - Preview what would be scrubbed without making changes
- **Smart format detection** - Uses Pillow's format detection, not just file extensions
- **Beautiful CLI** - Rich progress bars and formatted output
- **Privacy-first** - Removes GPS coordinates, camera info, timestamps, author data

## 📚 Educational Value

This project demonstrates:
- **Factory pattern** for extensible file type handling
- **Abstract base classes** for consistent handler interfaces
- **Concurrent processing** with thread-safe operations
- **CLI development** with Typer and Rich
- **Image metadata handling** with Pillow and piexif

## 📋 Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Heritage-XioN/metadata-scrubber-tool.git
cd metadata-scrubber-tool

# Create virtual environment and install dependencies
uv venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

uv pip install -r requirements.txt
```

## 📖 Usage

### Read Metadata

```bash
# Single file
python -m src.main read photo.jpg

# Recursive directory scan
python -m src.main read ./photos/ -r -ext jpg
```

### Scrub Metadata

```bash
# Single file
python -m src.main scrub photo.jpg --output ./cleaned

# Batch process with 8 workers
python -m src.main scrub ./photos/ -r -ext jpg --output ./cleaned --workers 8

# Preview without changes
python -m src.main scrub ./photos/ -r -ext jpg --dry-run
```

### CLI Options

| Command | Options |
|---------|---------|
| `read` | `-r` / `--recursive`, `-ext` / `--extension` |
| `scrub` | `-r`, `-ext`, `-o` / `--output`, `-d` / `--dry-run`, `-w` / `--workers` |
| Global | `-V` / `--verbose`,  `-v` / `--version` |

## 🏗️ Architecture

```
src/
├── main.py                 # CLI entry point (Typer app)
├── commands/
│   ├── read.py            # Read metadata command
│   └── scrub.py           # Scrub metadata command (batch processing)
├── services/
│   ├── metadata_factory.py # Factory for creating handlers
│   ├── metadata_handler.py # Abstract base class
│   ├── image_handler.py    # JPEG/PNG handler
│   └── batch_processor.py  # Concurrent batch processing
├── core/
│   ├── jpeg_metadata.py    # JPEG EXIF processor (piexif)
│   └── png_metadata.py     # PNG metadata processor (PIL)
└── utils/
    ├── display.py          # Rich output formatting
    ├── formatter.py        # Value formatting helpers
    ├── exceptions.py       # Custom exceptions
    └── logger.py           # Logging configuration
```

**Data Flow:**
```
CLI Command → MetadataFactory → Handler (read→wipe→save) → Output
                    ↓
              Format Detection
                    ↓
           JpegProcessor / PngProcessor
```

## ⚠️ Security Considerations

- **Always backup files** before scrubbing in production
- **Use `--dry-run`** to preview changes before committing
- **GPS coordinates** are completely stripped for privacy
- **Original files are not modified** - processed copies are created

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

Made with ❤️ for privacy
