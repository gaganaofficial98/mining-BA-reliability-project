# 12 — Module A: Predictive Maintenance Proof-of-Concept (Optional Stretch Module)

**Status:** Complete — 6 October 2026
**Owner:** Gagana Suresh
**Scope reminder (do not skip):** per `00-Master-Plan.md` Section 2, this module is a labeled, optional proof-of-concept sitting **outside** this engagement's locked BA scope (`01-Project-Charter.md` Section 3 explicitly excludes "building, training, or validating a machine-learning predictive model" from the engagement itself). It demonstrates that a predictive extension is *feasible*, not that one has been built, validated, or is ready to deploy. Productionizing this would be a phase-2 initiative, outside this engagement's boundary — see the link-forward to the Benefit Realization Report at the end of this document. This module is a footnote demonstrating range, never the headline of the README, video, or LinkedIn article (same guardrail as Module B).

**Data:** the same canonical AI4I 2020 dataset instance already verified elsewhere in this project. Before any modeling step, this document's own script re-checked the file's row count (10,000), total confirmed failures (339), and per-mode raw flag counts (TWF 46 / HDF 115 / PWF 95 / OSF 98 / RNF 19) against the figures already locked in `EDA-Findings.md` — all matched exactly, confirming this is the same dataset instance, not a different download that happens to look similar. **[DATASET]**

---

## 1. Why this earns a place (the honest version, not a sales pitch)

AI4I 2020 ships with a binary `Machine failure` label specifically so it can be used for exactly this kind of classification exercise. Recognizing that the data supports a predictive angle, and scoping a small, validated proof-of-concept rather than either ignoring that or overbuilding it into a second core deliverable, is itself a BA judgment call — knowing when a predictive model is worth demonstrating, and how to bound its scope so it doesn't become the project. This is on-story, not off-story, as long as its size stays protected — which is why this document is a single model, not a model-selection bake-off.

---

## 2. Methodology

### 2.1 The leakage decision — the single most important modeling judgment call in this document

AI4I's five failure-mode columns (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) are **not independent sensor readings** — they are the dataset's own *derived labels* for *why* `Machine failure` is 1. A row with `Machine failure = 1` has at least one of these five flags set, by construction (this is literally how the Q2/Q4 Pareto and preventable-vs-random analyses in `EDA-Findings.md` work). Feeding any of these five columns into the model as a predictor would not be prediction — it would be reading the answer off the back of the answer sheet, and would trivially score near-100% while meaning nothing about genuine early-warning capability.

**Decision: all five failure-mode flag columns are excluded from the feature set.** The model is given only the dataset's genuine independent sensor readings — `Air temperature [K]`, `Process temperature [K]`, `Rotational speed [rpm]`, `Torque [Nm]`, `Tool wear [min]` — plus AI4I's own product-quality `Type` column (L/M/H, one-hot encoded). This is the only feature set that makes the resulting precision/recall numbers mean anything as a genuine predictive-maintenance signal. **[ASSUMPTION: a deliberate scope/leakage decision, not a dataset-derived fact — disclosed here rather than silently applied.]**

### 2.2 Train/test split

A stratified 75/25 split (7,500 train / 2,500 test rows, `random_state=42` for reproducibility) preserves the real ~3.4% failure rate in both halves — a plain random split risks a test set with too few real failures to evaluate against, given how rare the positive class is. **[DATASET: 254 failures in train, 85 in test]**

### 2.3 Class-imbalance handling — stated explicitly, per the Master Plan's own warning

339 of 10,000 rows are failures — a 3.39% positive rate. The Master Plan is explicit that "most machines don't fail, so accuracy alone is a meaningless metric," and this is demonstrated, not just asserted, below (Section 3.1). Two concrete handling steps were taken: (1) `class_weight='balanced'` on both models trained, so the training loss penalizes missing a rare failure more heavily than misclassifying a common non-failure row; (2) every result below is reported on precision/recall/F1/confusion-matrix terms, with accuracy shown only for completeness, never as the headline metric.

