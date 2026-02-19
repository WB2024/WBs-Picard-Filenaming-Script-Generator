"""
Picard Script Components Library

Contains all valid MusicBrainz Picard variables, functions, and script snippets.
This ensures generated scripts use only valid, real variables - no made-up ones.
"""

# =============================================================================
# STANDARD MUSICBRAINZ TAGS (Available in all Picard installations)
# =============================================================================

STANDARD_TAGS = {
    # Basic Track Info
    "title": "Track title",
    "artist": "Track artist name",
    "artists": "Track artist names (multi-value)",
    "album": "Album title",
    "albumartist": "Album artist name",
    "albumartists": "Album artists (multi-value)",
    "tracknumber": "Track number on disc",
    "totaltracks": "Total tracks on disc",
    "discnumber": "Disc number",
    "totaldiscs": "Total discs in release",
    "discsubtitle": "Disc subtitle (if any)",
    
    # Dates
    "date": "Release date",
    "originaldate": "Original release date",
    "originalyear": "Original release year",
    
    # Release Info
    "releasetype": "Release type(s) - album, single, ep, etc.",
    "releasestatus": "Release status - Official, Promotion, Bootleg",
    "releasecountry": "Release country",
    "label": "Record label",
    "catalognumber": "Catalog number",
    "barcode": "Barcode",
    "media": "Media type - CD, Vinyl, Digital Media",
    "compilation": "Compilation flag (1 if true)",
    
    # People
    "composer": "Track composer",
    "conductor": "Conductor",
    "performer": "Performer(s)",
    "writer": "Writer",
    "lyricist": "Lyricist",
    
    # Sorting
    "artistsort": "Artist sort name",
    "albumartistsort": "Album artist sort name",
    "titlesort": "Title sort name",
    "albumsort": "Album sort name",
    
    # Genre/Mood
    "genre": "Genre",
    "mood": "Mood",
    
    # Technical (from audio file)
    "_bitrate": "Audio bitrate",
    "_sample_rate": "Sample rate (Hz)",
    "_bits_per_sample": "Bit depth",
    "_channels": "Number of audio channels",
    "_extension": "File extension (mp3, flac, etc.)",
    "_filename": "Original filename without extension",
    "_length": "Track length (mm:ss)",
    "_format": "Audio format name",
    
    # MusicBrainz IDs
    "musicbrainz_artistid": "MusicBrainz artist ID",
    "musicbrainz_albumid": "MusicBrainz album ID",
    "musicbrainz_albumartistid": "MusicBrainz album artist ID",
    "musicbrainz_trackid": "MusicBrainz track ID",
    "musicbrainz_recordingid": "MusicBrainz recording ID",
    "musicbrainz_releasegroupid": "MusicBrainz release group ID",
    
    # Internal Picard Variables
    "_releasecomment": "Release disambiguation comment",
    "_primaryreleasetype": "Primary release type",
    "_secondaryreleasetype": "Secondary release types",
    "_musicbrainz_tracknumber": "MusicBrainz track number (A1, B2 for vinyl)",
    "_absolutetracknumber": "Absolute track number across all discs",
    "_totalalbumtracks": "Total tracks on album (all discs)",
}

# =============================================================================
# ADDITIONAL ARTISTS VARIABLES PLUGIN TAGS
# (Available when "Additional Artists Variables" plugin is installed)
# =============================================================================

PLUGIN_ADDITIONAL_ARTISTS_TAGS = {
    # Album Artists
    "_artists_album_primary_std": "Primary album artist (standardized)",
    "_artists_album_primary_cred": "Primary album artist (as credited)",
    "_artists_album_primary_sort": "Primary album artist (sort name)",
    "_artists_album_all_std": "All album artists (standardized)",
    "_artists_album_all_cred": "All album artists (as credited)",
    "_artists_album_all_sort": "All album artists (sort names)",
    "_artists_album_all_sort_primary": "Primary artist sort + additional standard",
    "_artists_album_additional_std": "Additional album artists (standardized)",
    "_artists_album_additional_cred": "Additional album artists (as credited)",
    "_artists_album_count": "Number of album artists",
    
    # Track Artists
    "_artists_track_primary_std": "Primary track artist (standardized)",
    "_artists_track_primary_cred": "Primary track artist (as credited)",
    "_artists_track_primary_sort": "Primary track artist (sort name)",
    "_artists_track_all_std": "All track artists (standardized)",
    "_artists_track_all_cred": "All track artists (as credited)",
    "_artists_track_all_sort": "All track artists (sort names)",
    "_artists_track_additional_std": "Additional track artists (standardized)",
    "_artists_track_additional_cred": "Additional track artists (as credited)",
    "_artists_track_count": "Number of track artists",
}

