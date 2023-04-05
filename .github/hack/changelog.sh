#!/bin/sh

MARKER_PREFIX="## Version"
VERSION=$(echo "$1" | sed 's/^v//g')

IFS=''
found=0

while read -r "line"; do
  if [ $found -eq 0 ] && echo "$line" | grep -q "$MARKER_PREFIX $VERSION"; then
    echo "$line"
    found=1
    continue
  fi

  if [ $found -eq 1 ] && echo "$line" | grep -q -E "$MARKER_PREFIX [[:digit:]]+\.[[:digit:]]+\.[[:digit:]]"; then
    found=0
    break
  fi

  if [ $found -eq 1 ]; then
    echo "$line"
  fi
done < CHANGELOG.md