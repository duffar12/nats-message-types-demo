# Demo of NATS Request-Reply and Queued message types

NATS Request-Reply messages are used to setup one-one communication between two NATS clients
NATS. Queued messages are used to  load balance clients. Only one client in the queue will receive a message

Request-Reply and Queued messages can be combined to create a scalable and resilient messaging architecture.
Imagine that you have many different microservices servers that must communicate with another server. 
* To add resilience you run 5 instances of the same server.
* Rather than sending the same message to all 5 servers - adding the servers as queued subscribers means that NATS will randomly select only one server to receive it. I.e we have built  in load balancing
* Rather than the servers sending a reply to everything connected on the relevant channel, request-reply is used to only respond to the original microservices server


# Getting started
* Install NATS if you haven't already
* Run a NATS server
* Run 5 instances of nats-queued-handler.py
* Run 5 instances of nats-req-rep.py

Notice that only one queued-handler instance will receive a message from a single req-rep.py and vice versa.
This gives us the benefits of a one-one communication with the advantage of resilience, redundancy and scalability provided by NATS
