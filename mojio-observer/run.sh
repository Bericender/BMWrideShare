#!/bin/sh

java -Djava.library.path=/usr/local/lib -cp build/jar/mojio-observer.jar:/home/justin/dev/signalr-java-client/signalr-client-sdk/build/libs/signalr-client-sdk.jar:/usr/share/java/gson.jar:/usr/local/share/java/zmq.jar MojioObserver
