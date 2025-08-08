# MAGUS Arousal Modulator Specification

## Overview
This specification outlines the simplest implementation of a dynamic arousal modulator for the MeTTa-Magus decision system. The arousal modulator will create behavior patterns where arousal level determines action preference: high arousal favors exploration, medium arousal favors social interaction, and low arousal favors rest.

## Current System Analysis
- **Base System**: Geometric mean of considerations multiplied by product of discouragements
- **Actions**: Talk, Rest, Explore with static scoring
- **Goal**: Add dynamic arousal-based behavioral shifts with minimal code changes

## Arousal Modulator Design

### Core Components

#### 1. Arousal State Management
```metta
(= (arousal-level) 0.5)  ; Initial state: medium arousal (talk preference)
```
- **Range**: 0.0 (lowest) to 1.0 (highest)
- **Initial Value**: 0.5 (neutral, favoring Talk action)
- **Storage**: Simple global state variable

#### 2. Arousal Bias Function
```metta
(= (arousal-bias Explore) (+ 0.5 (arousal-level)))
(= (arousal-bias Talk) (+ 0.5 (- 1.0 (abs (- (arousal-level) 0.5)))))
(= (arousal-bias Rest) (+ 0.5 (- 1.0 (arousal-level))))
```

**Behavior Mapping**:
- **High Arousal (0.8-1.0)**: Explore bias = 1.3-1.5, Talk bias = 0.7-0.9, Rest bias = 0.2-0.5
- **Medium Arousal (0.4-0.6)**: Explore bias = 0.9-1.1, Talk bias = 0.9-1.0, Rest bias = 0.4-0.6
- **Low Arousal (0.0-0.3)**: Explore bias = 0.5-0.8, Talk bias = 0.7-0.9, Rest bias = 0.7-1.0

#### 3. Modified Decision Scoring
```metta
(= (decision-score $action)
   (* (arousal-bias $action)
      (* (gmean (get-considerations $action))
         (product (get-discouragements $action)))))
```
- **Integration**: Arousal bias multiplies existing score
- **Preservation**: Original scoring logic remains intact
- **Enhancement**: Dynamic behavioral adaptation

#### 4. Arousal Update Mechanism
```metta
(= (update-arousal $success)
   (if $success 
       (min 1.0 (+ (arousal-level) 0.1))
       (max 0.0 (- (arousal-level) 0.1))))
```
- **Success**: Increases arousal by 0.1 (max 1.0)
- **Failure**: Decreases arousal by 0.1 (min 0.0)
- **Bounds**: Automatic clamping to valid range

## Implementation Plan

### Phase 1: Core Integration
1. Add arousal-level state variable to `magus.metta`
2. Implement arousal-bias function with action-specific calculations
3. Modify existing decision-score function to include arousal multiplier
4. Add arousal update function for post-action feedback

### Phase 2: Testing and Validation
1. Test arousal bias calculations at different arousal levels
2. Verify decision-score integration maintains existing functionality
3. Validate arousal update mechanism with success/failure scenarios
4. Confirm behavioral shifts occur as expected

### Phase 3: Integration Points
1. Identify where action outcomes are determined (for update-arousal calls)
2. Add arousal state display to debugging output
3. Test complete feedback loop: decision → action → outcome → arousal update

## Expected Behavioral Patterns

### Arousal Cycle Examples
- **High Performance Cycle**: Success → Higher arousal → More exploration → Potential discovery → Continued success
- **Recovery Cycle**: Failure → Lower arousal → More rest → Recovery → Gradual return to activity
- **Social Equilibrium**: Medium arousal maintained → Consistent social interaction → Stable communication pattern

### Adaptive Responses
- **Exploration Success**: Agent becomes more adventurous, seeks new experiences
- **Social Success**: Maintains balanced interaction patterns
- **Rest Success**: Builds energy for future higher-arousal activities
- **Failure Response**: Automatically shifts toward lower-risk, restorative behaviors

## Technical Requirements

### Dependencies
- Existing MeTTa-Magus decision system
- Mathematical functions: `min`, `max`, `abs`, `+`, `-`, `*`
- Conditional logic: `if` statements

### Performance Impact
- **Minimal**: Single multiplication added to decision-score
- **Memory**: One additional floating-point state variable
- **Computation**: Simple arithmetic operations only

## Success Metrics

### Functional Requirements
1. Arousal level influences action selection as specified
2. Arousal updates correctly based on action outcomes
3. Existing decision-score functionality preserved
4. System maintains stability across arousal range

### Behavioral Validation
1. High arousal periods show increased Explore selection
2. Low arousal periods show increased Rest selection
3. Medium arousal periods show increased Talk selection
4. System demonstrates adaptive learning from outcomes

## Future Extensions

### Potential Enhancements
- Multiple arousal types (cognitive vs emotional)
- Arousal decay over time
- External arousal triggers
- Arousal-based consideration weighting

### MAGUS Integration Points
- Foundation for hierarchical goal modulation  
- Base layer for ethical constraint application
- Component in overgoal alignment system
- Building block for emergent goal structures

## Implementation Status
- **Status**: Specification Complete
- **Next Step**: Code implementation in `magus.metta`
- **Estimated Effort**: 10-15 lines of MeTTa code
- **Risk Level**: Low (preserves existing functionality)