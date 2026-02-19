"""
Preset Templates for Picard Script Generator

Pre-configured script settings for common use cases.
Users can select a preset and optionally customize it further.
"""

from script_builder import ScriptConfig


def get_preset_simple() -> ScriptConfig:
    """
    Simple preset - Basic folder and filename structure
    
    Output format:
    Artist/[Year] Album/01. Title.ext
    """
    return ScriptConfig(
        use_artist_folder=True,
        artist_folder_style="standard",
        use_album_folder=True,
        include_year_in_album=True,
        year_position="prefix",
        use_disc_subfolder=True,
        disc_folder_format="disc",
        include_disc_subtitle=False,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=False,
        include_artist_in_filename=False,
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=True,
        show_featured_artists=False,
        separate_singles=False,
        separate_soundtracks=False,
        replace_invalid_chars=True,
        max_album_length=100,
        max_title_length=100,
        max_filename_length=200,
        use_original_year=True,
        format_album_artist="standard",
        include_label=False,
        include_catalog=False,
        include_format=False,
        include_disambiguation=False,
    )


def get_preset_organized() -> ScriptConfig:
    """
    Organized preset - Alphabetical folders with disc subfolders
    
    Output format:
    A/Artist/[Year] Album/Disc 1/01. Title.ext
    """
    return ScriptConfig(
        use_artist_folder=True,
        artist_folder_style="first_letter_subfolder",
        use_album_folder=True,
        include_year_in_album=True,
        year_position="prefix",
        use_disc_subfolder=True,
        disc_folder_format="disc",
        include_disc_subtitle=True,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=False,
        include_artist_in_filename=False,
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=True,
        show_featured_artists=True,
        feat_format="feat.",
        separate_singles=False,
        separate_soundtracks=True,
        replace_invalid_chars=True,
        max_album_length=80,
        max_title_length=80,
        max_filename_length=180,
        use_original_year=True,
        format_album_artist="standard",
        include_label=False,
        include_catalog=False,
        include_format=False,
        include_disambiguation=True,
    )


def get_preset_detailed() -> ScriptConfig:
    """
    Detailed preset - Full metadata in folder names
    
    Output format:
    A/Artist/[Year] Album [Label] {Catalog}/Disc 1 - Subtitle/01. Title [feat. Artist].ext
    """
    return ScriptConfig(
        use_artist_folder=True,
        artist_folder_style="first_letter_subfolder",
        use_album_folder=True,
        include_year_in_album=True,
        year_position="prefix",
        use_disc_subfolder=True,
        disc_folder_format="disc",
        include_disc_subtitle=True,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=False,
        include_artist_in_filename=False,
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=True,
        va_artist_separator=" - ",
        show_featured_artists=True,
        feat_format="feat.",
        separate_singles=False,
        separate_soundtracks=True,
        replace_invalid_chars=True,
        max_album_length=100,
        max_title_length=100,
        max_filename_length=200,
        use_original_year=True,
        format_album_artist="standard",
        include_label=True,
        include_catalog=True,
        include_format=False,
        include_disambiguation=True,
    )


def get_preset_flat() -> ScriptConfig:
    """
    Flat preset - All files in artist folder, disc number in filename
    
    Output format:
    Artist/[Year] Album/1-01. Title.ext
    """
    return ScriptConfig(
        use_artist_folder=True,
        artist_folder_style="standard",
        use_album_folder=True,
        include_year_in_album=True,
        year_position="prefix",
        use_disc_subfolder=False,
        disc_folder_format="disc",
        include_disc_subtitle=False,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=True,
        include_artist_in_filename=False,
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=True,
        show_featured_artists=False,
        separate_singles=False,
        separate_soundtracks=False,
        replace_invalid_chars=True,
        max_album_length=100,
        max_title_length=100,
        max_filename_length=200,
        use_original_year=True,
        format_album_artist="standard",
        include_label=False,
        include_catalog=False,
        include_format=False,
        include_disambiguation=False,
    )


