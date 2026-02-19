# MusicBrainz Picard File Naming Script Generator

A simple, user-friendly Python CLI tool that generates MusicBrainz Picard file naming scripts through an interactive menu-driven interface.

## What is this?

Creating Picard file naming scripts can be complex and time-consuming. This tool simplifies the process by letting you make simple selections and choices, then automatically generates the correct Picard scripting code for you.

## Features

- **Simple Interactive Menu** - No scripting knowledge required
- **Preset Templates** - Start with common configurations
- **Customizable** - Fine-tune every aspect of your naming scheme
- **Valid Output** - Generated scripts are syntactically correct
- **Instant Preview** - See example output before saving
- **Export to File** - Save your script ready to import into Picard

## Installation

```bash
# Clone or download this repository
cd WBs-Picard-Filenaming-Script-Generator

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python picard_script_generator.py
```

Then follow the interactive prompts to build your script.

## Quick Start

1. Run the generator
2. Choose a preset template or start from scratch
3. Customize your folder structure
4. Customize your filename format
5. Preview the output
6. Save to file

## Generated Script

The generated script will be saved as `my_picard_script.pts` in the same directory as the generator. You can then import this into Picard:

1. Open MusicBrainz Picard
2. Go to Options → Options → File Naming
3. Click "Import" and select your generated script

## Requirements

- Python 3.8+
- rich
- questionary

## License

MIT License
