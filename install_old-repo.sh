#!/bin/bash

# IMPORTANT: We have to download the old repo of `chatgpt-wrapper`; since this repo is the last version that supports browser-based chats.

# Authorize
chmod +x *

# Unzip the old-repo! 
unzip main.zip;
cd chatgpt-wrapper-main/;

# Install the old-repo
pip install -e . --quiet;

# Echo
echo "INFO: The old-repo of chatgpt-wrapper has been installed successfully."
