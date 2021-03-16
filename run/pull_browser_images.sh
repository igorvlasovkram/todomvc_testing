#!/bin/bash

awk -F'"' '$0 ~/selenoid/ {print $4}' etc/selenoid/browsers.json | while read -r line; do docker pull "$line"; done