# TakeMeter Planning

## 1. Community

I chose r/NBA because it's one of the largest and most active sports communities online — millions of subscribers and consistent high-volume posting throughout the season and offseason. More importantly, the discourse is genuinely varied: the same subreddit hosts stat-heavy analytical breakdowns, emotional reactions to trades, sourced beat reporter posts, and bold opinion takes argued with nothing but conviction.

NBA fan culture is a strong fit for classification because the community has an internal sense of what makes a good take. Regular members visibly distinguish between posts that show their work — citing basketball-reference numbers, cap figures, historical comparisons — and posts that just assert opinions loudly. That shared standard is what makes the label boundaries meaningful to the community, not just to a classifier.

The discourse is varied enough to be interesting for three reasons. First, the NBA has a rich statistical tradition: sites like basketball-reference make specific claims verifiable, which means analytical and assertive posts look structurally different. Second, the offseason — trades, free agency, the draft — generates all discourse types simultaneously, producing dense and heterogeneous content in short windows. Third, the subreddit spans both top-level posts and comment threads, which differ systematically in style: top posts skew toward news and analysis, while comment sections are where reactions and hot takes concentrate.

## 2. Labels

### Definitions

**analysis** — The post makes a structured argument backed by statistics, historical comparisons, or tactical observations where the evidence is specific, verifiable, and the conclusion follows from it.

**hot_take** — The post makes a bold, confident claim or opinion without supporting evidence; it asserts rather than argues, and the conclusion could stand alone without any data cited.

**reaction** — The post is an immediate emotional response to a specific event, expressing a feeling in the moment with little to no argument.

**news** — The post is a factual report of an event, transaction, or statement with no editorial opinion; its primary value is the information itself, not an interpretation of it.

### Boundary Rules

- **analysis vs. hot_take**: If stripping out all cited evidence leaves a claim that could stand alone as a hot_take, label it **hot_take**. The evidence must be load-bearing — it must be what makes the conclusion defensible — not decoration around an assertion.
- **news vs. analysis**: Label what the OP is *doing*. If the OP frames sourced information to support their own conclusion, it is **analysis**. If the OP's role is purely to pass along information with no interpretive framing, it is **news**.
- **reaction vs. hot_take**: Label the primary mode. If the post is primarily expressing a feeling in response to an event, it is **reaction** — even if it contains an embedded opinion. If the post is primarily asserting a claim (event-triggered or not), it is **hot_take**.
- **news vs. hot_take (reported takes)**: If a post quotes or reports a bold opinion made by someone else (a player, coach, or reporter), label it **news**. The label applies to what the OP is doing, not to the content of what is being reported.

### Examples

**analysis**

> *Giannis Antetokounmpo leaves Milwaukee as the Bucks' all-time leader in points, rebounds, assists, and blocks*
>
> Giannis Antetokounmpo leaves Milwaukee as the Bucks' all-time leader in all four major statistical categories: points, rebounds, assists, and blocks. He and Kevin Garnett with the Timberwolves are the only players in NBA history to lead a franchise in all four categories.
>
> Bucks all-time points leaders: 1.) Giannis — 21,531 | 2.) Kareem — 14,211 | 3.) Khris Middleton — 12,586
> [Full leaderboards via Basketball Reference]

> *Highest Turnover Percentage On Drives In The 2025-26 NBA Playoffs (Min. 50 Total Drives)*
>
> Chet Holmgren — 14.0% | Jayson Tatum — 11.3% | James Harden — 11.1% | Evan Mobley — 10.8% | Dennis Schroder — 10.5% | Nikola Jokic — 10.0% | Victor Wembanyama — 10.0% | Keldon Johnson — 9.7% | Marcus Smart — 9.3% | Jalen Green — 9.1%

---

**hot_take**

> If Lebron played in MJ's era — the debate wouldn't even be real. LeBron would be the easy GOAT.

> Giannis/Bam/Portis? The Heat have to have something up their sleeves to move Bam too. He's just a worse Giannis. The spacing with Bam+Giannis would be the worst since the 90s.

---

**reaction**

> Ah nice we're the only ones left without a coach.
> *(In response to breaking news that Dusty May agreed to become head coach of the Dallas Mavericks)*

> IDGAF who wins the finals. OKC is out!!!!!!

---

**news**

