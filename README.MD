Fast and not a good readme documentation


How to test nats.


Step one Run redis server:

redis-server

Step two launch both py scripts in worker dir in new tabs:
python3  ./worker/send_nats.py #send message on nats channel
python3  ./worker/get_nats.py  #subscribe on nats channel and consume message


Step three launch django:
if not done yet do migrations to set up table models Dummy in the database.

cd ./test_project
python3 manage.py makemigrations
python3 manage.py migrate

then run server:

python3 manage.py runserver



Step four :

go to http://127.0.0.1:8000/test/
fill a name in the form and submit it.

you will see in the terminals where you launched send_nats / get_nats a display a message that displaying the name you entered
attesting that you send from a django signal a msg in the redis queue who iteslfs sent a message on the nats channel


flow

django side :
Front User -> Post request -> Save in db -> post_save trigger signal -> signal send a msg on a redis queue

send_nats side :

signal is sent to on a redis queue -> read message -> publish it on nats channel

get_nats side :
message is published on foo channel -> unqueue the message -> print the message


Annex documations consulted :

Doc nats :
https://www.scaleway.com/en/docs/nats/reference-content/nats-overview/
https://www.scaleway.com/en/nats/sla/ 
https://nats-io.github.io/nats.py/


Signal Django :

https://docs.djangoproject.com/en/5.2/topics/signals/



Wsgi vs asgi :
https://www.geeksforgeeks.org/python/difference-between-asgi-and-wsgi-in-django/


