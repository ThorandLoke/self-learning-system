#!/usr/bin/env python3
"""
Sync learning progress to knowledge base.
"""

import argparse
import json
import os
import shutil
from datetime import datetime


def load_learning_queue(base_path):
    path = os.path.join(base_path, ".learnings", "learning-queue.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def sync_to_memory(base_path, target_path):
    """Sync learning progress to memory directory."""
    target = os.path.expanduser(target_path)
    os.makedirs(target, exist_ok=True)
    
    # Copy learning rules
    rules_src = os.path.join(base_path, ".learnings", "LEARNING_RULES.md")
    if os.path.exists(rules_src):
        shutil.copy2(rules_src, os.path.join(target, "LEARNING_RULES.md"))
        print(f"✓ Synced: LEARNING_RULES.md")
    
    # Copy queue
    queue_src = os.path.join(base_path, ".learnings", "learning-queue.json")
    if os.path.exists(queue_src):
        shutil.copy2(queue_src, os.path.join(target, "learning-queue.json"))
        print(f"✓ Synced: learning-queue.json")
    
    # Update memory log
    today = datetime.now().strftime("%Y-%m-%d")
    log_entry = f"\n## Learning Sync ({today})\n- Progress synced to knowledge base\n"
    
    memory_log = os.path.join(target, "MEMORY.md")
    if os.path.exists(memory_log):
        with open(memory_log, "a") as f:
            f.write(log_entry)
    
    print(f"\n✅ Sync complete! Target: {target}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--target", default="~/.workbuddy/memory/")
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.workspace)
    sync_to_memory(base_path, args.target)


if __name__ == "__main__":
    main()
