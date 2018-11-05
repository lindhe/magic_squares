#!/bin/bash

# Make sure this is run from the toplevel of the repo
CURRENT=$(pwd)
TOPLEVEL=$(git rev-parse --show-toplevel)
if [ $CURRENT != $TOPLEVEL ]
then
    printf "You must run this from the toplevel of the repo!\n"
    exit 1
fi

# Deploy git hooks
ln -s $(pwd)/.hooks/commit-msg .git/hooks/commit-msg
