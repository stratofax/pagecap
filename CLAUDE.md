# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note: This project is archived.** Consider using [Playwright](https://playwright.dev/) for modern web capture needs.

## Project Overview

pagecap is a Python CLI tool that captures web pages as PNG screenshots using Selenium with headless Chrome. Requires Python 3.12+.

## Commands

```bash
# Setup
pipenv install          # Install dependencies
pipenv shell            # Activate virtual environment

# Run
python pagecap <url> [<url2> ...]   # Capture up to 7 URLs as PNGs
python pagecap --help               # Show help
python pagecap --version            # Show version

# Development
pylint pagecap/         # Lint the code
```

## Architecture

Single-package structure in `pagecap/`:
- `__main__.py` - CLI entry point using Click; contains `capture_page()` command and `make_png()` screenshot function
- `pagecap_metadata.py` - Package metadata (version, author, etc.) used by Click's `--version` option

The tool uses Selenium WebDriver to launch headless Chrome, dynamically sizes the browser window to the full page dimensions, and captures the body element as a PNG. Output files are numbered sequentially (1.png, 2.png, etc.) in the current directory.

## Dependencies

- **click** - CLI framework
- **selenium** - Browser automation (requires Chrome and matching ChromeDriver installed separately)
- **pylint** - Dev dependency for linting
