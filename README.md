<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      </li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Committing Changes</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We're trying to simulate yo

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gitblip/Analog-Neural_Network_simulation.git
   ```

    ![pic to help](assets/images/HelpfulPicyes.png)

2. Enter the repo and change your branch to avoid pushing to main
    ```sh
    cd Analog-Neural_Network_simulation
    git switch -c <branch-name>
    ```
3. Make sure to check which branch youre pushing your update to
   ```sh
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Committing changes

After createing a seperate and new branch, push updates to here

1. Create the .git folder (it should already have been created after cloning the repo)
    ```sh
    git init
    ```
2. After adding your changes, you need to add those changes that you want to ur init file before pushing to your branch
    ```sh
    git add .
    #this is a comment, not always ull need to add everything, sometimes u want add only seom things, figure it out if u to remove stuff from your commit or whatev is required, but beware of commit history and adding to commit before pushing the previous commit
    ```
3. Commit your changes
    ```sh
    git commit -m "whatev msg u want to display with your commit"
    git status
    #git status helps you see what files will be pushed
    ```
4. Check your branch and then push, DONT PUSH TO MAIN  
    ```sh
    git branch --show-current
    #for the first time youll need to run this
    git push -u origin <branch name>
    # '-u' sets your upstream sot hat next time onwards you can just type the following
    git push
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

# Project Skynet — Analog Compute-in-Memory for Edge Inference

A hardware-aware precision–efficiency study of analog compute-in-memory (CIM)
inference, with a 2×2 resistive crossbar testbed used to calibrate a Python
analog-aware simulator.

**Team:** Ashray BN, Amith Gabburi, Pradhyumnan R
**Mentor:** Sudha Radhika · BITS Pilani, Hyderabad Campus
**Duration:** Two semesters · **Target maturity:** TRL 4

---

## The claim

**Primary (the contribution).** Most analog-CIM studies validate their simulator
against SPICE or against nothing. We validate ours against copper.

> Standard analog-CIM simulation assumptions, parameterised from literature,
> over-predict the accuracy of a physically built analog MAC array by X%.
> Calibrating the simulator with independently measured non-idealities reduces
> that gap to Y%.

**Secondary (the application).** Once the simulator is trusted, use it:

> For a fixed 784–128–10 MLP on MNIST, *N*-bit is the minimum precision at which
> analog CIM achieves lower estimated energy and latency than a digital baseline
> while maintaining ≥95% classification accuracy.

Note the ordering. The precision sweep is well-covered in the literature (minimum
precision criteria, ADC boundary precision, NeuroSim-style tooling), so it is the
*result we apply the tool to*, not the novelty. The measurement is the novelty.
Every task below still happens — only the argument order changes.

Pin this somewhere visible. Revisit it monthly — the data will reshape it.

**Scope boundaries (state these explicitly, everywhere):**

- Inference only. No in-memory training.
- Simulation-backed. No chip fabrication.
- The hardware validates the *signal chain* (MAC → nonlinearity → conversion),
  not density or energy. Energy/latency numbers are literature-derived.
- MNIST, MLP, one architecture. Fixed on purpose — it's the control.

---

## Repository layout

```
Analog_Neural_Network/
├── README.md
├── notebook/              # lab notebook: date, what tried, what happened, what it means
├── baseline/              # PyTorch FP32 MLP training
├── quantization/          # PTQ / QAT pipelines
├── simulator/             # analog-aware inference forward pass (the core contribution)
├── hardware/
│   ├── ltspice/           # schematics + Monte Carlo decks
│   ├── bringup/           # stage-by-stage measurement logs
│   └── calibration/       # extracted non-ideality parameters
├── energy_model/          # assumptions table, cited parameters, sensitivity sweeps
├── figures/               # every figure regenerable from saved results
├── configs/               # one config file per experiment
└── paper/                 # Overleaf mirror, IEEE template, bib
```

---

## Status board

| Track | State | Next action |
|---|---|---|
| LTspice simulation | Done — 500-trial Monte Carlo validated (~1.1% relative σ) | Write up as a results subsection |
| Hardware parts | Specified; order pending/placed | Confirm delivery, start Stage 1 bring-up |
| PyTorch FP32 baseline | Not started / queued | **Start now** — unblocks everything downstream |
| Quantization study | Not started | Blocked on baseline |
| Analog-aware simulator | Not started | Can be scaffolded in parallel with baseline |
| Energy/latency model | Not started | Collect cited parameters during lit review |
| Frozen predictions | Not started | **Must be committed before the board is powered on** |
| Hardware calibration | Blocked on build | — |
| Sim-to-real gap (primary result) | Blocked on the two above | — |
| Paper draft | Not started | Start Methods section once simulator exists |

---

## Work split

Hardware build and bench measurement are handled **externally** and are not in
this split. The software divides into three owned areas with defined interfaces.
Assignments below are a starting point — swap them if they don't match who is
actually strongest where, but swap whole areas, not individual tasks.

| Owner | Area | Tracks |
|---|---|---|
| **Ashray** | Model & quantization | A, B |
| **Amith** | Analog-aware simulator | C |
| **Pradhyumnan** | Experiment harness, energy model, figures, validation | E0, F, G |

### Week 1, together: freeze the interfaces

Nothing can run in parallel until these three file formats are agreed and written
down. Do this before anyone writes real code; each person then builds against a
stub of the other two.

- [ ] **`checkpoints/*.npz`** — Ashray → Amith. Quantized weight tensors per layer,
      plus scale/zero-point and the bit-width used. Fixed key names.
- [ ] **`configs/*.yaml`** — Pradhyumnan → Amith. One file per experiment:
      `b_w`, `b_in`, `b_psum`, noise σ, ablation flags, seed, trial count.
- [ ] **`results/*.csv`** — Amith → Pradhyumnan. One row per trial: config id,
      seed, accuracy, per-layer output statistics.
- [ ] **`hardware/measured_params.yaml`** — external → Pradhyumnan. Weight-error σ,
      offset, gain, noise floor, drift. Agree the schema now so the bench team
      knows exactly what to record.

### Ashray — model & quantization

Owns everything upstream of the simulator. Delivers trained artefacts, not plots.

- Tracks A and B in full: FP32 baseline, activation variants, PTQ/QAT decision
  and implementation, quantized checkpoints at 2/4/6/8 bits, digital-only accuracy
- Owns open decisions **1 (ReLU vs sigmoid)** and **2 (PTQ vs QAT)**
- Paper sections: baseline architecture, quantization scheme
- Panel Q&A: why 784–128–10, why fixed architecture, PTQ vs QAT

### Amith — analog-aware simulator

Owns the core contribution's machinery. Builds components; does not run the sweeps.

- Track C in full: the forward pass (DAC quantization → MVM → noise → ADC
  quantization → activation), noise model, weight-error model, offset/gain model
- Exposes every non-ideality as an independently togglable flag so the ablations
  are configuration, not code changes
- Validates one configuration against `aihwkit` or DNN+NeuroSim
- Paper sections: simulator design, non-ideality models
- Panel Q&A: why build our own simulator, what the simulator does and doesn't model

### Pradhyumnan — harness, energy, figures, validation

Owns the experiment grid and the sim-to-real comparison. Acts as referee.

- **Track E0 in full** — generates the frozen predictions and commits them before
  the board is powered on
- Ablation harness and Monte Carlo runner (5 conditions × 4 precisions × 30 trials)
- Track F: energy/latency model, assumptions table with one citation per parameter,
  sensitivity analysis, digital baseline definition
- Track G: all figures, regenerable by script from saved results
- Ingests `measured_params.yaml` and produces the uncalibrated and calibrated gap
- Paper sections: results, energy methodology, limitations
- Panel Q&A: budget defence, digital baseline fairness, breadboard vs silicon scoping

> **Why the simulator owner does not own the comparison.** Whoever can tune the
> simulator must not be the one judging whether it matches hardware — that's how
> curve-fitting creeps in and kills the result. Keeping E0 with Pradhyumnan makes
> the firewall structural rather than a matter of discipline. Say this to the panel
> if asked how you avoided fitting the data; it's a good answer.

### Shared

- Literature matrix — split the reading three ways, one shared spreadsheet
- Weekly: update the status board, review each other's commits
- Lab notebook — each person keeps their own, dated

---

## Track A — Software baseline *(Ashray)*

- [ ] Git repo initialised; `.gitignore`, fixed random seeds, `requirements.txt`
- [ ] PyTorch 784–128–10 MLP trained on MNIST to FP32 convergence
- [ ] Record baseline test accuracy, training config, seed — this is the number
      everything else is compared against
- [ ] Train activation-function variants (ReLU, sigmoid, tanh) on the same
      architecture and seed
- [ ] **Resolve the activation inconsistency in the proposal.** It says sigmoid
      was chosen for analog friendliness, but the hardware is a ReLU precision
      rectifier. Pick one coherent story: either "ReLU via precision rectifier
      (ISCAIT 2025), with sigmoid evaluated in simulation only," or commit to
      sigmoid and redesign the activation block. Do this before the panel.
- [ ] Checkpoint saved and loadable; `train.py` reproducible from config

## Track B — Quantization *(Ashray)*

- [ ] **Decide PTQ vs QAT and state it explicitly.** Post-training quantization
      works at 8-bit, degrades at 4-bit, and typically collapses at 2-bit.
      Reviewers consider this choice central. If 2-bit is in scope, you need QAT.
- [ ] Implement per-layer weight quantization at 2/4/6/8 bits
- [ ] Separate the three precision axes and vary them independently:
      - `b_w` — weight precision (digital pot taps)
      - `b_in` — input/DAC precision
      - `b_psum` — partial-sum/ADC precision
- [ ] Measure digital-only accuracy at each precision level (no analog effects yet)
- [ ] Record symmetric vs asymmetric, per-tensor vs per-channel choices

## Track C — Analog-aware simulator *(Amith)*

Build your own forward pass. This is the contribution — don't use a library for it.

- [ ] Forward pass: quantize weights → DAC-quantize inputs → matrix–vector
      multiply → inject noise → ADC-quantize partial sums → activation
- [ ] Additive Gaussian noise model with σ justified by citation or measurement,
      never an arbitrary number
- [ ] ADC/DAC quantization models with configurable bit depth
- [ ] Weight-programming error model (σ from measured trimpot/digital-pot spread)
- [ ] Offset and gain error model
- [ ] **Ablation harness** — the study design that makes this credible:
      FP32 → quantization only → noise only → ADC/DAC only → all combined.
      "Which non-ideality actually hurts" is one of your most interesting answers.
- [ ] **20–30 Monte Carlo trials per configuration.** Analog noise is random;
      a single run is an anecdote. Report mean ± σ with error bars on every plot.
- [ ] Sanity-validate one configuration against IBM `aihwkit` or DNN+NeuroSim —
      a big credibility boost even though the simulator is your own

## Track D — Hardware PoC (2×2 crossbar) *(external build team)*

Components: MCP41010 digital pots ×4, TL074 op-amps, MCP4725 DAC, ADS1115 ADC,
Arduino Nano, 1% metal-film resistors, 1N4148, ±supply.

Bring up in stages. Never all at once — if the 2×2 misbehaves you must be able to
tell a single-synapse problem from an array problem.

- [ ] **Stage 1** — one resistor + one TIA. Verify `V_out = −(R_f/R)·V_in`.
      Meet op-amp offset and rail limits here, cheaply.
- [ ] **Stage 2** — one full column (2 resistors). Sweep a grid of (V₁,V₂),
      plot measured vs ideal → extract gain error and offset.
- [ ] **Stage 3** — second column → full 2×2 linear layer.
- [ ] **Stage 4** — ReLU block alone. Sweep −4 V → +4 V, record transfer curve
      (you're reproducing Fig. 10 of the ISCAIT paper — measure the knee).
- [ ] **Stage 5** — cascade crossbar → inverter → ReLU. Two working neurons.
- [ ] **Stage 6** — Arduino drives DAC/pots, reads ADC, streams to PC.
- [ ] **Stage 7** — signed weights via differential columns (positive/negative
      conductance pair per weight + downstream difference amplifier).
- [ ] **Stage 8** — program trained weights from PyTorch into the pots; run a
      toy task (AND/OR → XOR as stretch) and compare hardware vs software.
- [ ] Optional strong demo: take 2 pixels × 2 hidden neurons from the *actual*
      trained MNIST MLP, program those 4 weights, show hardware matches
      simulation for that tile. Ties the PoC directly to the main study.

## Track E — Calibration (the methodological core) *(Pradhyumnan, with bench data from the build team)*

### E0 — Predict before you measure (do not skip, do not reorder)

The failure mode that destroys this result: tuning the simulator until it matches
the measurements, then announcing it is "validated." That fits a curve to the data
it was supposed to predict and proves nothing. The safeguard is strict ordering.

- [ ] Freeze the simulator with **literature-derived parameters only** — no
      hardware numbers in it yet
- [ ] Choose a fixed input set; record the simulator's predicted outputs
- [ ] **Commit those predictions to git before the board is powered on.**
      Timestamped, untouched. This is the whole safeguard.
- [ ] Build, measure the same inputs, record measured outputs
- [ ] **Report the gap — this is the primary result**, whether it is 1% or 30%
- [ ] Only now: measure the parameters below *independently*, load them in,
      re-predict, and report the residual gap
- [ ] Report both numbers: how wrong uncalibrated literature assumptions were,
      and how much calibration recovers

### E1 — Parameter extraction

Measure on hardware, transplant into the simulator, then show they agree.

- [ ] **Weight error** — set each pot tap, measure actual resistance → σ of
      weight programming. Also characterise the tap-to-weight nonlinearity
      (`w = R_f/R` is nonlinear in tap index) — this is a novel contribution.
- [ ] **Offset / gain error** — linear fit of measured vs ideal from Stage 2.
- [ ] **Noise floor** — fix inputs, log ~1000 ADC samples, take σ. Expect 50 Hz
      mains pickup; twist wires, keep leads short.
- [ ] **Drift / thermal** — log output for 30 min, or warm the board gently.
- [ ] **Quantization** — the 12-bit DAC / 16-bit ADC *is* the model, running live;
      truncate in software to emulate 2/4/6/8-bit converters.
- [ ] Inverter-stage variance contribution (your Monte Carlo says it exceeds the
      crossbar's — confirm on hardware, it's a report-worthy architectural finding)
- [ ] **Validation run:** identical inputs through hardware and through the
      simulator loaded with measured parameters. If predicted matches measured
      within noise, the framework is validated. That's the claim.

**Framing caveat — rehearse this.** Breadboard non-idealities (op-amp offset,
resistor tolerance, mains pickup) are not nanoscale RRAM non-idealities
(conductance drift, IR drop, device variation). Never say "we measured our chip's
noise." Say: "we validated the simulation machinery at macro scale — it correctly
turns measured non-idealities into output errors — then used literature-derived
device parameters for chip-scale projections."

## Track F — Energy & latency model *(Pradhyumnan)*

- [ ] **One assumptions table, one citation per parameter.** Literature values for
      MAC and ADC energy span an order of magnitude across technology nodes.
- [ ] Anchor ADC energy vs resolution vs speed to Murmann's ADC Performance Survey
- [ ] Anchor digital baseline to Horowitz, "Computing's Energy Problem" (ISSCC 2014)
- [ ] **Define the digital baseline precisely.** A CPU is an unfair, easy win and
      reviewers will say so. Use an 8-bit digital MAC array at a stated technology
      node. Its energy *must include memory access* — that's the whole Von Neumann
      point; omit it and you've erased CIM's advantage.
- [ ] Per-precision energy and latency estimates including ADC/DAC overhead
- [ ] **Sensitivity analysis** — "if ADC energy were 3× higher, the crossover
      shifts from 4-bit to 6-bit." Converts your model's biggest vulnerability
      into a demonstration of thoroughness.

## Track G — Figures *(Pradhyumnan)*

Design experiments toward the money figure; decide it now.

- [ ] **Money figure (the contribution):** predicted vs measured outputs, shown
      twice — uncalibrated (literature parameters) and calibrated (measured
      parameters) — with the gap annotated in both panels
- [ ] **Second figure (the application, two panels):** accuracy vs bit-precision
      with error bars (analog vs digital) · energy-per-inference vs bit-precision,
      crossover annotated
- [ ] Ablation figure: which non-ideality costs how much accuracy
- [ ] ReLU transfer curve, measured vs LTspice
- [ ] Monte Carlo variance breakdown by stage
- [ ] Every figure regenerable by script from saved results
- [ ] Captions state the takeaway ("4-bit analog matches digital accuracy at 2.1×
      lower energy"), not just the contents

## Track H — Paper *(all three; sections owned per the split above)*

Write in this order: Methods → Results → Related Work → Introduction → Abstract → Title.

- [ ] Literature matrix spreadsheet: one row per paper, columns for
      device/technology, workload, precision studied, noise model, energy model,
      key result. The empty cell is your gap; the matrix becomes Related Work.
- [ ] Core reading: Keshav's "How to Read a Paper" · Horowitz ISSCC 2014 ·
      Murmann ADC survey · Shafiee et al. (ISAAC, ISCA 2016) · Sebastian et al.
      (Nature Nanotech 2020) · Gholami et al. quantization survey
- [ ] Zotero library set up, BibTeX exporting to Overleaf
- [ ] Overleaf project on the IEEE conference template
- [ ] Methods section — enough detail to reproduce: architecture, quantization
      scheme, noise equations, ADC/DAC model, energy equations with cited parameters
- [ ] Results — neutral reporting
- [ ] Discussion with an honest **Limitations** paragraph (simulation-only,
      MNIST-only, MLP-only, literature-derived energies, breadboard ≠ silicon)
- [ ] Related Work from the matrix, each theme ending with how you differ
- [ ] Introduction: context → problem → gap → "In this paper, we…" + 3–4 contributions
- [ ] Abstract last, ~200 words: problem, approach, headline number, implication
- [ ] Cite standard topologies properly: TIA column readout → Hu et al. /
      Shafiee et al.; precision rectifier ReLU → Zhang, Zhao & Zhu, ISCAIT 2025
- [ ] **Contributions list — claim only these three:**
      (1) a physically built, open, sub-₹10k analog MAC testbed;
      (2) a measured sim-to-real accuracy gap for standard CIM simulation
      assumptions, before and after calibration;
      (3) an open analog-aware simulator with every parameter cited.
      Do **not** claim the precision–accuracy tradeoff itself as novel — it is
      well-characterised, and claiming it invites a reviewer to list ten papers.
- [ ] Keep the MCP41010 tap nonlinearity and the inverter-stage variance finding
      in **Results**, as honest engineering observations. They are properties of
      this discrete build, not findings about CIM — they do not belong in
      Contributions.
- [ ] Limitations must state plainly that the precision tradeoff is already
      well-covered in literature and that the contribution is the validation
      methodology at macro scale
- [ ] 3–5 revision cycles with mentor — send sections as they're done, not one dump
- [ ] Agree authorship order and mentor inclusion **early**
- [ ] Target venues, in order of attainability: SIP report / campus symposium →
      arXiv preprint + public GitHub repo → INDICON or VLSI Design student track →
      IEEE AICAS (closest fit) → ISCAS (stretch)

## Track I — Admin & panel *(all three)*

- [ ] Replace the Lorem ipsum on the **Budget Estimation** and **Risk Management**
      slides — the brief explicitly requires defending the budget
- [ ] Rewrite the Future Plans slide: drop "NPU chip for wearables" (it contradicts
      "does not involve chip fabrication" in your own proposal). Replace with
      near-term (1→2×2→4×4 array, PTQ→QAT), medium-term (extend simulator to CNNs,
      calibrate against published silicon), long-term (release the framework as an
      open tool feeding a future silicon design)
- [ ] Budget sheet: purpose column + actual-vs-budgeted tab; vendor screenshots
      archived to the dated Drive folder; quote the precise total, not a round number
- [ ] Rehearsed answers for: why the budget grew · why digital pots not fixed
      resistors · why a 16-bit ADC when studying 2–8 bit · why resistive CIM not
      SRAM-CIM · did you build "real" analog CIM · why not transformers
- [ ] Lab notebook started and kept daily

---

## Open decisions (resolve before the panel)

1. **ReLU or sigmoid** as the primary activation — the proposal currently says both.
2. **PTQ or QAT** — determines whether 2-bit is reportable at all.
3. **Digital baseline definition** — which architecture, which technology node.
4. **Fallback benchmark** — if MNIST is too forgiving to show degradation,
   Fashion-MNIST is a one-line change. Say so before being asked.
5. **Paper framing** — sim-to-real validation (research venue) or low-cost
   testbed as a teaching instrument (education venue: IEEE MSE, TALE, FIE).
   The build is identical either way; decide which story before writing Methods.

## Terminology discipline

- Say **compute-in-memory**, not *neuromorphic*. Neuromorphic means spiking,
  event-driven architectures; say it and you'll be asked about STDP and
  integrate-and-fire models you aren't building.
- Say **inference**, not *training* — CIM here is weight-stationary.
- Never say the 2×2 board "runs MNIST." It validates the MAC + ReLU building
  block whose measured parameters feed the simulator, which scales to the MLP.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

