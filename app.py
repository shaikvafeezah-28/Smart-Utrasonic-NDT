import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Page settings
st.set_page_config(
    page_title="Smart Ultrasonic NDT",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Smart Ultrasonic NDT Inspection System")

st.write(
    "AI-Assisted Ultrasonic Signal Processing "
    "and Defect Detection"
)

st.divider()

# -----------------------------
# SELECT SPECIMEN CONDITION
# -----------------------------

condition = st.selectbox(
    "Select Specimen Condition",
    ["Normal", "Possible Defect"]
)

# -----------------------------
# GENERATE SIMULATED SIGNAL
# -----------------------------

time = np.linspace(0, 100, 1000)

# Small background noise
signal = 0.03 * np.random.randn(1000)

# Initial pulse
signal += 1.0 * np.exp(-((time - 10) / 1.5) ** 2)

# Back-wall echo
signal += 0.7 * np.exp(-((time - 80) / 2) ** 2)

# Add defect echo only for defect condition
if condition == "Possible Defect":
    signal += 0.8 * np.exp(-((time - 45) / 1.8) ** 2)

# -----------------------------
# PEAK DETECTION
# -----------------------------

peaks, properties = find_peaks(
    signal,
    height=0.25,
    distance=30
)

peak_times = time[peaks]
peak_amplitudes = signal[peaks]

# -----------------------------
# DISPLAY A-SCAN
# -----------------------------

st.subheader("📈 Ultrasonic A-Scan")

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(time, signal)

ax.plot(
    peak_times,
    peak_amplitudes,
    "x",
    markersize=10,
    label="Detected Peaks"
)

ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title("Ultrasonic A-Scan with Peak Detection")

ax.grid(True)
ax.legend()

st.pyplot(fig)

# -----------------------------
# DISPLAY PEAK INFORMATION
# -----------------------------

st.subheader("🔎 Detected Echoes")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Number of Peaks",
        len(peaks)
    )

with col2:
    if len(peaks) > 0:
        st.metric(
            "Maximum Amplitude",
            f"{max(peak_amplitudes):.2f}"
        )

# -----------------------------
# DEFECT INDICATION
# -----------------------------

if condition == "Possible Defect" and len(peaks) >= 3:

    st.warning(
        "⚠️ Possible defect indication detected"
    )


# PASTE NEW CODE HERE
st.subheader("🔍 Defect Analysis")

if condition == "Possible Defect" and len(peaks) >= 3:
    st.error("❌ Defect detected in specimen")

    st.write("The ultrasonic signal contains an additional echo.")
    st.write("This may indicate a possible internal defect.")

else:
    st.success("✅ No significant defect detected")

    st.write("The ultrasonic signal shows normal echo patterns.")
   # Find defect information only when enough peaks exist
if len(peaks) >= 3:
    defect_peak_index = np.argmax(
        peak_amplitudes[1:-1]
    ) + 1

    defect_position = peak_times[defect_peak_index]
    defect_amplitude = peak_amplitudes[defect_peak_index]
if condition == "Possible Defect" and len(peaks) >= 3:
    st.warning("⚠️ Possible defect indication detected")

    st.write(
        f"Defect position: {defect_position:.2f} time units"
    )

    st.write(
        f"Echo amplitude: {defect_amplitude:.2f}"
    )
else:
    st.success("🟢 No significant defect indication detected")