> *[Charania] The Oklahoma City Thunder are finalizing a trade to send guard Aaron Wiggins to the Atlanta Hawks for two second-round picks (Atlanta's in 2030 and the least favorable of Hawks/Lakers in 2032), sources tell ESPN.*
>
> Wiggins — drafted with the No. 55 pick in the 2021 Draft — developed into a championship role player in Oklahoma City's culture and now moves to an up-and-coming Hawks team.

> *[Fischer] The Bulls are trading Mo Gueye to Minnesota, sources say, to complete the three-team deal that sends Julius Randle and No. 28 in tomorrow's NBA Draft to Brooklyn for No. 33, and reroutes Nic Claxton into Chicago's cap space in the new league year.*
>
> Gueye's salary is non-guaranteed for 2026-27. (Note: This is Mouhamadou Gueye, the former Raptors guard — not Mouhamed Gueye, the current Hawks forward.)

## 3. Hard Edge Cases

### Edge Case 1: analysis ↔ hot_take (hardest)

**The pattern:** A post cites a long, verifiable list of statistics or credentials, then draws a sweeping comparative or qualitative conclusion that the evidence alone cannot support. The structure looks like analysis — specific numbers, named sources, historical references — but the conclusion goes well beyond what the data proves.

**Canonical example:** A post listing every Jalen Brunson award from high school through the NBA, then concluding he is "one of the most decorated basketball players of all time," that "few can measure up to him," and that the NBA should make him its face over Wembanyama, Edwards, and Shai. The awards are real and verifiable. But "few can measure up to him as a basketball player" does not follow from a list of awards — it is a sweeping claim that would require cross-era comparison, efficiency metrics, and playoff context to support. Strip out the award list and the conclusion stands alone as a hot_take assertion.

**Resolution rule:** Strip out all cited evidence. If the conclusion could stand alone as a hot_take without it, label it **hot_take**. Evidence must be load-bearing — it must be what makes the conclusion defensible — not a preamble to an assertion.

---

### Edge Case 2: news ↔ analysis

**The pattern:** A post quotes a beat reporter or insider source, but the OP uses that quote as evidence for their own causal argument rather than simply passing along information. The attribution signals news; the framing signals analysis.

**Canonical example:** A post titled "Trae Young got a max because of the new lottery changes," quoting DC beat reporter JP Findlay saying Trae's market changed after lottery reform, with multiple teams offering max deals. The quote is sourced journalism. But the OP's title frames it as a causal argument — lottery reform caused Trae's market to shift — making the reporter's quote a piece of evidence rather than the point of the post.

**Resolution rule:** Label what the OP is doing. If the OP uses sourced information to support their own conclusion, it is **analysis**. If the OP's role is to relay information with no interpretive framing of their own, it is **news**.

---

### Edge Case 3: reaction ↔ hot_take

**The pattern:** A post is triggered by a specific event and expresses emotion, but also contains a bold embedded opinion. Both the reactive register and the assertive claim are present.

**Canonical example:** "I see this and think of Kevin Garnett WHY the f\*ck you crying like you won the championship… You still got the finals." The post is clearly triggered by seeing something (reactive), invokes a comparison (assertive), and is mostly dismissive/emotional rather than argumentative.

**Resolution rule:** Label the primary mode. If the dominant register is emoting or dismissing in response to an event, it is **reaction**. If the dominant register is asserting a claim — even an event-triggered one — it is **hot_take**. A passing analogy or reflex comparison does not make a reaction a hot_take.

---

### Edge Case 4: analysis ↔ hot_take (discovered during annotation)

**The pattern:** A post cites a single verifiable statistic and then draws a sweeping editorial conclusion from it. The stat is real but the conclusion far exceeds what it proves.

**Annotation example:** "Giannis shooting 17-19 from the FT line in a close out game 6 after being a historically bad shooter is one of the most ridiculous things to happen in finals history. Fucking poetic." The pre-labeler flagged the 17-19 stat as evidence of analysis. But stripping it out, "one of the most ridiculous things to happen in finals history" is a pure assertion that no single statistic can support. The stat gives context but the conclusion stands alone without it.

**Resolution:** Applied the strip-evidence test from Edge Case 1. Labeled **hot_take**. One verifiable data point does not make a post analysis if the conclusion drawn from it is disproportionate.

---

### Edge Case 5: analysis ↔ reaction (fact-citing reaction)

**The pattern:** A brief post states a verifiable historical fact immediately followed by an exclamation of surprise or emotion. The fact is real but the post's purpose is to express a feeling, not to argue anything.

**Annotation example:** "Denver is the first team in NBA history to come back from multiple 3-1 deficits in a single postseason... WOW" The pre-labeler saw the historical fact and labeled it analysis. But the post makes no argument — it states the fact and reacts to it. There is no conclusion, no evidence chain, no structured claim.

**Resolution:** Labeled **reaction**. Citing a fact is not the same as analyzing it. A post that exists to express surprise at a fact is a reaction to that fact, not an analysis of it.

---

### Edge Case 6: news ↔ analysis (editorial content with journalist attribution)

**The pattern:** A post uses journalist attribution in brackets — a strong news signal — but the content is a subjective ranked list or editorial piece, not a factual report.

**Annotation example:** "[Bleacher Report] The 50 Worst NBA Trades of All Time, Ranked" The bracket pattern triggered the news classifier. But the content is a ranked editorial (subjective, judgment-based), not a factual transaction report.

**Resolution:** Labeled **analysis**. Attribution in brackets identifies the source, not the genre of the content. An editorial ranking is analysis. This refined the news boundary rule: bracket attribution is a necessary but not sufficient condition for the news label — the content itself must be a factual report.

## 4. Data Collection Plan

### Source

All examples will be drawn from r/NBA, pulling from both top-level posts and comments. Posts and comments have different label distributions: top-level posts skew toward news and analysis, while comment sections are where reactions and hot takes concentrate. Both are needed to build a balanced dataset.

Collection will use a hybrid approach: the PullPush Reddit API (which supports both submission and comment endpoints) to pull candidates in bulk, followed by manual annotation. The API handles sourcing at scale; manual review handles labeling, which requires judgment the API cannot provide.

### Target Volume

**250 total examples collected, targeting ~50 usable per label (~200 usable total).**

The extra 50 examples serve as a buffer for posts that turn out to be unlabelable — content that does not cleanly fit any of the four established labels. Rather than forcing a label onto junk data, those posts will be discarded. Collecting 250 ensures the usable set stays close to 200 even after filtering.

| Label | Target (usable) | Notes |
|---|---|---|
| analysis | ~50 | Harder to find at volume; may require targeted search |
| hot_take | ~50 | Common; risk of oversampling |
| reaction | ~50 | Common in comments; easy to oversample |
| news | ~50 | Easy to find during trade/free agency periods |

### Sampling Strategy

Random collection from r/NBA will naturally oversample news and reactions (breaking trade news floods the subreddit during the offseason) and undersample analysis (stat breakdowns are less frequent). To counteract this, collection will not be purely random — posts will be sourced across different time periods and post types to ensure variety.

### If a Label Is Underrepresented After 200 Usable Examples

Do not continue random collection — it will produce more of the already-overrepresented labels. Instead, use targeted search:

- **analysis underrepresented**: Filter for posts containing basketball-reference links, salary/cap figures, or stat tables. These are strong signals for verifiable evidence.
- **hot_take underrepresented**: Search for GOAT debates, era comparison threads, and opinion posts with high comment volume but no cited evidence.
- **reaction underrepresented**: Pull from game thread comments during or immediately after games.
- **news underrepresented**: Pull from the period around the NBA Draft, trade deadline, or free agency opening.

## 5. Evaluation Metrics

### Why Accuracy Alone Is Not Enough

Accuracy is misleading for this task because the dataset will likely have class imbalance — news and reactions are easier to collect at volume and may dominate. A model that over-predicts common labels can achieve high accuracy while being nearly useless on underrepresented ones. A good classifier must perform across all four labels, not just the frequent ones.

### Primary Metric: Macro F1

Macro F1 averages the F1 score across all four labels equally, regardless of how many examples each label has. This means the model must perform well on analysis and hot_take — the harder, less frequent labels — to score well overall. It is the right aggregate metric when all label types matter equally.

### Supporting Metrics: Per-Class Precision and Recall

Macro F1 summarizes performance but hides the nature of failures. Per-class precision and recall reveal how the model is failing on each label:

- **Low precision** on a label means the model is over-predicting it — labeling too many posts as that class.
- **Low recall** on a label means the model is under-predicting it — missing actual examples of that class.

These distinctions matter for interpreting model behavior and for honest assessment in the evaluation report.

### Diagnostic: Confusion Matrix

The confusion matrix is the most informative output for this specific task. During label design, three hard edge case pairs were identified: **analysis ↔ hot_take**, **news ↔ analysis**, and **reaction ↔ hot_take**. The confusion matrix will show whether the model's errors concentrate where predicted, or whether unexpected failure modes emerge. The fine-tuning notebook generates this automatically.

### Baseline Comparison

Both the fine-tuned DistilBERT model and the Groq baseline (llama-3.3-70b-versatile) will be evaluated on the same held-out test set using the same metrics: macro F1, per-class precision and recall, and the confusion matrix. Keeping the evaluation consistent across both models makes the comparison valid and meaningful. This framing will be carried forward into the evaluation report.

## 6. Definition of Success

### Realistic Ceiling

The practical ceiling for this project is the Groq baseline (llama-3.3-70b-versatile). That model has 70 billion parameters and broad language understanding but no task-specific training. The checkable criterion this maps to: fine-tuned macro F1 ≥ Groq baseline macro F1 − 0.05. Landing within 5 points of — or beating — a 70B zero-shot model with a 67M fine-tuned model is already a meaningful result given the 1000× size gap. Both scores are read off the same held-out test set, so the comparison is direct.

A result above ~0.90 accuracy would be a red flag for data leakage or labels that are too easy — not a genuine success.

With 4 labels and a roughly balanced dataset (~50 examples per label), the random baseline is ~0.25 and the majority-class baseline is also ~0.25. Both are the floor the model must beat decisively.

### Tier 1 — "The model learned something" (assignment-level success)

- Fine-tuned accuracy ≥ 0.60 **and** macro F1 ≥ 0.60 — decisively beats both the ~0.25 majority baseline and ~0.25 random baseline.
- Per-class recall ≥ 0.50 for **all four labels** — no collapsed class.
- Fine-tuned macro F1 ≥ Groq baseline macro F1 − 0.05 — a 67M-parameter model landing within 5 points of, or beating, a 70B zero-shot model is already a win given the 1000× size gap.

### Tier 2 — "Genuinely useful / deployable" (good enough for a real tool)

All of Tier 1, **plus**:

- Analysis precision ≥ 0.75
- Overall accuracy ≥ 0.70 (approaching the human ceiling)

**Analysis precision is the hard gate.** The intended product is an assistive highlighter that surfaces high-quality takes for human readers. In that setting, falsely elevating a hot_take or reaction to "analysis" erodes trust faster than missing a genuinely good take. The tool ships human-in-the-loop, as a soft signal — not an autonomous moderator.

### Failure / Not Deployable

Any of the following constitutes failure:

- Performance worse than the majority-class baseline
- Per-class recall < 0.40 for any label (class collapse)
- Analysis precision < 0.60 (the model cannot be trusted to surface good takes)

### Self-Check

Every threshold is a single number read off the test-set predictions or confusion matrix. At evaluation time, each criterion is pass/fail with no judgment call required:

| Criterion | Threshold | Pass/Fail |
|---|---|---|
| Accuracy | ≥ 0.60 (Tier 1) / ≥ 0.70 (Tier 2) | TBD |
| Macro F1 | ≥ 0.60 | TBD |
| Per-class recall (all four labels) | ≥ 0.50 | TBD |
| Fine-tuned macro F1 vs. Groq baseline | within −0.05 or better | TBD |
| Analysis precision | ≥ 0.75 (Tier 2) / ≥ 0.60 (minimum) | TBD |

## 7. AI Tool Plan

### Label Stress-Testing (completed before annotation)

Stress-testing was done before writing this document by working through real r/NBA posts and identifying posts that resist clean classification. Two hard boundary types were identified and documented in section 3: **analysis ↔ hot_take** (evidence cited as decoration for a disproportionate conclusion) and **news ↔ analysis** (sourced quote used as evidence for the OP's own causal argument). Resolution rules for both are in place before annotation begins.

### Annotation Assistance

All 200+ examples will be annotated manually first, without seeing any LLM output. After completing the manual pass, an LLM (Groq llama-3.3-70b-versatile) will label the same examples independently. Any case where the LLM label disagrees with the human label becomes a review item — the post is re-read against the label definitions and resolution rules in section 2 before the label is finalized.

This order matters: manual annotation first prevents the LLM's output from anchoring judgment on hard cases. Disagreements are used as a flag for review, not as a correction.

All examples that triggered a disagreement will be tracked and disclosed in the AI usage section of the final report.

### Failure Analysis

After model evaluation, the full set of wrong predictions will be grouped by predicted vs. true label pair and given to an LLM with the prompt: *"Here are posts the model mislabeled. What patterns do these share — in length, structure, vocabulary, or content?"*

The pairs to examine first are **analysis predicted as hot_take** and **hot_take predicted as analysis**, since those are the anticipated failure mode based on the edge case analysis in section 3. Unexpected confusion pairs — anything the confusion matrix shows that was not predicted — will be examined second.

LLM-identified patterns will be verified by reading the actual posts before being included in the evaluation report. Pattern claims that cannot be confirmed by direct reading will not be reported.
