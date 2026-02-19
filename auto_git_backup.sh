#!/bin/bash
PROJECT_DIR=~/s21-mobile-debug
REPORTS_DIR="$PROJECT_DIR/reports"

cd $PROJECT_DIR || exit

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backup_reports_$TIMESTAMP.tar.gz"

if [ -d "$REPORTS_DIR" ]; then
    tar -czf "$BACKUP_FILE" reports/
    echo "Reports backup created: $BACKUP_FILE"
else
    echo "No reports folder found, skipping backup."
fi

git add .
COMMIT_MESSAGE="Auto-commit: $TIMESTAMP"

if ! git diff --cached --quiet; then
    git commit -m "$COMMIT_MESSAGE"
    git push origin main
    echo "Changes committed and pushed to GitHub."
else
    echo "No changes detected. Nothing to commit."
fi
