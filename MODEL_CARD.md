# Model / system card

## Intended use

Run explicit retrieve, draft and verify stages with source-linked observations and a bounded context. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

A fixed state graph retrieves up to three relevant passages, drafts a structured brief and verifies each evidence quote is a literal substring of its cited retrieved passage. Live drafting uses a local LLM; fixture mode exercises the graph with replayed drafting output.

## Evaluation protocol

Inject invalid quotes and unknown sources to test rejection. Record all stage outputs for review. This is a deterministic workflow with an optional LLM drafting stage, not multiple autonomous agents.

## Known limits

An exact quote proves the text was present but cannot prove the surrounding interpretation or completeness. Context instructions are untrusted; the generator must not select tool permissions.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Add independent claim support evaluation, contradictory sources, retry policies, query planning and licensed source ingestion.