### 2.4 Technique used to build this document (for the prompt library): plan-then-critique loop, explicitly applied to the naive-baseline trap

Before building the committed model, two deliberate checks were run, in this order, exactly as the Master Plan's "How to use Claude" column for this task specifies:

1. **Naive-baseline check, run first.** What would a model that learned nothing score? (Section 3.1.) This is the concrete version of "check you're not just optimizing accuracy on an imbalanced dataset" — not a hypothetical warning, an actual number to beat.
2. **A quick logistic-regression sanity pass, run before committing to a final model.** Section 3.2. This is a genuine plan-then-critique step: it tests whether the simplest reasonable model already struggles in a way consistent with this project's own prior findings (Q5/Q6's deterministic threshold-interaction mechanisms), and that result is what justifies the model choice in Section 3.3 — the choice isn't an arbitrary pick between the Master Plan's two allowed options (logistic regression or random forest), it's evidence-driven.

---

## 3. Results — reported honestly, including where the model underperforms

### 3.1 Naive baseline (always predict "no failure")

| Metric | Value |
|---|---|
| Accuracy | **96.60%** |
| Precision (failure class) | undefined (zero predicted positives) |
| Recall (failure class) | **0.00%** |

A model that never flags a single failure scores 96.6% accuracy while catching exactly zero real breakdowns. This is the naive-baseline trap the Master Plan calls out by name — stated here as a number, not a warning label, and every other result in this document is judged against *this* baseline on precision/recall, never against accuracy. **[DATASET]**

### 3.2 Logistic regression — sanity check only, not the committed model

| Metric | Value |
|---|---|
| Precision (failure class) | 13.9% |
| Recall (failure class) | 80.0% |

A plain linear model, even with class weighting, produces a flood of false alarms (precision in the low teens) to hit a reasonable recall. This is consistent with `EDA-Findings.md`'s own Q5/Q6 conclusion that several failure modes (OSF, HDF, PWF) are governed by **threshold and multiplicative interactions** between sensor variables (e.g., `Tool wear × Torque` exceeding a tier-specific limit) — exactly the kind of relationship a linear model cannot capture without hand-engineered interaction terms, and a tree-based model captures natively. This result is the actual justification for the model choice below, not a coin flip between the Master Plan's two permitted options. **[DATASET]**

### 3.3 Committed model: Random Forest (`n_estimators=200`, `class_weight='balanced'`, `random_state=42`)

Deliberately **not** hyperparameter-tuned beyond this one reasonable setting — per the Master Plan's own "no hyperparameter-tuning rabbit holes" instruction. No ensembling of multiple model types; a random forest is internally an ensemble of trees, but it is used here as the single committed model the Master Plan names as a valid choice, not combined with any second model.

| Metric | Value |
|---|---|
| Accuracy | 97.92% (reported for completeness only — not the headline metric) |
| **Precision (failure class)** | **90.24%** |
| **Recall (failure class)** | **43.53%** |
| F1 (failure class) | 58.73% |
| Average precision (PR-AUC) | 0.7507 |
| ROC-AUC | 0.9725 |

**Confusion matrix (test set, 2,500 rows, 85 real failures):**

| | Predicted: No failure | Predicted: Failure |
|---|---|---|
| **Actual: No failure** | TN = 2,411 | FP = 4 |
| **Actual: Failure** | FN = 48 | TP = 37 |

**Honest read of this result — not softened:** at the default 0.5 probability threshold, the model is precision-heavy and recall-weak. It misses **more than half** of the real test-set failures (48 of 85) while raising very few false alarms (only 4 of 2,415 genuine non-failures). This is a real, disclosed limitation, not a flattering headline — a model that misses 56% of real breakdowns is not yet a usable early-warning tool at this operating point. **[DATASET]**

### 3.4 Operating-point trade-off — the business decision underneath the default threshold

The 0.5 threshold above is scikit-learn's default, not a business decision. Exactly like Q5's buffer-zone analysis in `EDA-Findings.md`, how aggressively to flag a failure is a policy choice that trades false alarms against missed failures, and that choice belongs with the Reliability Engineer and Maintenance Manager, not baked into a default:

