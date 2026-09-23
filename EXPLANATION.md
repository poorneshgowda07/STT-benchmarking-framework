# How Our STT Benchmarking System Works (Simple Explanation)

This document explains what our Speech-to-Text (STT) Benchmarking system does, step-by-step, in plain English. 

You can use this to explain the system to stakeholders, product managers, or other engineers.

---

### 1. The Core Purpose
- **What it does:** It automatically tests different Voice AI models (like OpenAI Whisper, Google Chirp, Deepgram, Sarvam) to see which one performs the best.
- **Why we built it:** To make data-driven decisions instead of guessing. It tells us exactly which model is the most accurate, the fastest, and the most cost-effective for our specific use cases (e.g., Indian languages, noisy audio, or fast speech).

### 2. How the Testing Pipeline Works (Step-by-Step)
When we run a benchmark, the system follows this exact process:

- **Step 1: Dataset Validation**
  - We feed the system audio files and the "ground truth" (what was actually spoken).
  - The system checks that every file is valid and has all necessary details (like language, accent, and environment).

- **Step 2: Hashing (Tamper-Proofing)**
  - Every audio file gets a unique digital fingerprint (SHA-256 hash). 
  - *Why?* This proves that we ran the test on the exact same audio every time, making our tests 100% scientifically reproducible.

- **Step 3: The Race (Benchmarking Engine)**
  - The system sends the same audio file to all the different AI providers (Google, OpenAI, etc.) at the same time.
  - It records exactly what the AI transcribed and exactly how many milliseconds it took to respond.

- **Step 4: Metric Calculation (Scoring)**
  - The system compares the AI's answer to the real answer.
  - It calculates the **WER (Word Error Rate)** — the percentage of words the AI got wrong (inserted, deleted, or substituted).
  - It calculates **Latency percentiles (P50, P95)** — telling us how fast the system is for the average user vs. the slowest 5% of users.

- **Step 5: Evidence Collection**
  - Instead of just giving a number, the system saves the "receipts".
  - If an AI model fails terribly on a file, the system saves the audio, what the AI guessed, and the exact error. 
  - *Why?* So we can manually listen and understand *why* the AI failed (e.g., it couldn't understand a heavy accent).

### 3. How the Results are Presented
After the race is over, the system automatically generates:

- **Individual Scorecards:** A detailed report card for each individual AI model (e.g., "Whisper got 95% accuracy and took 2 seconds").
- **The Leaderboard:** A simple spreadsheet (CSV) ranking all the models from best to worst.
- **The Final Report:** A readable document (Markdown/HTML) summarizing the winners, the losers, and the specific areas where models failed.

### 4. Key Engineering Benefits
- **No Secret Cheating:** The raw responses from the AI providers are permanently saved. Nobody can tweak the numbers later.
- **Modular Design:** If a new AI startup launches tomorrow, we don't have to rebuild the whole system. We just add a small "adapter" for them and run the race again.
- **Offline Mocking:** Developers can test the pipeline on their local laptops using fake data without spending a single dollar on real API credits.

### 5. Summary
Think of this system as an automated race track for Voice AI. We provide the track (audio) and the stopwatch. The AI models run the race, and our system automatically hands out the medals and writes the sports report.
