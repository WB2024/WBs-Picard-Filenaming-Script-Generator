# PicardScripts/SCRIPT_GUIDE.md at master - PicardScripts - Gitea: Git with a cup of tea

Picard File Naming Script - Technical Guide
-------------------------------------------

Complete technical reference for MusicBrainz Picard File Naming Script v3.0

**Note:** This guide references `Picard_Rename_Script.txt` as the working script file. For importing into Picard, use `Picard_Rename_Script.ptsp` (Picard Script Package format).

* * *

Table of Contents
-----------------

1. [How Picard Scripting Works](#user-content-1-how-picard-scripting-works)
2. [Script Execution Flow](#user-content-2-script-execution-flow)
3. [Complete Configuration Options](#user-content-3-complete-configuration-options)
4. [Character Replacement](#user-content-4-character-replacement)
5. [VBR Bitrate Mapping](#user-content-5-vbr-bitrate-mapping)
6. [Path Generation Examples](#user-content-6-path-generation-examples)
7. [Advanced Features](#user-content-7-advanced-features)
8. [Variables Reference](#user-content-8-variables-reference)
9. [Customization Guide](#user-content-9-customization-guide)

* * *

1\. How Picard Scripting Works
------------------------------

### 1.1 What is TaggerScript?

TaggerScript is Picard's built-in scripting language for file naming and tag manipulation. It allows you to:

* Build file and folder paths dynamically from metadata
* Perform conditional logic based on tag values
* Transform and clean up metadata
* Set custom variables for use later in the script

### 1.2 Basic Syntax

**Functions** are called with `$function(arguments)`

**Variables** are referenced with `%variable%`

**Setting Variables** uses `$set(name,value)`

**Comments** use `$noop(text)`

### 1.3 Key Concepts

**Tags vs Variables:**

* **Tags** come from MusicBrainz or existing file metadata: `%artist%`, `%album%`, `%tracknumber%`
* **Variables** are created by the script: `%_myvar%`, `%_isLive%`, `%_nFilePath%`

**Execution Order:**

* Scripts execute top-to-bottom
* Variables must be defined before they're used
* The final output is whatever the script "returns" (last non-$noop statement)

**String Concatenation:**

* Just put values next to each other: `%artist% - %title%` -> "Beatles - Yesterday"
* Use `/` for path separators: `%artist%/%album%/` -> "Beatles/Abbey Road/"

* * *

2\. Script Execution Flow
-------------------------

### 2.1 Visual Flow Diagram

### 2.2 Step-by-Step Execution

**Step 1: Constants Loading**

* MusicBrainz special IDs loaded
* Default names set (\[Unknown Artist\], \[Various Artists\], etc.)
* Regex constants defined

**Step 2: Configuration Loading**

* All user settings loaded
* Settings determine which sections execute
* Settings control what metadata is shown

**Step 3: Default Variables**

* Plugin variables loaded with fallbacks
* If "Additional Artists Variables" plugin not present, uses basic tags
* Album and track titles get default values if missing

**Step 4: Working Variables Initialization**

* Disc and track numbers extracted
* Padding calculated based on total counts
* Featured artists detected by comparing album vs track artist
* Year extracted from date tags

**Step 5: Album Title Enhancement**

* Disambiguation comment added if present
* Release year, label, catalog added if enabled
* Title trimmed if longer than max length

**Step 6: Music Type Detection**

* All release type flags set based on MusicBrainz tags
* Special cases detected (Various Artists, Tribute, Cover, etc.)
* Incomplete status determined

**Step 7: Tag Cleanup**

* Placeholder tags removed if they still contain defaults
* Prevents "Title", "Artist" from being written to files

**Step 8: Filename Variables Setup**

* Sanitized versions created for all metadata used in paths
* Sort tags used as fallbacks
* "The " prefix removed for sorting

**Step 9: Character Filtering**

* Tag-level replacements (written to actual file metadata)
* Filename-level replacements (used in paths only)
* Ensures Windows/Linux/macOS/Samba compatibility

**Step 10: Audio Metrics Detection**

* Bitrate analyzed to determine CBR vs VBR
* VBR mapped to quality level (V0-V9)
* Sample rate, bit depth, channels extracted

**Step 11: Path Generation**

* Genre subsort applied first (if enabled)
* Special collections routed (Soundtrack, Various, Audiobooks)
* Artist letter folder created
* Artist name folder created
* Type subfolder added (if enabled)
* Album folder built with all metadata
* Disc subfolder added (if multi-disc)

**Step 12: Filename Generation**

* Track number formatted (padded or vinyl style)
* Track title added
* Duration added (if enabled)
* Audio quality added (if enabled)

**Output:**

* Complete path returned to Picard
* Picard moves/renames file to this location

* * *

3\. Complete Configuration Options
----------------------------------

### 3.1 All Settings Reference Table

* Variable: DEVELOPMENT SETTINGS
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _devMode
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Use test values (1) or real metadata (0)
* Variable: _quickNoNameFormat
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Skip formatting (1) or full format (0)
* Variable: DISPLAY OPTIONS
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _showDate
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Show year in album folder name
* Variable: _showRecordLabel
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Show record label in album folder
* Variable: _showReleaseStatus
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Show release status (Official, Promotion, etc.)
* Variable: _showCatalogueNumber
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Show catalog number in album folder
* Variable: _showIDNum
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Show MusicBrainz ID and catalog
* Variable: _showTime
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Show track duration in filename
* Variable: _showBandwidth
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Show audio quality metrics in filename
* Variable: PRIMARY ORGANIZATION
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _orderTypeForRoot
  * Type: Integer
  * Default: 2
  * Values: 1, 2
  * Description: 1=Category, 2=Artist letter folders
* Variable: _orderTypeForArtist
  * Type: Integer
  * Default: 1
  * Values: 1, 2, 3
  * Description: 1=First name, 2=Last name, 3=None
* Variable: _separateByTypeInArtistDirectory
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Separate albums/singles/EPs into subfolders
* Variable: _separateAlbum
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Put albums in Albums/ subfolder
* Variable: _rootLevelTypeSeparation
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Separate by file type at root (/MP3/, /FLAC/)
* Variable: _albumLevelTypeSeparation
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Separate by file type in album
* Variable: _albumNameAtTypeSeparation
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Show album name before type folder
* Variable: INCOMPLETE ALBUMS
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _extraTrackHandling
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: How to handle albums with extra tracks
* Variable: _earlierPresortForIncompletes
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Separate incomplete albums early
* Variable: MULTI-DISC
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _useSubDiscDirectory
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Multi-disc albums in disc subfolders
* Variable: _mergeDiscWhenNotUsingSubDirectory
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Skip disc folder if only one disc
* Variable: _showDiscSubtitle
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Show disc subtitle if present
* Variable: _nameForTypeCD
  * Type: String
  * Default: Disc
  * Values: -
  * Description: Name for CD disc folders
* Variable: _nameForTypeVinyl
  * Type: String
  * Default: Side
  * Values: -
  * Description: Name for vinyl disc folders
* Variable: _useMusicBrainzStyleForVinylTrack
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Use A1, B1 style for vinyl tracks
* Variable: SPECIAL COLLECTIONS
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _soundTracksDirectory
  * Type: String
  * Default: Soundtrack/
  * Values: -
  * Description: Soundtrack albums folder name
* Variable: _variousArtistsDirectory
  * Type: String
  * Default: Various/
  * Values: -
  * Description: Various Artists folder name
* Variable: _compilationsGSubDirectory
  * Type: String
  * Default: Compilations/
  * Values: -
  * Description: Global compilations folder name
* Variable: _audiobooksDirectory
  * Type: String
  * Default: Audiobook/
  * Values: -
  * Description: Audiobooks folder name
* Variable: _podcastSubDirectory
  * Type: String
  * Default: Podcast/
  * Values: -
  * Description: Podcasts folder name
* Variable: _incompleteDirectory
  * Type: String
  * Default: Partial
  * Values: -
  * Description: Incomplete albums suffix/folder name
* Variable: TYPE SUBFOLDER NAMES
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _albumSubDirectory
  * Type: String
  * Default: Albums/
  * Values: -
  * Description: Albums subfolder name
* Variable: _compilationsASubDirectory
  * Type: String
  * Default: Compilation/
  * Values: -
  * Description: Artist compilations subfolder
* Variable: _coverSubDirectory
  * Type: String
  * Default: Cover/
  * Values: -
  * Description: Cover albums subfolder
* Variable: _tributeSubDirectory
  * Type: String
  * Default: Tribute/
  * Values: -
  * Description: Tribute albums subfolder
* Variable: _singlesSubDirectory
  * Type: String
  * Default: Singles/
  * Values: -
  * Description: Singles subfolder
* Variable: _liveSubDirectory
  * Type: String
  * Default: Live/
  * Values: -
  * Description: Live albums subfolder
* Variable: _epSubDirectory
  * Type: String
  * Default: EP/
  * Values: -
  * Description: EPs subfolder
* Variable: _broadcastSubDirectory
  * Type: String
  * Default: Broadcast/
  * Values: -
  * Description: Broadcasts subfolder
* Variable: _interviewSubDirectory
  * Type: String
  * Default: Interview/
  * Values: -
  * Description: Interviews subfolder
* Variable: _videoSubDirectory
  * Type: String
  * Default: Video/
  * Values: -
  * Description: Videos subfolder
* Variable: _otherSubDirectory
  * Type: String
  * Default: Others/
  * Values: -
  * Description: Other releases subfolder
* Variable: GENRE SUBSORT
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _isSubSort
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: Enable genre-based pre-sorting
* Variable: _subSortGame
  * Type: String
  * Default: Arcade/
  * Values: -
  * Description: Game soundtracks folder
* Variable: _subSortDJBits
  * Type: String
  * Default: DJBits/
  * Values: -
  * Description: DJ/remix folder
* Variable: _subSortClassical
  * Type: String
  * Default: Classical/
  * Values: -
  * Description: Classical music folder
* Variable: _subSortDemento
  * Type: String
  * Default: Dementia/
  * Values: -
  * Description: Comedy/novelty folder
* Variable: _subSort12Inch
  * Type: String
  * Default: 12 Inch Mix/
  * Values: -
  * Description: 12" mixes folder
* Variable: _subSortDisney
  * Type: String
  * Default: Disney/
  * Values: -
  * Description: Disney music folder
* Variable: _subSortPodcast
  * Type: String
  * Default: Podcast/
  * Values: -
  * Description: Podcasts folder
* Variable: _subSortInterview
  * Type: String
  * Default: Interview/
  * Values: -
  * Description: Interviews folder
* Variable: _subSortBroadcast
  * Type: String
  * Default: Broadcast/
  * Values: -
  * Description: Broadcasts folder
* Variable: _subSortReserved
  * Type: String
  * Default: Singles Candidates/
  * Values: -
  * Description: Reserved/special folder
* Variable: _subSortPreTag
  * Type: String
  * Default: No MBID/
  * Values: -
  * Description: Untagged folder
* Variable: _subSortHoliday
  * Type: String
  * Default: Holiday/
  * Values: -
  * Description: Holiday music folder
* Variable: _subSortCountry
  * Type: String
  * Default: Country/
  * Values: -
  * Description: Country music folder
* Variable: _subSortBlues
  * Type: String
  * Default: Blues/
  * Values: -
  * Description: Blues music folder
* Variable: _subSortJazz
  * Type: String
  * Default: Jazz/
  * Values: -
  * Description: Jazz music folder
* Variable: _subSort2Oct
  * Type: String
  * Default: Spooktacular/
  * Values: -
  * Description: October seasonal folder
* Variable: _subSort2Nov
  * Type: String
  * Default: Fallback/
  * Values: -
  * Description: November seasonal folder
* Variable: _subSort2Dec
  * Type: String
  * Default: Here Comes Santa/
  * Values: -
  * Description: December seasonal folder
* Variable: _subSort2Jan
  * Type: String
  * Default: Wintertime/
  * Values: -
  * Description: January seasonal folder
* Variable: _subSort2Feb
  * Type: String
  * Default: Will You Be My Valentine?/
  * Values: -
  * Description: February seasonal folder
* Variable: _subSort2Mar
  * Type: String
  * Default: Spring is in the Air/
  * Values: -
  * Description: March seasonal folder
* Variable: _subSort2Apr
  * Type: String
  * Default: Foolish/
  * Values: -
  * Description: April seasonal folder
* Variable: _subSort2May
  * Type: String
  * Default: Maybe/
  * Values: -
  * Description: May seasonal folder
* Variable: _subSort2June
  * Type: String
  * Default: SumSumSummertime/
  * Values: -
  * Description: June seasonal folder
* Variable: _subSort2July
  * Type: String
  * Default: Fireworks & Stuff/
  * Values: -
  * Description: July seasonal folder
* Variable: _subSort2Aug
  * Type: String
  * Default: SumSumSummertime/
  * Values: -
  * Description: August seasonal folder
* Variable: _subSort2Sept
  * Type: String
  * Default: SumSumSummertime/
  * Values: -
  * Description: September seasonal folder
* Variable: TRIBUTE/COVER
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _altArtistSort
  * Type: Integer
  * Default: 1
  * Values: 0, 1
  * Description: File tribute/cover under original artist
* Variable: TRACK SEPARATION
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _showTrackArtistSeparation
  * Type: Integer
  * Default: 0
  * Values: 0, 1
  * Description: Separate tracks by artist in album
* Variable: LENGTH/PADDING
  * Type: 
  * Default: 
  * Values: 
  * Description: 
* Variable: _PaddedDiscNumMinLength
  * Type: Integer
  * Default: 1
  * Values: 1-9
  * Description: Minimum disc number padding
* Variable: _PaddedTrackNumMinLength
  * Type: Integer
  * Default: 2
  * Values: 1-9
  * Description: Minimum track number padding
* Variable: _aTitleMaxLength
  * Type: Integer
  * Default: 65
  * Values: 1-999
  * Description: Maximum album title length
* Variable: _tTitleMaxLength
  * Type: Integer
  * Default: 65
  * Values: 1-999
  * Description: Maximum track title length
* Variable: _tFilenameMaxLength
  * Type: Integer
  * Default: 120
  * Values: 1-999
  * Description: Maximum complete filename length

### 3.2 Development Settings

#### `_devMode`

**Purpose:** Test the script with hardcoded values instead of real metadata.

**Values:**

* `0` - Normal operation (use real file metadata)
* `1` - Test mode (use hardcoded values defined in Section 10)

**When to use:**

* Testing script changes without actual music files
* Debugging audio metrics detection
* Verifying path generation logic

**WARNING:** Must be set to `0` for actual use! If left at `1`, all files will use the same test values.

**Test values (when `_devMode = 1`):**

#### `_quickNoNameFormat`

**Purpose:** Skip filename formatting for quick sorting from unmatched files.

**Values:**

* `0` - Full formatting with all metadata (default)
* `1` - Minimal formatting (keeps original filename)

**When to use:**

* Sorting large batches of unmatched files quickly
* When you just want directory organization, not filename changes

**Effect:**

* Disables `_showTime` and `_showBandwidth` automatically
* Uses `%_filename%` instead of `%_titleForFilename%`
* Still organizes into folders normally

* * *

### 3.3 Display Options

#### `_showDate`

**Purpose:** Show release year in album folder name.

**Values:**

* `0` - Album name only
* `1` - Album name with year (default)

**Examples:**

**Notes:**

* Uses first available: `originalyear`, `originaldate`, `date`
* Shows first 4 characters (year only, not full date)
* Shows "0000" if no date available

#### `_showRecordLabel`

**Purpose:** Show record label in album folder name.

**Values:**

* `0` - Don't show label (default)
* `1` - Show label

**Examples:**

**Notes:**

* Only shows first label if multiple
* Requires `label` tag to be present

#### `_showReleaseStatus`

**Purpose:** Show release status (Official, Promotion, Bootleg, etc.) in album folder.

**Values:**

* `0` - Don't show status (default)
* `1` - Show status

**Examples:**

**Common statuses:**

* Official
* Promotion
* Bootleg
* Pseudo-Release

#### `_showCatalogueNumber`

**Purpose:** Show catalog number in album folder name.

**Values:**

* `0` - Don't show catalog number (default)
* `1` - Show catalog number

**Examples:**

#### `_showIDNum`

**Purpose:** Show MusicBrainz Album ID and catalog number.

**Values:**

* `0` - Don't show
* `1` - Show (default)

**Format:** `[mbid] {catalog}`

**Examples:**

**Use case:** Helps identify exact MusicBrainz release if you have multiple versions

#### `_showTime`

**Purpose:** Show track duration in filename.

**Values:**

* `0` - Don't show duration
* `1` - Show duration (default)

**Format:** `[XmYYs]`

**Examples:**

**Notes:**

* Automatically disabled if `_quickNoNameFormat = 1`
* Uses Picard's `%_length%` variable
* Format: minutes + "m" + seconds + "s"

#### `_showBandwidth`

**Purpose:** Show audio quality metrics in filename.

**Values:**

* `0` - Don't show metrics
* `1` - Show metrics (default)

**Format:** `[bitrate samplerate type channels]`

**Examples:**

**Metrics shown:**

* **Bitrate:** 320, V0, V2, etc. (see VBR Mapping section)
* **Sample Rate:** 44100KHz, 48000KHz, 96000KHz, etc. (full Hz value)
* **Type:** CBR, VBR, or file format for lossless
* **Channels:** 2ch (stereo), 6ch (5.1 surround), etc.

* * *

### 3.4 Primary Organization Structure

#### `_orderTypeForRoot`

**Purpose:** Choose root directory organization method.

**Values:**

* `1` - By category/genre (requires Last.fm.ng plugin)
* `2` - By artist first letter (default, recommended)

**Examples:**

**Option 1 - Category:**

**Option 2 - Artist Letter:**

**Notes:**

* Option 1 requires `albumgrouping` tag (from Last.fm.ng plugin)
* Option 2 is most common and doesn't require extra plugins

#### `_orderTypeForArtist`

**Purpose:** Choose how artist names are sorted.

**Values:**

* `1` - First letter of first name (default)
* `2` - First letter of last name (uses sort tags)
* `3` - No alphabetical separation

**Examples:**

**Option 1 - First Name:**

**Option 2 - Last Name:**

**Option 3 - No Separation:**

**Notes:**

* Option 2 relies on MusicBrainz `albumartistsort` and `artistsort` tags
* "The", "A", "An" are automatically handled by MusicBrainz sort tags
* Option 3 can create very long lists in root directory

#### `_separateByTypeInArtistDirectory`

**Purpose:** Separate releases by type into subfolders.

**Values:**

* `0` - All releases directly in artist folder
* `1` - Separate into subfolders (default)

**Examples:**

**Option 0 - No Separation:**

**Option 1 - With Separation:**

**Subfolder types created:**

* Albums/ (if `_separateAlbum = 1`)
* Singles/
* EP/
* Live/
* Compilation/
* Cover/
* Tribute/
* Broadcast/
* Interview/
* Video/
* Others/

#### `_separateAlbum`

**Purpose:** Put regular albums in an Albums/ subfolder.

**Values:**

* `0` - Albums directly in artist folder (default)
* `1` - Albums in Albums/ subfolder

**Requires:** `_separateByTypeInArtistDirectory = 1`

**Examples:**

**Option 0:**

**Option 1:**

**When to use:** Some users prefer all release types in subfolders for consistency.

* * *

### 3.5 Multi-Disc Handling

#### `_useSubDiscDirectory`

**Purpose:** Create separate subdirectories for each disc in multi-disc albums.

**Values:**

* `0` - All discs in same folder with disc prefix in track number
* `1` - Each disc in its own subfolder (default)

**Examples:**

**Option 0 - Same Folder:**

**Option 1 - Disc Subfolders:**

**Notes:**

* Option 0 is useful for devices that don't support subfolders
* Option 1 is cleaner and more organized

#### `_showDiscSubtitle`

**Purpose:** Show disc subtitle if present in MusicBrainz data.

**Values:**

* `0` - Just disc number
* `1` - Include subtitle (default)

**Examples:**

**Option 0:**

**Option 1:**

**Notes:**

* Only applies when `_useSubDiscDirectory = 1`
* Disc subtitles come from MusicBrainz, not always present

#### `_useMusicBrainzStyleForVinylTrack`

**Purpose:** Use vinyl-style track numbering (A1, A2, B1, B2) for vinyl releases.

**Values:**

* `0` - Standard numbering (01, 02, 03)
* `1` - Vinyl style (A1, B1) (default)

**Applies to:** Media type = "Vinyl" only

**Examples:**

**Option 0 - Standard:**

**Option 1 - Vinyl Style:**

**Requirements:**

* Release must have MusicBrainz track numbers (not all do)
* Media tag must be "Vinyl"

* * *

### 3.6 Genre SubSort

#### How Genre SubSort Works

Genre SubSort creates custom root-level folders based on the `genresort` tag. This is an advanced feature for organizing large, diverse libraries.

**Workflow:**

1. Set custom `genresort` tag on files (not from MusicBrainz)
2. Script detects keyword in `genresort` value
3. Routes to corresponding subsort folder

**Example:**

* **Tag:** `genresort = Holiday`
* **Trigger:** Script detects "Holiday" in tag
* **Folder:** `_subSortHoliday = Holiday/`
* **Result:** `/Holiday/Artist/Album/`

#### Available Subsort Categories

| Trigger Keyword                | Folder Variable   | Default Folder      | Use Case                  |
| ------------------------------ | ----------------- | ------------------- | ------------------------- |
| Holiday                        | _subSortHoliday   | Holiday/            | Christmas, seasonal music |
| Classical                      | _subSortClassical | Classical/          | Classical music           |
| Jazz                           | _subSortJazz      | Jazz/               | Jazz music                |
| Blues                          | _subSortBlues     | Blues/              | Blues music               |
| Country                        | _subSortCountry   | Country/            | Country music             |
| Game                           | _subSortGame      | Arcade/             | Video game soundtracks    |
| Disney                         | _subSortDisney    | Disney/             | Disney music              |
| odcast                         | _subSortPodcast   | Podcast/            | Podcasts                  |
| nterview                       | _subSortInterview | Interview/          | Interviews                |
| roadcast                       | _subSortBroadcast | Broadcast/          | Broadcasts                |
| 12 Inch                        | _subSort12Inch    | 12 Inch Mix/        | 12" remix singles         |
| Novelty, Comedy, Demento, FuMP | _subSortDemento   | Dementia/           | Comedy/novelty music      |
| DJ Bits                        | _subSortDJBits    | DJBits/             | DJ tools, samples         |
| *-*                            | _subSortReserved  | Singles Candidates/ | Special marker            |
| ***                            | _subSortPreTag    | No MBID/            | Untagged files            |

#### Seasonal Subsort (Second Level)

You can also use seasonal keywords for a second level of sorting:

| Trigger Keyword | Folder                                | Season            |
| --------------- | ------------------------------------- | ----------------- |
| Spook           | Spooktacular/                         | Halloween/October |
| Fall            | Fallback/                             | November          |
| Santa           | Here Comes Santa/                     | December          |
| Winter          | Wintertime/                           | January           |
| Valentine       | Will You Be My Valentine?/            | February          |
| Spring          | Spring is in the Air/                 | March             |
| Fool            | Foolish/                              | April             |
| Maybe           | Maybe/                                | May               |
| Summer, Firew   | SumSumSummertime/, Fireworks & Stuff/ | June-September    |

**Example:**

#### Creating Your Own Subsort

1. **Define folder name:**

2. **Add detection logic in Section 11:**

3. **Tag your files:**

4. **Result:**

* * *

4\. Character Replacement
-------------------------

### 4.1 Why Character Replacement?

Different operating systems and filesystems have different rules for allowed characters in file and folder names:

* **Windows:** Disallows `:`, `?`, `*`, `<`, `>`, `|`, `"`, `/`, `\`
* **Linux/macOS:** More permissive but `/` still reserved for path separator
* **Samba/CIFS:** Network shares have additional restrictions

Additionally, some characters can cause issues with:

* Command-line tools
* Backup software
* Cloud storage sync
* Media players

This script ensures cross-platform compatibility by replacing problematic characters.

### 4.2 Complete Replacement Table

#### Tag-Level Replacements (Written to File Metadata)

These replacements modify the actual tags written to your music files:

* Original: ...
  * Replacement: &
  * Tags Affected: album, title, discsubtitle
  * Reason: Ellipsis standardization
  * Example: "Best... Song" -> "Best & Song"
* Original: No. X
  * Replacement: X
  * Tags Affected: album, title, discsubtitle
  * Reason: Remove "No." prefix
  * Example: "No. 1 Hit" -> "1 Hit"
* Original: 12"
  * Replacement: 12 Inch
  * Tags Affected: album, title, discsubtitle, media
  * Reason: Standardize vinyl notation
  * Example: '12" Vinyl' -> "12 Inch Vinyl"
* Original: "text"
  * Replacement: 'text'
  * Tags Affected: All artist/album/title tags
  * Reason: Samba compatibility
  * Example: 'The "Best"' -> "The 'Best'"

**Why tag-level?** These improve consistency and readability of your metadata, not just filenames.

#### Filename-Level Replacements (File/Folder Names Only)

These replacements only affect paths, not file metadata:

| Original | Replacement | Scope                       | Reason                      | Example                      |
| -------- | ----------- | --------------------------- | --------------------------- | ---------------------------- |
| #        | -           | All filename variables      | Hash alternative            | "Track #1" -> "Track -1"     |
| :        | _           | All filename variables      | Windows incompatible        | "Title: Sub" -> "Title_ Sub" |
| ?        | G           | All filename variables      | Windows incompatible        | "Why?" -> "WhyG"             |
|          |             | è                           | Album, title, disc subtitle | Pipe alternative             |
| >        | [removed]   | Album, title, disc subtitle | Windows incompatible        | "A>B" -> "AB"                |
| <        | [removed]   | Album, title, disc subtitle | Windows incompatible        | "A<B" -> "AB"                |
| *        | 1           | All variables               | Windows incompatible        | "A*B" -> "A1B"               |
| &        | &           | All variables               | HTML entity                 | "A & B" -> "A & B"           |

**Why filename-only?** These are purely for filesystem compatibility, no need to modify the actual metadata.

### 4.3 Scope: Which Variables Are Affected?

**Tag-Level Scope (all of these):**

* `album`
* `title`
* `discsubtitle`
* `media`
* `albumartist`
* `artist`
* `albumartistsort`
* `artistsort`

**Filename-Level Scope (all of these):**

* `_titleForFilename`
* `_albumForFilename`
* `_discsubtitleForFilename`
* `_artistForFilename`
* `_albumartistForFilename`
* `_artistsortForFilename`
* `_albumartistsortForFilename`

### 4.4 Platform-Specific Issues

#### Windows Path Restrictions

Windows disallows these characters in paths: `< > : " / \ | ? *`

**How the script handles it:**

* `:` -> `_` (colon to underscore)
* `?` -> `G` (question mark removed)
* `*` -> `1` (asterisk to "1")
* `>` -> removed
* `<` -> removed
* `|` -> `è`
* `"` -> `'` (double to single quotes)

### 4.5 Customizing Character Replacements

#### Adding a New Replacement

**Example:** Replace `@` with `(at)`

1. **For tags (Section 9, tag-level):**

2. **For filenames (Section 9, filename-level):**

#### Changing an Existing Replacement

**Example:** Change `:` replacement from `_` to `-`

Find this line in Section 9:

Change to:

Repeat for all filename variables.

#### Using Regex Replacements

For more complex patterns, use `$rreplace()`:

**Example:** Remove all parentheses and contents:

**Example:** Convert "feat. Artist" to "\[Artist\]":

* * *

5\. VBR Bitrate Mapping
-----------------------

### 5.1 What is VBR?

**CBR (Constant Bitrate):**

* Fixed bitrate throughout the entire file
* Example: 320 kbps CBR - every second uses exactly 320 kbit
* File size is predictable
* Common presets: 320, 256, 192, 128, 96, 64 kbps

**VBR (Variable Bitrate):**

* Bitrate varies based on complexity of audio
* Complex parts (loud, detailed) get higher bitrate
* Simple parts (silence, simple tones) get lower bitrate
* Better quality/size ratio than CBR
* Picard reports average bitrate

**How to detect:** If Picard's average bitrate doesn't match a standard CBR preset (320, 256, 192, etc.), assume VBR.

### 5.2 Detection Logic

The script determines CBR vs VBR by checking if the bitrate matches standard presets:

**Example:**

* Picard reports `320.0 kbps` -> Exactly 320 -> CBR
* Picard reports `245.3 kbps` -> Not a standard preset -> VBR (likely V0)

### 5.3 LAME VBR Quality Levels

LAME is the most popular MP3 encoder and defines standard VBR presets (V0-V9).

#### Complete VBR Mapping Table

* Bitrate Range (kbps): 339+
  * LAME Preset: Custom/Extreme
  * Script Label: 320+
  * Quality Description: Extreme quality VBR
  * Typical Use: Very high quality VBR
* Bitrate Range (kbps): 320-339
  * LAME Preset: V0 alt
  * Script Label: 320
  * Quality Description: Extreme
  * Typical Use: Alternative V0 extreme
* Bitrate Range (kbps): 260-319
  * LAME Preset: Custom
  * Script Label: V0+
  * Quality Description: High+
  * Typical Use: High quality VBR+
* Bitrate Range (kbps): 220-260
  * LAME Preset: V0
  * Script Label: V0
  * Quality Description: Excellent (245 avg)
  * Typical Use: Most popular high quality
* Bitrate Range (kbps): 192-220
  * LAME Preset: V1
  * Script Label: V1
  * Quality Description: Excellent (225 avg)
  * Typical Use: Slightly smaller than V0
* Bitrate Range (kbps): 170-191
  * LAME Preset: V2
  * Script Label: V2
  * Quality Description: Transparent (190 avg)
  * Typical Use: Most can't tell from original
* Bitrate Range (kbps): 150-170
  * LAME Preset: V3
  * Script Label: V3
  * Quality Description: Good (175 avg)
  * Typical Use: Good quality, smaller size
* Bitrate Range (kbps): 140-150
  * LAME Preset: V4
  * Script Label: V4
  * Quality Description: Good (165 avg)
  * Typical Use: Acceptable quality
* Bitrate Range (kbps): 130-140
  * LAME Preset: V5
  * Script Label: V5
  * Quality Description: Moderate (130 avg)
  * Typical Use: Moderate quality
* Bitrate Range (kbps): 120-130
  * LAME Preset: V6
  * Script Label: V6
  * Quality Description: Moderate (115 avg)
  * Typical Use: Smaller files
* Bitrate Range (kbps): 96-120
  * LAME Preset: V7
  * Script Label: V7
  * Quality Description: Acceptable
  * Typical Use: Noticeably compressed
* Bitrate Range (kbps): 70-95
  * LAME Preset: V8
  * Script Label: V8
  * Quality Description: Low
  * Typical Use: Low quality
* Bitrate Range (kbps): 45-69
  * LAME Preset: V9
  * Script Label: V9
  * Quality Description: Very low
  * Typical Use: Very low quality
* Bitrate Range (kbps): <45
  * LAME Preset: N/A
  * Script Label: [actual kbps]
  * Quality Description: Poor
  * Typical Use: Below standard range

### 5.4 Filename Examples

**CBR:**

**VBR:**

**Lossless:**

### 5.5 How the Mapping Code Works

**Step 1:** Extract integer bitrate

Removes decimal: `245.3` -> `245`

**Step 2:** Check if CBR

**Step 3:** If VBR, map to quality level

Uses nested `$if()` with `$gt()` (greater than) to find the right range.

### 5.6 Special Cases

#### 320+ kbps VBR

Some extreme quality VBR encodes can average above 320 kbps (up to ~340 kbps for MP3).

**Detection:** Bitrate > 339 kbps **Label:** `320+`

**Example:**

#### Non-Standard VBR

Files encoded with custom VBR settings outside LAME standard ranges show actual bitrate.

**Example:** 71 kbps average (between V9 and below standard range)

#### Lossless Files

FLAC, ALAC, and other lossless formats don't use CBR/VBR labels. Instead, they show file format.

**Example:**

* * *

6\. Path Generation Examples
----------------------------

### 6.1 Example 1: Basic Artist Album (Single-Disc CD)

**Configuration:**

**Metadata:**

**Path Construction (Step-by-Step):**

**Final Path:**

* * *

### 6.2 Example 2: Multi-Disc Album with Subtitles

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Paths:**

* * *

### 6.3 Example 3: Vinyl with MusicBrainz Track Numbering

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Paths:**

* * *

### 6.4 Example 4: Various Artists Compilation

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Paths:**

* * *

### 6.5 Example 5: Album with Type Separation

**Configuration:**

**Metadata (3 releases):**

**Album:**

**Single:**

**Live:**

**Path Construction:**

**Final Paths:**

* * *

### 6.6 Example 6: Tribute Album with Original Artist Routing

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Path:**

**Note:** This requires manually setting two custom tags: `coverTributeSort = Tribute` and `albumartistsort = Queen`.

* * *

### 6.7 Example 7: Genre Pre-Sort (Classical)

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Path:**

* * *

### 6.8 Example 8: Soundtrack

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Path:**

* * *

### 6.9 Example 9: Incomplete Album

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Path:**

**Override:** Set custom tag `SavePerfectAnyway = yes` to skip the "- Partial" prefix.

* * *

### 6.10 Example 10: EP with Bitrate Display

**Configuration:**

**Metadata:**

**Path Construction:**

**Final Paths:**

* * *

7\. Advanced Features
---------------------

### 7.1 Genre-Based Sorting

**(See Section 3.6 - Genre SubSort)**

### 7.2 Tribute and Cover Album Handling

#### Overview

The tribute/cover feature allows you to file tribute and cover albums under the original artist being tributed or covered, rather than under the performing artist.

**Use case:** You want "A Tribute to Queen" by Various Artists filed under Queen, not Various Artists.

#### Requirements

This feature requires **manually setting two custom tags**:

1. **`coverTributeSort`** - Set to "Tribute" or "Cover"
2. **`albumartistsort`** - Set to the original artist name

**Why manual?** MusicBrainz doesn't have a standard "this is a tribute album" field, so we use custom tags.

#### How to Set Custom Tags in Picard

1. Select the album in Picard
2. Right-click -> **Tags from file names** or **Edit Tags**
3. Add a new tag:
   * Tag name: `coverTributeSort`
   * Value: `Tribute` (or `Cover`)
4. Add another tag:
   * Tag name: `albumartistsort`
   * Value: Original artist name (e.g., "Queen")
5. Save the file

#### Configuration

#### Example Workflow

**Album:** "We Will Rock You - Queen Tribute" by Various Artists

**Step 1: Tag the album**

**Step 2: Script detects**

**Step 3: Routes to original artist**

Uses `albumartistsort = Queen` for the folder.

**Result:**

#### Cover Albums

Same process, but use `coverTributeSort = Cover`:

**Example:** "Devolution" by DEVO (covers)

**Tags:**

**Result:**

#### Limitations

* Must manually tag each tribute/cover album
* MusicBrainz doesn't provide this automatically
* albumartistsort must be spelled exactly as you want the folder named

### 7.3 DevMode (Development/Testing)

#### Purpose

DevMode allows you to test the script's audio metrics detection without actual music files.

**Use case:**

* Testing VBR mapping logic
* Debugging bitrate detection
* Verifying path generation

#### Configuration

**WARNING:** Must be set to `0` for actual use!

#### Test Values

When `_devMode = 1`, the script uses these hardcoded values instead of real file metadata:

#### What DevMode Does

1. **Bitrate Detection:**

2. **Audio Metrics:**

3. **Title:**

#### Expected Output (DevMode = 1)

All files will use test values:

Bitrate 71.426 maps to V8.

#### How to Test

1. Set `_devMode = 1` in configuration
2. Copy script to Picard
3. Tag any file
4. Check filename - should show test values
5. **IMPORTANT:** Set `_devMode = 0` before actual use!

### 7.4 Custom Tag Integration

The script supports several custom tags you can set manually for special handling.

#### `SavePerfectAnyway`

**Purpose:** Override incomplete album detection.

**Values:** `yes` (any other value = not set)

**Use case:** You have a complete album but Picard thinks it's incomplete (e.g., you removed tracks intentionally).

**How to set:**

1. Right-click file -> Edit Tags
2. Add tag: `SavePerfectAnyway = yes`
3. Save

**Effect:**

#### `SaveIncompleteAnyway`

**Purpose:** Force incomplete album to go to incomplete directory.

**Values:** `yes`

**Use case:** Opposite of above - force incomplete routing.

**Effect:**

#### `BitRateSplit`

**Purpose:** Add bitrate to album folder name.

**Values:** `Yes`

**Configuration:** (Not in default script, must add manually)

**Example modification:**

**Result:**

#### `coverTributeSort`

**(See Section 7.2 - Tribute and Cover Albums)**

#### `genresort`

**(See Section 3.6 - Genre SubSort)**

* * *

8\. Variables Reference
-----------------------

### 8.1 MusicBrainz Standard Tags

These tags come from MusicBrainz or existing file metadata:

| Tag                         | Description                 | Example                        |
| --------------------------- | --------------------------- | ------------------------------ |
| %artist%                    | Track artist name           | "The Beatles"                  |
| %albumartist%               | Album artist name           | "The Beatles"                  |
| %album%                     | Album title                 | "Abbey Road"                   |
| %title%                     | Track title                 | "Come Together"                |
| %date%                      | Release date                | "1969-09-26"                   |
| %originaldate%              | Original release date       | "1969-09-26"                   |
| %originalyear%              | Original release year       | "1969"                         |
| %tracknumber%               | Track number                | "1"                            |
| %totaltracks%               | Total tracks on disc        | "17"                           |
| %discnumber%                | Disc number                 | "1"                            |
| %totaldiscs%                | Total discs in release      | "2"                            |
| %discsubtitle%              | Disc subtitle               | "Acoustic"                     |
| %media%                     | Media type                  | "CD", "Vinyl", "Digital Media" |
| %label%                     | Record label                | "Apple Records"                |
| %catalognumber%             | Catalog number              | "XPCD-123"                     |
| %releasetype%               | Release type(s)             | "album", "single", "live"      |
| %releasestatus%             | Release status              | "Official", "Promotion"        |
| %_releasecomment%           | Disambiguation comment      | "Blue Album"                   |
| %musicbrainz_albumid%       | MusicBrainz Album ID        | "abc123..."                    |
| %musicbrainz_albumartistid% | MusicBrainz Album Artist ID | "def456..."                    |
| %_musicbrainz_tracknumber%  | MusicBrainz track number    | "A1", "B2" (vinyl)             |
| %genre%                     | Genre                       | "Rock"                         |
| %albumgrouping%             | Album grouping              | "Rock", "Pop" (Last.fm)        |
| %compilation%               | Compilation flag            | "1" if compilation             |
| %_length%                   | Track length                | "4:20"                         |
| %_bitrate%                  | Average bitrate             | "320.0", "245.3"               |
| %_sample_rate%              | Sample rate                 | "44100"                        |
| %_bits_per_sample%          | Bit depth                   | "16", "24"                     |
| %_channels%                 | Number of channels          | "2", "6"                       |
| %_extension%                | File extension              | "mp3", "flac"                  |
| %_filename%                 | Original filename           | "track01"                      |

### 8.2 Additional Artists Variables Plugin Tags

These tags require the "Additional Artists Variables" plugin:

#### Album Variables

| Tag                               | Description                             |
| --------------------------------- | --------------------------------------- |
| %_artists_album_primary_id%       | ID of primary album artist              |
| %_artists_album_primary_std%      | Primary album artist [standardized]     |
| %_artists_album_primary_cred%     | Primary album artist [as credited]      |
| %_artists_album_primary_sort%     | Primary album artist [sort name]        |
| %_artists_album_additional_id%    | IDs of additional album artists         |
| %_artists_album_additional_std%   | Additional album artists [standardized] |
| %_artists_album_additional_cred%  | Additional album artists [as credited]  |
| %_artists_album_all_std%          | All album artists [standardized]        |
| %_artists_album_all_cred%         | All album artists [as credited]         |
| %_artists_album_all_sort%         | All album artists [sort names]          |
| %_artists_album_all_sort_primary% | Primary [sort] + additional [std]       |
| %_artists_album_all_count%        | Number of album artists                 |

#### Track Variables

| Tag                               | Description                             |
| --------------------------------- | --------------------------------------- |
| %_artists_track_primary_id%       | ID of primary track artist              |
| %_artists_track_primary_std%      | Primary track artist [standardized]     |
| %_artists_track_primary_cred%     | Primary track artist [as credited]      |
| %_artists_track_primary_sort%     | Primary track artist [sort name]        |
| %_artists_track_additional_id%    | IDs of additional track artists         |
| %_artists_track_additional_std%   | Additional track artists [standardized] |
| %_artists_track_additional_cred%  | Additional track artists [as credited]  |
| %_artists_track_all_std%          | All track artists [standardized]        |
| %_artists_track_all_cred%         | All track artists [as credited]         |
| %_artists_track_all_sort%         | All track artists [sort names]          |
| %_artists_track_all_sort_primary% | Primary [sort] + additional [std]       |
| %_artists_track_all_count%        | Number of track artists                 |

**What does \[standardized\] vs \[as credited\] mean?**

* **Standardized:** Official artist name from MusicBrainz database
* **As credited:** How the artist is credited on this specific release
* **Sort:** Name formatted for sorting (e.g., "Beatles, The")

**Example:**

### 8.3 Script Internal Variables

Variables created and used by the script (all start with `_`):

#### Constants (Section 1)

| Variable            | Value             | Description                      |
| ------------------- | ----------------- | -------------------------------- |
| %_cUnknownArtistID% | 125ec42a-...      | MusicBrainz Unknown Artist ID    |
| %_cVariousArtistID% | 89ad4ac3-...      | MusicBrainz Various Artists ID   |
| %_cUnknownArtist%   | [Unknown Artist]  | Display name for unknown artist  |
| %_cVariousArtist%   | [Various Artists] | Display name for various artists |
| %_cUnknownAlbum%    | [Unknown Album]   | Display name for unknown album   |
| %_cNoTitle%         | [Unknown Title]   | Display name for unknown title   |
| %_cClassical%       | [Classical]       | Classical music folder name      |
| %_cSoundtrack%      | [Soundtracks]     | Soundtrack folder name           |
| %_cSingles%         | [~Singles~]       | Singles folder name              |
| %_cOther%           | [Other]           | Other releases folder name       |

#### Working Variables (Section 4)

| Variable          | Description                            |
| ----------------- | -------------------------------------- |
| %_nMedia%         | Media type                             |
| %_nTotalDiscs%    | Total discs                            |
| %_nDiscNum%       | Disc number                            |
| %_nTotalTracks%   | Total tracks                           |
| %_nTrackNum%      | Track number                           |
| %_nAlbumArtistID% | Album artist ID                        |
| %_nInitial%       | Artist initial folder (e.g., "~ B ~/") |
| %_nFeat%          | Featured artist string                 |
| %_PaddedDiscNum%  | Padded disc number                     |
| %_PaddedTrackNum% | Padded track number                    |
| %_nYear%          | Year in [YYYY] format                  |
| %_nTNum%          | Complete track number (disc+track)     |

#### Filename Variables (Section 8)

| Variable                      | Description                 |
| ----------------------------- | --------------------------- |
| %_titleForFilename%           | Sanitized track title       |
| %_albumForFilename%           | Sanitized album title       |
| %_discsubtitleForFilename%    | Sanitized disc subtitle     |
| %_albumartistForFilename%     | Sanitized album artist      |
| %_artistForFilename%          | Sanitized track artist      |
| %_albumartistsortForFilename% | Sanitized album artist sort |
| %_artistsortForFilename%      | Sanitized track artist sort |

#### Audio Metrics Variables (Section 10)

| Variable         | Description                           |
| ---------------- | ------------------------------------- |
| %_intBitRate%    | Integer bitrate value                 |
| %_bitRateSpeed%  | Sample rate (e.g., "44100KHz")        |
| %_bitsPerSample% | Bit depth                             |
| %_audioChannels% | Channel count                         |
| %_bitRateType%   | "CBR" or "VBR"                        |
| %_cbrRateValue%  | CBR bitrate value                     |
| %_vbrRateValue%  | VBR bitrate value                     |
| %_fileCBRRate%   | CBR label for filename                |
| %_fileVBRRate%   | VBR label for filename (V0, V2, etc.) |

#### Detection Flags (Section 6)

| Variable          | Value                   | Description                        |
| ----------------- | ----------------------- | ---------------------------------- |
| %_isAlbum%        | 1 if album              | Is this an album release?          |
| %_isSingle%       | 1 if single             | Is this a single?                  |
| %_isLive%         | 1 if live               | Is this a live recording?          |
| %_isEP%           | 1 if EP                 | Is this an EP?                     |
| %_isBroadcast%    | 1 if broadcast          | Is this a broadcast?               |
| %_isInterview%    | 1 if interview          | Is this an interview?              |
| %_isArtistCompil% | 1 if artist compilation | Artist compilation?                |
| %_isAudiobook%    | 1 if audiobook          | Is this an audiobook?              |
| %_isOther%        | 1 if other              | Is this "other" type?              |
| %_isTribute%      | 1 if tribute            | Is this a tribute album?           |
| %_isCover%        | 1 if cover              | Is this a cover album?             |
| %_isPodcast%      | 1 if podcast            | Is this a podcast?                 |
| %_isSoundTrack%   | 1 if soundtrack         | Is this a soundtrack?              |
| %_isIncomplete%   | 1 if incomplete         | Is the album incomplete?           |
| %_isVideo%        | 1 if video              | Is this a video?                   |
| %_isVarious%      | 1 if various            | Is album artist "Various Artists"? |
| %_isGlobalCompil% | 1 if compilation        | Is compilation flag set?           |

* * *

9\. Customization Guide
-----------------------

### 9.1 Adding New Character Replacements

**Scenario:** You want to replace `@` with `(at)` in filenames.

**Step 1:** Decide scope (tags or filenames)

For filenames only, go to Section 9, filename-level replacements.

**Step 2:** Add replacement

Find the filename replacement block:

**Step 3:** Add your new line

**Result:**

### 9.2 Creating New Genre Subsort Categories

**Scenario:** You want to add a "Soundtrack - Games" category for video game soundtracks.

**Step 1:** Define folder name (Section 2.8)

**Step 2:** Add detection logic (Section 11)

Find the genre subsort detection block:

Add your new line:

**Step 3:** Tag your files

Add custom tag `genresort = Game Soundtrack` to your video game soundtracks.

**Result:**

### 9.3 Modifying Path Structure

#### Example 1: Remove Year from Album Folder

**Find:**

**Change to:**

**Or simply set:**

#### Example 2: Change Artist Letter Folder Format

**Current:** `/B/Artist/` **Want:** `/Artists-B/Artist/`

**Find (Section 11):**

**Change to:**

**Result:** `/Artists-B/Beatles, The/Album/`

#### Example 3: Add Custom Prefix to All Paths

**Want:** `/Music/` prefix before everything

**Find (Section 11, start of path generation):**

**Change to:**

**Result:** `/Music/B/Beatles, The/Album/`

### 9.4 Adjusting Filename Format

#### Example 1: Remove Audio Quality from Filename

**Find (Section 12):**

**Change to:**

**Or simply set:**

#### Example 2: Change Track Number Format

**Current:** `01. Track` **Want:** `01 - Track`

**Find (Section 12):**

**Change to:**

**Result:** `01 - Come Together [4m20s].mp3`

#### Example 3: Add File Size to Filename

**Want:** Show file size in MB

**Add before filename (Section 12):**

**Result:** `01. Track [23MB] [320 44100KHz CBR 2ch].mp3`

### 9.5 Adding New Metadata to Filenames

#### Example: Add Composer to Classical Music

**Step 1:** Check if tag exists

Picard provides `%composer%` tag.

**Step 2:** Add to filename (Section 12)

**Result:** `01. Bach - Brandenburg Concerto No. 1.flac`

#### Example: Add BPM to Filename

**Step 1:** Picard provides `%bpm%` tag

**Step 2:** Add to filename

**Result:** `01. Track [120BPM] [320 44100KHz CBR 2ch].mp3`

* * *

Appendix: Quick Reference
-------------------------

### Common Picard Functions

| Function                  | Description            | Example                         |
| ------------------------- | ---------------------- | ------------------------------- |
| $set(var,value)           | Set variable           | $set(_x,hello)                  |
| $if(cond,then,else)       | Conditional            | $if(%artist%,yes,no)            |
| $if2(a,b,c)               | First non-empty        | $if2(%artist%,Unknown)          |
| $noop(...)                | No operation (comment) | $noop( Comment )                |
| $upper(text)              | Uppercase              | $upper(hello) -> HELLO          |
| $lower(text)              | Lowercase              | $lower(HELLO) -> hello          |
| $left(text,n)             | First n chars          | $left(Beatles,4) -> Beat        |
| $right(text,n)            | Last n chars           | $right(Beatles,4) -> tles       |
| $len(text)                | Length                 | $len(Hello) -> 5                |
| $replace(text,old,new)    | Replace string         | $replace(A:B,:,_) -> A_B        |
| $rreplace(text,regex,new) | Replace regex          | $rreplace(A123B,\\d+,X) -> AXB  |
| $num(n,len)               | Pad number             | $num(5,3) -> 005                |
| $gt(a,b)                  | Greater than           | $gt(10,5) -> 1 (true)           |
| $lt(a,b)                  | Less than              | $lt(5,10) -> 1 (true)           |
| $eq(a,b)                  | Equals                 | $eq(hello,hello) -> 1           |
| $ne(a,b)                  | Not equals             | $ne(a,b) -> 1 (true)            |
| $in(text,search)          | Contains               | $in(hello,ll) -> 1              |
| $trim(text)               | Remove whitespace      | $trim(  hi  ) -> hi             |
| $firstalphachar(text,def) | First letter           | $firstalphachar(Beatles,#) -> B |

### Configuration Quick Settings

**Basic Setup:**

**Minimal Filename:**

**Multi-Disc (Merged):**

**No Type Separation:**
