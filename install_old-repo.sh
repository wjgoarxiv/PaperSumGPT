#!/bin/bash

# IMPORTANT: We have to download the old repo of `chatgpt-wrapper`; since this repo is the last version that supports browser-based chats.

# Authorize
chmod +x *

# Download the old-repo
wget https://github.com/mmabrouk/chatgpt-wrapper/archive/5de50d92d2b9937165f22463350b1fac660e8e54.zip;
unzip 5de50d92d2b9937165f22463350b1fac660e8e54.zip;
cd llm-workflow-engine-5de50d92d2b9937165f22463350b1fac660e8e54/;

# Install the old-repo
pip install -e . --quiet;

# Echo
echo "INFO: The old-repo of chatgpt-wrapper has been installed successfully."