| Threshold | Precision | Recall | False alarms (of 2,415 real non-failures) | Failures missed (of 85) |
|---|---|---|---|---|
| 0.50 (default) | 90.2% | 43.5% | 4 | 48 |
| 0.40 | 85.0% | 60.0% | 9 | 34 |
| 0.30 | 76.0% | 67.1% | 18 | 28 |
| 0.25 | 68.5% | 71.8% | 28 | 24 |
| 0.20 | 60.6% | 77.6% | 43 | 19 |
| 0.15 | 48.6% | 81.2% | 73 | 16 |
| 0.10 | 38.8% | 85.9% | 115 | 12 |

**No single row here is "the" answer** — that's the point of showing the table rather than picking the flattering row. A maintenance team willing to tolerate more false alarms in exchange for catching more real failures would move left down this table; a team with limited inspection capacity would stay closer to the default. This document does not make that call — same "the analysis exists, the threshold decision doesn't" discipline already applied to FR-07's amber-escalation threshold and the Q5 buffer-zone recommendation. **[DATASET]**

### 3.5 Per-failure-mode recall — does the model's weak spot match what Q5/Q6 already predicted?

Using the test set's 85 real failures at the default 0.5 threshold, broken down by which original failure-mode flag each missed/caught failure actually carried (the flag columns are used here only to label *which real failure was caught or missed* — never as a model input, consistent with Section 2.1):

| Failure mode | Test-set failures | Caught | Recall | Consistent with Q5/Q6? |
|---|---|---|---|---|
| OSF (Overstrain) | 20 | 13 | 65.0% | Yes — Q5/Q6 found OSF 100%/100% *deterministic* on its own threshold rule; the model's lower recall here reflects that it's learning the pattern generally from 5 raw sensors, not applying the exact cited tier-specific threshold rule itself |
| PWF (Power Failure) | 17 | 9 | 52.9% | Directionally consistent — Q6 found PWF deterministic via `Torque × rotational speed`, a multiplicative relationship a tree model should approximate reasonably well |
| HDF (Heat Dissipation) | 36 | 16 | 44.4% | Directionally consistent — Q6's HDF rule depends on *both* a temperature-difference condition AND a speed condition holding simultaneously; the model picks up a meaningful share but not all of a two-condition joint rule |
| TWF (Tool Wear) | 13 | **0** | **0.0%** | **Consistent — and the honest headline finding of this section.** Q6 already found TWF only "Detectable — probabilistic," with its own cited 90%/90% bar failing on precision (93.5% recall but just 5.4% precision) even with the *exact* documented tool-wear window rule. A general-purpose classifier with no access to that specific window, with TWF representing only 46 of 10,000 rows in training, catches **zero** of the 13 TWF failures in this test set. This is not a bug — it's the same finding Q6 already made, now reproduced independently by a completely different method (a general classifier vs. a hand-specified threshold rule), which is a real, if modest, corroboration rather than a new discovery. |
| RNF (Random) | 0 | — | — | No RNF-flagged failures landed in this test split at all — consistent with `EDA-Findings.md`'s own finding that RNF's primary-cause count across the *entire* dataset is 0 of 339 (RNF only ever co-occurs with another real mode, never drives a confirmed failure alone) — there was nothing for a model to even attempt to catch. |

**This table is the single most important piece of evidence in this document for the "is this a naive majority-class predictor in disguise" question the Master Plan explicitly asks to be red-teamed.** A naive or leaking model would show uniformly excellent or uniformly meaningless results across all five modes. This model instead shows a *specific, mechanistically explainable* pattern — strong on the modes Q5/Q6 already proved are deterministic, completely blind on the one mode Q5/Q6 already proved is genuinely hard — which is exactly the signature of a model that has learned something real about the underlying physical mechanisms, not one gaming the imbalanced-accuracy metric. **[DATASET]**

