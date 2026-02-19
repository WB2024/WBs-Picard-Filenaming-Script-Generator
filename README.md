# MusicBrainz Picard File Naming Script Generator

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?logo=buy-me-a-coffee)](https://buymeacoffee.com/succinctrecords)

A simple, user-friendly Python CLI tool that generates MusicBrainz Picard file naming scripts through an interactive menu-driven interface.

**No scripting knowledge required!** Just answer a few simple questions, and get perfectly formatted Picard scripts ready to use.

---

## What is this?

[MusicBrainz Picard](https://picard.musicbrainz.org/) is a powerful music tagger that can automatically organize your music library. However, creating custom file naming scripts requires learning Picard's scripting language and can be complex and error-prone.

**This tool solves that problem.** It provides:
- 🎯 **Simple interactive menus** - No coding required
- 📦 **6 ready-to-use preset templates** - Common configurations already built
- 🔧 **Full customization** - Fine-tune every detail if you want
- ✅ **Guaranteed valid output** - Generated scripts use only real Picard variables and proper syntax
- 👀 **Live preview** - See examples before saving
- 💾 **One-click export** - Save and import directly into Picard

Creating Picard file naming scripts can be complex and time-consuming. This tool simplifies the process by letting you make simple selections and choices, then automatically generates the correct Picard scripting code for you.

---

## Why Use This Generator?

✨ **Save Time** - Create complex scripts in minutes, not hours  
🛡️ **Error-Free** - No syntax errors, all variables are real and validated  
📚 **Learn by Example** - See how Picard scripts work by examining the output  
🎨 **Flexible** - From simple to advanced configurations  
🔄 **Reusable** - Save and share your configurations  

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/WB2024/WBs-Picard-Filenaming-Script-Generator.git
   cd WBs-Picard-Filenaming-Script-Generator
   ```

   Or download the ZIP file from GitHub and extract it.

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - `rich` - For beautiful terminal output
   - `questionary` - For interactive menus

3. **Verify installation**

   ```bash
   python picard_script_generator.py
   ```

   You should see the main menu appear.

## Usage

Run the generator from the command line:

```bash
python picard_script_generator.py
```

Then follow the interactive prompts to build your script.

## Quick Start Guide

### Option 1: Use a Preset (Fastest)

1. Run `python picard_script_generator.py`
2. Select **"🚀 Quick Start - Use a preset template"**
3. Choose a preset that matches your needs
4. Preview the example output
5. Choose **"✓ Generate this script"**
6. Save the script
7. Import into Picard

### Option 2: Customize a Preset

1. Run the generator
2. Select **"🚀 Quick Start - Use a preset template"**
3. Choose a starting preset
4. Select **"📝 Customize this preset"**
5. Modify settings interactively
6. Preview and save

### Option 3: Build from Scratch

1. Run the generator
2. Select **"🔧 Custom Build - Configure everything step by step"**
3. Answer the wizard questions:
   - Folder structure (Artist? Album?)
   - Album details (Year? Label? Catalog?)
   - Multi-disc handling (Subfolders? Numbering?)
   - Filename format (Track numbers? Featured artists?)
   - Special handling (Various Artists? Soundtracks?)
4. Preview and save

## Example Output

Here's what your files might look like with different presets:

### Simple Preset
```
Music/
├── The Beatles/
│   └── [1969] Abbey Road/
│       ├── 01. Come Together.mp3
│       ├── 02. Something.mp3
│       └── 03. Maxwell's Silver Hammer.mp3
└── Pink Floyd/
    └── [1973] The Dark Side of the Moon/
        ├── 01. Speak to Me.mp3
        └── 02. Breathe.mp3
```

### Organized Preset (with alphabetical grouping)
```
Music/
├── B/
│   └── Beatles, The/
│       └── [1969] Abbey Road (Remaster)/
│           └── Disc 1/
│               ├── 01. Come Together.mp3
│               └── 02. Something.mp3
└── P/
    └── Pink Floyd/
        └── [1973] The Dark Side of the Moon/
            └── Disc 1/
                └── 01. Speak to Me.mp3
```

### Various Artists Albums
```
Music/
└── Various Artists/
    └── [2020] Now That's What I Call Music 75/
        ├── 01. Artist A - Track Title.mp3
        ├── 02. Artist B - Track Title.mp3
        └── 03. Artist C - Track Title.mp3
```

## Generated Script

The generated script will be saved as `my_picard_script.pts` (or your custom name) in the same directory as the generator. 

### Importing into Picard

1. Open MusicBrainz Picard
2. Go to **Options → Options → File Naming**
3. Click **"Import"** and select your generated `.pts` file
4. Enable **"Rename files when saving"**
5. Click **OK**

Your files will now be organized according to your custom naming scheme!

## Available Presets

- **Simple** - `Artist/[Year] Album/01. Title`
- **Organized** - `A/Artist/[Year] Album/Disc 1/01. Title`
- **Detailed** - `A/Artist/[Year] Album [Label] {Cat#}/01. Title`
- **Flat** - `Artist/[Year] Album/1-01. Title` (no disc subfolders)
- **Minimal** - `Album/01. Artist - Title` (no artist folders)
- **Audiophile** - `B/Beatles, The/[Year] Album [FLAC]/01. Title`

## Features

All generated scripts include:
- ✅ Valid Picard TaggerScript syntax
- ✅ Real MusicBrainz variables (verified, no made-up variables)
- ✅ Proper fallback values for missing metadata
- ✅ Windows/Linux/macOS compatible character handling
- ✅ Multi-disc album support
- ✅ Various Artists handling
- ✅ Featured artists detection
- ✅ Configurable track number padding
- ✅ Optional year, label, catalog number, format display

## Troubleshooting

**Import Error: Missing packages**
```bash
pip install --upgrade rich questionary
```

**Script doesn't start**
- Ensure you're using Python 3.8 or higher: `python --version`
- Try using `python3` instead of `python` on some systems

**Generated script has errors in Picard**
- The generator only uses valid Picard syntax and real variables
- If issues occur, please report them on GitHub Issues

## Support the Project

If you find this tool useful, consider supporting its development:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?logo=buy-me-a-coffee)](https://buymeacoffee.com/succinctrecords)

Your support helps maintain and improve this project. Thank you! ☕

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add new preset templates

## License

MIT License
