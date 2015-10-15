#!/bin/bash

while true; do
    logger "63.131.134.196 pinged!"
    ping -c 3 63.131.134.14 > /dev/null
    sleep 5
done