### 3.6 Feature importances — an independent cross-check against Q5/Q6's cited mechanisms

| Feature | Importance |
|---|---|
| Rotational speed [rpm] | 0.304 |
| Torque [Nm] | 0.296 |
| Tool wear [min] | 0.202 |
| Air temperature [K] | 0.102 |
| Process temperature [K] | 0.075 |
| Type (L/M/H, combined) | 0.021 |

The model's own top three features — rotational speed, torque, tool wear — are exactly the three variables the AI4I-cited generation rules (Matzka, S. 2020) use to define OSF, PWF, and TWF. The model was never told these rules; it discovered their importance purely from fitting 7,500 labeled rows. This is a second, independent piece of evidence (alongside Section 3.5) that the model has learned the dataset's real underlying structure rather than an artifact of the class imbalance. **[DATASET]**

---

## 4. Limitations — disclosed, not hidden

- **This is a demonstration, not a validated production model.** A single train/test split (no k-fold cross-validation) was used, consistent with the Master Plan's "no hyperparameter-tuning rabbit holes" scope — a production deployment would need cross-validated performance estimates, not a single split's numbers.
- **The default 0.5 threshold's 43.5% recall is a real, disclosed limitation, not a result to round up.** Section 3.4's trade-off table makes the actual operating-point decision available, but does not make that decision — it belongs with the Reliability Engineer and Maintenance Manager, the same calibration discipline already required elsewhere in this project (FR-07's escalation threshold, Q5's buffer-zone recommendation).
- **TWF's 0% test-set recall is a genuine model weak spot, not a data bug** — see Section 3.5's full discussion. It corroborates, rather than contradicts, Q6's own independent finding that TWF is the one failure mode in this dataset that doesn't cleanly support a high-precision detection rule.
- **Same cross-sectional limitation as Q5/Q6 applies here too:** AI4I's rows are independent snapshots, not a time-ordered sequence per asset. This model proves sensor conditions at a single moment are distinguishable between failing and non-failing equipment — it does not prove, and should never be quoted as proving, how much real advance warning time a deployed version would deliver on a real asset.
- **Class-weight balancing affects training, not the evaluation threshold** — `class_weight='balanced'` changes how the model is penalized during training, but the 0.5 decision threshold used for the headline Section 3.3 numbers is still scikit-learn's unweighted default. This is why Section 3.4's threshold sweep exists — without it, a reader could mistake "I handled class imbalance" for "the model is tuned to find the business-optimal number of failures," which it is not.

---

## 5. Forward-looking recommendation (links to the Benefit Realization Report)

**This validates that a predictive extension is feasible; productionizing it would be a phase-2 initiative outside this engagement's locked scope.** Concretely: a general classifier built on five raw sensor readings, with zero per-mode feature engineering, independently rediscovers the same two findings Q5/Q6 already established by hand-specifying physical threshold rules — strong, mechanistically explainable performance on OSF/PWF/HDF, and a genuine, well-understood blind spot on TWF. That convergence across two independent methods is itself a modest but real piece of evidence that a predictive-maintenance capability is worth a scoped phase-2 investment, **not** a claim that this proof-of-concept is ready to flag real equipment today. `09-Benefit-Realization-Report.md` should be updated to add this as a forward-looking phase-2 candidate, distinct from and later than the phase-1 recommendations it already carries (the Step 4 escalation checkpoint, the torque/tool-wear threshold monitoring rule) — not folded into this engagement's committed benefits.

See `Interview-Prep-QA.md` for the technical follow-up questions this module invites (why Random Forest over logistic regression, why these five features and not more, what the 43.5%/90.2% operating point means for a real deployment) and how to hold the line under them without overclaiming readiness.

---

## 6. Reproducibility

Script: `module_a_ml_poc.py` (committed alongside this write-up in the eventual repo under `12-ML-Proof-of-Concept/`, per `00-Master-Plan.md` §5.1). `random_state=42` fixed throughout for the train/test split and both models — running the script again reproduces every number in this document exactly.
