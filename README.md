# Samsung Galaxy S21 – Ultra Mobile Debug

Dieses Repository enthält die Mobile-Light Edition des Debug-Frameworks für das Samsung Galaxy S21, lauffähig auf Termux.

## Features
- Logcat Analyse (ANR, FATAL, OOM, SystemUI, Knox)
- Memory & CPU Snapshot
- Health Score Berechnung
- JSON Reports automatisch im `reports/` Ordner
- Auto Git Commit + Push Script (`auto_git_backup.sh`)
- Mobile-Termux-ready, kein Root erforderlich

## Installation & Nutzung
1. Installiere Termux aus F-Droid
2. Update & Python installieren:
   pkg update && pkg upgrade
   pkg install python git
3. Repository klonen (SSH empfohlen):
   git clone git@github.com:macyb27/s21-mobile-debug.git
   cd s21-mobile-debug
4. Optional Bootstrap:
   ./auto_bootstrap.sh
5. Debug starten:
   python3 mobile_debug.py
6. Auto Git Push + Backup:
   ./auto_git_backup.sh

## Ordnerstruktur
s21-mobile-debug/
├── mobile_debug.py
├── auto_bootstrap.sh
├── auto_git_backup.sh
├── README.md
├── WHAT_TO_DO.txt
└── reports/
