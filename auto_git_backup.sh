
# ⚡ Ultra Auto Git & Backup Script – S21 Termux

PROJECT_DIR=~/s21_debug/s21-mobile-debug
REPORTS_DIR="$PROJECT_DIR/reports"

cd $PROJECT_DIR || exit

# -------------------------
# 1️⃣ Backup Reports (optional)
# -------------------------
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backup_reports_$TIMESTAMP.tar.gz"

if [ -d "$REPORTS_DIR" ]; then
    tar -czf "$BACKUP_FILE" reports/
    echo "Reports backup created: $BACKUP_FILE"
else
    echo "No reports folder found, skipping backup."
fi

# -------------------------
# 2️⃣ Git Commit & Push
# -------------------------
git add .
COMMIT_MESSAGE="Auto-commit: $TIMESTAMP"

# Commit only if there are changes
if ! git diff --cached --quiet; then
    git commit -m "$COMMIT_MESSAGE"
    git push origin main
    echo "Changes committed and pushed to GitHub."
else
    echo "No changes detected. Nothing to commit."
fi
