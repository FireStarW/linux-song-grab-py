# linux-song-grab-py

A python reimplementation of [grab-song](https://github.com/aFoxNamedMorris/grab-song) by @aFoxNamedMorris , developed independantly of [pygrab-song](https://github.com/aFoxNamedMorris/pygrab-song) (I didn't know it existed -_-), meant to scrape song data for use in OBS.

Initially I created this with the intent to integrate it into an [OBS python script](https://obsproject.com/docs/scripting.html) but ran into documentation and motivation problems

Run this script with:

        $ python3 linux-song-grab.py
  
From the first opened media player, it will output the song title, artist, album, and year to both individual text files and a oneliner text file, along with the album art to its base directory.

![Visual demonstration of script in action](https://s26.postimg.cc/8amg0apdl/song-grab.png)
