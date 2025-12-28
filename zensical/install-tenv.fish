#!/usr/bin/env fish

# Install tenv from GitHub releases

set LATEST_VERSION (curl --silent https://api.github.com/repos/tofuutils/tenv/releases/latest | jq -r .tag_name)

if test -z "$LATEST_VERSION"
    echo "Error: Could not fetch latest version"
    exit 1
end

echo "Downloading tenv version: $LATEST_VERSION"

set FILENAME "tenv_"$LATEST_VERSION"_amd64.deb"
curl -O -L "https://github.com/tofuutils/tenv/releases/latest/download/$FILENAME"

if test $status -ne 0
    echo "Error: Failed to download $FILENAME"
    exit 1
end

echo "Installing $FILENAME..."
sudo dpkg -i "$FILENAME"

if test $status -eq 0
    echo "Successfully installed tenv $LATEST_VERSION"
    # Clean up the downloaded file
    rm "$FILENAME"
else
    echo "Error: Installation failed"
    exit 1
end
