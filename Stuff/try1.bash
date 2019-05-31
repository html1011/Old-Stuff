#!/usr/bin/env bash
echo "Attempt"
cat << EOF >> ~/.bashrc
function realness () {
    ls
}
export -f realness
EOF
shopt -s expand_aliases
source ~/.bashrc
realness
