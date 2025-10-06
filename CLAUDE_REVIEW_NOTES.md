# MAGUS Review Notes – outstanding issues after M2/M3/M4 updates

## Key Issues
- `metagoals.metta`, `test-m3-integration.metta`, and the M3 unit tests still use `!(import!)` with literal file paths. Hyperon treats these as illegal module names, so the modules never load. All imports should go through a registered alias (or use `!(load ...)`).
- The M4 ethical runner/ablation layer calls helper functions that do not exist: `apply-metagoals-to-context`, `apply-anti-goals` (list variant), `score-all-v2`, `select-best-candidate`, and `candidate-score`. These must be implemented or replaced with real, tested pipeline functions.
- `Milestone_4/ethical/scenarios.metta` relies on `Tuple` (not defined in `types.metta`) and still imports dependencies via raw paths. Scenario registration currently raises `IncorrectNumberOfArguments` during testing.
- M3 tests continue to rely on inline lambdas and `(Action …)` matches; `planner-bt.metta` now emits `BTAction` nodes and best-practice guidelines explicitly forbid inline lambdas in tests.
- Metagoal novelty/uncertainty adjustments remain fixed constants (`0.2`, `0.1`), so M2 metrics are not actually feeding into scoring.
- The Python regression runner (`Milestone_4/tests/test_m4_pipeline.py`) only prints results—no assertions—so failures like the context-constructor error are reported as “PASS”.
- New logging helpers still mutate the Atomspace with `map-atom … (lambda … (remove-atom …))`, conflicting with the updated best-practice guidance to keep volatile state out of spaces.

## Suggested Next Steps
1. Replace all path-based `import!` calls with `register-module!`/`import!` combinations or `load` statements; update tests (`test-m3-integration.metta`, `test-scoring-v2.metta`, etc.) accordingly.
2. Implement the missing scenario-runner helpers (or refactor to existing functions) so candidate generation, scoring, and selection genuinely run. Align the types: `apply-anti-goals` should return a filtered candidate list.
3. Update the scenario schema to use provided types (or add a `Tuple` ADT), switch to `load` imports, and verify the constructor works. Strengthen the Python regression tests to assert on success/failure.
4. Refactor M3 tests to eliminate inline lambdas and convert the planner assertions to the current `BTAction` representation.
5. Replace the novelty/uncertainty placeholders with calculations based on the Milestone-2 measurability/correlation data.
6. Add assertions to the Python regression runner so it fails when MeTTa reports errors.
7. Audit the new logging/cleanup helpers and remove the remaining Atomspace-mutation lambdas in favour of pure fold/map variants or explicit helper functions.
