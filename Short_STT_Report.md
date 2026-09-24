# STT Model Benchmarking Report

---

## Phase 1: Best GitHub Tools for STT Benchmarking

| Tool | Link | Purpose |
|------|------|---------|
| pipecat-ai/stt-benchmark | [GitHub](https://github.com/pipecat-ai/stt-benchmark) | Built for Voice AI agents. Measures latency + semantic WER. |
| Picovoice/speech-to-text-benchmark | [GitHub](https://github.com/Picovoice/speech-to-text-benchmark) | Compares cloud STT APIs (Google, Azure, Whisper, AWS). |
| HuggingFace Open ASR Leaderboard | [HuggingFace](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) | Industry-standard accuracy leaderboard. |
| AI4Bharat/vistaar | [GitHub](https://github.com/AI4Bharat/vistaar) | Indian language STT benchmark (12 languages). |

---

## Phase 2: Components of a Good STT Model

1. **Accuracy** — Low WER on clean and noisy audio.
2. **Latency** — First word appears in under 300ms.
3. **Streaming** — Real-time word-by-word output (not batch).
4. **Language Support** — Supports your target languages + code-mixing.
5. **Speaker Diarization** — Identifies "who said what."
6. **Text Formatting** — Auto punctuation, capitalization, number formatting.
7. **Custom Vocabulary** — Boost recognition of brand names / domain terms.
8. **Cost** — Affordable per-minute pricing at your scale.

---

## Phase 3: Key Benchmarking Metrics

| Metric | What It Measures |
|--------|-----------------|
| **WER** | % of words transcribed incorrectly |
| **CER** | % of characters wrong (critical for Indian languages) |
| **TTFP** | Time until first word appears (ms) |
| **P95 Latency** | Worst-case response time for 95% of users |
| **RTF** | Processing speed vs audio duration |
| **Entity Accuracy** | Did it get names, numbers, dates right? |
| **DER** | Speaker diarization accuracy |

---

## Phase 4: Which STT to Use for Each Application

| Application | What Matters Most | Best Model |
|-------------|------------------|------------|
| **Voice AI Agent** | Sub-300ms latency + endpointing + telephony audio | **Deepgram Nova-3** |
| **Indian Voice AI** | Code-mixing + Indic languages | **Sarvam Saaras v4** |
| **Batch Transcription** | Highest accuracy | **AssemblyAI Universal-3** (3.1% WER) |
| **Medical/Legal** | Compliance + custom vocabulary | **Azure Speech** |
| **Self-Hosted/Private** | Data sovereignty + no vendor lock-in | **Whisper Turbo** (free, runs on your GPU) |
| **Live Captioning** | Low flicker + good punctuation | **AssemblyAI Universal-3** |

---

## Phase 5: Real-World Model Numbers

| Model | Real-World WER | Streaming Latency | Cost/hr |
|-------|---------------|-------------------|---------|
| AssemblyAI Universal-3 | **3.1%** | 240-300ms | $0.45 |
| Deepgram Nova-3 | 5.2% | **150-280ms** | $0.46 |
| Whisper Large-v3 | 4.1-10.1% | ❌ Batch only | $0.36 |
| Google Chirp 2 | ~11.6% | 350-600ms | $0.96 |
| Sarvam Saaras v4 | 16% (Indic) | 300-450ms | $0.36 |
| Azure Speech | 3.8-6.5% | 280-420ms | $1.00 |

---

## Phase 6: Voice AI Agent — How Should STT Perform?

Total response budget for natural conversation: **< 900ms**

| Step | Target |
|------|--------|
| Endpointing (detect user stopped) | < 300ms |
| Transcript finalization | < 200ms |
| LLM generates reply | < 200ms |
| TTS speaks reply | < 200ms |

**Winner for Voice AI:** Deepgram Nova-3 (fastest streaming + built-in end-of-turn detection)
**Winner for Indian Voice AI:** Sarvam Saaras (22 languages + code-mixing)
