# MAGUS Project Overview - 18-08: AI Decision-Making & Goal Hierarchy Systems

## The Problem We're Solving

**Core Challenge**: Creating AI systems that can make intelligent decisions, manage competing goals, and adapt their behavior dynamically - essentially building the "motivational architecture" for Artificial General Intelligence (AGI).

Traditional AI systems are brittle because they follow fixed rules. Real intelligence requires:
- **Dynamic goal prioritization** (energy vs exploration vs social connection)
- **Self-modifying behavior** (learning from success/failure to change decision patterns)  
- **Meta-cognition** (evaluating and improving the goal system itself)
- **Ethical alignment** (ensuring AI goals remain beneficial to humans)

## What We're Building: MAGUS Framework

**MAGUS** = **Modular Adaptive Goal and Utility System**

A cognitive architecture that bridges classical AI decision theory with modern AGI research, implementing goal hierarchies inspired by biological motivational systems.

### Core Architecture Components

1. **Goal Hierarchy System**
   - **Primary Demands**: Energy, Affinity (social), Exploration (curiosity) 
   - **OVERGOAL Meta-System**: Evaluates and modifies the goal system itself
   - **Self-Modification**: System can rewrite its own behavior functions

2. **Decision Scoring Pipeline**
   - **Considerations**: Positive factors (geometric mean for balanced evaluation)
   - **Discouragements**: Blocking factors (product multiplication for veto power)
   - **Final Score**: `weight × geometric_mean(considerations) × product(discouragements)`

3. **Arousal Modulation System**
   - **Dynamic Behavior Shifts**: High arousal → exploration, Low arousal → rest
   - **Adaptive Learning**: Success/failure updates arousal, changing future decisions

## Our Specialized Agent Team

### 🎯 **MAGUS Integration Coordinator**
- **Role**: Team orchestrator, GitLab workflow manager, learning mentor
- **Focus**: System integration, cognitive architecture research, teaching complex concepts

### 🔬 **OpenPsi Research Analyst**  
- **Role**: Academic research specialist
- **Focus**: Analyzing OpenPsi motivational frameworks, Dörner's Psi theory, mapping to MAGUS

### ⚙️ **MeTTa-Magus Specialist**
- **Role**: Symbolic programming expert
- **Focus**: Clean, efficient MeTTa code, OpenCog Hyperon integration, performance optimization

### 🏗️ **Decision Systems Architect**
- **Role**: Algorithm designer and implementer  
- **Focus**: Mathematical foundations, working code, real-time optimization, validation

### 🐍 **MeTTa Python Mirror**
- **Role**: Educational accessibility specialist
- **Focus**: Python equivalents, interactive demos, stakeholder presentations

## Why MeTTa Language is Crucial

**MeTTa** (Meta Type Talk) is uniquely suited for MAGUS because:

### 1. **Code = Data = Knowledge**
```metta
; The same structure represents both data and executable logic
(demand energy 0.2)           ; Data: energy demand state
(= (behaviorFor energy) ...)  ; Code: function that uses the data
```

### 2. **Self-Modification Capabilities**
MeTTa systems can literally rewrite their own functions while running:
```metta
(= (adaptBehaviorFor energy)  ; System creates NEW behavior functions
    (:: energy-NEW-behavior   ; Based on current internal state
        recommended-action CONSERVE-ENERGY
        note system-adapted-automatically))
```

### 3. **Symbolic Pattern Matching**
Perfect for goal hierarchies and decision trees:
```metta
(= (decision-score $action)
   (* (arousal-bias $action)
      (* (gmean (get-considerations $action))
         (product (get-discouragements $action)))))
```

### 4. **OpenCog Integration**
MeTTa integrates with the OpenCog Atomspace, connecting to broader cognitive architectures (PLN, ECAN attention allocation, NARS reasoning).

## What We're Drawing From

### Academic Foundations
- **OpenPsi Framework**: Biological motivation models (drives, urges, goal promotion/demotion)
- **Dörner's Psi Theory**: Computational models of human motivation and emotion
- **PLN (Probabilistic Logic Networks)**: Uncertain reasoning under incomplete information
- **Decision Theory**: Mathematical frameworks for multi-criteria optimization

