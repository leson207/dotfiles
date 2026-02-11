#!/usr/bin/env bash

LOG="$HOME/.checkpoint/history.log"
LAST="$HOME/.checkpoint/last.txt"
DATE="$(date '+%Y-%m-%d %H:%M')"

TIME_MSG=$(date +%H | awk '{ if ($1 >= 22) print "🛑\033[31mShould you stop now?\033[0m" }')
PROMPT=$(zenity --entry \
	--title="🧠 CHECKPOINT" \
	--text="Still working on: $INTENT ?\nWhat did you just do?\n$TIME_MSG" \
	--width=450)

# Block unlock if empty
while [ -z "$PROMPT" ]; do
	PROMPT=$(zenity --entry \
		--title="🧠 CHECKPOINT (required)" \
		--text="Write something to unlock." \
		--width=450)
done

echo "[$DATE]" >>"$LOG"
echo "$PROMPT" >>"$LOG"
echo "--------------------------------" >>"$LOG"

echo "$PROMPT" >"$LAST"
