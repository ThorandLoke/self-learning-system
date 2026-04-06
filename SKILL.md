---
name: self-learning-system
description: "A systematic self-learning framework for AI agents with structured review cycles, hands-on coding challenges, and progressive skill building. Enables agents to learn continuously through daily practice, weekly reviews, and targeted challenges."
metadata:
  version: "1.0.0"
  author: "Thor & Loke"
  created: "2026-04-05"
  tags: ["learning", "education", "practice", "self-improvement", "coding-challenges"]
---

# Self-Learning System

A comprehensive learning framework for AI agents to build skills systematically through daily practice, weekly reviews, and hands-on challenges.

## When to Use This Skill

Use this skill when:
- Setting up a new learning routine for an AI agent
- Creating structured learning plans with clear milestones
- Designing hands-on coding challenges to reinforce concepts
- Implementing spaced repetition and review cycles
- Tracking learning progress over time
- Building a personal knowledge base through practice

## Quick Start

### 1. Initialize Learning Environment

```bash
# Create learning directory structure
python3 ~/.workbuddy/skills/self-learning-system/scripts/init-learning.py \
  --workspace /path/to/workspace \
  --agent-name "YourAgentName"
```

### 2. Start Daily Learning

```bash
# Run daily learning routine
python3 ~/.workbuddy/skills/self-learning-system/scripts/daily-routine.py
```

### 3. Take a Challenge

```bash
# Start a coding challenge
python3 ~/.workbuddy/skills/self-learning-system/scripts/start-challenge.py \
  --level 2 \
  --topic "async-programming"
```

## Learning Framework

### The 5-Phase Learning Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEARNING CYCLE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐                 │
│   │  Review  │───→│ Practice │───→│  Learn   │                 │
│   │  (复习)  │    │  (实战)  │    │  (新知)  │                 │
│   └──────────┘    └──────────┘    └──────────┘                 │
│        ↑                              │                         │
│        └──────────┬───────────────────┘                         │
│                   │                                              │
│              ┌────┴────┐    ┌──────────┐                        │
│              │ Organize│───→│  Sync    │                        │
│              │ (整理)  │    │  (同步)  │                        │
│              └─────────┘    └──────────┘                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Daily Routine (30-60 minutes)

1. **Review (5-10 min)** - Review previous day's learning
2. **Practice (15-30 min)** - Complete a coding challenge
3. **Learn (10-15 min)** - Study new concepts
4. **Organize (5 min)** - Document insights
5. **Sync (5 min)** - Sync to knowledge base

### Weekly Schedule

| Day | Focus | Activity |
|-----|-------|----------|
| Monday | Review | Weekly review of all topics |
| Tuesday-Thursday | Learn | New topics and concepts |
| Friday | Apply | Apply learning to real projects |
| Saturday | Challenge | Extended coding challenge |
| Sunday | Summary | Weekly summary and planning |

## Challenge System

### Difficulty Levels

| Level | Stars | Duration | Description |
|-------|-------|----------|-------------|
| L1 | ⭐ | 15-30 min | Basic concept implementation |
| L2 | ⭐⭐ | 30-60 min | Intermediate feature building |
| L3 | ⭐⭐⭐ | 1-2 hours | Complex system design |
| L4 | ⭐⭐⭐⭐ | Half day | Full project implementation |

### Challenge Categories

- **Algorithms**: Data structures, sorting, graph algorithms
- **System Design**: Caching, rate limiting, message queues
- **Web Development**: APIs, authentication, real-time features
- **DevOps**: Docker, CI/CD, monitoring
- **Performance**: Optimization, profiling, scaling

### Built-in Challenges

See `assets/challenges/` for ready-to-use challenges:
- `challenge_001_redis_cache/` - Redis cache decorator
- `challenge_002_rate_limiter/` - FastAPI rate limiter
- `challenge_003_promise_impl/` - Promise/A+ implementation
- `challenge_004_async_worker/` - Background task queue
- `challenge_005_docker_compose/` - Multi-service deployment

## Learning Rules

### Core Principles

