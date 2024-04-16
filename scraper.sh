#!/bin/sh

url=$1
if [ -z $1 ]; then
    echo "Please specify a URL"
    exit 1
fi

# fetch website
html=$(curl -s $url)
retval=$?
if [ $retval != 0 ]; then
    echo "Failed to fetch website via curl, return code $retval"
    exit 1
fi

for dataset in G4NDL G4EMLOW PhotonEvaporation RadioactiveDecay G4PARTICLEXS G4PII RealSurface G4SAIDDATA G4ABLA G4INCL G4ENSDFSTATE G4TENDL; do
    echo "Looking for $dataset"
    filtered_line=$(curl -s $url | grep $dataset)
    filtered_version=$(echo $filtered_line | sed -E "s%.*${dataset}-(.+?)\".*%\1%")
    filtered_url=$(echo $filtered_line | sed -E "s%.*(https.+?\.tar\.gz).*%\1%")
    echo "'$filtered_version': '$filtered_url'"
done
