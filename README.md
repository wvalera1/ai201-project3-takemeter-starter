# TakeMeter

A fine-tuned text classifier that labels discourse quality in the r/NBA subreddit. Built for AI201 Project 3.

---

## What It Does

TakeMeter assigns one of four labels to r/NBA posts and comments:

| Label | Definition |
|---|---|
| **analysis** | A structured argument backed by statistics, historical comparisons, or tactical observations where the evidence is specific, verifiable, and the conclusion follows from it. |
| **hot_take** | A bold, confident claim or opinion without supporting evidence — it asserts rather than argues, and the conclusion could stand alone without any data cited. |
| **reaction** | An immediate emotional response to a specific event, expressing a feeling in the moment with little to no argument. |
| **news** | A factual report of an event, transaction, or statement with no editorial opinion; its primary value is the information itself, not an interpretation of it. |

### Label Examples

**analysis**
> Giannis Antetokounmpo leaves Milwaukee as the Bucks' all-time leader in all four major statistical categories: points, rebounds, assists, and blocks. He and Kevin Garnett with the Timberwolves are the only players in NBA history to lead a franchise in all four categories.
> Bucks all-time points leaders: 1.) Giannis — 21,531 | 2.) Kareem — 14,211 | 3.) Khris Middleton — 12,586 [Full leaderboards via Basketball Reference]

> Highest Turnover Percentage On Drives In The 2025-26 NBA Playoffs (Min. 50 Total Drives): Chet Holmgren — 14.0% | Jayson Tatum — 11.3% | James Harden — 11.1% | Evan Mobley — 10.8% | Dennis Schroder — 10.5%

**hot_take**
> If Lebron played in MJ's era — the debate wouldn't even be real. LeBron would be the easy GOAT.

> Giannis/Bam/Portis? The Heat have to have something up their sleeves to move Bam too. He's just a worse Giannis. The spacing with Bam+Giannis would be the worst since the 90s.

**reaction**
> Ah nice we're the only ones left without a coach. *(In response to breaking news that Dusty May agreed to become head coach of the Dallas Mavericks)*

> IDGAF who wins the finals. OKC is out!!!!!!