1. **Spaced Repetition** - Review topics at increasing intervals
2. **Active Recall** - Practice without looking at notes
3. **Deliberate Practice** - Focus on weak areas
4. **Project-Based** - Apply learning to real code
5. **Document Everything** - Write down insights

### Priority Matrix

```
    High Impact
         │
    P0   │   P1
  Do Now │  This Week
         │
  ───────┼─────────
         │
    P2   │   P3
  This   │  Future
  Month  │
         │
    Low Impact
```

## Configuration

### Learning Profile (`~/.learning-profile.json`)

```json
{
  "agent_name": "Loke",
  "daily_goal_minutes": 60,
  "preferred_topics": ["backend", "system-design", "performance"],
  "challenge_difficulty": "adaptive",
  "review_interval_days": [1, 3, 7, 14, 30],
  "sync_enabled": true,
  "sync_target": "~/.workbuddy/memory/"
}
```

### Topic Queue (`~/.learning-queue.json`)

```json
{
  "current": {
    "topic": "redis-caching",
    "started": "2026-04-05",
    "progress": 75
  },
  "queue": [
    {"topic": "asyncio", "priority": "P0"},
    {"topic": "docker-multi-stage", "priority": "P1"},
    {"topic": "kubernetes", "priority": "P2"}
  ],
  "completed": [
    {"topic": "python-decorators", "completed": "2026-04-04"}
  ]
}
```

## Progress Tracking

### Daily Log Format

```markdown
# 2026-04-05 Learning Log

## Today's Focus
- Topic: Redis Caching Strategies
- Challenge: #001 Redis Cache Decorator
- Time: 45 minutes

## What I Learned
1. Cache Aside pattern is most flexible
2. TTL should include random jitter to prevent thundering herd
3. Decorators can handle both sync and async functions

## Challenge Results
- Status: ✅ Completed
- Difficulty: ⭐⭐
- Time Spent: 30 minutes
- Key Implementation: Used functools.wraps to preserve metadata

## Code Written
- `challenge_001_redis_cache_decorator.py` (120 lines)
- `challenge_001_notes.md` (insights and learnings)

## Tomorrow's Plan
- Review today's implementation
- Start Challenge #002: Rate Limiter
- Study FastAPI middleware patterns
```

### Weekly Summary Format

```markdown
# Week 14 Learning Summary (2026-04-01 to 2026-04-07)

## Statistics
- Total Learning Time: 5 hours 30 minutes
- Challenges Completed: 3
- Topics Covered: 4
- Code Written: 800+ lines

## Topics Mastered
- ✅ Redis caching strategies
- ✅ Python async/await patterns
- ✅ FastAPI middleware design

## Challenges Completed
1. #001 Redis Cache Decorator ⭐⭐
2. #002 Rate Limiter ⭐⭐
3. #003 Promise Implementation ⭐⭐⭐

## Applied to Projects
- BoligBeregner: Added Redis caching layer
- JobMatchAI: Optimized database queries

## Next Week's Focus
- Kubernetes fundamentals
- Microservices patterns
- Challenge #004: Distributed Lock
```

## Scripts Reference

### `scripts/init-learning.py`
Initialize learning environment for a workspace.

**Usage:**
```bash
python3 scripts/init-learning.py --workspace /path/to/project --agent-name "AgentName"
```

**Creates:**
- `.learnings/` directory structure
- `LEARNING_RULES.md` template
- `learning-queue.json` with default topics

### `scripts/daily-routine.py`
Run the daily learning routine.

**Usage:**
```bash
python3 scripts/daily-routine.py [--quick] [--focus TOPIC]
```

**Options:**
- `--quick`: Skip review, go straight to practice (15 min)
- `--focus TOPIC`: Focus on specific topic today

### `scripts/start-challenge.py`
Start a coding challenge.

**Usage:**
```bash
python3 scripts/start-challenge.py --level 2 --topic "caching"
```

**Options:**
- `--level 1-4`: Difficulty level
- `--topic`: Challenge category
- `--random`: Pick random challenge

### `scripts/review-topics.py`
Review previously learned topics.

