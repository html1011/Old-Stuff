#!/bin/bash
node() {
    if hash node 2>/dev/null; then
        echo "Installed"
    else
        echo "Not installed"
    fi
}
node