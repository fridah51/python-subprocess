#!/bin/bash

log_file="/tmp/hello_debug.log"
echo "Script started" >> $log_file

read event
echo "Received event: $event" >> $log_file

subdomain=$(echo "$event" | awk '{print $3}' | sed 's/.sh$//')
echo "Subdomain extracted: $subdomain" >> $log_file


echo "Hello, World!" > hello.txt

echo "Done" >> $log_file