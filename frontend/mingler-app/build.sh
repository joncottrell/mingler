#! /bin/bash

npm run build

rm -rf ../../backend/public
mv -f build ../../backend/public