# =============================================================================
# PICARD SCRIPTING FUNCTIONS
# =============================================================================

PICARD_FUNCTIONS = {
    # Assignment Functions
    "$set": "Set a variable: $set(name,value)",
    "$setmulti": "Set a multi-value variable: $setmulti(name,value,separator)",
    "$unset": "Remove a variable: $unset(name)",
    "$copy": "Copy tag value: $copy(new,old)",
    "$delete": "Delete a tag: $delete(name)",
    
    # Text Functions
    "$left": "Get leftmost characters: $left(text,n)",
    "$right": "Get rightmost characters: $right(text,n)",
    "$len": "Get length of text: $len(text)",
    "$upper": "Convert to uppercase: $upper(text)",
    "$lower": "Convert to lowercase: $lower(text)",
    "$title": "Convert to title case: $title(text)",
    "$replace": "Replace text: $replace(text,old,new)",
    "$rreplace": "Regex replace: $rreplace(text,regex,replacement)",
    "$rsearch": "Regex search: $rsearch(text,regex)",
    "$num": "Pad number: $num(number,length)",
    "$pad": "Pad text: $pad(text,length,char)",
    "$strip": "Strip whitespace: $strip(text)",
    "$trim": "Trim text: $trim(text)",
    "$substr": "Substring: $substr(text,start,end)",
    "$find": "Find position: $find(text,search)",
    "$firstalphachar": "First alphabetic char: $firstalphachar(text,default)",
    "$initials": "Get initials: $initials(text)",
    "$delprefix": "Delete prefix (The, A, An): $delprefix(text)",
    "$swapprefix": "Move prefix to end: $swapprefix(text)",
    "$reverse": "Reverse text: $reverse(text)",
    "$truncate": "Truncate text: $truncate(text,length)",
    "$firstwords": "Get first N words: $firstwords(text,n)",
    
    # Multi-Value Functions
    "$getmulti": "Get item from multi-value: $getmulti(name,index)",
    "$lenmulti": "Length of multi-value: $lenmulti(name)",
    "$join": "Join multi-value: $join(name,separator)",
    "$slice": "Slice multi-value: $slice(name,start,end)",
    "$sortmulti": "Sort multi-value: $sortmulti(name)",
    "$reversemulti": "Reverse multi-value: $reversemulti(name)",
    "$unique": "Remove duplicates: $unique(name)",
    "$map": "Map function to multi-value: $map(name,code)",
    "$foreach": "Loop over multi-value: $foreach(name,code)",
    "$performer": "Get performer by type: $performer(type)",
    
    # Conditional Functions
    "$if": "Conditional: $if(condition,then,else)",
    "$if2": "First non-empty: $if2(value1,value2,...)",
    "$eq": "Equals: $eq(a,b)",
    "$ne": "Not equals: $ne(a,b)",
    "$gt": "Greater than: $gt(a,b)",
    "$gte": "Greater than or equal: $gte(a,b)",
    "$lt": "Less than: $lt(a,b)",
    "$lte": "Less than or equal: $lte(a,b)",
    "$and": "Logical AND: $and(a,b)",
    "$or": "Logical OR: $or(a,b)",
    "$not": "Logical NOT: $not(a)",
    "$in": "Contains: $in(text,search)",
    "$inmulti": "Check if in multi-value: $inmulti(multi,value)",
    "$eq_any": "Equals any: $eq_any(value,option1,option2,...)",
    "$eq_all": "Equals all: $eq_all(value,a,b,...)",
    "$ne_any": "Not equals any: $ne_any(value,option1,option2,...)",
    "$ne_all": "Not equals all: $ne_all(value,a,b,...)",
    "$startswith": "Starts with: $startswith(text,prefix)",
    "$endswith": "Ends with: $endswith(text,suffix)",
    "$is_complete": "All tracks matched: $is_complete()",
    "$is_audio": "Is audio file: $is_audio()",
    "$is_video": "Is video file: $is_video()",
    "$is_multi": "Is multi-value: $is_multi(name)",
    
    # Mathematical Functions
    "$add": "Addition: $add(a,b)",
    "$sub": "Subtraction: $sub(a,b)",
    "$mul": "Multiplication: $mul(a,b)",
    "$div": "Division: $div(a,b)",
    "$mod": "Modulo: $mod(a,b)",
    "$min": "Minimum: $min(a,b)",
    "$max": "Maximum: $max(a,b)",
    
    # Date/Time Functions
    "$datetime": "Format date/time: $datetime(format)",
    "$dateformat": "Format date: $dateformat(date,format)",
    "$year": "Extract year: $year(date)",
    "$month": "Extract month: $month(date)",
    "$day": "Extract day: $day(date)",
    
    # Information Functions
    "$matchedtracks": "Number of matched tracks: $matchedtracks()",
    "$countryname": "Country name from code: $countryname(code)",
    
    # Loop Functions
    "$while": "While loop: $while(condition,code)",
    
    # Miscellaneous
    "$noop": "No operation (comment): $noop(text)",
    "$get": "Get variable value: $get(name)",
}

