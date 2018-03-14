#!/bin/bash

 get_release() {
     # Does this commit have an associated release tag?
     git tag --points-at HEAD | tail -n1 2>/dev/null |
         sed -e 's/^release-//'
 }
