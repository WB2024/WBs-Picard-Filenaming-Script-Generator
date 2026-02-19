#!/usr/bin/env python3
"""
MusicBrainz Picard File Naming Script Generator

A simple CLI tool to generate Picard file naming scripts through
an interactive menu-driven interface.

Run: python picard_script_generator.py
"""

import os
import sys
from pathlib import Path
from datetime import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich import box
    import questionary
    from questionary import Style
except ImportError:
    print("Missing required packages. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "questionary"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich import box
    import questionary
    from questionary import Style

from script_builder import ScriptConfig, ScriptBuilder, generate_simple_script
from presets import PRESETS, get_preset_by_name, get_preset_example

# Initialize Rich console
console = Console()

# Custom questionary style
custom_style = Style([
    ('qmark', 'fg:cyan bold'),
    ('question', 'fg:white bold'),
    ('answer', 'fg:green bold'),
    ('pointer', 'fg:cyan bold'),
    ('highlighted', 'fg:cyan bold'),
    ('selected', 'fg:green'),
    ('separator', 'fg:cyan'),
    ('instruction', 'fg:gray'),
])


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print the application header"""
    header = """
╔═══════════════════════════════════════════════════════════════════════╗
║           MusicBrainz Picard File Naming Script Generator             ║
║                                                                       ║
║        Generate perfect Picard scripts with simple selections         ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
    console.print(header, style="cyan")


def print_footer():
    """Print navigation hints"""
    console.print("\n[dim]Tip: Press Ctrl+C at any time to return to the main menu[/dim]")


def show_main_menu():
    """Display the main menu and get user choice"""
    clear_screen()
    print_header()
    
    choices = [
        questionary.Choice("🚀 Quick Start - Use a preset template", value="preset"),
        questionary.Choice("🔧 Custom Build - Configure everything step by step", value="custom"),
        questionary.Choice("📋 View Presets - See all available presets", value="view_presets"),
        questionary.Choice("❓ Help - Learn about Picard scripting", value="help"),
        questionary.Choice("🚪 Exit", value="exit"),
    ]
    
    answer = questionary.select(
        "What would you like to do?",
        choices=choices,
        style=custom_style,
    ).ask()
    
    return answer


def show_preset_selection():
    """Show preset selection menu"""
    clear_screen()
    print_header()
    console.print("\n[bold cyan]📦 Choose a Preset Template[/bold cyan]\n")
    
    # Build choices with descriptions
    choices = []
    for key, preset in PRESETS.items():
        label = f"{preset['name']}: {preset['description']}"
        choices.append(questionary.Choice(label, value=key))
    
    choices.append(questionary.Choice("← Back to Main Menu", value="back"))
    
    answer = questionary.select(
        "Select a preset:",
        choices=choices,
        style=custom_style,
    ).ask()
    
    return answer


def show_preset_details(preset_name: str):
    """Show details of a preset and ask for confirmation"""
    clear_screen()
    print_header()
    
    preset = PRESETS[preset_name]
    config = get_preset_by_name(preset_name)
    
    console.print(f"\n[bold green]✓ Selected: {preset['name']}[/bold green]\n")
    
    # Show example output
    console.print(Panel(
        f"[cyan]{preset['example']}[/cyan]",
        title="[bold]Example Output[/bold]",
        border_style="cyan"
    ))
    
    # Show configuration details
    table = Table(title="Configuration Details", box=box.ROUNDED)
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Artist Folder", "✓ Yes" if config.use_artist_folder else "✗ No")
    table.add_row("Album Folder", "✓ Yes" if config.use_album_folder else "✗ No")
    table.add_row("Year in Album", "✓ Yes" if config.include_year_in_album else "✗ No")
    table.add_row("Disc Subfolders", "✓ Yes" if config.use_disc_subfolder else "✗ No")
    table.add_row("Track Padding", str(config.track_padding_length))
    table.add_row("Featured Artists", "✓ Yes" if config.show_featured_artists else "✗ No")
    
    console.print(table)
    
    choices = [
        questionary.Choice("✓ Generate this script", value="generate"),
        questionary.Choice("📝 Customize this preset", value="customize"),
        questionary.Choice("← Back to preset list", value="back"),
    ]
    
    return questionary.select(
        "\nWhat would you like to do?",
        choices=choices,
        style=custom_style,
    ).ask()


def customize_config(config: ScriptConfig) -> ScriptConfig:
    """Allow user to customize a configuration"""
    clear_screen()
    print_header()
    console.print("\n[bold cyan]🔧 Customize Your Script[/bold cyan]")
    console.print("[dim]Modify the settings below. Press Enter to keep the default.[/dim]\n")
    
    while True:
        # Show current settings as a menu
        choices = [
            questionary.Choice(
                f"Artist Folder: {'Yes' if config.use_artist_folder else 'No'}", 
                value="artist_folder"
            ),
            questionary.Choice(
                f"Album Folder: {'Yes' if config.use_album_folder else 'No'}", 
                value="album_folder"
            ),
            questionary.Choice(
                f"Year in Album: {'Yes' if config.include_year_in_album else 'No'} ({config.year_position})", 
                value="year_album"
            ),
            questionary.Choice(
                f"Disc Subfolders: {'Yes' if config.use_disc_subfolder else 'No'}", 
                value="disc_subfolder"
            ),
            questionary.Choice(
                f"Track Number Padding: {config.track_padding_length} digits", 
                value="track_padding"
            ),
            questionary.Choice(
                f"Featured Artists: {'Yes' if config.show_featured_artists else 'No'}", 
                value="featured"
            ),
            questionary.Choice(
                f"Include Label: {'Yes' if config.include_label else 'No'}", 
                value="label"
            ),
            questionary.Choice(
                f"Include Catalog #: {'Yes' if config.include_catalog else 'No'}", 
                value="catalog"
            ),
            questionary.Choice(
                f"Include Format: {'Yes' if config.include_format else 'No'}", 
                value="format"
            ),
            questionary.Choice(
                f"Alphabetical Folders: {'Yes' if config.artist_folder_style == 'first_letter_subfolder' else 'No'}", 
                value="alpha_folders"
            ),
            questionary.Separator(),
            questionary.Choice("✓ Done - Generate script", value="done"),
            questionary.Choice("← Cancel", value="cancel"),
        ]
        
        answer = questionary.select(
            "Select a setting to modify:",
            choices=choices,
            style=custom_style,
        ).ask()
        
        if answer == "done" or answer == "cancel":
            return config if answer == "done" else None
        
        # Handle each setting
        if answer == "artist_folder":
            config.use_artist_folder = questionary.confirm(
                "Include artist folder?",
                default=config.use_artist_folder,
                style=custom_style,
            ).ask()
            
        elif answer == "album_folder":
            config.use_album_folder = questionary.confirm(
                "Include album folder?",
                default=config.use_album_folder,
                style=custom_style,
            ).ask()
            
        elif answer == "year_album":
            config.include_year_in_album = questionary.confirm(
                "Include year in album folder?",
                default=config.include_year_in_album,
                style=custom_style,
            ).ask()
            if config.include_year_in_album:
                config.year_position = questionary.select(
                    "Year position:",
                    choices=["prefix", "suffix"],
                    default=config.year_position,
                    style=custom_style,
                ).ask()
                
        elif answer == "disc_subfolder":
            config.use_disc_subfolder = questionary.confirm(
                "Use disc subfolders for multi-disc albums?",
                default=config.use_disc_subfolder,
                style=custom_style,
            ).ask()
            if config.use_disc_subfolder:
                config.disc_folder_format = questionary.select(
                    "Disc folder naming:",
                    choices=[
                        questionary.Choice("Disc 1, Disc 2...", value="disc"),
                        questionary.Choice("CD 1, CD 2...", value="cd"),
                        questionary.Choice("Side A, Side B... (for vinyl)", value="side"),
                    ],
                    style=custom_style,
                ).ask()
                
        elif answer == "track_padding":
            padding = questionary.select(
                "Track number padding:",
                choices=[
                    questionary.Choice("1 digit (1, 2, 3...)", value="1"),
                    questionary.Choice("2 digits (01, 02, 03...)", value="2"),
                    questionary.Choice("3 digits (001, 002, 003...)", value="3"),
                ],
                default=str(config.track_padding_length),
                style=custom_style,
            ).ask()
            config.track_padding_length = int(padding)
            
        elif answer == "featured":
            config.show_featured_artists = questionary.confirm(
                "Show featured artists in filename?",
                default=config.show_featured_artists,
                style=custom_style,
            ).ask()
            if config.show_featured_artists:
                config.feat_format = questionary.select(
                    "Featured artist format:",
                    choices=[
                        questionary.Choice("[feat. Artist]", value="feat."),
                        questionary.Choice("[ft. Artist]", value="ft."),
                        questionary.Choice("[featuring Artist]", value="featuring"),
                        questionary.Choice("[with Artist]", value="with"),
                    ],
                    style=custom_style,
                ).ask()
                
        elif answer == "label":
            config.include_label = questionary.confirm(
                "Include record label in album folder?",
                default=config.include_label,
                style=custom_style,
            ).ask()
            
        elif answer == "catalog":
            config.include_catalog = questionary.confirm(
                "Include catalog number in album folder?",
                default=config.include_catalog,
                style=custom_style,
            ).ask()
            
        elif answer == "format":
            config.include_format = questionary.confirm(
                "Include audio format (FLAC, MP3) in album folder?",
                default=config.include_format,
                style=custom_style,
            ).ask()
            
        elif answer == "alpha_folders":
            use_alpha = questionary.confirm(
                "Group artists alphabetically (A/, B/, C/...)?",
                default=config.artist_folder_style == "first_letter_subfolder",
                style=custom_style,
            ).ask()
            config.artist_folder_style = "first_letter_subfolder" if use_alpha else "standard"
    
    return config


def custom_build_wizard() -> ScriptConfig:
    """Step-by-step wizard to build a custom configuration"""
    clear_screen()
    print_header()
    console.print("\n[bold cyan]🔧 Custom Script Builder[/bold cyan]")
    console.print("[dim]Answer a few questions to build your perfect naming script.[/dim]\n")
    
    config = ScriptConfig()
    
    # Step 1: Folder Structure
    console.print("[bold]Step 1/5: Folder Structure[/bold]\n")
    
    config.use_artist_folder = questionary.confirm(
        "Create artist folders?",
        default=True,
        style=custom_style,
    ).ask()
    
    if config.use_artist_folder:
        use_alpha = questionary.confirm(
            "Group artists alphabetically (A/, B/, C/...)?",
            default=False,
            style=custom_style,
        ).ask()
        config.artist_folder_style = "first_letter_subfolder" if use_alpha else "standard"
        
        use_sort = questionary.confirm(
            "Use artist sort name? (e.g., 'Beatles, The' instead of 'The Beatles')",
            default=False,
            style=custom_style,
        ).ask()
        config.format_album_artist = "sort" if use_sort else "standard"
    
    config.use_album_folder = questionary.confirm(
        "Create album folders?",
        default=True,
        style=custom_style,
    ).ask()
    
    # Step 2: Album Folder Details
    console.print("\n[bold]Step 2/5: Album Folder Details[/bold]\n")
    
    if config.use_album_folder:
        config.include_year_in_album = questionary.confirm(
            "Include release year in album folder?",
            default=True,
            style=custom_style,
        ).ask()
        
        if config.include_year_in_album:
            config.year_position = questionary.select(
                "Year position:",
                choices=[
                    questionary.Choice("[Year] Album Name", value="prefix"),
                    questionary.Choice("Album Name [Year]", value="suffix"),
                ],
                style=custom_style,
            ).ask()
            
            config.use_original_year = questionary.confirm(
                "Prefer original release year over reissue year?",
                default=True,
                style=custom_style,
            ).ask()
        
        config.include_disambiguation = questionary.confirm(
            "Include disambiguation (e.g., 'Abbey Road (Remaster)')?",
            default=False,
            style=custom_style,
        ).ask()
        
        include_extra = questionary.confirm(
            "Include additional info in album folder?",
            default=False,
            style=custom_style,
        ).ask()
        
        if include_extra:
            config.include_label = questionary.confirm(
                "  Include record label?",
                default=False,
                style=custom_style,
            ).ask()
            config.include_catalog = questionary.confirm(
                "  Include catalog number?",
                default=False,
                style=custom_style,
            ).ask()
            config.include_format = questionary.confirm(
                "  Include audio format (FLAC, MP3)?",
                default=False,
                style=custom_style,
            ).ask()
    
    # Step 3: Multi-disc Handling
    console.print("\n[bold]Step 3/5: Multi-disc Albums[/bold]\n")
    
    config.use_disc_subfolder = questionary.confirm(
        "Create subfolders for multi-disc albums?",
        default=True,
        style=custom_style,
    ).ask()
    
    if config.use_disc_subfolder:
        config.disc_folder_format = questionary.select(
            "Disc folder naming:",
            choices=[
                questionary.Choice("Disc 1, Disc 2...", value="disc"),
                questionary.Choice("CD 1, CD 2...", value="cd"),
                questionary.Choice("Side A, Side B...", value="side"),
            ],
            style=custom_style,
        ).ask()
        
        config.include_disc_subtitle = questionary.confirm(
            "Include disc subtitle if available?",
            default=True,
            style=custom_style,
        ).ask()
    else:
        config.include_disc_in_track = questionary.confirm(
            "Include disc number in track number (1-01, 1-02)?",
            default=True,
            style=custom_style,
        ).ask()
    
    # Step 4: Filename Format
    console.print("\n[bold]Step 4/5: Filename Format[/bold]\n")
    
    config.include_track_number = questionary.confirm(
        "Include track number?",
        default=True,
        style=custom_style,
    ).ask()
    
    if config.include_track_number:
        padding = questionary.select(
            "Track number padding:",
            choices=[
                questionary.Choice("1 digit (1, 2, 3...)", value="1"),
                questionary.Choice("2 digits (01, 02, 03...)", value="2"),
                questionary.Choice("3 digits (001, 002, 003...)", value="3"),
            ],
            default="2",
            style=custom_style,
        ).ask()
        config.track_padding_length = int(padding)
    
    config.include_title = True  # Always include title
    
    config.include_artist_in_filename = questionary.confirm(
        "Always include artist in filename?",
        default=False,
        style=custom_style,
    ).ask()
    
    # Step 5: Special Handling
    console.print("\n[bold]Step 5/5: Special Handling[/bold]\n")
    
    config.include_track_artist_for_va = questionary.confirm(
        "Include track artist for Various Artists albums?",
        default=True,
        style=custom_style,
    ).ask()
    
    config.show_featured_artists = questionary.confirm(
        "Show featured artists in filename?",
        default=True,
        style=custom_style,
    ).ask()
    
    if config.show_featured_artists:
        config.feat_format = questionary.select(
            "Featured artist format:",
            choices=[
                questionary.Choice("[feat. Artist]", value="feat."),
                questionary.Choice("[ft. Artist]", value="ft."),
                questionary.Choice("[featuring Artist]", value="featuring"),
                questionary.Choice("[with Artist]", value="with"),
            ],
            style=custom_style,
        ).ask()
    
    config.separate_soundtracks = questionary.confirm(
        "Put soundtracks in a separate 'Soundtracks' folder?",
        default=False,
        style=custom_style,
    ).ask()
    
    return config


def preview_script(config: ScriptConfig):
    """Generate and preview the script"""
    clear_screen()
    print_header()
    console.print("\n[bold cyan]📝 Script Preview[/bold cyan]\n")
    
    # Build the script
    builder = ScriptBuilder(config)
    script = builder.build()
    
    # Show preview in a panel
    console.print(Panel(
        script,
        title="[bold]Generated Script[/bold]",
        border_style="green",
        expand=False
    ))
    
    return script


def save_script(script: str, filename: str = None) -> str:
    """Save the script to a file"""
    if filename is None:
        filename = questionary.text(
            "Enter filename (without extension):",
            default="my_picard_script",
            style=custom_style,
        ).ask()
    
    # Get the directory of the script
    script_dir = Path(__file__).parent
    filepath = script_dir / f"{filename}.pts"
    
    # Write the script
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(script)
    
    return str(filepath)


def show_presets_overview():
    """Show a table of all presets"""
    clear_screen()
    print_header()
    console.print("\n[bold cyan]📋 Available Presets[/bold cyan]\n")
    
    table = Table(title="Preset Templates", box=box.ROUNDED)
    table.add_column("Name", style="cyan bold")
    table.add_column("Description", style="white")
    table.add_column("Example Output", style="green")
    
    for key, preset in PRESETS.items():
        table.add_row(preset["name"], preset["description"], preset["example"])
    
    console.print(table)
    
    console.print("\n[dim]Press Enter to return to the main menu...[/dim]")
    input()


def show_help():
    """Show help and information about Picard scripting"""
    clear_screen()
    print_header()
    
    help_text = """
[bold cyan]About Picard File Naming Scripts[/bold cyan]

MusicBrainz Picard uses a scripting language called TaggerScript to format 
file and folder names when organizing your music library.

[bold]Basic Concepts:[/bold]

• [cyan]%variable%[/cyan] - References metadata tags (e.g., %artist%, %album%, %title%)
• [cyan]$function()[/cyan] - Calls functions (e.g., $upper(), $left(), $if())
• [cyan]$set(var,value)[/cyan] - Creates custom variables
• [cyan]$noop(text)[/cyan] - Comments (ignored by Picard)

[bold]Common Variables:[/bold]

• %artist% - Track artist
• %albumartist% - Album artist
• %album% - Album title
• %title% - Track title
• %tracknumber% - Track number
• %totaltracks% - Total tracks
• %discnumber% - Disc number
• %date% - Release date
• %originaldate% - Original release date
• %_extension% - File extension (mp3, flac, etc.)

[bold]Common Functions:[/bold]

• $if(condition,then,else) - Conditional logic
• $if2(a,b,c) - Returns first non-empty value
• $num(number,digits) - Pad numbers (e.g., $num(5,2) = "05")
• $left(text,n) - Get first n characters
• $replace(text,old,new) - Replace text
• $upper(text) / $lower(text) - Change case

[bold]How This Generator Works:[/bold]

This tool asks you simple questions about how you want your files organized,
then generates the correct Picard script automatically. The generated script
uses only valid Picard syntax and real metadata variables.

[bold]After Generating:[/bold]

1. Copy the generated script or use the saved .pts file
2. Open MusicBrainz Picard
3. Go to Options → Options → File Naming
4. Paste or import your script
5. Enable "Rename files when saving"

Press Enter to return to the main menu...
"""
    console.print(help_text)
    input()


def main():
    """Main application entry point"""
    try:
        while True:
            choice = show_main_menu()
            
            if choice == "exit" or choice is None:
                console.print("\n[cyan]Goodbye! Happy organizing! 🎵[/cyan]\n")
                break
            
            elif choice == "preset":
                while True:
                    preset_choice = show_preset_selection()
                    
                    if preset_choice == "back" or preset_choice is None:
                        break
                    
                    action = show_preset_details(preset_choice)
                    
                    if action == "generate":
                        config = get_preset_by_name(preset_choice)
                        script = preview_script(config)
                        
                        if questionary.confirm(
                            "\nSave this script to a file?",
                            default=True,
                            style=custom_style,
                        ).ask():
                            filepath = save_script(script)
                            console.print(f"\n[bold green]✓ Script saved to:[/bold green] {filepath}")
                            console.print("\n[dim]Press Enter to continue...[/dim]")
                            input()
                        break
                    
                    elif action == "customize":
                        config = get_preset_by_name(preset_choice)
                        config = customize_config(config)
                        
                        if config is not None:
                            script = preview_script(config)
                            
                            if questionary.confirm(
                                "\nSave this script to a file?",
                                default=True,
                                style=custom_style,
                            ).ask():
                                filepath = save_script(script)
                                console.print(f"\n[bold green]✓ Script saved to:[/bold green] {filepath}")
                                console.print("\n[dim]Press Enter to continue...[/dim]")
                                input()
                        break
                    
                    elif action == "back":
                        continue
            
            elif choice == "custom":
                config = custom_build_wizard()
                script = preview_script(config)
                
                if questionary.confirm(
                    "\nSave this script to a file?",
                    default=True,
                    style=custom_style,
                ).ask():
                    filepath = save_script(script)
                    console.print(f"\n[bold green]✓ Script saved to:[/bold green] {filepath}")
                    console.print("\n[dim]Press Enter to continue...[/dim]")
                    input()
            
            elif choice == "view_presets":
                show_presets_overview()
            
            elif choice == "help":
                show_help()
    
    except KeyboardInterrupt:
        console.print("\n\n[cyan]Returning to main menu...[/cyan]")
        main()


if __name__ == "__main__":
    main()