def get_preset_minimal() -> ScriptConfig:
    """
    Minimal preset - Just album folders with tracks
    
    Output format:
    Album/01. Title.ext
    """
    return ScriptConfig(
        use_artist_folder=False,
        artist_folder_style="standard",
        use_album_folder=True,
        include_year_in_album=False,
        year_position="prefix",
        use_disc_subfolder=False,
        disc_folder_format="disc",
        include_disc_subtitle=False,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=True,
        include_artist_in_filename=True,
        artist_separator=" - ",
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=False,
        show_featured_artists=False,
        separate_singles=False,
        separate_soundtracks=False,
        replace_invalid_chars=True,
        max_album_length=100,
        max_title_length=100,
        max_filename_length=200,
        use_original_year=True,
        format_album_artist="standard",
        include_label=False,
        include_catalog=False,
        include_format=False,
        include_disambiguation=False,
    )


def get_preset_audiophile() -> ScriptConfig:
    """
    Audiophile preset - Includes format info, sorted by artist sort name
    
    Output format:
    A/Artist, The/[Year] Album [FLAC]/Disc 1/01. Title.ext
    """
    return ScriptConfig(
        use_artist_folder=True,
        artist_folder_style="first_letter_subfolder",
        use_album_folder=True,
        include_year_in_album=True,
        year_position="prefix",
        use_disc_subfolder=True,
        disc_folder_format="disc",
        include_disc_subtitle=True,
        pad_track_number=True,
        track_padding_length=2,
        include_disc_in_track=False,
        include_artist_in_filename=False,
        include_track_number=True,
        include_title=True,
        include_track_artist_for_va=True,
        show_featured_artists=True,
        feat_format="feat.",
        separate_singles=False,
        separate_soundtracks=True,
        replace_invalid_chars=True,
        max_album_length=100,
        max_title_length=100,
        max_filename_length=200,
        use_original_year=True,
        format_album_artist="sort",
        include_label=False,
        include_catalog=False,
        include_format=True,
        include_disambiguation=True,
    )


# Dictionary of all available presets
PRESETS = {
    "simple": {
        "name": "Simple",
        "description": "Basic: Artist/[Year] Album/01. Title",
        "getter": get_preset_simple,
        "example": "The Beatles/[1969] Abbey Road/01. Come Together.mp3"
    },
    "organized": {
        "name": "Organized",
        "description": "Alphabetical: A/Artist/[Year] Album/Disc 1/01. Title",
        "getter": get_preset_organized,
        "example": "T/The Beatles/[1969] Abbey Road (Remaster)/Disc 1/01. Come Together.mp3"
    },
    "detailed": {
        "name": "Detailed",
        "description": "Full info: A/Artist/[Year] Album [Label] {Cat#}/01. Title",
        "getter": get_preset_detailed,
        "example": "T/The Beatles/[1969] Abbey Road [Apple] {PCS7088}/01. Come Together.mp3"
    },
    "flat": {
        "name": "Flat",
        "description": "No disc folders: Artist/[Year] Album/1-01. Title",
        "getter": get_preset_flat,
        "example": "The Beatles/[1969] Abbey Road/1-01. Come Together.mp3"
    },
    "minimal": {
        "name": "Minimal",
        "description": "Album only: Album/01. Artist - Title",
        "getter": get_preset_minimal,
        "example": "Abbey Road/01. The Beatles - Come Together.mp3"
    },
    "audiophile": {
        "name": "Audiophile",
        "description": "With format: A/Artist/[Year] Album [FLAC]/01. Title",
        "getter": get_preset_audiophile,
        "example": "B/Beatles, The/[1969] Abbey Road [FLAC]/01. Come Together.flac"
    },
}


def get_preset_list():
    """Get list of preset names and descriptions"""
    return [(key, preset["name"], preset["description"]) 
            for key, preset in PRESETS.items()]


def get_preset_by_name(name: str) -> ScriptConfig:
    """Get a preset configuration by name"""
    if name in PRESETS:
        return PRESETS[name]["getter"]()
    raise ValueError(f"Unknown preset: {name}")


def get_preset_example(name: str) -> str:
    """Get example output for a preset"""
    if name in PRESETS:
        return PRESETS[name]["example"]
    return ""
