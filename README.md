# monitor-my-pc

```
just had the urge to create this.

sometime you ngrok tensorboard when you go grocery shopping
but also wants to check basic pc stats...
you should probably use nagios, but if you are too lazy to setup nagios
you should give `monitor-my-pc` a try.

```

## monitor your pc remotely with ngrok

```
# create `.env` file to specify `AUTHTOKEN=****` for ngrok.

# up the services
docker-compose up -d

# from the logs get ngrok link to remote monitor your pc!
docker logs -f monitor-my-pc_ngrok_1

```

# sample web ui

 ![web ui](/static/screenshot.png)