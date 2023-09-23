#!/bin/bash
set -euf -o pipefail

# Download the MBPP
wget --no-check-certificate --content-disposition https://github.com/google-research/google-research/blob/master/mbpp/mbpp.jsonl

# Download the HumanEval
DATAFILE_URL="https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz"
DATAFILE_NAME="HumanEval.jsonl.gz"

wget --no-check-certificate --content-disposition -O $DATAFILE_URL $DATAFILE_NAME
gzip -df $DATAFILE_NAME
rm $DATAFILE_NAME
