##djangompd

This is django based web client for Music Player Daemon(mpd).


###Setup

This is a standard django project, follow the instructions below
to get the dev server running on your computer


```bash
$ virtualenv mpd
$ cd mpd
$ source bin/activate
$ git clone git@github.com:maxking/djangompd.git
$ cd djangompd
$ pip install -r requirements.txt
$ python manage.py runserver
```

The last line above should start your dev-server at http://localhost:8000
