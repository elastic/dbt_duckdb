#!/usr/bin/env bash

# set color variables
GREEN='\e[32m'
GREEN_REVERSE='\e[32;7m'
RED='\e[31m'
YELLOW='\e[33m'
ELASTIC='\e[36;1;45m'
ENDC='\e[0m'

# initial print to terminal
echo ""
echo -e "${GREEN}Checking GCP Login Status...${ENDC} ☕☕☕"
echo ""
sleep .5

# check for gcloud ADC's
if [ ! -f "/root/.config/gcloud/application_default_credentials.json" ]; then
    export GOOGLE_APPLICATION_CREDENTIALS=
    echo -e "${RED}To Log into GCP..${ENDC}"
    echo ""
    sleep .5
    gcloud auth application-default login \
    --project=elastic-edm-dev \
    --no-launch-browser \
    --scopes='https://www.googleapis.com/auth/bigquery','https://www.googleapis.com/auth/drive.readonly','https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/iam.test'
    echo ""
else
    echo -e "${GREEN}You are logged into BigQuery... ✔${ENDC}"
    echo ""
    sleep .5
fi

# Give the Green Light
echo -e "${GREEN_REVERSE}Be sure to make a branch for your development!${ENDC} ↱"
echo ""
sleep .5
echo -e "${ELASTIC}Enjoy!${ENDC} 🤖🤖🤖"

exit