# =============================================================================
# SPECIAL MUSICBRAINZ IDs
# =============================================================================

SPECIAL_IDS = {
    "UNKNOWN_ARTIST_ID": "125ec42a-7229-4250-afc5-e057484327fe",
    "VARIOUS_ARTISTS_ID": "89ad4ac3-39f7-470e-963a-56509c546377",
}

# =============================================================================
# COMMON RELEASE TYPES
# =============================================================================

RELEASE_TYPES = {
    "primary": ["album", "single", "ep", "broadcast", "other"],
    "secondary": [
        "compilation", "soundtrack", "spokenword", "interview", "audiobook",
        "audio drama", "live", "remix", "dj-mix", "mixtape", "street", "demo"
    ],
}

# =============================================================================
# MEDIA TYPES
# =============================================================================

MEDIA_TYPES = [
    "CD", "Vinyl", "Digital Media", "Cassette", "DVD", "DVD-Audio", 
    "SACD", "Blu-ray", "HDCD", "USB Flash Drive", "Shellac", "Reel-to-Reel"
]

# =============================================================================
# FILE EXTENSIONS WITH FORMATS
# =============================================================================

AUDIO_FORMATS = {
    "mp3": {"name": "MP3", "lossy": True},
    "flac": {"name": "FLAC", "lossy": False},
    "m4a": {"name": "AAC", "lossy": True},
    "ogg": {"name": "Ogg Vorbis", "lossy": True},
    "opus": {"name": "Opus", "lossy": True},
    "wav": {"name": "WAV", "lossy": False},
    "aiff": {"name": "AIFF", "lossy": False},
    "alac": {"name": "ALAC", "lossy": False},
    "ape": {"name": "APE", "lossy": False},
    "wma": {"name": "WMA", "lossy": True},
    "dsf": {"name": "DSD", "lossy": False},
    "dff": {"name": "DSD", "lossy": False},
    "mpc": {"name": "Musepack", "lossy": True},
    "wv": {"name": "WavPack", "lossy": False},
}

# =============================================================================
# WINDOWS INCOMPATIBLE CHARACTERS
# =============================================================================

WINDOWS_INVALID_CHARS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

# Character replacements for safe filenames
SAFE_REPLACEMENTS = {
    ':': '_',
    '?': '',
    '*': '',
    '<': '',
    '>': '',
    '|': '-',
    '"': "'",
    '/': '-',
    '\\': '-',
}
