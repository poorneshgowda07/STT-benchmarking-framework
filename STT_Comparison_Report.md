# Which STT Model Should You Use? — A Complete Comparison

---

## What Makes a Good STT Model?

Every STT model is judged on these 8 things:

| # | Component | Simple Meaning |
|---|-----------|---------------|
| 1 | **Accuracy (WER)** | How many words it gets right. Lower WER = better. |
| 2 | **Speed (Latency)** | How fast the first word appears after you speak. |
| 3 | **Streaming** | Can it give you words in real-time while the person is still talking? |
| 4 | **Language Support** | How many languages it understands. Can it handle Hindi+English mixed? |
| 5 | **Speaker Diarization** | Can it tell apart "who said what" in a conversation? |
| 6 | **Text Formatting** | Does it auto-add punctuation, capitalize names, format numbers? |
| 7 | **Custom Vocabulary** | Can you teach it your brand names and special terms? |
| 8 | **Cost** | How much it charges per minute of audio. |

---

## What Are the Benchmarking Metrics?

These are the "tests" we run on every STT model:

| Metric | What It Means | Good Score | Bad Score |
|--------|--------------|------------|-----------|
| **WER (Word Error Rate)** | % of words the AI got wrong | Below 5% | Above 15% |
| **CER (Character Error Rate)** | % of characters wrong (important for Hindi, Tamil) | Below 3% | Above 10% |
| **TTFP (Time to First Partial)** | Milliseconds until the first word appears | Under 300ms | Over 600ms |
| **P95 Latency** | Response time for the slowest 5% of users | Under 500ms | Over 1500ms |
| **Entity Accuracy** | Did it get names, phone numbers, amounts right? | Above 95% | Below 80% |
| **RTF (Real-Time Factor)** | How fast it processes audio (lower = faster) | Below 0.1 | Above 1.0 |
| **DER (Diarization Error Rate)** | How accurately it identifies different speakers | Below 15% | Above 30% |

---

## Model-by-Model Breakdown (Zero to Hero)

### 1. Deepgram Nova-3

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | 5.2% | ✅ Good |
| Streaming Latency (TTFP) | 150-280ms | ✅ Excellent — Fastest in the market |
| Streaming Support | True real-time streaming | ✅ Yes |
| Endpointing (detecting user stopped) | Built-in (Flux engine) | ✅ Excellent — No extra tool needed |
| Language Support | 30+ languages | ⚠️ Decent but weaker on Indian languages |
| Code-Mixing (Hindi+English) | Limited | ❌ Not its strength |
| Speaker Diarization | Yes | ✅ Good |
| Custom Vocabulary (Keyword Boost) | Yes — very strong | ✅ Excellent |
| Text Formatting | Auto punctuation + capitalization | ✅ Good |
| Telephony (Phone call audio) | Specifically built for it | ✅ Excellent |
| Hallucination (fake words in silence) | Very low | ✅ Good |
| Cost | $0.46/hr ($0.0077/min) | ⚠️ Mid-range |

**Best For:** Real-time voice AI agents, call centers, telephony.
**Weak At:** Indian languages, code-mixing.
**Overall Rating: 8.5/10**

---

### 2. AssemblyAI Universal-3

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | 3.1% | ✅ Best accuracy in the market |
| Streaming Latency (TTFP) | 240-300ms | ✅ Good |
| Streaming Support | True streaming via WebSocket | ✅ Yes |
| Endpointing | Available | ✅ Good |
| Language Support | 20+ languages | ⚠️ Decent |
| Code-Mixing (Hindi+English) | Limited | ❌ Not its strength |
| Speaker Diarization | Yes — very accurate | ✅ Excellent |
| Custom Vocabulary | Yes | ✅ Good |
| Text Formatting | Excellent punctuation + casing + number formatting | ✅ Excellent |
| Telephony | Good | ✅ Good |
| Hallucination | Very low | ✅ Excellent |
| Extra Features | Sentiment analysis, summarization, PII redaction | ✅ Bonus |
| Cost | $0.45/hr ($0.0075/min) | ⚠️ Mid-range |

**Best For:** Batch transcription, meeting notes, analytics, highest accuracy needs.
**Weak At:** Not the fastest for real-time voice agents, limited Indian language support.
**Overall Rating: 9/10**

---

### 3. OpenAI Whisper Large-v3

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | 4.1-10.1% (varies by domain) | ⚠️ Inconsistent |
| Streaming Latency (TTFP) | No native streaming (batch only) | ❌ Bad for real-time |
| Streaming Support | No — must use workarounds (chunked) | ❌ No |
| Endpointing | None built-in | ❌ Not available |
| Language Support | 99+ languages | ✅ Excellent — Best multilingual coverage |
| Code-Mixing (Hindi+English) | Moderate | ⚠️ OK but not great |
| Speaker Diarization | No | ❌ Not available |
| Custom Vocabulary | No keyword boosting | ❌ Not available |
| Text Formatting | Basic | ⚠️ OK |
| Telephony | Struggles with 8kHz audio | ❌ Weak |
| Hallucination | Known problem — generates fake words during silence | ❌ Bad |
| Self-Hosting | Free weights, run on your own GPU | ✅ Excellent |
| Cost (API) | $0.36/hr ($0.006/min) | ✅ Cheap |
| Cost (Self-hosted) | ~$0.06/hr | ✅ Very cheap |

**Best For:** Self-hosting, offline use, privacy-sensitive apps, multilingual.
**Weak At:** Real-time streaming, telephony, hallucinations, no diarization.
**Overall Rating: 6.5/10**

---

### 4. OpenAI Whisper Turbo

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | ~7.7% | ⚠️ Slightly worse than Large-v3 |
| Speed | 4x faster than Large-v3 | ✅ Great |
| Streaming Support | No (batch only) | ❌ No |
| Language Support | 99+ languages | ✅ Excellent |
| Self-Hosting | Free weights, smaller model, faster | ✅ Best for self-hosting |
| Hallucination | Same issue as Large-v3 | ❌ Bad |
| Cost (Self-hosted) | ~$0.06/hr | ✅ Cheapest option |

**Best For:** High-volume batch processing on your own servers.
**Weak At:** Same weaknesses as Large-v3 but trades accuracy for speed.
**Overall Rating: 6/10**

---

### 5. Google Chirp 2

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | ~11.6% | ❌ Below average |
| Streaming Latency (TTFP) | 350-600ms | ❌ Slow |
| Streaming Support | Yes (StreamingRecognize) | ✅ Yes |
| Language Support | 100+ languages including rare ones | ✅ Best for rare/low-resource languages |
| Code-Mixing | Moderate | ⚠️ OK |
| Speaker Diarization | Yes | ✅ Good |
| Custom Vocabulary | Yes (Speech Adaptation) | ✅ Good |
| Text Formatting | Good | ✅ Good |
| Cost | $0.96/hr ($0.016/min) | ❌ Expensive |

**Best For:** Rare languages, Google Cloud ecosystem users.
**Weak At:** Accuracy is behind competitors, slow latency, expensive.
**Overall Rating: 5.5/10**

---

### 6. Sarvam Saaras v4

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER (Indian languages) | 16-19% | ⚠️ Higher WER but best among all for Indic |
| Indian Language Support | All 22 Indian languages | ✅ Unmatched |
| Code-Mixing (Hindi+English, Kannada+English) | Native support | ✅ Excellent — Best in the market |
| Streaming Latency | 300-450ms | ⚠️ Decent |
| Streaming Support | Yes | ✅ Yes |
| Speaker Diarization | Yes | ✅ Good |
| English Accuracy | Below Western models | ❌ Not its focus |
| Custom Vocabulary | Limited | ⚠️ Basic |
| Text Formatting | Good for Indic scripts | ✅ Good |
| Cost | $0.36/hr (₹30/hr) | ✅ Affordable |

**Best For:** Indian language apps, Hinglish/Kanglish code-mixing, Indian call centers.
**Weak At:** Pure English accuracy, custom vocabulary options.
**Overall Rating: 7/10 (for Indian use cases) | 4/10 (for English-only)**

---

### 7. Microsoft Azure Speech

| Category | Score / Detail | Verdict |
|----------|---------------|---------|
| Real-World WER | 3.8-6.5% | ✅ Very good |
| Streaming Latency (TTFP) | 280-420ms | ✅ Good |
| Streaming Support | Yes (WebSocket/gRPC) | ✅ Yes |
| Language Support | 100+ languages | ✅ Excellent |
| Speaker Diarization | Yes | ✅ Good |
| Custom Vocabulary (Phrase List) | Best in industry | ✅ Excellent |
| Text Formatting | Excellent | ✅ Excellent |
| Compliance (HIPAA, SOC2, GDPR) | Full enterprise compliance | ✅ Best |
| Cost | $1.00/hr ($0.0167/min) | ❌ Most expensive |

**Best For:** Enterprise, healthcare (HIPAA), legal, Microsoft Teams integration.
**Weak At:** Expensive, not the fastest.
**Overall Rating: 8/10**

---

## Quick Comparison: All Models Side by Side

| Model | Accuracy (WER) | Speed (TTFP) | Streaming | Indian Languages | Cost/hr | Best Use Case |
|-------|---------------|-------------|-----------|-----------------|---------|--------------|
| **AssemblyAI Universal-3** | ⭐ 3.1% | 240-300ms | ✅ | ❌ | $0.45 | Best accuracy |
| **Deepgram Nova-3** | 5.2% | ⭐ 150ms | ✅ | ❌ | $0.46 | Fastest (Voice AI) |
| **Azure Speech** | 3.8-6.5% | 280-420ms | ✅ | ⚠️ | $1.00 | Enterprise/Compliance |
| **Whisper Large-v3** | 4.1-10% | ❌ Batch | ❌ | ⚠️ | $0.36 | Self-hosting |
| **Sarvam Saaras v4** | 16% (Indic) | 300-450ms | ✅ | ⭐ Best | $0.36 | Indian languages |
| **Google Chirp 2** | ~11.6% | 350-600ms | ✅ | ⚠️ | $0.96 | Rare languages |

---

## For a Voice AI Agent — What Should STT Do?

A voice AI agent (like a phone banking bot) needs the total conversation response in under 900ms:

| Step | What Happens | Time Budget |
|------|-------------|-------------|
| User stops speaking | STT detects silence (endpointing) | < 300ms |
| Transcript is finalized | STT locks the final text | < 200ms |
| AI generates a reply | LLM processes and responds | < 200ms |
| AI speaks the reply | TTS converts text to voice | < 200ms |

**Which STT wins for Voice AI?**
- **English calls:** Deepgram Nova-3 (fastest streaming + built-in endpointing)
- **Indian language calls:** Sarvam Saaras (code-mixing + Indic support)
- **Highest accuracy needed:** AssemblyAI Universal-3

---

## Final Verdict: Is There a 100% Perfect STT?

**No.** No STT model gives 100% accuracy in all scenarios. Here is the honest truth:

| If You Need... | Use This Model | Why |
|----------------|---------------|-----|
| Best overall accuracy | AssemblyAI Universal-3 | 3.1% WER — lowest error rate |
| Fastest real-time response | Deepgram Nova-3 | 150ms — nobody is faster |
| Indian languages + code-mixing | Sarvam Saaras v4 | Only model built specifically for India |
| Full data privacy (self-hosted) | Whisper Turbo | Free, runs on your own GPU |
| Enterprise compliance (HIPAA) | Azure Speech | Best security certifications |
| Cheapest at scale | Whisper Turbo (self-hosted) | ~$0.06/hr |

> **The right STT depends on YOUR use case.** There is no single winner. But if forced to pick ONE for general English use: **AssemblyAI Universal-3** has the best balance of accuracy, speed, and features.
