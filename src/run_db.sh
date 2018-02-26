#!/bin/bash

pg_restore -v   -U postgres -d postgres /src/pustakalaya.dump
