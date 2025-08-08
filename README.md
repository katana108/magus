# MAGUS Goal Hierarchy System

Anna's experimental implementation of goal hierarchies for the MAGUS (Modular Adaptive Goal and Utility System) framework, built in MeTTa language.

## Project Overview

This project explores goal-driven decision making for AGI systems, implementing both traditional action-evaluation systems and novel goal hierarchy architectures. The work builds on OpenPsi motivational frameworks while developing new approaches for self-modifying AI goal systems.

## What We've Built

### Core Systems

1. **Action Evaluation System** (`magus.metta`) - Original MAGUS implementation  
2. **Goal Hierarchy System** (`working-self-modify.metta`) - Anna's experimental demand-based architecture
3. **OVERGOAL Meta-System** - Self-evaluating goal fitness framework
4. **Goal Weighting System v1** (`magus-goal-weighting-v1.metta`) - Modular importance × urgency calculations *(Added 2025-08-08)*
5. **Action Evaluation Prototype v1** (`magus-action-evaluation-prototype-v1.metta`) - Considerations/discouragements system *(Added 2025-08-08)*

### Key Files Created

#### Main Implementations
- **`magus.metta`** - Original MAGUS decision system with geometric mean scoring
  - Actions: Talk, Rest, Explore
  - Arousal modulator affecting action preferences
  - Geometric mean of considerations × product of discouragements

- **`working-self-modify.metta`** - Anna's demand-based goal hierarchy
  - Three primary demands: Energy, Affinity, Exploration  
  - Self-modifying behavior generation
  - OVERGOAL system for goal fitness evaluation

#### Modular Decision System v1 *(Added 2025-08-08)*
- **`magus-goal-weighting-v1.metta`** - Goal importance and urgency calculations
  - Weight = importance × urgency (where urgency = 1.0 - satisfaction)
  - Fixed importance values: Exploration=0.6, Affinity=0.7, Energy=0.9
  - Current satisfaction levels determine urgency dynamically
  
- **`magus-action-evaluation-prototype-v1.metta`** - Action scoring with considerations/discouragements
  - Each action evaluated for each goal separately
  - Considerations: geometric_mean (higher = better for goal)
  - Discouragements: product (lower = more blocking)
  - Final score: weight × geometric_mean(considerations) × product(discouragements)
  - Integrates with goal weighting system for dynamic weights

- **`magus-goal-weighting-v1.py`** - Python mirror of goal weighting system
- **`magus-action-evaluation-prototype-v1.py`** - Python mirror of action evaluation system

#### Test and Development Files
- **`anna-demands-test.metta`** - Basic testing of demand/goal creation
- **`self-modifying-demo.metta`** - Early complex demo (syntax issues)
- **`simple-self-modify.metta`** - Simplified version for debugging

#### Documentation
- **`CLAUDE.md`** - Project context and MeTTa guidance
- **`MAGUS-Arousal-Modulator-Specification.md`** - Arousal system specification
- **`Village_of_Grit_Testing_Specs.md`** - AI agent testing scenario for validation *(Added 2025-08-08)*

## Key Discoveries

### 1. OpenPsi vs MAGUS Terminology
- **OpenPsi Demands** = MAGUS Primary Goals (Energy, Affinity, Exploration)
- **OpenPsi Goals** = MAGUS Subgoals (specific measurable objectives)  
- **OpenPsi Actions** = MAGUS Actions (atomic executable behaviors)

### 2. MeTTa's Code-as-Data Power
Successfully demonstrated how:
- Demand atoms `(demand energy 0.2)` generate executable decision logic
- System creates new behavior functions based on internal state changes
- Same code produces different behaviors when data changes

### 3. OVERGOAL Implementation
Built working meta-goal system that:
- Evaluates measurability of goals (80% average)
- Assesses correlation between goals (60% average)  
- Recommends goal structure changes (48% fitness → "RESTRUCTURE-GOALS")
- Never fully satisfied (drives continuous self-improvement)

## Technical Architecture

### Demand-Based Foundation
```metta
!(addDemand &demands energy 0.2)    ; Low energy - critical
!(addDemand &demands affinity 0.8)  ; High social connection  
!(addDemand &demands exploration 0.5) ; Medium curiosity
```

### Self-Modifying Behavior
```metta
(= (behaviorFor energy)
    (let $val (getDemandValue energy)
        (:: energy-behavior
            current-level $val
            recommended-action URGENT-REST)))
```

### OVERGOAL Meta-Evaluation
```metta
(= (overgoal-satisfaction)
    (:: overgoal-satisfaction 
        measurability $avg-measurability
        correlation $avg-correlation
        overall-fitness (* $avg-measurability $avg-correlation)))
```

## Running the Code

### Prerequisites
- MeTTa Python interpreter (`metta-py`)
- Hyperon MeTTa environment

### Basic Usage
```bash
# Test basic demand system
metta-py anna-demands-test.metta

# Run full self-modifying system with OVERGOAL
metta-py working-self-modify.metta

# Run original MAGUS action evaluation
metta-py magus.metta
```

## Key Learning Insights

### MeTTa Language Concepts
- **Atoms**: Fundamental knowledge units (demands, goals, actions)
- **Spaces**: Separate "databases" for organizing different atom types
- **Pattern Matching**: Core paradigm for data extraction and logic
- **Confidence**: Reliability measures affecting decision weight
- **Code = Data**: Functions and data use same atom format, enabling self-modification

### Design Principles
- **Simple math**: Goal hierarchies need basic comparison, not complex scoring
- **Utility functions**: Bridge between actions and demand satisfaction  
- **Urge calculation**: `desired_value - current_value` drives goal activation
- **Hierarchical flow**: Parent demands activate child goals through rule chains

## Current Status

### Working Systems ✅
- Basic demand creation and management
- Self-modifying behavior generation based on internal state
- OVERGOAL meta-evaluation of goal system fitness
- Code-as-data demonstrations
- **Modular decision system v1 with goal weighting and action evaluation** *(Completed 2025-08-08)*
- **Python mirrors for educational and integration purposes** *(Completed 2025-08-08)*

### Recent Achievements (2025-08-08) ✨
- **Complete decision pipeline**: Goal weights → Action evaluation → Best action selection
- **Verified mathematical correctness**: Geometric mean for considerations, product for discouragements
- **Modular architecture**: Separate goal weighting and action evaluation systems that integrate seamlessly
- **Dual implementation**: Both MeTTa and Python versions for maximum accessibility
- **Test results**: REST action (0.526) beats EXPLORE (0.174) in prototype test scenario

### Next Steps 🚀
- Test with Village of Grit scenarios (stage 2)
- Design proper utility functions linking actions to demands
- Implement goal promotion/demotion based on OVERGOAL feedback
- Add temporal dynamics and learning mechanisms
- Integrate with broader MAGUS cognitive architecture

## Research Context

This work contributes to AGI motivational architecture research by:
- Bridging classical OpenPsi frameworks with modern goal-driven AI
- Demonstrating practical self-modifying goal systems
- Implementing OVERGOAL meta-cognition for ethical alignment
- Exploring MeTTa language capabilities for symbolic AGI development

## Files Structure
```
metta-magus/
├── README.md                              # This file
├── CLAUDE.md                              # Project documentation
├── magus.metta                           # Original action-evaluation system
├── working-self-modify.metta             # Main goal hierarchy + OVERGOAL system
├── anna-demands-test.metta               # Basic testing framework
├── MAGUS-Arousal-Modulator-Specification.md  # Arousal system spec
└── [other experimental files]
```

---

*Last updated: 2025-08-08*  
*Status: Modular decision system v1 complete, ready for Village of Grit testing*