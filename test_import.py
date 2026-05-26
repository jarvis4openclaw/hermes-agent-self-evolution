#!/usr/bin/env python3
"""Quick test to verify evolution module can be imported."""
import sys
sys.path.insert(0, '/home/wahid/hermes-agent-self-evolution')

try:
    from evolution.skills import evolve_skill
    print("SUCCESS: evolve_skill module loaded")
    print(f"Available functions: {dir(evolve_skill)}")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)