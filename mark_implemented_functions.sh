#!/usr/bin/env bash

# find all lines with a checkbox '- [ ]' and get the line without the '- [ ]' (remove first 6 chars)
grep -e '-\ \[ \]' README.md | cut -c6- | while read function; do
	# check if function defined in source file
	if    grep -E "^def ${function}" pyaoi.py 1> /dev/null; then
		# check checkbox
		sed       -i "s/^-\ \[\ \] ${function}$/- [x] ${function}/g" README.md
	fi
done
