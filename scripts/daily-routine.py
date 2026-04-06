#!/usr/bin/env python3
"""
Daily learning routine script.
Guides through the 5-phase learning cycle.
"""

import argparse
import json
import os
import random
from datetime import datetime, timedelta


def load_learning_queue(base_path: str) -> dict:
    """Load learning queue from JSON."""
    queue_path = os.path.join(base_path, ".learnings", "learning-queue.json")
    if os.path.exists(queue_path):
        with open(queue_path, "r") as f:
            return json.load(f)
    return {"queue": [], "completed": [], "stats": {}}


def save_learning_queue(base_path: str, queue: dict) -> None:
    """Save learning queue to JSON."""
    queue_path = os.path.join(base_path, ".learnings", "learning-queue.json")
    with open(queue_path, "w") as f:
        json.dump(queue, f, indent=2)


def get_recent_logs(base_path: str, days: int = 7) -> list:
    """Get recent daily log files."""
    logs = []
    logs_dir = os.path.join(base_path, ".learnings")
    
    for i in range(days):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        log_path = os.path.join(logs_dir, f"{date}.md")
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                logs.append({"date": date, "content": f.read()})
    
    return logs


def phase_1_review(base_path: str) -> None:
    """Phase 1: Review previous learning."""
    print("\n" + "="*60)
    print("📚 PHASE 1: REVIEW (5-10 minutes)")
    print("="*60)
    
    logs = get_recent_logs(base_path, days=3)
    
    if not logs:
        print("No previous logs found. Starting fresh!")
        return
    
    print(f"\nFound {len(logs)} recent learning sessions:")
    for log in logs:
        print(f"  - {log['date']}")
    
    print("\n📝 Review Questions:")
    print("1. What did you learn yesterday?")
    print("2. Can you explain the key concepts without looking at notes?")
    print("3. What code did you write?")
    print("4. Any challenges or insights?")
    
    print("\n💡 Tip: Active recall is more effective than re-reading.")
    print("   Try to remember before checking your notes.")


def phase_2_practice(base_path: str, level: int = None) -> None:
    """Phase 2: Practice with a challenge."""
    print("\n" + "="*60)
    print("💻 PHASE 2: PRACTICE (15-30 minutes)")
    print("="*60)
    
    # Get available challenges
    challenges_dir = os.path.join(base_path, ".learnings", "challenges")
    os.makedirs(challenges_dir, exist_ok=True)
    
    # If no level specified, suggest based on progress
    if level is None:
        queue = load_learning_queue(base_path)
        completed = queue.get("stats", {}).get("challenges_completed", 0)
        if completed < 3:
            level = 1
        elif completed < 10:
            level = 2
        else:
            level = 3
    
    stars = "⭐" * level
    print(f"\n🎯 Suggested Challenge Level: {stars}")
    print(f"   Duration: {15 * level}-{30 * level} minutes")
    
    print("\n📋 To start a challenge, run:")
    print(f"   python3 scripts/start-challenge.py --level {level}")
    
    print("\n💡 Tips for success:")
    print("   - Timebox strictly (use a timer)")
    print("   - If stuck >10 min, check hints")
    print("   - Focus on working solution first")
    print("   - Document insights as you go")


def phase_3_learn(base_path: str, focus_topic: str = None) -> None:
    """Phase 3: Learn new concepts."""
    print("\n" + "="*60)
    print("🧠 PHASE 3: LEARN (10-15 minutes)")
    print("="*60)
    
    queue = load_learning_queue(base_path)
    
    if focus_topic:
        topic = focus_topic
    elif queue.get("queue"):
        # Get highest priority topic
        p0_topics = [t for t in queue["queue"] if t.get("priority") == "P0"]
        if p0_topics:
            topic = p0_topics[0]["topic"]
        else:
            topic = queue["queue"][0]["topic"]
    else:
        topic = "Choose a topic from your queue"
    
    print(f"\n📖 Today's Topic: {topic}")
    
    print("\n🎯 Learning Activities:")
    print("1. Read documentation or tutorial (5 min)")
    print("2. Study code examples (5 min)")
    print("3. Take notes on key concepts (5 min)")
    
    print("\n✍️ Note-Taking Template:")
    print("   - Core concept: [one sentence summary]")
    print("   - Key points: [3-5 bullet points]")
    print("   - Code example: [minimal working example]")
    print("   - Questions: [what to explore next]")


