#!/bin/sh

PATH=/usr/bin

LOGFILE=/home/abingham/Desktop/duplicity.log

. /home/abingham/bin/s3_credentials

# Remove backups older than a year
duplicity remove-older-than 1Y s3+http://austin_bingham_backup_gpass >> $LOGFILE
duplicity remove-older-than 1Y s3+http://austin_bingham_backup_gnucash >> $LOGFILE

# Perform backups
duplicity --allow-source-mismatch /home/abingham/.gpass s3+http://austin_bingham_backup_gpass >> $LOGFILE
duplicity --allow-source-mismatch /home/abingham/Documents/gnucash s3+http://austin_bingham_backup_gnucash >> $LOGFILE

unset PASSPHRASE
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
