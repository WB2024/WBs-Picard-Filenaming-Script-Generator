# 11xx/picard-scripts: MusicBrainz Naming & Tagging scripts - Codeberg.org
The script includes several variables and functions for formatting metadata fields, such as the artist name, album title, track number, and disc number:

##### Multi-disc release check

This checks if the current release is a part of multiple discs release, add it to the album directory name with a padded number if necessary.

```
$set(checkPadDiscNumber
	,$if2(
		$if($gte(%totaldiscs%,10000),	$if(%discnumber%, \(Disc $num(%discnumber%,5)\)),)
		,$if($gte(%totaldiscs%,1000),	$if(%discnumber%, \(Disc $num(%discnumber%,4)\)),)
		,$if($gte(%totaldiscs%,100),	$if(%discnumber%, \(Disc $num(%discnumber%,3)\)),)
		,$if($gte(%totaldiscs%,10),		$if(%discnumber%, \(Disc $num(%discnumber%,2)\)),)
		,$if($gt(%totaldiscs%,1),		$if(%discnumber%, \(Disc $num(%discnumber%,1)\)),)
	)
)
```


##### Track number padding

Similar to [Multi-disc release check](https://codeberg.org/11xx/picard-scripts/src/branch/master/%2AMulti-disc%20release%20check) but it always adds the track number with at least a padding of 2, e.g. "`05`".

```
$set(checkPadTrackNumber
	,$if2(
		$if(%_paddedtracknumber%,%_paddedtracknumber%)
		,$if($gte(%totaltracks%,10000),	$if(%tracknumber%,$num(%tracknumber%,5)),)
		,$if($gte(%totaltracks%,1000),	$if(%tracknumber%,$num(%tracknumber%,4)),)
		,$if($gte(%totaltracks%,100),	$if(%tracknumber%,$num(%tracknumber%,3)),)
		,$if($gte(%totaltracks%,10),	$if(%tracknumber%,$num(%tracknumber%,2)),)
		,$if($gte(%totaltracks%,1),		$if(%tracknumber%,$num(%tracknumber%,2)),)
	)
)
```


##### Media format information on album directory name

Adds extension and media format information to the album name, including:

*   sampling rate
*   bit-depth
*   extension
*   special media (Vinyl, SACD, DSD)

```
$set(mediaFormatSpec
	$noop(DSD is always '1bit' so only output this if greater than 1)
	,$if($gt(%_bits_per_sample%,1),%_bits_per_sample%bit )
	$noop(#TODO: Fix Opus output here:)
	$div(%_sample_rate%,1000)$if($ne($mod(%_sample_rate%,1000),0),.$left($mod(%_sample_rate%,1000),1))kHz
	$if($not($eq_any(%_extension%,dsf,dff,dsd)),$upper( %_extension%))
	$if($in(%media%,Vinyl), Vinyl)
	$noop(Output this before SACD because there are Vinyl rips recorded in DSD)
	$if($eq_any(%_extension%,dsf,dff,dsd), DSD)
	$if($in(%media%,SACD), SACD)
)
```


*   Note: I use a special/custom tag for tracking albums that are not in MusicBrainz's databases. Here the following line can be added to append a marker string to the album directory name:
    
    ```
if($eq(%NOT_ON_MUSICBRAINZ_DB%,true), #NOTONMBDB)

```

    

##### Get release type

Check if release type is `single` to append that to file naming

```
$set(getReleaseType
		,$if($eq(%releasetype%,single),\(Single\))
		$if($eq(%releasetype%,ep),\(EP\))
)
```


##### Get artist initial

```
$set(getInitial
	,$upper($left($if2(%albumartist%,%artist%),1))
)
```


##### Various Artists root directory

Check if `%albumartist%` is `Various Artists` to use that as the artist root directory for releases that are such.

```
$set(getVariousArtistsRoot
	,$if($eq(%albumartist%,Various Artists),Various Artists)
)
```


##### Get release year

Returns the first value of either `%originalyear%`, `%originaldate%` or `%date%`.

```
$set(getReleaseYear
	,$if2(
		$if(%originalyear%,$left(%originalyear%,4))
		,$if(%originaldate%,$left(%originaldate%,4))
		,$if(%date%,$left(%date%,4))
	)
)
```


##### Get album name truncated

Truncates the album name from `%album%`.

```
$noop( limit album name output to 120 characters )
$set(getAlbumNameTruncated
	,$left( $replace(%album%,/,), 120)
)
```


##### Check if `%albumartist%` is `Various Artists`

```
$set(notVariousArtists
	,$ne(%albumartist%,Various Artists)
)
```


##### Check for special vinyl track numbering

Vinyl releases usually use a SIDE>TRACKNUMBER format like `A1`, `A2`, and `B3`, `B4`.

```
$set(checkVinylTrackNumber
	,$if($and($in(%media%,Vinyl),%_musicbrainz_tracknumber%),%_musicbrainz_tracknumber%)
)
```


##### Output only album artist or first from the multiple value field

Gets the first value of either `%albumartist%` or, `%artist%` and if it is a multiple-artists field choose the first value, up untill the standard separator "`;`".

```
$set(getAlbumArtist
	,$if2(
		$noop(This searches for the first multiple artist separator `;' and truncates after it:)
		$left($if2(%albumartist%,%artist%),$find($if2(%albumartist%,%artist%),;))
		,$if2(%albumartist%,%artist%)
	)
)
```


##### Get channels number if more than 2

```
$set(getMultiChannels
	,$if($gt(%_channels%,2), %_channels%Ch)
)
```


##### Get either vinyl or normal track numbers

Complimentary of [Check for special vinyl track numbering](https://codeberg.org/11xx/picard-scripts/src/branch/master/%2ACheck%20for%20special%20vinyl%20track%20numbering) and [Track number padding](https://codeberg.org/11xx/picard-scripts/src/branch/master/%2ATrack%20number%20padding).

```
$set(getTrackNumber
	,$if2(%checkVinylTrackNumber%,%checkPadTrackNumber%)
)
```


##### Track title truncated

```
$set(getTitleTruncated
	,$left(%title%,120)
)
```


##### Disc subtitle

Some releases have a "disc subtitle" that specify location or work.

```
$set(getDiscSubtitle
	,$if(%discsubtitle%,\(%discsubtitle%\))
)
```