### Technical References
- **hyperon-openpsi repository**: Working OpenPsi implementation patterns
- **OpenCog Atomspace**: Knowledge representation and reasoning infrastructure  
- **ECAN**: Attention allocation mechanisms for goal prioritization
- **Village of Grit**: Testing environment with realistic decision scenarios

## Current Implementation Status

### ✅ **Working Systems**

#### **Self-Modifying Goal Hierarchy**
- **File**: `working-self-modify.metta`
- **What it does**: Demonstrates true AI self-modification where the system rewrites its own behavior functions based on internal demand states
- **Key innovation**: Code-as-data approach where demand atoms generate executable decision logic
- **Current state**: Working OVERGOAL meta-system that evaluates goal fitness and recommends restructuring

#### **Original MAGUS Action Evaluation**
- **File**: `magus.metta`
- **What it does**: Traditional utility-based decision system with arousal modulation affecting action preferences (Talk, Rest, Explore)
- **Key features**: Geometric mean scoring, arousal bias calculations, epsilon-based best-action selection
- **Current state**: Complete implementation with arousal update mechanisms for success/failure learning

#### **Modular Goal Weighting System v1**
- **Files**: `magus-goal-weighting-v1.metta` + `magus-goal-weighting-v1.py`
- **What it does**: Calculates dynamic goal weights using importance × urgency formula where urgency = 1.0 - satisfaction
- **Key innovation**: Separates goal prioritization from action evaluation for modular architecture
- **Current state**: Fixed importance values (Energy=0.9, Affinity=0.7, Exploration=0.6) with dynamic satisfaction tracking

#### **Action Evaluation Prototype v1**
- **Files**: `magus-action-evaluation-prototype-v1.metta` + `magus-action-evaluation-prototype-v1.py`
- **What it does**: Evaluates actions against multiple goals using considerations/discouragements framework
- **Key features**: Integrates with goal weighting system, handles real-time decision scoring for game environments
- **Current state**: Complete decision pipeline from goal weights → action scores → best action selection

#### **Testing & Validation Framework**
- **Files**: `Village_of_Grit_Testing_Specs.md`, `anna-demands-test.metta`
- **What it does**: Provides realistic scenarios for testing MAGUS decision-making in MUD game environment
- **Key features**: Detailed action specifications with considerations/discouragements for Exploration, Affinity, Energy goals
- **Current state**: Comprehensive test scenarios ready for integration with live systems

### 🚀 **Active Development Areas**

#### **Arousal Modulator Integration**
- **File**: `MAGUS-Arousal-Modulator-Specification.md`
- **Status**: Specification complete, implementation in progress
- **Goal**: Dynamic behavioral shifts where arousal level influences action preference patterns

#### **OpenCog Cognitive Architecture Integration**
- **Focus**: Connecting MAGUS with PLN reasoning, ECAN attention allocation, Atomspace knowledge representation
- **Research**: Mapping OpenPsi patterns to MAGUS framework components

#### **Real-Time Performance Optimization**
- **Target**: Game environment compatibility with sub-100ms decision cycles
- **Areas**: Mathematical optimization, efficient data structures, scalable goal hierarchies

## Research Impact & Applications

### AGI Research Contributions
- **Practical self-modification**: Demonstrated working systems that modify their own behavior
- **Goal hierarchy frameworks**: Bridging biological motivation with computational systems
- **Meta-cognitive alignment**: OVERGOAL systems for ethical AI development

### Real-World Applications  
- **Game AI**: Intelligent NPCs with realistic motivational behavior
- **Robotics**: Adaptive goal management for autonomous systems
- **Cognitive Assistants**: AI that can reprioritize based on context and user needs
- **Safety Research**: Frameworks for AI systems that can evaluate and constrain their own goals

## Why This Matters

MAGUS represents a bridge between **classical AI decision theory** and **cutting-edge AGI research**. By implementing working systems that can modify their own goals and evaluate their own effectiveness, we're contributing to the foundational research needed for beneficial, aligned artificial intelligence.

The combination of MeTTa's symbolic power, OpenPsi's biological grounding, and our modular architecture creates a platform for exploring fundamental questions about intelligence, motivation, and AI safety.

---
*Weekly Project Overview - Week of 18-08*  
*Repository: `/Users/amikeda/Magus_files/magi/metta-magus`*  
*Next review: 25-08*