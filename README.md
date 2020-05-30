# AWCHelper

A simple tool to help create the submission lines of the challenges. 
It searchs in your account for the start/end date and writes them down

## Usage

You must provide it with your Anilist username, link to the anime and challente to fulfill  
Example:  
  
* Anilist User: Juanikus
* Anime Link: https://anilist.co/anime/12679/Joshiraku/ (can also be _https://anilist.co/anime/12679/_)
* Challenge Text: Watch an anime with the genre / tags: "Comedy" AND "Female Protagonist" OR "Male Protagonist"  
  
Output:
```
Start: 24/02/20 Finish: 05/04/20 __Watch an anime with the genre / tags: "Comedy" AND "Female Protagonist" OR "Male Protagonist"__ [Joshiraku](https://anilist.co/anime/12679/Joshiraku/)
```
![Example](/example.png)
## Files

The .exe comes with an _icon.ico_ and, after the first run, a _user.db_ (which is used to store the username, avoiding writting it every time) is generated. you can hide those but do **NOT** delete them, the program wouldn't work