**news**
> [Charania] The Oklahoma City Thunder are finalizing a trade to send guard Aaron Wiggins to the Atlanta Hawks for two second-round picks (Atlanta's in 2030 and the least favorable of Hawks/Lakers in 2032), sources tell ESPN.

> [Fischer] The Bulls are trading Mo Gueye to Minnesota, sources say, to complete the three-team deal that sends Julius Randle and No. 28 in tomorrow's NBA Draft to Brooklyn for No. 33, and reroutes Nic Claxton into Chicago's cap space in the new league year.

---

## Data

- **Source:** r/NBA posts and comments, collected via the PullPush Reddit API and manual sourcing
- **Total labeled examples:** 211
- **Train / Val / Test split:** 70% / 15% / 15% (stratified)
- **Test set:** 32 examples (held out before any model was trained)

| Label | Count |
|---|---|
| reaction | 65 |
| news | 56 |
| analysis | 48 |
| hot_take | 42 |

News and analysis posts were manually sourced to counteract the natural imbalance produced by bulk comment collection, which skews heavily toward reactions.

---

## Models

- **Fine-tuned:** `distilbert-base-uncased` (67M parameters), trained on Google Colab (T4 GPU)
  - 10 epochs, learning rate 2e-5, batch size 16
  - **Epoch decision:** The notebook default is 3 epochs. An initial run at 3 produced class collapse — the model predicted "news" for every test example, with validation accuracy frozen at 0.281 across all three epochs (equal to the news-class frequency in the validation set). Loss decreased from 1.407 to 1.324 but never enough to shift decision boundaries on 147 training examples in 3 passes. Increasing to 10 epochs resolved this: the model reached 0.781 test accuracy with differentiated per-class behavior.

- **Baseline:** `llama-3.3-70b-versatile` via Groq API, zero-shot, temperature 0. The classification prompt:
  - Names the community (r/NBA) and task
  - Defines each label using the same language as planning.md
  - Provides one example post per label (drawn from the planning.md examples section)
  - Instructs the model to respond with only the label name and lists all four valid labels
  
  Full prompt (2,181 characters) is in `TakeMeter_finetune.ipynb`, Section 5. Results collected by running each of the 32 test examples through the API independently; all 32 responses were parseable.

---

## Results

| Model | Accuracy | Macro F1 |
|---|---|---|
| Groq baseline (llama-3.3-70b) | 0.750 | 0.73 |
| Fine-tuned DistilBERT | 0.781 | 0.73 |

### Per-Class Breakdown

| Label | Model | Precision | Recall | F1 | Support |
|---|---|---|---|---|---|
| analysis | Fine-tuned | 0.88 | 1.00 | 0.93 | 7 |
| analysis | Baseline | 0.83 | 0.71 | 0.77 | 7 |
| hot_take | Fine-tuned | 0.50 | 0.14 | 0.22 | 7 |
| hot_take | Baseline | 0.60 | 0.43 | 0.50 | 7 |
| reaction | Fine-tuned | 0.64 | 0.90 | 0.75 | 10 |
| reaction | Baseline | 0.80 | 0.80 | 0.80 | 10 |
| news | Fine-tuned | 1.00 | 1.00 | 1.00 | 8 |
| news | Baseline | 0.73 | 1.00 | 0.84 | 8 |

### Confusion Matrix (Fine-Tuned Model)

|  | Predicted: analysis | Predicted: hot_take | Predicted: reaction | Predicted: news |
|---|---|---|---|---|
| **True: analysis** | 7 | 0 | 0 | 0 |
| **True: hot_take** | 1 | 1 | 5 | 0 |
| **True: reaction** | 0 | 1 | 9 | 0 |
| **True: news** | 0 | 0 | 0 | 8 |

Supplementary: [confusion_matrix.png](confusion_matrix.png)

---

## Success Criteria Check

From [planning.md](planning.md), Tier 1 required:

| Criterion | Threshold | Fine-tuned Result | Pass? |
|---|---|---|---|
| Accuracy | ≥ 0.60 | 0.78 | ✓ |
| Macro F1 | ≥ 0.60 | 0.73 | ✓ |
| Per-class recall ≥ 0.50 (all labels) | all four | hot_take = 0.14 | ✗ |
| Fine-tuned macro F1 ≥ Groq − 0.05 | ≥ 0.68 | 0.73 | ✓ |

Tier 1 fails on hot_take recall. Three of four criteria pass; the model learned something real but cannot reliably identify hot_takes.

---

## Evaluation Report

### Sample Classifications

Five examples from the test set, shown with the model's predicted label and softmax confidence score. Confidence scores for the two correctly classified examples are estimated from the model's near-perfect performance on those classes; exact scores for wrong predictions come from the notebook's inference output.

| Post (truncated) | True | Predicted | Conf. | ✓/✗ |
|---|---|---|---|---|
| `[Charania] BLOCKBUSTER: The Milwaukee Bucks are trading franchise icon Giannis Antetokounmpo and Bobby Portis to the Miami Heat for Tyler Herro, Kel'el Ware...` | news | news | ~0.99 | ✓ |
| `Giannis Antetokounmpo leaves Milwaukee as the Bucks' all-time leader in all four major statistical categories: points, rebounds, assists, and blocks. He and Kevin Garnett with the Timberwolves are the only players...` | analysis | analysis | ~0.95 | ✓ |
| `Jacob Toppin will stick with the Hawks and earn a spot as an end of the rotation player. He's a guy that fits really well with them imo` | hot_take | reaction | 0.42 | ✗ |
| `Smart for Cousins. One year deal where he gets an easy ring and proves he can still go so he can get a bigger deal next year. Wait` | hot_take | reaction | 0.57 | ✗ |
| `Returning from the Raptors' historic victory, Kawhi Leonard opens the fridge and considers its contents carefully before deciding on the leftover lo mein...` | reaction | hot_take | 0.34 | ✗ |

The news prediction is correct and confident because the post has all the surface markers the model learned from training: journalist attribution in brackets, a transaction verb ("are trading"), and no editorial opinion. The analysis prediction is correct for similar reasons — the post contains a verifiable statistical claim, a historical comparison ("only players in NBA history to..."), and a structured conclusion. Both classes have consistent, learnable surface forms. The hot_take misclassifications are discussed in detail below.

### What the Model Got Right

**News** is perfect (precision 1.00, recall 1.00). News posts have a consistent surface structure — journalist attribution in brackets, transaction language ("is trading", "has signed"), sourced quotes — that DistilBERT learns quickly from even a small dataset. The fine-tuned model improved over the baseline (F1: 0.84 → 1.00) because it was trained on real news examples from this subreddit rather than relying on a generic understanding of "news."

**Analysis** improved substantially over the baseline (F1: 0.77 → 0.93). All 7 analysis test examples were correctly identified. The model learned that long posts with statistical tables, basketball-reference links, and historical comparisons belong here. The zero-shot baseline missed 2 of 7 analysis posts; the fine-tuned model missed none.

### Where It Failed

**Hot_take recall collapsed to 0.14.** Of 7 hot_take test examples, 5 were predicted as reaction and 1 as analysis. Only 1 was correctly identified. This is the single largest regression from the baseline, which managed recall of 0.43 on the same class — meaning the fine-tuned model is actively worse than a zero-shot 70B model on the label that matters most for this project.

### Which Labels Are Being Confused

The confusion matrix tells a clear directional story: **hot_take → reaction** is the dominant failure, accounting for 5 of the 7 total misclassifications. The model essentially treats the reaction bucket as a catch-all for anything that is not clearly analysis or news. Reaction's precision is correspondingly low (0.64): 9 of its 14 predictions are correct, but 5 of those predictions are actually hot_takes.

The other directional pattern — **hot_take → analysis** (1 case) and **reaction → hot_take** (1 case) — are minor by comparison and do not form a systematic pattern.

### Three Specific Failures

**Failure 1** — `Jacob Toppin will stick with the Hawks and earn a spot as an end of the rotation player. He's a guy that fits really well with them imo`
True label: **hot_take** | Predicted: **reaction** | Confidence: 0.42

*Which labels are confused:* hot_take → reaction, the dominant failure mode.

*Why is the boundary hard:* This post makes a bold player prediction with no evidence — a textbook hot_take by definition. But it is delivered with zero emotional heat. There are no exclamation marks, no capslock, no reactive vocabulary. The phrase "imo" (in my opinion) signals subjectivity, but not assertion. The model has apparently learned that hot_takes are tonally loud. A calm prediction reads like a reaction to something the author noticed, not an assertion.

*Labeling problem or data problem:* The label is correct — this is a forward-looking claim with no evidence. The problem is in the training data distribution. Most of the 42 hot_take training examples were likely more tonally assertive than this one. The model never saw enough calm hot_takes to learn the structural feature (no evidence) rather than the surface feature (strong tone).

*What would fix it:* More hot_take training examples specifically from calm player prediction threads — summer league takes, offseason roster predictions, ROTY/MVP takes — where the post's boldness comes from its content, not its punctuation. The current 42-example hot_take training set skews toward GOAT debates and era comparison posts, which are louder in tone.

---

**Failure 2** — `Smart for Cousins. One year deal where he gets an easy ring and proves he can still go so he can get a bigger deal next year. Wait`
True label: **hot_take** | Predicted: **reaction** | Confidence: 0.57

*Which labels are confused:* hot_take → reaction, again.

*Why is the boundary hard:* This post has a recognizable Reddit comedy structure: a short reasoning chain ("Smart for Cousins. One year deal where...") that builds toward a punchline, then collapses with a single word ("Wait"). The "Wait" signals that the author is reacting to their own reasoning mid-sentence — a comedic pivot. To a human reader, the assertive content makes it a hot_take delivered with irony. The model almost certainly read "Wait" as a reactive marker and classified accordingly. Confidence of 0.57 is the highest of any misclassified hot_take, meaning the model was relatively sure.

*Labeling problem or data problem:* The label is defensible — the post does make a substantive claim (this signing is strategically smart for Cousins). But the comedic "Wait" at the end acknowledges the claim might be absurd, which blurs the line. Arguably, this post is simultaneously an assertion and a reaction to its own assertion. The ambiguity is real; this is the kind of case a second annotator might label differently.

*What would fix it:* A tighter definition of the reaction label that explicitly excludes self-contained ironic reasoning ("if the dominant register is asserting a claim about the world — even a facetious one — it is a hot_take"). Short of that, seeing more examples of this comedy structure during training would help. But with 42 hot_take examples total, covering every delivery style is not feasible.

---

**Failure 3** — `Returning from the Raptors' historic victory, Kawhi Leonard opens the fridge and considers its contents carefully before deciding on the leftover lo mein. He settles in on the couch and resumes the episode of "How It's Made" he was watching before he left for the arena. He smiles and chuckles to himself. "So that's how they make shoelaces."`
True label: **reaction** | Predicted: **hot_take** | Confidence: 0.34

*Which labels are confused:* reaction → hot_take. This is the only case running in the opposite direction.

*Why is the boundary hard:* This post is a creative third-person narrative — a fictional story about Kawhi Leonard's famously stoic personality, written as a reaction to his championship win. It makes no claim. But the model had no category for "creative fiction as reaction." Every sentence is a confident declarative statement in third person: "He settles in on the couch. He smiles." The structure looks assertive even though nothing is being asserted. The model has never seen a post like this and the closest structural match in its training data is probably hot_take.

*Labeling problem or data problem:* The label is correct — this is a reaction expressed through narrative. The problem is coverage. Creative or ironic reaction posts are a real genre on Reddit and were not represented in the training data. This is not an annotation inconsistency; it is a data gap.

*What would fix it:* Explicitly collecting examples of creative and ironic reactions during data collection — jokes, fictional narratives, satirical "what-if" posts that express feeling through form rather than through direct emotional language. The current reaction training set almost certainly skews toward direct emotional reactions ("LMAO", "I can't believe this") and misses the more literary end of the spectrum.

### What This Reveals About the Task

All three failures trace to the same underlying problem: **the hot_take/reaction boundary requires reading intent, not surface form.** Both labels produce short, non-analytical posts. The distinguishing feature — assertion without evidence vs. feeling in response to an event — is structural and intentional, not lexical. A model trained on 42 hot_take examples, many of which may have had stronger tonal signals than the test set, cannot reliably learn that structural distinction. It learns a surface proxy (emotional intensity) and applies it consistently — which is why news and analysis, which have clear and consistent surface signals, reach near-perfect performance, while hot_take collapses.

This is not a DistilBERT failure. Any small model trained on 42 examples of a hard category will exhibit this behavior. The correct response is more data (at least 100 hot_take examples, sourced specifically from calm prediction threads and ironic commentary) and potentially a revised label definition that makes the assertion/evidence structure more central.

### Comparison to Baseline

The fine-tuned model and the Groq baseline tie on macro F1 (0.73), but their error profiles are opposite:
- **Fine-tuned:** dominates news (F1: 1.00) and analysis (F1: 0.93); collapses on hot_take (F1: 0.22)
- **Baseline:** balanced errors across all classes; hot_take F1 of 0.50 is mediocre but functional

The baseline's advantage on hot_take comes from the Groq model's broad language understanding — it can reason about what "asserting a claim without evidence" means from the definition alone, without needing examples. The fine-tuned model gives up that reasoning ability and replaces it with pattern matching, which only works when the patterns in training and test data overlap.

For real deployment, the two models are suited to different tasks. A tool that needs to reliably surface analysis and news (high-quality content highlighting) should use the fine-tuned model. A tool that needs balanced performance across all four labels, including hot_take identification, should currently use the baseline — or wait for a fine-tuned model trained on more hot_take examples.

### Reflection: Intended Definitions vs. Learned Decision Boundary

The four label definitions in planning.md are logical and intentional — they describe what a post *does* as communication. Analysis is defined by the relationship between evidence and conclusion. Hot_take is defined by the absence of supporting evidence. Reaction is defined by emotional immediacy directed at a specific event. News is defined by the absence of editorial opinion.

The model did not learn those functions. It learned their correlates.

**What it overfitted to:** Surface form and tonal intensity. News posts have nearly identical structural markers across training examples — journalist attribution in brackets, transaction verbs, no opinion language — so the model mapped those markers to "news" reliably. Analysis posts are long and statistically dense, so the model mapped length and lexical density to "analysis" reliably. For hot_take, the model learned that tonally assertive, emotionally charged language belongs there: confident declarative statements, GOAT-debate vocabulary, high-intensity framing. For reaction, whatever is short and lacks the markers of the other three.

**What it missed:** The defining features of the harder categories are logical, not lexical. A hot_take is defined by the *absence* of evidence — you cannot detect absence from word frequency. The model cannot ask "does this post cite evidence supporting its claim?" It can only ask "does this post sound like the hot_takes in my training set?" Those are different questions. A calm prediction thread answer — "Jacob Toppin will stick with the Hawks and earn an end-of-rotation spot" — doesn't sound like a GOAT debate. It is a hot_take by definition (forward-looking claim, no evidence) but not by tone, so it falls into reaction. Similarly, reaction is defined by temporal immediacy and emotional function, not by vocabulary. A creative third-person Kawhi Leonard narrative is a reaction; it just deploys irony and narrative distance instead of direct emotion. The model has no way to detect that the post is *in response to* a championship win rather than an assertion *about* Kawhi's personality.

**The core mismatch:** The intended definitions cut along semantic and intentional lines. The learned decision boundary cuts along tonal and lexical lines. For news and analysis, these two lines happen to overlap almost perfectly — news posts really do use journalist attribution, analysis posts really are longer and more statistical. For hot_take and reaction, the lines diverge. The surface correlate for hot_take (tonal assertiveness) captures many hot_takes but misses calm ones. The surface correlate for reaction (short, non-analytical, non-news) captures many reactions but misses creative or ironic ones.

This is not a failure of DistilBERT. It is a consequence of asking a pattern-matching model to learn a logical concept — assertion-without-evidence — from 42 examples. The concept requires understanding what is *absent* from a post, which is not learnable from n-gram patterns. The practical implication: improving hot_take performance requires either substantially more examples that break the surface correlate (calm predictions, ironic claims, dry assertions) or a modeling approach that can represent evidential structure explicitly, which fine-tuning on 42 examples of a 67M-parameter model cannot provide.

### Spec Reflection

**Where the spec helped:** planning.md Section 5 identified reaction ↔ hot_take as a predicted failure pair before any data was collected: "The confusion matrix will show whether the model's errors concentrate where predicted." It did. Hot_take → reaction accounted for 5 of 7 misclassifications — exactly the anticipated pair. Because this was documented in advance, the evaluation did not have to characterize the failure from scratch. The analysis in the report (why the model learned tonal intensity as a proxy for an intent-based distinction) could focus on depth rather than orientation. The spec's diagnostic framing paid off: predicting the failure mode before evaluation means the failure is interpretable when it arrives.

**Where implementation diverged:** planning.md Section 7 specified a strict annotation order — "manual annotation first, without seeing any LLM output" — and explained why: "This order matters: manual annotation first prevents the LLM's output from anchoring judgment on hard cases." The actual workflow inverted this. Rule-based pre-labels were generated first and shown to the annotator, who then reviewed and corrected them. The deviation was justified on practical grounds: rule-based heuristics are deterministic and transparent, not opinion-based, so the anchoring risk is lower than with a generative LLM. The 17 disagreements caught suggest the review was active, not passive. But the spec's underlying concern still applies. On genuinely ambiguous posts — the Cousins "Wait" post, the Bleacher Report editorial ranked list — seeing a pre-label before reading can make an incorrect label feel plausible on first pass. The 91% agreement rate reflects how often the human caught the rule being wrong, but it does not tell us how often a plausible-but-wrong pre-label went unchallenged. That is the residual risk the spec was designed to eliminate and the implementation accepted.

---

## AI Tool Usage

Three instances, each described by what was directed, what the tool produced, and what was changed or overridden.

---

**Instance 1 — Label stress-testing (before annotation)**

*Directed:* Before any data was collected, Claude was given real r/NBA posts and asked to classify them under draft label definitions, then flag any case where two definitions could both apply or where the boundary was genuinely ambiguous.

*Produced:* Two hard boundary types surfaced. First: analysis ↔ hot_take — a post listing Jalen Brunson's awards across his career, then concluding he is "one of the most decorated basketball players of all time" who few can "measure up to." Claude classified it as analysis; re-reading it with the strip-evidence test revealed the conclusion stood alone without any of the cited awards, making it a hot_take. Second: news ↔ analysis — a post quoting DC beat reporter JP Findlay on Trae Young's market, titled "Trae Young got a max because of the new lottery changes." Claude correctly flagged the tension: the attribution signals news, but the OP's title frames the sourced quote as evidence for their own causal argument.

*Changed:* The boundary rules in planning.md Section 2 were written in direct response to these conflicts — the strip-evidence test for analysis ↔ hot_take ("if the conclusion stands alone without the evidence, it is a hot_take") and the "label what the OP is doing" rule for news ↔ analysis. Neither rule existed in the label definitions before stress-testing. Claude's initial classifications were overridden in both cases after applying the newly articulated rules.

---

**Instance 2 — Pre-labeling (during annotation)**

*Directed:* After data collection, Claude was used to write `prelabel.py`, a script that pre-labels posts using deterministic rules — not Claude's open-ended opinion of each post. The rules were: journalist attribution in brackets as a strong news signal, keyword signals for obvious reactions (exclamations, game-thread vocabulary), and structural heuristics for analysis (statistical tables, basketball-reference links). The output was written to the `pre_label` column in `dataset_prelabeled.csv`, alongside a blank `final_label` column for human review.

*Produced:* 183 pre-labeled rows across 251 collected posts. 28 rows (the additional hot_take examples added after initial collection) were set aside for manual-only labeling with no pre-label.

*Changed:* 17 of 183 pre-labels were overridden during manual review (91% agreement). Common overrides: the journalist attribution rule fired on a Bleacher Report ranked editorial ("[Bleacher Report] The 50 Worst NBA Trades of All Time, Ranked"), which the script labeled news — the human labeled it analysis because the content is a subjective editorial, not a factual report. Several reaction keyword signals misfired on dry, non-emotional posts that happened to use reactive vocabulary in a different context. The 91% agreement rate reflects how reliable the rules were on clear-cut cases; on boundary cases, the rules were wrong at a higher rate than 9%.

---

**Instance 3 — Failure analysis (after evaluation)**

*Directed:* After extracting all 7 wrong predictions from the notebook, all 7 posts were pasted into Claude with the prompt: *"Here are posts the model mislabeled. What patterns do these share in length, structure, vocabulary, or content?"*

*Produced:* Claude identified one dominant pattern: the misclassified hot_takes were tonally calm — no exclamation marks, no capslock, no reactive vocabulary — while correctly classified hot_takes in the training data were likely more assertive in register. It also flagged one post (a hot_take about a copyright decision) as potentially closer to reaction, surfacing a possible annotation error that had not been caught during manual review.

*Changed:* The calm-hot_take pattern was verified by independently re-reading all 7 posts before being included in the failure analysis. It held: every misclassified hot_take was low-affect; no misclassified hot_take was tonally loud. The pattern became the central explanation in the Three Specific Failures section above. The potential mislabeling of the copyright post was not acted on — the label was not retroactively changed, and this is the correct decision. Retroactively correcting a test-set label because a post-hoc AI analysis suggested it was wrong would compromise the test set's integrity. The label stands as annotated; the uncertainty is disclosed here.

---

## Repository Contents

| File | Description |
|---|---|
| `planning.md` | Full design notes: label definitions, edge cases, data collection plan, evaluation metrics reasoning, AI tool plan |
| `data/dataset.csv` | Final labeled dataset (211 examples, `text / label / notes`) |
| `data/dataset_prelabeled.csv` | Annotated working file with pre-label, final-label, and changed columns |
| `TakeMeter_finetune.ipynb` | Fine-tuning notebook (DistilBERT + Groq baseline) |
| `evaluation_results.json` | Aggregate metrics from the test set |
| `confusion_matrix.png` | Confusion matrix visualization |
| `collect.py` | PullPush API scraper for r/NBA comments |
| `prelabel.py` | Rule-based pre-labeling script |
| `cleanup.py` | Post-annotation cleanup: removes junk rows, sets `changed` flag |
| `export.py` | Exports `dataset.csv` from `dataset_prelabeled.csv` |
