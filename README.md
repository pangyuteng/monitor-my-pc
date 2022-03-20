# monitor-my-pc

```
just had the urge to create this.

sometime you ngrok tensorboard when you go grocery shopping
but also wants to check basic pc stats...
you should probably use nagios, but if you don't wnat to setup nagios
you can try `monitor-my-pc`.

```

## monitor your pc remotely with ngrok

```

#create `.env` file to specify `AUTHTOKEN=****` for ngrok.

# up the services
docker-compose up -d

# from the log get link to remote monitor your pc.
docker logs -f monitor-my-pc_ngrok_1

```

# sample web ui

 ![web ui](/static/screenshot.png)