#!/bin/sh

source s3_credentials

duplicity --file-to-restore aikido/ikyu.txt file:///home/abingham/projects/backup/personal_backup /home/abingham/ikyu.txt

unset PASSPHRASE
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY