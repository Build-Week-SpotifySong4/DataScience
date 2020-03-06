# DataScience

> Current live link:
> https://spotify-ml-component.herokuapp.com/

### routes 

index /api/v1 GET
> returns a simple hello world message

get_song_by_id /api/v1/song/<track_id> GET 
> returns Spotify song details given a Spotify track_id

recommend_using_track_id /api/v1/recommend/<tack_id> GET 
> returns recommendations for songs given a Spotify track_id


### setup

```sh
$ export APP_SETTINGS="ml_component.server.config.DevelopmentConfig"
$ export SECRET_KEY="change_me"
$ createdb spotify_suggester
$ pipenv install 
$ pipenv run python manage.py create_db
$ pipenv run python manage.py db init
$ pipenv run python manage.py db migrate
```

now you can run the application: 
```sh
$ pipenv run python manage.py runserver
```


> Want to specify a different port?
>
> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```


### Testing

```sh
$ pipenv run python manage.py test
```
