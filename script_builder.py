"""
Script Builder Module

Generates MusicBrainz Picard file naming scripts based on user configuration.
All generated code uses only valid Picard scripting syntax and real variables.
"""

from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime


@dataclass
class ScriptConfig:
    """Configuration for script generation"""
    
    # Folder Structure
    use_artist_folder: bool = True
    artist_folder_style: str = "standard"  # standard, sort, first_letter_subfolder
    use_album_folder: bool = True
    include_year_in_album: bool = True
    year_position: str = "prefix"  # prefix, suffix
    
    # Multi-disc Handling
    use_disc_subfolder: bool = True
    disc_folder_format: str = "disc"  # disc, side, cd
    include_disc_subtitle: bool = True
    
    # Track Number Format
    pad_track_number: bool = True
    track_padding_length: int = 2
    include_disc_in_track: bool = False
    
    # Filename Elements
    include_artist_in_filename: bool = False
    artist_separator: str = " - "
    include_track_number: bool = True
    include_title: bool = True
    
    # Various Artists Handling
    include_track_artist_for_va: bool = True
    va_artist_separator: str = " - "
    
    # Featured Artists
    show_featured_artists: bool = True
    feat_format: str = "feat."  # feat., ft., featuring, with
    
    # Release Type Handling
    separate_singles: bool = False
    separate_soundtracks: bool = False
    separate_compilations: bool = False
    
    # Character Replacements
    replace_invalid_chars: bool = True
    
    # Length Limits
    max_album_length: int = 100
    max_title_length: int = 100
    max_filename_length: int = 200
    
    # Special Options
    use_original_year: bool = True
    format_album_artist: str = "standard"  # standard, sort
    lowercase_extension: bool = False
    
    # Additional Info in Album Folder
    include_label: bool = False
    include_catalog: bool = False
    include_format: bool = False
    include_disambiguation: bool = False


class ScriptBuilder:
    """Builds Picard file naming scripts from configuration"""
    
    def __init__(self, config: ScriptConfig):
        self.config = config
        self.script_parts = []
    
    def build(self) -> str:
        """Generate the complete Picard script"""
        self.script_parts = []
        
        # Add header
        self._add_header()
        
        # Add user settings variables
        self._add_settings_section()
        
        # Add constants
        self._add_constants_section()
        
        # Add working variables
        self._add_working_variables()
        
        # Add character sanitization
        if self.config.replace_invalid_chars:
            self._add_character_sanitization()
        
        # Build the file path
        self._add_file_path_generation()
        
        # Build the filename
        self._add_filename_generation()
        
        # Add final output
        self._add_output()
        
        return "\n".join(self.script_parts)
    
    def _add_header(self):
        """Add script header with metadata"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.script_parts.append(f"""$noop(
########################################################################
#                                                                      #
#  MusicBrainz Picard File Naming Script                               #
#  Generated: {timestamp}                               #
#                                                                      #
#  Created with Picard Script Generator                                #
#                                                                      #
########################################################################
)
""")
    
    def _add_settings_section(self):
        """Add configurable settings section"""
        self.script_parts.append("""$noop(
########################################################################
#  USER SETTINGS - Modify these values to customize behavior           #
########################################################################
)""")
        
        self.script_parts.append(f"""
$noop( Padding minimum lengths )
$set(_PaddedDiscNumMinLength,1)
$set(_PaddedTrackNumMinLength,{self.config.track_padding_length})

$noop( Maximum lengths for truncation )
$set(_aTitleMaxLength,{self.config.max_album_length})
$set(_tTitleMaxLength,{self.config.max_title_length})
$set(_tFilenameMaxLength,{self.config.max_filename_length})
""")
    
    def _add_constants_section(self):
        """Add constants for special handling"""
        self.script_parts.append("""
$noop(
########################################################################
#  CONSTANTS                                                           #
########################################################################
)
$set(_cUnknownArtistID,125ec42a-7229-4250-afc5-e057484327fe)
$set(_cVariousArtistID,89ad4ac3-39f7-470e-963a-56509c546377)
$set(_cUnknownArtist,[Unknown Artist])
$set(_cVariousArtist,Various Artists)
$set(_cUnknownAlbum,[Unknown Album])
$set(_cNoTitle,[Unknown Title])
""")
    
    def _add_working_variables(self):
        """Add working variables with fallbacks"""
        self.script_parts.append("""
