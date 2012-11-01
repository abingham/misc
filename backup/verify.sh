#!/bin/sh

source s3_credentials

duplicity verify s3+http://austin_bingham_backups /home/abingham/.backup

unset PASSPHRASE
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY

