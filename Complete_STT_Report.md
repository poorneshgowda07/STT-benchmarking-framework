# Complete STT Benchmarking & Evaluation Report

> A fully explained, beginner-friendly guide to Speech-to-Text model evaluation, benchmarking, and selection.

---

## Part 1: What is STT and Why Does Benchmarking Matter?

**STT (Speech-to-Text)** is the technology that converts spoken human voice into written text. It is the backbone of:
- Voice AI agents (like customer service bots)
- Call center transcription
- Live subtitles and captions
- Voice search ("Hey Siri", "OK Google")
- Medical and legal transcription

**Why benchmarking matters:** There are dozens of STT models available today (OpenAI Whisper, Deepgram Nova, Google Chirp, Sarvam Saaras, AssemblyAI Universal, Azure Speech). Each one claims to be "the best." But the truth is — **no single model is best for everything.** One model might be the most accurate but also the slowest. Another might be blazing fast but terrible at understanding Indian accents.

**Benchmarking** is the scientific process of testing all these models under identical conditions and measuring their performance with standardized metrics, so you can make a data-driven decision instead of guessing.

---

## Part 2: What We Built — The STT Benchmarking Framework

We built a complete, executable Python framework that automates the entire benchmarking lifecycle:

```
Audio Dataset
     ↓
Data Validation (check files are valid)
     ↓
Audio Normalization (convert to standard format)
     ↓
SHA-256 Hashing (create digital fingerprint for reproducibility)
     ↓
Benchmark Configuration (select models, languages, parameters)
     ↓
Model Adapter (connect to each provider's API)
     ↓
STT Inference (send audio, get transcript back)
     ↓
Raw Response Storage (save the exact API response permanently)
     ↓
Transcript Normalization (clean text for fair comparison)
     ↓
Metric Calculation (WER, CER, Latency percentiles)
     ↓
Evidence Extraction (save examples of successes and failures)
     ↓
Scorecard Generation (individual report card per model)
     ↓
Leaderboard (rank all models)
     ↓
Report Generation (final comprehensive document)
```

**Key design principle:** Every stage is reproducible. We hash every audio file and every configuration so that another engineer can run the exact same experiment and get the exact same results.

---

## Part 3: The 8 Components of a Good STT Model

Not all STT models are created equal. Here are the 8 dimensions that define a production-grade STT model:

### Component 1: Accuracy
- Can the model correctly transcribe what was said?
- Does it handle background noise, echo, and poor audio quality?
- Does it work on compressed phone call audio (8kHz telephony)?
- Can it handle different accents (South Indian, North Indian, British, American)?
- Does it hallucinate (generate fake words during silence)? Whisper is notorious for this.

### Component 2: Latency (Speed)
- **Time-to-First-Partial (TTFP):** How many milliseconds until the first word appears on screen?
  - For a voice AI agent, this must be under 250ms or the conversation feels laggy.
- **Endpointing:** How quickly does the model detect that the user has stopped talking?
  - If this is too slow, the AI waits awkwardly before responding (the "walkie-talkie effect").
- **Real-Time Factor (RTF):** If RTF = 0.1, the model processes 10 minutes of audio in just 1 minute.

### Component 3: Streaming Support
- **True streaming** means the model processes audio in tiny 20-80ms chunks and gives you words in real-time as the person speaks.
- **Batch mode** means you upload the entire audio file, wait, and get the full transcript back.
- For voice AI agents, true streaming is mandatory. For offline analytics, batch is fine.

### Component 4: Speaker Diarization
- Can the model tell "who said what"?
- In a customer service call, you need to know which words came from the agent and which from the customer.
- **DER (Diarization Error Rate)** measures how accurately it assigns speech to the correct speaker.

### Component 5: Text Formatting
- Does it add punctuation (commas, periods, question marks)?
- Does it capitalize proper nouns ("Delhi" not "delhi")?
- Does it convert spoken numbers to digits ("twenty five thousand" → "25,000")?
- Does it filter profanity or redact sensitive data (credit card numbers)?

### Component 6: Language Support
- How many languages does it support?
- Can it handle code-mixing (Hindi + English in the same sentence)?
  - Example: "Sir, mera credit card block ho gaya hai"
  - Most Western models completely fail at this. Sarvam Saaras excels at it.
- Can it auto-detect the language without being told?

### Component 7: Custom Vocabulary
- Can you give the model a list of special words to boost recognition?
  - Example: If you work at "KreditBee", you can tell the model to listen for that word specifically.
- This is critical for domain-specific applications (finance, healthcare, legal).

### Component 8: Cost
- STT models charge per minute of audio processed.
- Prices range from $0.001/min (self-hosted Whisper) to $0.017/min (Azure).
- The cheapest option is not always the best. You need to calculate the **cost-vs-accuracy tradeoff**.

---

## Part 4: All Benchmarking Metrics Explained (Simple Language)

### A. Accuracy Metrics

**WER (Word Error Rate) — The #1 Metric**
- The percentage of words the AI got wrong.
- Formula: WER = (Substitutions + Deletions + Insertions) / Total Reference Words
- Example:
  - Reference: "I want to apply for a credit card" (8 words)
  - AI Output: "I want two apply for credit card" (7 words)
  - Errors: "to" → "two" (1 substitution) + "a" was deleted (1 deletion) = 2 errors
  - WER = 2/8 = 25%
- **Lower WER = Better.** Top models achieve 3-5% on real-world audio.

**CER (Character Error Rate)**
- Same concept as WER, but counts individual characters instead of words.
- Critical for Indian languages like Hindi, Tamil, and Kannada where one wrong character can completely change the word's meaning.
- Example in Hindi: "करना" (to do) vs "कराना" (to get done) — a single character difference changes the meaning entirely.

**MER (Match Error Rate)**
- Similar to WER but bounded between 0% and 100% (WER can technically exceed 100% if the AI inserts many extra words).

**WIL (Word Information Lost)**
- Measures how much information was lost between what was said and what was transcribed.
- Considers both precision (did the AI add extra words?) and recall (did the AI miss words?).

**Entity Accuracy**
- Did the AI correctly transcribe specific important things like:
  - Phone numbers: "9876543210"
  - Account numbers: "HDFC0001234"
  - Currency amounts: "₹25,000"
  - Person names: "Poornesh"
  - Company names: "KreditBee"
- This matters more than overall WER in production. Getting an account number wrong is catastrophic even if every other word was perfect.

**LLM-WER (Semantic WER)**
- Standard WER is "dumb." It penalizes "22" vs "twenty two" as a massive error, even though they mean the exact same thing.
- LLM-WER uses an AI language model to judge whether the meaning was preserved, not just the surface words.
- This is especially important for Indian languages where the same word can be spelled differently in different scripts.

### B. Latency Metrics

**P50 (Median Latency)**
- 50% of requests were faster than this number.
- This represents the "average" user experience.
- Example: P50 = 800ms means half your users get a response in under 0.8 seconds.

**P95 (95th Percentile Latency)**
- 95% of requests were faster than this number.
- This represents the "worst-case" experience for most users.
- Example: P95 = 1700ms means only 5% of users wait longer than 1.7 seconds.
- **You must optimize for P95, not P50.** If your P50 is great but P95 is terrible, 1 in 20 users will have a horrible experience.

**P99 (99th Percentile Latency)**
- The absolute worst case (only 1% of users experience this).
- Important for enterprise SLAs and contract guarantees.

**RTF (Real-Time Factor)**
- Processing time divided by audio duration.
- RTF = 0.1 means the model transcribes 60 seconds of audio in just 6 seconds (10x faster than real-time).
- RTF must be < 1.0 for streaming (otherwise the model is slower than the person speaking).

**TTFP (Time to First Partial)**
- How many milliseconds until the very first word appears.
- For voice AI agents: must be under 250ms.
- For live captioning: can be up to 2 seconds.

---

## Part 5: The 3 Global Benchmarking Methodologies

We designed 3 different ways to test STT models, each answering a different question:

### Methodology 1: Controlled Benchmark (Scientific Baseline)
- **What it tests:** The model's pure capability under perfect conditions.
- **How:** Use studio-quality, clean audio with zero background noise.
- **Analogy:** Testing a car's top speed on a smooth, empty highway.
- **Question it answers:** "What is the absolute best this model can do?"
- **Metrics:** WER, CER, MER, WIL, Entity accuracy, Number accuracy.

### Methodology 2: Real-World Production Benchmark (Robustness)
- **What it tests:** How the model performs in actual production environments.
- **How:** Use audio with background noise, phone compression (8kHz), Indian accents, fast speech, interruptions, and poor network conditions.
- **Analogy:** Testing the car on a potholed road during a rainstorm.
- **Question it answers:** "How will this model perform in our actual call center?"
- **Metrics:** WER, Entity accuracy, Endpointing latency, Failure rate, Timeout rate, Throughput.

### Methodology 3: Adversarial/Failure Benchmark (Edge-Case Hunting)
- **What it tests:** Where exactly does each model break?
- **How:** Feed deliberately difficult audio: code-mixed speech ("nanage credit card apply madbeku"), financial numbers ("₹25,000 EMI"), rapid speech, self-corrections, and long silences.
- **Analogy:** Crash-testing the car by driving it into a wall.
- **Question it answers:** "What are the dangerous blind spots of this model?"
- **Metrics:** Number errors, Entity errors, Code-mix errors, Hallucinations, Endpoint errors.

---

## Part 6: Real-World Model Comparison (Verified Numbers)

These numbers come from independent benchmarks (Artificial Analysis, HuggingFace Open ASR Leaderboard, and provider documentation):

### Accuracy Comparison

| Model | Clean Audio WER | Real-World WER | Best For |
|-------|----------------|---------------|----------|
| **AssemblyAI Universal-3** | 2.1-2.8% | **3.1%** | Highest overall accuracy |
| **Azure Speech** | 2.0-3.0% | 3.8-6.5% | Enterprise + compliance |
| **OpenAI Whisper Large-v3** | 1.5-2.0% | 4.1-10.1% | Self-hosting + multilingual |
| **Deepgram Nova-3** | 2.5-3.5% | 5.2% | Real-time voice agents |
| **Google Chirp 2** | 3.0-4.2% | ~11.6% | Low-resource languages |
| **Sarvam Saaras v4** | 6.5-8.0% (Indic) | 16-19% (Indic) | Indian languages + code-mixing |

### Latency Comparison

| Model | Streaming Latency (TTFP) | Batch Speed | Streaming Support? |
|-------|------------------------|-------------|-------------------|
| **Deepgram Nova-3** | **150-280ms** | 500x+ real-time | ✅ True streaming |
| **AssemblyAI Universal-3** | 240-300ms | 50-80x real-time | ✅ True streaming |
| **Azure Speech** | 280-420ms | 30-50x real-time | ✅ True streaming |
| **Sarvam Saaras** | 300-450ms | 20x real-time | ✅ Streaming |
| **Google Chirp 2** | 350-600ms | High throughput | ✅ Streaming |
| **OpenAI Whisper** | N/A (batch only) | 4-25x real-time | ❌ Batch only |

### Cost Comparison

| Model | Cost per Hour | Cost per Minute | Self-Hostable? |
|-------|-------------|----------------|---------------|
| **Whisper Turbo (self-hosted)** | ~$0.06/hr | ~$0.001/min | ✅ Yes (free weights) |
| **Sarvam Saaras** | $0.36/hr (₹30/hr) | ~$0.006/min | ❌ Cloud API only |
| **OpenAI Whisper API** | $0.36/hr | $0.006/min | ❌ Cloud API |
| **AssemblyAI Universal-3** | $0.45/hr | $0.0075/min | ❌ Cloud API |
| **Deepgram Nova-3** | $0.46/hr | $0.0077/min | ❌ Cloud API |
| **Google Chirp 2** | $0.96/hr | $0.016/min | ❌ Cloud API |
| **Azure Speech** | $1.00/hr | $0.0167/min | ❌ Cloud API |

---

## Part 7: How to Evaluate STT for a Voice AI Agent

A Voice AI agent (like a phone banking bot) is the most demanding STT use case. Here is exactly what a good STT model must do:

### The Total Latency Budget
For a natural-sounding conversation, the total pipeline must respond within **700-900ms**:
```
User stops speaking
    ↓
STT Endpointing detects silence (target: 300ms)
    ↓
STT finalizes transcript (target: 200ms)
    ↓
LLM generates response (target: 200ms)
    ↓
TTS converts response to speech (target: 200ms)
    ↓
User hears the AI respond
```

If this total exceeds ~1 second, the conversation feels like a walkie-talkie.

### Critical Requirements for Voice AI

| Requirement | Why It Matters | Target |
|-------------|---------------|--------|
| Sub-300ms TTFP | AI can start processing intent immediately | < 250ms |
| Fast Endpointing | No awkward pauses after user stops talking | < 300ms |
| Barge-in Support | User can interrupt the AI mid-sentence | < 200ms |
| Telephony Audio (8kHz) | Phone calls use heavily compressed audio | WER < 15% |
| Number Accuracy | Account numbers, OTPs, phone numbers | > 95% |
| Code-Mix Support | Hindi-English switching in same sentence | Must work |
| Low Hallucination | AI should NOT generate fake words during silence | Zero tolerance |

### The Winner for Voice AI Agents: **Deepgram Nova-3**
- Sub-250ms true streaming
- Integrated end-of-turn detection (no separate VAD needed)
- Built for telephony audio
- Keyword boosting for custom terms

### For Indian Voice AI Agents: **Sarvam Saaras**
- Supports all 22 Indian languages
- Handles Hindi-English code-mixing natively
- 20-40% better than Whisper on Indian accents
- Affordable at ₹30/hour

---

## Part 8: Optimization Strategies

### A. How to Reduce Latency
1. **Edge VAD (Voice Activity Detection):** Cut out silence on the user's device before sending audio to the cloud. Less data = faster processing.
2. **Optimal Chunk Size:** Send audio in 200ms chunks. Too small (50ms) = network overhead. Too large (500ms) = delayed first response.
3. **Persistent Connections:** Use WebSockets or gRPC instead of HTTP. Avoids handshake overhead on every request.
4. **Connection Warming:** Keep the connection to the STT API open and ready, so there's zero delay when the user starts speaking.

### B. How to Improve Accuracy
1. **Custom Vocabulary:** Feed the model a list of domain-specific words (company names, product names, industry jargon).
2. **LLM Post-Processing:** Use a fast LLM to fix obvious STT errors before passing the transcript to your main AI.
3. **Multi-Model Ensemble:** Run two STT models simultaneously and pick the better result (expensive but effective for critical applications).

### C. How to Reduce Cost
1. **Hash Caching:** Don't re-process identical audio files. Store results and look them up by file fingerprint.
2. **Audio Compression:** Convert WAV files to FLAC or Opus (70% smaller, same quality).
3. **Tiered Processing:** Use a cheap/fast model for initial screening, and only send difficult samples to the expensive/accurate model.

---

## Part 9: The Decision Flowchart

```
What is your PRIMARY need?
│
├── "I need the fastest response for a voice agent"
│   └── → Deepgram Nova-3
│
├── "I need the highest accuracy for transcription"
│   └── → AssemblyAI Universal-3 Pro
│
├── "I need Indian language support"
│   └── → Sarvam Saaras v4
│
├── "I need to self-host for data privacy"
│   └── → OpenAI Whisper Large-v3 Turbo (on your own GPU)
│
├── "I need enterprise compliance (HIPAA/SOC2)"
│   └── → Azure Speech
│
└── "I need the cheapest option at scale"
    └── → Whisper Turbo (self-hosted, ~$0.06/hr)
```

---

## Part 10: Summary

| Question | Answer |
|----------|--------|
| Which model is most accurate? | AssemblyAI Universal-3 Pro (3.1% real-world WER) |
| Which model is fastest? | Deepgram Nova-3 (150ms streaming latency) |
| Which model is best for Indian languages? | Sarvam Saaras v4 (22 languages + code-mixing) |
| Which model is cheapest? | Whisper Turbo self-hosted (~$0.06/hr) |
| Which model is best for Voice AI agents? | Deepgram Nova-3 (streaming + endpointing + telephony) |
| Can I benchmark all of these myself? | Yes — using the framework we built in this repository |

> **Final Rule:** Never say "Model X is the best" without specifying the criteria. Different workloads produce different winners. Always benchmark on YOUR OWN audio data before making a production decision.

---

*This report was compiled from independent research across GitHub repositories (pipecat-ai/stt-benchmark, Picovoice/speech-to-text-benchmark, AI4Bharat/vistaar, sarvamai/llm_wer), the Artificial Analysis STT Leaderboard, HuggingFace Open ASR Leaderboard, and official provider documentation. All numbers reflect 2025-2026 verified data.*
