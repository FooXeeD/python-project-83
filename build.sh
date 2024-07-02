#!/usr/bin/env bash

make install && psql -U mikl_pv -a -d $DATABASE_URL -f database.sql