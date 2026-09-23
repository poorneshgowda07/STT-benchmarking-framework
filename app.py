import streamlit as st
import pandas as pd
import json
import os
import glob

st.set_page_config(page_title="STT Benchmarking", layout="wide")

st.title("🎙️ Speech-to-Text (STT) Benchmarking Dashboard")
st.markdown("Explore the performance, latency, and failure evidence of various Voice AI models.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "benchmarks", "results")
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence", "errors")

@st.cache_data
def load_data():
    scorecards = []
    scorecard_files = glob.glob(os.path.join(RESULTS_DIR, "*_scorecard.json"))
    for file in scorecard_files:
        with open(file, 'r', encoding='utf-8') as f:
            scorecards.append(json.load(f))
            
    evidence_data = {}
    evidence_files = glob.glob(os.path.join(EVIDENCE_DIR, "*_evidence.json"))
    for file in evidence_files:
        model_id = os.path.basename(file).replace("_evidence.json", "")
        with open(file, 'r', encoding='utf-8') as f:
            evidence_data[model_id] = json.load(f)
            
    return scorecards, evidence_data

scorecards, evidence_data = load_data()

if not scorecards:
    st.warning("No benchmark results found. Please run the benchmarking pipeline first.")
    st.stop()

# --- LEADERBOARD ---
st.header("🏆 Global Leaderboard")
leaderboard_data = []
for sc in scorecards:
    leaderboard_data.append({
        "Model": sc["model_id"],
        "Average WER": f"{sc['accuracy']['average_wer']:.1%}",
        "Average CER": f"{sc['accuracy']['average_cer']:.1%}",
        "P50 Latency (ms)": round(sc["latency"]["p50"], 2),
        "P95 Latency (ms)": round(sc["latency"]["p95"], 2)
    })

df = pd.DataFrame(leaderboard_data).sort_values(by="Average WER")
st.dataframe(df, use_container_width=True)

st.divider()

# --- MODEL DEEP DIVE ---
st.header("🔍 Model Deep Dive & Evidence")

model_names = [sc["model_id"] for sc in scorecards]
selected_model = st.selectbox("Select a model to explore:", model_names)

# Get selected model data
selected_scorecard = next(sc for sc in scorecards if sc["model_id"] == selected_model)
selected_evidence = evidence_data.get(selected_model, {"successes": [], "failures": []})

col1, col2, col3 = st.columns(3)
col1.metric("Samples Evaluated", selected_scorecard["total_samples_evaluated"])
col2.metric("Average WER", f"{selected_scorecard['accuracy']['average_wer']:.1%}")
col3.metric("P95 Latency", f"{selected_scorecard['latency']['p95']:.2f} ms")

st.subheader("⚠️ Error Evidence (Failures)")
if selected_evidence["failures"]:
    for fail in selected_evidence["failures"]:
        with st.expander(f"Sample: {fail['sample_id']} (WER: {fail['wer']:.1%})"):
            st.error(f"**Error Type:** {fail.get('error_type', 'Unknown')} - Severity: {fail.get('severity', 'Unknown')}")
            st.markdown(f"**✅ Expected (Reference):** `{fail['reference']}`")
            st.markdown(f"**❌ Predicted (Hypothesis):** `{fail['prediction']}`")
            # In a real app, you could load the audio file here using st.audio()
else:
    st.success("No major failures found for this model in the current evidence log.")

st.subheader("✅ Perfect Transcriptions (Successes)")
if selected_evidence["successes"]:
    for succ in selected_evidence["successes"]:
        with st.expander(f"Sample: {succ['sample_id']}"):
            st.markdown(f"**Transcript:** `{succ['prediction']}`")
else:
    st.info("No perfect successes logged in evidence.")
