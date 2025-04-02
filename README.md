# 🔮 Demand Forecasting App

A powerful Streamlit-based web application for demand forecasting that combines the strengths of Prophet and N-Beats models, enhanced with Gemini AI for intelligent pattern detection and analysis.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.10+-ff4b4b.svg)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://www.tensorflow.org/)

## ✨ Features

- **🔄 Multi-Model Forecasting**:
  - **Prophet**: Meta's time series forecasting tool that handles seasonality and holiday effects
  - **N-Beats**: Deep neural architecture specifically designed for time series forecasting with interpretable outputs

- **📊 Interactive Analysis**:
  - Upload CSV files with historical sales data
  - Visualize forecasts with interactive charts
  - Compare different forecasting models

- **🤖 AI-Powered Insights**:
  - Gemini Bot for image-based trend analysis (forecast visualizations)
  - Gemini Bot for data-based Q&A (CSV analysis)

- **💾 Export Options**:
  - Download forecasts as CSV
  - Save forecast visualizations as images

## 🧠 Understanding the Models

### Prophet
Prophet is a forecasting procedure developed by Meta (formerly Facebook) that:
- Automatically detects seasonal patterns (daily, weekly, yearly)
- Handles missing data and outliers gracefully
- Accommodates holiday effects and special events
- Uses a decomposable model with trend, seasonality, and holiday components
- Is particularly effective for business forecasting with multiple seasonalities

### N-Beats (Neural Basis Expansion Analysis for Time Series)
N-Beats is a deep learning approach that:
- Uses deep neural networks specifically designed for time series
- Provides interpretable forecasts through trend and seasonality decomposition
- Often outperforms traditional statistical methods for complex patterns
- Can capture non-linear relationships in your data
- Works well even with limited historical data

## 🛠️ Tech Stack

- **Backend**: Python
- **ML Models**: Prophet, N-Beats (TensorFlow/Keras)
- **AI Integration**: Google Gemini API
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib

## 🎬 Demo

https://github.com/user-attachments/assets/9fc5bf11-8f60-4780-8e4d-2280cb09943a

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/demand-forecasting-app.git
   cd demand-forecasting-app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

5. **Run the application**:
   ```bash
   streamlit run multipage.py
   ```

## 🚀 Usage

### Generate Forecasts
1. Upload a CSV file with `Date` and `Sales` columns
2. Select forecast end date
3. Choose between Prophet or N-Beats model
4. View and download forecasts

### Chat with Image
1. Upload forecast visualization images
2. Get AI-powered analysis of trends and patterns

### Chat with Data
1. Upload your sales data (CSV or Excel)
2. Ask questions about trends, anomalies, and insights

## 📋 Data Requirements

CSV files must contain:
- A `Date` column (formats supported: `DD-MM-YYYY`, `MM/DD/YYYY`, etc.)
- A `Sales` column with numerical values

<details>
<summary>📝 Example CSV format</summary>

```
Date,Sales
01/01/2023,100
01/02/2023,150
01/03/2023,200
```
</details>

## 📂 File Structure

<details>
<summary>View project structure</summary>

```
demand-forecasting-app/
├── main.py               # Main forecasting functionality
├── multipage.py          # Multi-page app configuration
├── image_bot.py          # Image analysis with Gemini
├── data_bot.py           # Data analysis with Gemini
├── prophet_script.py     # Prophet model utilities
├── nbeats.py             # N-Beats model implementation
├── .env.example          # Environment variables template
├── requirements.txt      # Dependencies
└── README.md             # This file
```
</details>

## 📸 Screenshots

<details>
<summary><b>Project Map</b></summary>
<img src="https://github.com/user-attachments/assets/699243ba-465e-47af-a561-7d7456fcbd18" alt="Project Map">
</details>

<details>
<summary><b>Forecast Generation</b></summary>
<img src="https://github.com/user-attachments/assets/5d3a5260-3089-4aac-99e1-493d0ca1b7bb" alt="Forecast Generation">
<img src="https://github.com/user-attachments/assets/85ba92e6-7a27-49f4-b494-257c38933e2c" alt="Forecast Output">
<img src="https://github.com/user-attachments/assets/cdda008e-a14e-4c1f-9151-dd4f83ec7d12" alt="Forecast Details">
<img src="https://github.com/user-attachments/assets/fd6964b5-fbf3-4f96-916f-8947d5982c57" alt="Additional View">
<img src="https://github.com/user-attachments/assets/b30650ee-389b-4aab-8acf-b64bd1cea4b8" alt="Results View">
</details>

<details>
<summary><b>Graph Analysis</b></summary>
<img src="https://github.com/user-attachments/assets/93a0b02d-7b25-446b-a851-e58b51989500" alt="Image Analysis">
</details>

<details>
<summary><b>Data Analysis</b></summary>
<img src="https://github.com/user-attachments/assets/d58a26d3-34fb-4931-a439-29af9f4a7201" alt="Data Chat">
<img src="https://github.com/user-attachments/assets/447374a1-06a8-48fd-b0ae-15bd25d842da" alt="Analysis View">
</details>

## 🤔 When to Use Each Model

| Factor | Prophet | N-Beats |
|--------|---------|---------|
| **Data Size** | Works well with limited data | Better with more historical data |
| **Seasonality** | Excellent at detecting multiple seasonal patterns | Good for complex, non-linear seasonality |
| **Noise Handling** | Robust to missing data and outliers | May need cleaner data |
| **Computation** | Faster training | More computationally intensive |
| **Best For** | Business data with clear seasonal patterns | Complex relationships and patterns |

## 👤 Author

For any questions or issues, please open an issue on GitHub: [@Siddharth Mishra](https://github.com/Sid3503)

---

<p align="center">
  Made with ❤️ and lots of ☕
</p>
