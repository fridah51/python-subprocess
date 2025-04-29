#!/bin/bash

read subdomain

echo "Hello, World!" > /app/scripts/hello.txt
echo "Deploy App Event detected: $subdomain"
echo "----------------------Running from sh file--------------"