**Usage:**
```bash
python3 scripts/review-topics.py [--days 7] [--format quiz]
```

**Options:**
- `--days N`: Review topics from last N days
- `--format quiz|summary|cards`: Review format

### `scripts/sync-progress.py`
Sync learning progress to knowledge base.

**Usage:**
```bash
python3 scripts/sync-progress.py [--target ~/.workbuddy/memory/]
```

## Best Practices

### For Effective Learning

1. **Consistency over intensity** - 30 min daily beats 3 hours once a week
2. **Active over passive** - Write code, don't just read
3. **Spaced repetition** - Review at 1, 3, 7, 14, 30 day intervals
4. **Teach to learn** - Write notes as if teaching someone else
5. **Apply immediately** - Use new knowledge in real projects

### For Challenge Success

1. **Timebox strictly** - Don't spend 3 hours on a 30-min challenge
2. **Fail fast** - If stuck >10 min, look at hints
3. **Review solutions** - Compare your approach with best practices
4. **Document insights** - Write down what you learned
5. **Refactor later** - First make it work, then make it better

### For Knowledge Retention

1. **Write quick reference cards** - One page per topic
2. **Create cheat sheets** - Commands, patterns, formulas
3. **Build a personal wiki** - Link related concepts
4. **Use analogies** - Connect new concepts to known ones
5. **Practice retrieval** - Test yourself without looking at notes

## Integration with Other Skills

### With `continuous-learning-loop`
Use this skill for the "Learn" and "Practice" phases, then use `continuous-learning-loop` to sync and apply to projects.

### With `knowledge-base`
Store learning insights in your knowledge base for long-term retention and retrieval.

### With `project-management`
Link challenges to real project tasks for practical application.

## Troubleshooting

### "I'm not making progress"
- Check if challenges are too easy/hard (adjust level)
- Ensure daily consistency (even 15 min is better than skipping)
- Review if topics are relevant to your goals

### "I forget what I learned"
- Increase review frequency
- Write more detailed notes
- Create quick reference cards
- Apply knowledge to real projects immediately

### "Challenges are too hard"
- Start with lower difficulty
- Break challenge into smaller steps
- Study prerequisite topics first
- Use hints and reference solutions

### "I don't have enough time"
- Use `--quick` mode for 15-min sessions
- Focus on one topic per week
- Combine learning with project work
- Review during idle moments

## Examples

### Example 1: Setting Up New Agent

```bash
# Initialize learning system
python3 scripts/init-learning.py --workspace ~/projects/my-agent --agent-name "Nova"

# Start first challenge
python3 scripts/start-challenge.py --level 1 --random

# Run daily routine
python3 scripts/daily-routine.py
```

### Example 2: Focus Week on Async Programming

```bash
# Configure focus
python3 scripts/daily-routine.py --focus "async-programming"

# Day 1-2: Learn concepts
# (study async/await, event loop, tasks)

# Day 3: Challenge #001
python3 scripts/start-challenge.py --level 2 --topic "async"

# Day 4: Apply to project
# (add async support to existing code)

# Day 5: Review and document
python3 scripts/review-topics.py --days 5
```

### Example 3: Building Knowledge Base

```bash
# Daily routine for 30 days
for i in {1..30}; do
  python3 scripts/daily-routine.py
  python3 scripts/sync-progress.py
done

# Generate summary
python3 scripts/generate-summary.py --month 2026-04
```

## Resources

### Reference Materials
- `references/learning-theory.md` - Cognitive science of learning
- `references/spaced-repetition.md` - Review scheduling algorithms
- `references/challenge-design.md` - How to create good challenges

### Challenge Templates
- `assets/challenges/template/` - Starter template for new challenges
- `assets/challenges/checklist.md` - Challenge quality checklist

### Quick References
- `assets/quick-ref/python-async.md`
- `assets/quick-ref/redis-commands.md`
- `assets/quick-ref/docker-basics.md`

---

**Remember**: The goal is not to finish quickly, but to learn deeply. Take your time, practice consistently, and enjoy the process of mastery.
