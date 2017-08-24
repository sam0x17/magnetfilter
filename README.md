# Magnet Link Filter Utility
This simple python script can be used to add the best current trackers to an existing
magnet link. HTTP trackers are added first, followed by the top 20 current trackers.
The reason for this is rtorrent has a known problem with UDP trackers, so I like those
to be listed last. The utility also replaces zer0day.ch with tracker.zer0day.to.

## Usage

```
$ ./magnetfilter.py [magnet link here]

```

The filtered magnet link will be printed to the terminal
