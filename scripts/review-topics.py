#!/usr/bin/env python3
"""
Review previously learned topics.
"""

import argparse
import os
from datetime import datetime, timedelta


def get_recent_logs(base_path, days=7):
    """Get recent daily logs."""
    logs = []
    logs_dir = os.path.join(base_path, ".learnings")
    
    for i in range(days):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        log_path = os.path.join(logs_dir, f"{date}.md")
        if os.path.exists(log_path):
            with open(log_path) as f:
                logs.append({"date": date, "content": f.read()})
    
    return logs


def generate_quiz(logs):
    """Generate review questions from logs."""
    print("\n📝 REVIEW QUIZ")
    print("="*50)
    
    questions = [
        "What was the main topic you learned yesterday?",
        "Can you explain it without looking at notes?",
        "What code did you write?",
        "What challenges did you face?",
        "How would you apply this to a real project?"
    ]
    
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q}")
    
    print("\n💡 Try to answer before checking your notes!")


def show_summary(logs):
    """Show summary of recent learning."""
    print(f"\n📊 LAST {len(logs)} DAYS SUMMARY")
    print("="*50)
    
    for log in logs:
        print(f"\n📅 {log['date']}")
        # Extract "What I Learned" section
        content = log['content']
        if "## What I Learned" in content:
            section = content.split("## What I Learned")[1].split("##")[0]
            for line in section.strip().split("\n")[:5]:
                if line.strip():
                    print(f"   {line.strip()}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--format", choices=["quiz", "summary"], default="quiz")
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.workspace)
    logs = get_recent_logs(base_path, args.days)
    
    if not logs:
        print("No recent logs found.")
        return
    
    print(f"📚 Found {len(logs)} learning sessions")
    
    if args.format == "quiz":
        generate_quiz(logs)
    else:
        show_summary(logs)


if __name__ == "__main__":
    main()