$noop(
########################################################################
#  WORKING VARIABLES - Set up variables with fallback values           #
########################################################################
)

$noop( Album Artist - with fallbacks )
$set(_nAlbumArtist,$if2(%albumartist%,%artist%,%_cUnknownArtist%))
$set(_nAlbumArtistSort,$if2(%albumartistsort%,%artistsort%,%_nAlbumArtist%))

$noop( Track Artist )
$set(_nTrackArtist,$if2(%artist%,%_cUnknownArtist%))

$noop( Album and Track titles )
$set(_nAlbum,$if2(%album%,%_cUnknownAlbum%))
$set(_nTitle,$if2(%title%,%_cNoTitle%))

$noop( Disc and track numbers with fallbacks )
$set(_nTotalDiscs,$if2(%totaldiscs%,1))
$set(_nDiscNum,$if2(%discnumber%,1))
$set(_nTotalTracks,$if2(%totaltracks%,1))
$set(_nTrackNum,$if2(%tracknumber%,1))
""")
        
        # Add year variable
        if self.config.use_original_year:
            self.script_parts.append("""
$noop( Release year - prefer original date )
$set(_nYear,$left($if2(%originaldate%,%originalyear%,%date%,0000),4))
""")
        else:
            self.script_parts.append("""
$noop( Release year )
$set(_nYear,$left($if2(%date%,%originaldate%,%originalyear%,0000),4))
""")
        
        # Padding calculations
        self.script_parts.append("""
$noop( Calculate padding lengths based on totals )
$set(_DiscPadLength,$if($gt($len(%_nTotalDiscs%),%_PaddedDiscNumMinLength%),$len(%_nTotalDiscs%),%_PaddedDiscNumMinLength%))
$set(_TrackPadLength,$if($gt($len(%_nTotalTracks%),%_PaddedTrackNumMinLength%),$len(%_nTotalTracks%),%_PaddedTrackNumMinLength%))

$noop( Padded disc and track numbers )
$set(_nPaddedDiscNum,$num(%_nDiscNum%,%_DiscPadLength%))
$set(_nPaddedTrackNum,$num(%_nTrackNum%,%_TrackPadLength%))
""")
    
    def _add_character_sanitization(self):
        """Add character sanitization for Windows compatibility"""
        self.script_parts.append("""
$noop(
########################################################################
#  CHARACTER SANITIZATION - Replace invalid characters                 #
########################################################################
)

