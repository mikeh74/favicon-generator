# favicon-generator

A Python CLI tool to generate .ico favicon files from images (JPEG, PNG, or WEBP).

## Installation

Install using pipx (recommended):

```bash
pipx install favicon-generator
```

Or install with pip:

```bash
pip install favicon-generator
```

For development:

```bash
pip install -e .
```

## Usage

Basic usage:

```bash
favicon-generator image.png
```

This will create `image.ico` in the same directory.

Specify a custom output filename:

```bash
favicon-generator image.jpg -o my-favicon.ico
```

Crop image to square before processing:

```bash
favicon-generator image.webp --crop -o favicon.ico
```

### Options

- `INPUT_FILE`: Path to the input image (JPEG, PNG, or WEBP)
- `-o, --output`: Specify output .ico filename (default: input name with .ico extension)
- `-c, --crop`: Crop image to square before processing
- `--version`: Show version information
- `--help`: Show help message

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- WEBP (.webp)

## Features

- Converts images to multi-resolution .ico files
- Supports common image formats (JPEG, PNG, WEBP)
- Optional center-crop to square
- Custom output filenames
- Generates multiple icon sizes for better compatibility (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)

## License

MIT License - see LICENSE file for details
