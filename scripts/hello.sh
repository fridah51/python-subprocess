#!/bin/bash

subdomain="$1"

# Use double quotes, not curly braces, for variable interpolation in paths
echo "Hello, World!" > "/home/scripts/${subdomain}.txt"
echo "Deploy App Event for event: $subdomain"
echo "----------------------Running from sh file--------------"