$noop( Create sanitized versions of metadata for file/folder names )
$set(_nAlbumSafe,$rreplace(%_nAlbum%,[\\\\/:*?"<>|]+,_))
$set(_nTitleSafe,$rreplace(%_nTitle%,[\\\\/:*?"<>|]+,_))
$set(_nAlbumArtistSafe,$rreplace(%_nAlbumArtist%,[\\\\/:*?"<>|]+,_))
$set(_nTrackArtistSafe,$rreplace(%_nTrackArtist%,[\\\\/:*?"<>|]+,_))
""")
    
    def _add_file_path_generation(self):
        """Generate the folder path structure"""
        self.script_parts.append("""
$noop(
########################################################################
#  FOLDER PATH GENERATION                                              #
########################################################################
)
""")
        
        path_parts = []
        
        # Artist folder
        if self.config.use_artist_folder:
            if self.config.artist_folder_style == "first_letter_subfolder":
                self.script_parts.append("""
$noop( Get first letter for artist grouping )
$set(_nInitial,$upper($firstalphachar($if2(%_nAlbumArtistSort%,%_nAlbumArtistSafe%),#)))
""")
                path_parts.append("%_nInitial%")
            
            if self.config.format_album_artist == "sort":
                path_parts.append("%_nAlbumArtistSort%")
            else:
                if self.config.replace_invalid_chars:
                    path_parts.append("%_nAlbumArtistSafe%")
                else:
                    path_parts.append("%_nAlbumArtist%")
        
        # Handle Various Artists
        self.script_parts.append("""
$noop( Check for Various Artists )
$set(_isVA,$eq(%musicbrainz_albumartistid%,%_cVariousArtistID%))
""")
        
        # Separate soundtracks
        if self.config.separate_soundtracks:
            self.script_parts.append("""
$noop( Check for Soundtrack )
$set(_isSoundtrack,$in(%_secondaryreleasetype%,soundtrack))
""")
        
        # Album folder
        if self.config.use_album_folder:
            album_folder_parts = []
            
            if self.config.include_year_in_album:
                if self.config.year_position == "prefix":
                    album_folder_parts.append("[%_nYear%]")
                    if self.config.include_disambiguation:
                        if self.config.replace_invalid_chars:
                            album_folder_parts.append(" %_nAlbumSafe%$if(%_releasecomment%, \\(%_releasecomment%\\),)")
                        else:
                            album_folder_parts.append(" %_nAlbum%$if(%_releasecomment%, \\(%_releasecomment%\\),)")
                    else:
                        if self.config.replace_invalid_chars:
                            album_folder_parts.append(" %_nAlbumSafe%")
                        else:
                            album_folder_parts.append(" %_nAlbum%")
                else:
                    if self.config.replace_invalid_chars:
                        album_folder_parts.append("%_nAlbumSafe%")
                    else:
                        album_folder_parts.append("%_nAlbum%")
                    album_folder_parts.append(" [%_nYear%]")
            else:
                if self.config.replace_invalid_chars:
                    album_folder_parts.append("%_nAlbumSafe%")
                else:
                    album_folder_parts.append("%_nAlbum%")
            
            if self.config.include_label:
                album_folder_parts.append("$if(%label%, [%label%],)")
            
            if self.config.include_catalog:
                album_folder_parts.append("$if(%catalognumber%, {%catalognumber%},)")
            
            if self.config.include_format:
                album_folder_parts.append(" [$upper(%_extension%)]")
            
            path_parts.append("".join(album_folder_parts))
        
        # Build the path variable
        if path_parts:
            # Handle Various Artists path
            if self.config.use_artist_folder and self.config.separate_soundtracks:
                self.script_parts.append(f"""
$noop( Build folder path )
$set(_nFilePath,
    $if(%_isSoundtrack%,
        Soundtracks/{"/".join(path_parts[1:]) if len(path_parts) > 1 else path_parts[0]},
        $if(%_isVA%,
            %_cVariousArtist%/{path_parts[-1] if len(path_parts) > 0 else ""},
            {"/".join(path_parts)}
        )
    )
)
""")
            elif self.config.use_artist_folder:
                self.script_parts.append(f"""
$noop( Build folder path )
$set(_nFilePath,
    $if(%_isVA%,
        %_cVariousArtist%/{path_parts[-1] if len(path_parts) > 1 else path_parts[0]},
        {"/".join(path_parts)}
    )
)
""")
            else:
                self.script_parts.append(f"""
$noop( Build folder path )
$set(_nFilePath,{"/".join(path_parts)})
""")
        else:
            self.script_parts.append("""
$noop( No folder structure )
$set(_nFilePath,)
""")
        
        # Add disc subfolder for multi-disc releases
        if self.config.use_disc_subfolder:
            disc_name = {
                "disc": "Disc",
                "side": "Side", 
                "cd": "CD"
            }.get(self.config.disc_folder_format, "Disc")
            
            if self.config.include_disc_subtitle:
                self.script_parts.append(f"""
$noop( Add disc subfolder for multi-disc releases )
$if($gt(%_nTotalDiscs%,1),
    $set(_nFilePath,%_nFilePath%/{disc_name} %_nPaddedDiscNum%$if(%discsubtitle%, - %discsubtitle%,))
)
""")
            else:
                self.script_parts.append(f"""
$noop( Add disc subfolder for multi-disc releases )
$if($gt(%_nTotalDiscs%,1),
    $set(_nFilePath,%_nFilePath%/{disc_name} %_nPaddedDiscNum%)
)
""")
    
    def _add_filename_generation(self):
        """Generate the filename structure"""
        self.script_parts.append("""
$noop(
########################################################################
#  FILENAME GENERATION                                                 #
########################################################################
)
""")
        
        filename_parts = []
        
        # Track number
        if self.config.include_track_number:
            if self.config.include_disc_in_track and not self.config.use_disc_subfolder:
                filename_parts.append("$if($gt(%_nTotalDiscs%,1),%_nPaddedDiscNum%-,)%_nPaddedTrackNum%")
            else:
                filename_parts.append("%_nPaddedTrackNum%")
        
        # Artist (for Various Artists or if configured)
        if self.config.include_artist_in_filename or self.config.include_track_artist_for_va:
            artist_part = self.config.replace_invalid_chars and "%_nTrackArtistSafe%" or "%_nTrackArtist%"
            if self.config.include_artist_in_filename:
                filename_parts.append(f"{self.config.artist_separator}{artist_part}")
            elif self.config.include_track_artist_for_va:
                filename_parts.append(f"$if(%_isVA%,{self.config.va_artist_separator}{artist_part},)")
        
        # Title
        if self.config.include_title:
            title_part = self.config.replace_invalid_chars and "%_nTitleSafe%" or "%_nTitle%"
            if filename_parts:
                # Add separator if we have something before
                if self.config.include_track_number:
                    filename_parts.append(f". {title_part}")
                else:
                    filename_parts.append(f" - {title_part}")
            else:
                filename_parts.append(title_part)
        
        # Featured artists
        if self.config.show_featured_artists:
            feat_label = {
                "feat.": "feat.",
                "ft.": "ft.",
                "featuring": "featuring",
                "with": "with"
            }.get(self.config.feat_format, "feat.")
            
            self.script_parts.append(f"""
$noop( Determine if there are featured artists )
$set(_nFeat,
    $if($and($ne(%artist%,%albumartist%),$ne(%_isVA%,1)),
        $if($in(%artist%,feat.),
            ,
            $if($ne($lower(%artist%),$lower(%albumartist%)),
                 [{feat_label} %_nTrackArtist%],
            )
        ),
    )
)
""")
            filename_parts.append("%_nFeat%")
        
        # Build filename variable
        if filename_parts:
            self.script_parts.append(f"""
$noop( Build filename )
$set(_nFileName,{"".join(filename_parts)})
""")
        
        # Apply length limits
        self.script_parts.append("""
$noop( Truncate filename if too long )
$if($gt($len(%_nFileName%),%_tFilenameMaxLength%),
    $set(_nFileName,$left(%_nFileName%,$sub(%_tFilenameMaxLength%,3))...)
)
""")
    
    def _add_output(self):
        """Add the final output"""
        self.script_parts.append("""
$noop(
########################################################################
#  OUTPUT - Final path and filename                                    #
########################################################################
)

$noop( Combine path and filename, ensure no double slashes )
$if(%_nFilePath%,
    %_nFilePath%/%_nFileName%,
    %_nFileName%
)
""")


def generate_simple_script(
    include_artist: bool = True,
    include_album: bool = True,
    include_year: bool = True,
    include_track_number: bool = True,
    track_padding: int = 2
) -> str:
    """
    Generate a simple Picard script with minimal options.
    Perfect for users who just want something basic.
    """
    parts = []
    
    # Header
    parts.append("$noop( Simple Picard Naming Script )")
    parts.append("")
    
    # Build path
    path_components = []
    if include_artist:
        path_components.append("$if2(%albumartist%,%artist%,[Unknown Artist])")
    
    album_str = ""
    if include_album:
        if include_year:
            album_str = "[$left($if2(%originaldate%,%date%,0000),4)] $if2(%album%,[Unknown Album])"
        else:
            album_str = "$if2(%album%,[Unknown Album])"
        path_components.append(album_str)
    
    # Build filename
    filename = ""
    if include_track_number:
        filename = f"$num(%tracknumber%,{track_padding}). $if2(%title%,[Unknown Title])"
    else:
        filename = "$if2(%title%,[Unknown Title])"
    
    # Combine
    if path_components:
        full_path = "/".join(path_components) + "/" + filename
    else:
        full_path = filename
    
    # Sanitize
    parts.append(f"$rreplace({full_path},[\\\\/:*?\"<>|]+,_)")
    
    return "\n".join(parts)


def generate_advanced_script(config: ScriptConfig) -> str:
    """Generate an advanced Picard script from full configuration"""
    builder = ScriptBuilder(config)
    return builder.build()
