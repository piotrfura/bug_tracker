#!/bin/sh
cp -r /app/mkdocs/site/* /app/mkdocs/public/
exec "$@"
