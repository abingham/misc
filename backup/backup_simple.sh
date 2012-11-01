export PASSPHRASE=s4YCsGDBhVgt
export LOGFILE=/Users/abingham/Desktop/duplicity.log

duplicity remove-older-than 1Y file:///Users/abingham/Google\ Drive/backup/gnucash >> $LOGFILE

duplicity --allow-source-mismatch /Users/abingham/Documents/gnucash/ file:///Users/abingham/Google\ Drive/backup/gnucash >> $LOGFILE

unset PASSPHRASE