def phase_4_organize(base_path: str) -> None:
    """Phase 4: Organize and document."""
    print("\n" + "="*60)
    print("📝 PHASE 4: ORGANIZE (5 minutes)")
    print("="*60)
    
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(base_path, ".learnings", f"{today}.md")
    
    print(f"\n📄 Update your daily log: {today}.md")
    
    print("\n✅ Checklist:")
    print("  [ ] What you learned today")
    print("  [ ] Challenge results and insights")
    print("  [ ] Code written (with line counts)")
    print("  [ ] Tomorrow's plan")
    
    print("\n💡 Quick Reference Cards:")
    print("   Create one-page summaries for quick review")
    print(f"   Location: .learnings/quick-ref/")


def phase_5_sync(base_path: str) -> None:
    """Phase 5: Sync to knowledge base."""
    print("\n" + "="*60)
    print("🔄 PHASE 5: SYNC (5 minutes)")
    print("="*60)
    
    print("\n📤 Sync Options:")
    print("1. Sync to local knowledge base")
    print("   python3 scripts/sync-progress.py")
    print("\n2. Sync to external system")
    print("   (configure in .learning-profile.json)")
    
    # Update stats
    queue = load_learning_queue(base_path)
    stats = queue.get("stats", {})
    stats["last_learning_date"] = datetime.now().isoformat()
    
    # Update streak
    last_date = stats.get("last_learning_date")
    if last_date:
        last = datetime.fromisoformat(last_date)
        if (datetime.now() - last).days <= 1:
            stats["current_streak"] = stats.get("current_streak", 0) + 1
        else:
            stats["current_streak"] = 1
    
    queue["stats"] = stats
    save_learning_queue(base_path, queue)
    
    print(f"\n📊 Current Streak: {stats.get('current_streak', 0)} days")
    print("   Keep it up! 🔥")


def print_summary() -> None:
    """Print daily routine summary."""
    print("\n" + "="*60)
    print("📋 DAILY ROUTINE SUMMARY")
    print("="*60)
    print("""
Total Time: 30-60 minutes

Phase 1: Review      (5-10 min)  📚 回顾昨日所学
Phase 2: Practice    (15-30 min) 💻 完成实战挑战
Phase 3: Learn       (10-15 min) 🧠 学习新知识点
Phase 4: Organize    (5 min)     📝 整理学习笔记
Phase 5: Sync        (5 min)     🔄 同步到知识库

💡 Remember: Consistency beats intensity!
   15 minutes daily > 3 hours once a week
""")


def main():
    parser = argparse.ArgumentParser(description="Daily learning routine")
    parser.add_argument("--workspace", default=".", help="Path to workspace")
    parser.add_argument("--quick", action="store_true", help="Quick mode (skip review)")
    parser.add_argument("--focus", help="Focus on specific topic")
    
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.workspace)
    
    print("🎓 Welcome to Your Daily Learning Routine!")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %A')}")
    
    if args.quick:
        print("\n⚡ Quick Mode: Skipping review phase")
        phase_2_practice(base_path)
        phase_3_learn(base_path, args.focus)
        phase_4_organize(base_path)
        phase_5_sync(base_path)
    else:
        phase_1_review(base_path)
        phase_2_practice(base_path)
        phase_3_learn(base_path, args.focus)
        phase_4_organize(base_path)
        phase_5_sync(base_path)
    
    print_summary()
    
    print("\n✅ Daily routine complete!")
    print("   See you tomorrow! 🚀")


if __name__ == "__main__":
    main()
