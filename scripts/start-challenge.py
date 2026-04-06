#!/usr/bin/env python3
"""
Start a coding challenge.
"""

import argparse
import os
import random
from datetime import datetime


CHALLENGES = {
    1: [
        {"id": "001", "title": "Hello World API", "topic": "web-dev"},
        {"id": "002", "title": "List Reversal", "topic": "algorithms"},
    ],
    2: [
        {"id": "004", "title": "Redis Cache Decorator", "topic": "caching"},
        {"id": "005", "title": "Rate Limiter", "topic": "api-design"},
    ],
    3: [
        {"id": "007", "title": "Promise Implementation", "topic": "async"},
        {"id": "008", "title": "LRU Cache", "topic": "algorithms"},
    ]
}


def get_challenge(level, topic=None):
    available = CHALLENGES.get(level, [])
    if topic:
        available = [c for c in available if c.get("topic") == topic]
    return random.choice(available) if available else None


def create_challenge_files(base_path, challenge, level):
    cid = challenge["id"]
    challenge_dir = os.path.join(base_path, ".learnings", "challenges", f"challenge_{cid}")
    os.makedirs(challenge_dir, exist_ok=True)
    
    # Create README
    readme = f"""# Challenge #{cid}: {challenge['title']}

## Difficulty: {'⭐' * level}

## Requirements
- [ ] Implement solution
- [ ] Pass test cases
- [ ] Write notes

Started: {datetime.now().strftime("%Y-%m-%d %H:%M")}
"""
    
    with open(os.path.join(challenge_dir, "README.md"), "w") as f:
        f.write(readme)
    
    # Create solution template
    with open(os.path.join(challenge_dir, "solution.py"), "w") as f:
        f.write(f"# Challenge #{cid} Solution\n\n# TODO: Implement\n\ndef main():\n    pass\n")
    
    # Create notes template
    with open(os.path.join(challenge_dir, "notes.md"), "w") as f:
        f.write("# Notes\n\n## Approach\n\n## Key Insights\n\n## Time Spent\n")
    
    return challenge_dir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--level", type=int, default=1)
    parser.add_argument("--topic")
    parser.add_argument("--random", action="store_true", dest="random_choice")
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.workspace)
    challenge = get_challenge(args.level, args.topic)
    
    if not challenge:
        print(f"No challenge found for level {args.level}")
        return
    
    print(f"🎯 Starting Challenge #{challenge['id']}: {challenge['title']}")
    print(f"   Level: {'⭐' * args.level}")
    print(f"   Topic: {challenge['topic']}")
    
    challenge_dir = create_challenge_files(base_path, challenge, args.level)
    print(f"\n📁 Created: {challenge_dir}")
    print("\nGood luck! 💪")


if __name__ == "__main__":
    main()
