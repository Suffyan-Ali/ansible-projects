#!/bin/bash
TARGET="/var/www/html"
GIT_WORK_TREE="$TARGET" git checkout -f
chown -R www-data:www-data $TARGET
