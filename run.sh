#!/usr/bin/env bash

BASE_DIR="$(dirname "$(readlink -f $0)" )";
FEATURE="$1";

test -n "$FEATURE" && \
    FEATURE="$(readlink -f $FEATURE)";

cd "$BASE_DIR";

behave "${FEATURE:---}";

