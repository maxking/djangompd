##djangompd

This is django based web client for Music Player Daemon(mpd).

###Prerequisites

Python 2.7+  
[MPD](http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki)  
[Virtualenv](https://virtualenv.pypa.io/en/latest/index.html)  

###Setup

This is a standard django project, follow the instructions below
to get the dev server running on your computer.

```bash
$ virtualenv mpd
$ cd mpd
$ source bin/activate
$ git clone git@github.com:maxking/djangompd.git
$ cd djangompd
$ pip install -r requirements.txt
$ python manage.py runserver
```

The last line above should start your dev-server at [http://localhost:8000][http://localhost:8000].

If you are having trouble playing the music, please try editing the MPD configuration file `/etc/mpd.conf`. Change the music and playlist search default directory.  Check for audio configuration if you are still unable to play video. For complete configuration options see [MPD Configuration Wiki](http://www.musicpd.org/doc/user/config.html).

###ToDo List: Frontend
- [ ] redesign frontend using [Polymer framework](https://www.polymer-project.org/)


