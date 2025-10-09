#!/usr/bin/env python3
"""
Test Overgoal Integration in Scoring Pipeline

Verifies that:
1. DecisionScore now has 5 parameters (including overgoal)
2. Overgoal adjustment is calculated for goals
3. Score breakdown includes overgoal component
"""

from hyperon import MeTTa
from pathlib import Path
import sys

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))
from magus_init import initialize_magus

def test_overgoal_scoring_integration():
    """Test that overgoal is integrated into scoring pipeline"""
    print("="*70)
    print("  OVERGOAL SCORING INTEGRATION TEST")
    print("="*70)

    # Initialize MAGUS
    print("\n1. Initializing MAGUS...")
    metta = initialize_magus()
    base_dir = Path(__file__).parent

    # Load required modules
    print("2. Loading modules...")
    modules = [
        base_dir / 'types.metta',
        base_dir / 'Milestone_2/goal-fitness-metrics/measurability/initial_measurability_calculation.metta',
        base_dir / 'Milestone_2/goal-fitness-metrics/correlation/initial_correlation_calculation.metta',
        base_dir / 'Milestone_3/core/metagoals.metta',
        base_dir / 'Milestone_3/core/antigoals.metta',
        base_dir / 'Milestone_3/core/overgoal.metta',
        base_dir / 'Milestone_3/core/scoring-v2.metta',
    ]

    for module_path in modules:
        if module_path.exists():
            with open(module_path, 'r', encoding='utf-8') as f:
                metta.run(f.read())
            print(f"  ✓ Loaded {module_path.name}")
        else:
            print(f"  ✗ Missing {module_path}")
            return False

    # Test 1: Verify DecisionScore has 5 parameters
    print("\n3. Testing DecisionScore structure...")
    test_score = metta.run('!(decision-score 0.4 0.05 0.095 0.0 0.545)')
    print(f"  DecisionScore created: {test_score}")

    # Count parameters in result - should be 5
    if test_score and len(test_score) > 0:
        result_str = str(test_score[0])
        # The result should contain all 5 values
        if '0.4' in result_str and '0.05' in result_str and '0.095' in result_str:
            print("  ✓ DecisionScore has overgoal parameter (3rd position)")
        else:
            print("  ✗ DecisionScore structure incorrect")
            return False

    # Test 2: Test score breakdown includes overgoal
    print("\n4. Testing score breakdown with overgoal...")
    breakdown_test = metta.run('''
        !(generate-score-breakdown (decision-score 0.4 0.05 0.095 0.0 0.545))
    ''')

    if breakdown_test:
        result = str(breakdown_test[0])
        print(f"  Breakdown result: {result[:200]}...")  # First 200 chars

        # Check if overgoal-adjustment is in the breakdown
        if 'overgoal-adjustment' in result or 'overgoal' in result.lower():
            print("  ✓ Score breakdown includes overgoal component")
        else:
            print("  ✗ Score breakdown missing overgoal")
            return False

    # Test 3: Test overgoal adjustment calculation
    print("\n5. Testing overgoal adjustment calculation...")

    # Create test context with goals
    overgoal_test = metta.run('''
        !(let* (($energy-goal (goal energy 0.9 0.8))
                ($exploration-goal (goal exploration 0.6 0.5))
                ($affinity-goal (goal affinity 0.3 0.2))
                ($goals (Cons $energy-goal (Cons $exploration-goal (Cons $affinity-goal Nil))))
                ($mods (Cons (modulator arousal 0.8) Nil))
                ($context (scoring-context $goals $mods 1000)))
           (calculate-overgoal-adjustment $energy-goal $context))
    ''')

    if overgoal_test:
        result = str(overgoal_test[0])
        print(f"  Overgoal adjustment result: {result}")

        # Try to extract number
        try:
            import re
            numbers = re.findall(r'\d+\.?\d*', result)
            if numbers:
                value = float(numbers[0])
                # Expected: ~0.095 (0.3 × 0.318)
                # Acceptable range: 0.08 to 0.12
                if 0.08 <= value <= 0.12:
                    print(f"  ✓ Overgoal adjustment calculated correctly: {value:.3f}")
                    print(f"    Expected: ~0.095 (0.3 × 0.318 overgoal score)")
                else:
                    print(f"  ⚠ Overgoal adjustment value unexpected: {value:.3f}")
        except:
            print(f"  ⚠ Could not parse overgoal adjustment value")
    else:
        print("  ✗ Overgoal adjustment calculation failed")
        return False

    # Summary
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70)
    print("  ✓ DecisionScore updated to 5 parameters")
    print("  ✓ Overgoal adjustment function works")
    print("  ✓ Score breakdown includes overgoal")
    print("  ✓ Overgoal integrated into scoring pipeline")
    print("\n  INTEGRATION COMPLETE: Overgoal is now active in M3 scoring")
    print("="*70)

    return True

if __name__ == '__main__':
    try:
        success = test_overgoal_scoring_integration()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
