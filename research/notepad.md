# Project Progress and Exploration Notes

### **Progress So Far**

1. **Understanding PPG Signals**

   - Explored what Photoplethysmography (PPG) signals are and how they work.
   - Learned that PPG signals measure blood volume changes in microvascular tissue using light absorption.

2. **Heart Rate Variability (HRV)**

   - Investigated HRV, its significance, and how to interpret it as a marker of physiological and emotional health.
   - Learned that HRV measures the variation in time between successive heartbeats (R-R or N-N intervals).

3. **Connecting PPG and HRV**

   - Explored methods to derive HRV from PPG signals.
   - Realized that PPG can be an accessible alternative to ECG for HRV analysis, though it comes with challenges (e.g., noise).

4. **Effects of HRV on Health and Wellness**

   - Discovered how HRV serves as a proxy for overall health:
     - **Low HRV**: Indicates stress, fatigue, or an overactive **Sympathetic Nervous System (SNS)** (fight-or-flight).
     - **High HRV**: Linked to relaxation, recovery, and an active **Parasympathetic Nervous System (PNS)** (rest-and-digest).

5. **PPG Signal Noise and Challenges**

   - Identified common types of noise in PPG signals (motion artifacts, ambient light interference, and signal drift).
   - Researched methods to clean PPG data, including filtering techniques and signal preprocessing.

6. **Extracting HRV Features**

   - Explored key HRV metrics derived from PPG:
     - **NN intervals**: Time between successive beats.
     - **RMSSD**: Root mean square of successive differences, representing short-term variability.
     - **SDNN**: Standard deviation of NN intervals, reflecting overall HRV.

7. **Initial Hypothesis**

   - Formulated a hypothesis: "HRV decreases during stress and increases during relaxation."
   - Conducted a basic comparison of HRV data between high-stress and low-stress situations.

8. **Windowed Signal Analysis**
   - Used different signal window lengths (10, 20, 30 seconds) to observe how stress affects HRV metrics over short intervals.

---

### **Future Explorations**

1. **Deep Dive into Stress and HRV**

   - Further validate the relationship between HRV and stress using larger datasets.
   - Examine how various stress types (e.g., cognitive vs. physical) affect HRV differently.

2. **Refining Noise Handling Techniques**

   - Explore advanced denoising methods like adaptive filtering or machine-learning-based noise removal.
   - Test the impact of noise handling on HRV accuracy.

3. **Feature Engineering for HRV**

   - Investigate additional HRV features, such as Poincaré plot indices, LF/HF ratio, and spectral analysis.

4. **Linking HRV to the Nervous System**

   - Clarify the role of SNS vs. PNS in modulating HRV during stress and relaxation.
   - Examine whether specific HRV patterns can indicate a shift in nervous system dominance.

5. **Dataset-Specific Hypotheses**

   - Test hypotheses on curated datasets to study:
     - Stress response over long-term vs. short-term periods.
     - HRV patterns across different demographics (e.g., age, fitness level).

6. **Explore Other Health Correlations**

   - Investigate HRV relationships with sleep quality, mental health, or chronic conditions.

7. **Visualization and Reporting**
   - Develop intuitive visualizations to compare HRV patterns across different scenarios.
   - Document findings in an accessible format for presentations and reports.
