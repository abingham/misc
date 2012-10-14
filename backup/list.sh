#!/bin/sh

source s3_credentials

duplicity list-current-files s3+http://austin_bingham_backups_personal

unset PASSPHRASE
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
