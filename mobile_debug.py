import subprocess
import os
import json
from datetime import datetime

REPORT_DIR = "reports"

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

def get_logcat():
    try:
        logs = subprocess.check_output(["logcat", "-d"], stderr=subprocess.DEVNULL)
        return logs.decode(errors="ignore")
    except Exception:
        return ""

def analyze_logs(logs):
    issues = []
    score = 100

    if "FATAL EXCEPTION" in logs:
        issues.append("Java Crash Detected")
        score -= 30
    if "ANR" in logs:
        issues.append("ANR Detected")
        score -= 20
    if "OutOfMemoryError" in logs:
        issues.append("OOM Detected")
        score -= 25
    if "Knox" in logs:
        issues.append("Knox Security Event")
    if "SystemUI" in logs:
        issues.append("SystemUI Activity")

    return score, issues

def memory_snapshot():
    try:
        mem = subprocess.check_output(["cat", "/proc/meminfo"])
        return mem.decode()
    except:
        return "Memory info unavailable"

def cpu_snapshot():
    try:
        cpu = subprocess.check_output(["cat", "/proc/loadavg"])
        return cpu.decode()
    except:
        return "CPU info unavailable"

def save_report(score, issues, mem, cpu):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{REPORT_DIR}/report_{timestamp}.json"

    data = {
        "timestamp": timestamp,
        "health_score": score,
        "issues": issues,
        "memory_snapshot": mem[:1000],
        "cpu_snapshot": cpu.strip()
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename

def main():
    print("Samsung Galaxy S21 Ultra Mobile Debug Mode")
    print("Collecting logs...")

    logs = get_logcat()
    score, issues = analyze_logs(logs)

    mem = memory_snapshot()
    cpu = cpu_snapshot()

    report = save_report(score, issues, mem, cpu)

    print("Health Score:", score)
    print("Issues:", issues)
    print("Report saved:", report)

if __name__ == "__main__":
    main()
