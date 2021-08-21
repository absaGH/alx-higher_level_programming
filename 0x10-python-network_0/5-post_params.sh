#!/bin/bash
# script that sends a POST request to the passed URL & display response body
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
