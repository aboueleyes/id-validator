#!/usr/bin/bash

server='http://127.0.0.1:8000/core/'
ids=(30003211203135 20003216763121 12203211203135 38803211203135 29903211403135 )


for id in ${ids[@]}; do
    echo "id: $id"
    curl $server$id
    echo
done
