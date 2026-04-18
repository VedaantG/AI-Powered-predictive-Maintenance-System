🔧 AI-Powered Predictive Maintenance System for IoT Devices

📌 Overview

This project implements an AI-based predictive maintenance system using simulated IoT sensor data.
The system predicts potential machine failures in advance, enabling proactive maintenance and reducing unexpected downtime.

It is designed to reflect real-world industrial use cases in manufacturing, automotive, and energy sectors.

---

🎯 Problem Statement

Traditional maintenance strategies are either:

- Reactive (fix after failure) → costly downtime
- Preventive (scheduled maintenance) → inefficient

This project solves the problem by:

Predicting machine failures using sensor data and machine learning.

---

🏭 Industry Relevance

Predictive maintenance is widely used in:

- Manufacturing plants
- Power plants
- Automotive systems
- Aviation engines

Business Impact:

- ⬇ Downtime
- ⬇ Maintenance cost
- ⬆ Equipment lifespan
- ⬆ Operational efficiency

---

⚙️ Tech Stack

- Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- Model: Random Forest Classifier
- Tools: Git, GitHub

---

📊 Dataset

- Dataset Used: AI4I 2020 Predictive Maintenance Dataset
- Type: Simulated IoT sensor data

Features:

- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Machine type

Target:

- "Machine failure" (0 = Normal, 1 = Failure)

---

🧠 Project Workflow

Sensor Data → Preprocessing → Feature Engineering → Model Training → Prediction → Evaluation → Visualization

---

🏗️ System Architecture

[IoT Sensor Data]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
[Data Preprocessing]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
[Feature Selection]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
[ML Model (Random Forest)]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
[Failure Prediction]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
[Alert System + Visualization]

---

🔧 Model Optimization (Key Highlight)

Initial model showed:

- High accuracy
- Poor failure detection (low recall)

Solution: Threshold Tuning

Threshold| Recall| Precision<br>
&nbsp;0.5 &nbsp;|&nbsp;59%&nbsp;|&nbsp;86%<br>
&nbsp;0.3 &nbsp;|&nbsp;69%&nbsp;|&nbsp;70%<br>
&nbsp;0.2 &nbsp;|&nbsp;75%&nbsp;|&nbsp;58%<br>

Insight:

«Lowering the threshold improved failure detection significantly.»

Engineering Decision:

In predictive maintenance:

- Missing a failure (False Negative) is more costly than false alarms
- Hence, the model was optimized for higher recall

---

📈 Results

- Accuracy: ~97%
- Recall (Failure Detection): ~75%
- Precision: ~58%

Key Outcome:

- Significant reduction in missed failures
- Improved reliability of failure prediction

---

📊 Visual Outputs

- Confusion Matrix
- Feature Importance Graph

(Stored in "/images/" folder)

---

🚀 Installation & Setup

git clone https://github.com/your-username/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

---

▶️ How to Run

python main.py

---

📁 Project Structure

AI-Predictive-Maintenance-IoT/<br>
│<br>
├── data/<br>
├── src/<br>
├── models/<br>
├── images/<br>
├── outputs/<br>
├── README.md<br>
├── requirements.txt<br>
└── main.py

---

🧪 Key Learnings

- Handling imbalanced datasets
- Importance of recall vs accuracy
- Real-world cost-sensitive ML decisions
- Building modular ML pipelines
- Applying ML to industrial IoT problems

---

🔥 Future Improvements

- Add time-series modeling (LSTM)
- Deploy dashboard using Streamlit
- Real-time IoT data simulation
- Multi-class failure prediction

---

🤝 Contributing

Feel free to fork and improve the project.

---

📌 Author

Vedaant Gaonkar<br>
[Github](https://github.com/VedaantG)<br>
[LinkedIn](https://www.linkedin.com/in/vedaant-gaonkar-452618352)

---

⭐ Final Note

This project focuses on practical industry application of machine learning, not just achieving high accuracy, but making meaningful engineering decisions.