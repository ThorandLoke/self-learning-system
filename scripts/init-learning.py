#!/usr/bin/env python3
"""
Initialize learning environment for an AI agent.
Creates directory structure and configuration files.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path


def create_directory_structure(base_path: str) -> None:
    """Create the learning directory structure."""
    dirs = [
        ".learnings/practice",
        ".learnings/challenges",
        ".learnings/notes",
        ".learnings/reviews",
        ".learnings/quick-ref",
    ]
    
    for dir_path in dirs:
        full_path = os.path.join(base_path, dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"✓ Created: {full_path}")


def create_learning_rules(base_path: str, agent_name: str) -> None:
    """Create LEARNING_RULES.md template."""
    rules_content = f"""# Learning Rules - {agent_name}

## Agent Profile
- **Name**: {agent_name}
- **Created**: {datetime.now().strftime("%Y-%m-%d")}
- **Daily Goal**: 60 minutes
- **Current Streak**: 0 days

## Learning Framework

### The 5-Phase Cycle
1. **Review** (5-10 min) - Review previous learning
2. **Practice** (15-30 min) - Coding challenge
3. **Learn** (10-15 min) - New concepts
4. **Organize** (5 min) - Document insights
5. **Sync** (5 min) - Update knowledge base

### Weekly Schedule
- **Monday**: Weekly review
- **Tuesday-Thursday**: New topics
- **Friday**: Apply to projects
- **Saturday**: Extended challenge
- **Sunday**: Summary & planning

## Topic Queue

### Currently Learning
- [ ] Topic 1 (started: {datetime.now().strftime("%Y-%m-%d")})

### Queue (P0 - Do Now)
- [ ] Topic 2
- [ ] Topic 3

### Queue (P1 - This Week)
- [ ] Topic 4
- [ ] Topic 5

### Queue (P2 - This Month)
- [ ] Topic 6

### Completed ✅
- None yet

## Challenge Progress

### Current Challenge
- **ID**: #001
- **Level**: ⭐⭐
- **Status**: Not started
- **Started**: -
- **Completed**: -

### Completed Challenges
- None yet

## Statistics

### This Week
- Learning Time: 0 minutes
- Challenges: 0
- Topics: 0
- Code Lines: 0

### This Month
- Learning Time: 0 minutes
- Challenges: 0
- Topics: 0
- Code Lines: 0

## Quick Reference

### Review Schedule
- Day 1: Immediate review after learning
- Day 3: First spaced repetition
- Day 7: Weekly review
- Day 14: Bi-weekly review
- Day 30: Monthly review

### Challenge Levels
- ⭐: 15-30 min (basic)
- ⭐⭐: 30-60 min (intermediate)
- ⭐⭐⭐: 1-2 hours (advanced)
- ⭐⭐⭐⭐: Half day (expert)

## Notes
- Start with Level 1 challenges
- Focus on consistency over intensity
- Document insights immediately
- Apply learning to real projects
"""
    
    rules_path = os.path.join(base_path, ".learnings", "LEARNING_RULES.md")
    with open(rules_path, "w") as f:
        f.write(rules_content)
    print(f"✓ Created: {rules_path}")


def create_learning_queue(base_path: str) -> None:
    """Create learning-queue.json with default topics."""
    queue = {
        "current": None,
        "queue": [
            {"topic": "python-basics", "priority": "P0", "difficulty": "L1"},
            {"topic": "data-structures", "priority": "P0", "difficulty": "L1"},
            {"topic": "algorithms", "priority": "P1", "difficulty": "L2"},
            {"topic": "system-design", "priority": "P1", "difficulty": "L2"},
            {"topic": "performance", "priority": "P2", "difficulty": "L3"},
        ],
        "completed": [],
        "stats": {
            "total_time_minutes": 0,
            "challenges_completed": 0,
            "topics_completed": 0,
            "code_lines_written": 0,
            "current_streak": 0,
            "last_learning_date": None
        }
    }
    
    queue_path = os.path.join(base_path, ".learnings", "learning-queue.json")
    with open(queue_path, "w") as f:
        json.dump(queue, f, indent=2)
    print(f"✓ Created: {queue_path}")


def create_daily_log_template(base_path: str) -> None:
    """Create today's daily log template."""
    today = datetime.now().strftime("%Y-%m-%d")
    log_content = f"""# {today} Learning Log

## Today's Focus
- Topic: 
- Challenge: 
- Time:  minutes

## What I Learned
1. 
2. 
3. 

## Challenge Results
- Status: 
- Difficulty: 
- Time Spent:  minutes
- Key Implementation: 

## Code Written
- 

## Tomorrow's Plan
- 

## Notes
- 
"""
    
    log_path = os.path.join(base_path, ".learnings", f"{today}.md")
    with open(log_path, "w") as f:
        f.write(log_content)
    print(f"✓ Created: {log_path}")


def create_profile(base_path: str, agent_name: str) -> None:
    """Create agent learning profile."""
    profile = {
        "agent_name": agent_name,
        "created": datetime.now().isoformat(),
        "daily_goal_minutes": 60,
        "preferred_topics": ["backend", "system-design", "performance"],
        "challenge_difficulty": "adaptive",
        "review_interval_days": [1, 3, 7, 14, 30],
        "sync_enabled": True,
        "sync_target": "~/.workbuddy/memory/",
        "learning_style": "project-based"
    }
    
    profile_path = os.path.join(base_path, ".learnings", ".learning-profile.json")
    with open(profile_path, "w") as f:
        json.dump(profile, f, indent=2)
    print(f"✓ Created: {profile_path}")


def main():
    parser = argparse.ArgumentParser(description="Initialize learning environment")
    parser.add_argument("--workspace", required=True, help="Path to workspace")
    parser.add_argument("--agent-name", default="Agent", help="Name of the learning agent")
    
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.workspace)
    
    print(f"🎓 Initializing learning environment for {args.agent_name}")
    print(f"📁 Workspace: {base_path}")
    print()
    
    # Create directories
    create_directory_structure(base_path)
    
    # Create configuration files
    create_learning_rules(base_path, args.agent_name)
    create_learning_queue(base_path)
    create_profile(base_path, args.agent_name)
    create_daily_log_template(base_path)
    
    print()
    print("✅ Learning environment initialized!")
    print()
    print("Next steps:")
    print("1. Review .learnings/LEARNING_RULES.md")
    print("2. Customize learning-queue.json with your topics")
    print("3. Run: python3 scripts/daily-routine.py")


if __name__ == "__main__":
    main()
