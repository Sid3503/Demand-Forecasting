# Demand Forecasting App 📊

A Streamlit-based web application for demand forecasting using Prophet and N-Beats models, enhanced with Gemini AI for pattern detection and analysis.

## Features ✨

- **Multi-Model Forecasting**:
  - Facebook's Prophet model for time series forecasting
  - N-Beats neural network for deep learning-based predictions
- **Interactive Analysis**:
  - Upload CSV files with historical sales data
  - Visualize forecasts with interactive charts
- **AI-Powered Insights**:
  - Gemini Bot for image-based trend analysis (forecast visualizations)
  - Gemini Bot for data-based Q&A (CSV analysis)
- **Export Options**:
  - Download forecasts as CSV
  - Save forecast visualizations as images

## Tech Stack 🛠️

- **Backend**: Python
- **ML Models**: Prophet, N-Beats (TensorFlow/Keras)
- **AI Integration**: Google Gemini API
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib

## Walkthrough

https://github.com/user-attachments/assets/9fc5bf11-8f60-4780-8e4d-2280cb09943a

## Installation ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/demand-forecasting-app.git
   cd demand-forecasting-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

5. Run the application:
   ```bash
   streamlit run multipage.py
   ```

## Usage 🚀

1. **Generate Forecasts**:
   - Upload a CSV file with `Date` and `Sales` columns
   - Select forecast end date
   - Choose between Prophet or N-Beats model
   - View and download forecasts

2. **Chat with Image**:
   - Upload forecast visualization images
   - Get AI-powered analysis of trends and patterns

3. **Chat with Data**:
   - Upload your sales data (CSV or Excel)
   - Ask questions about trends, anomalies, and insights

## File Structure 📂

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

## Data Requirements 📋

CSV files must contain:
- A `Date` column (formats supported: `DD-MM-YYYY`, `MM/DD/YYYY`, etc.)
- A `Sales` column with numerical values

Example format:
```
Date,Sales
01/01/2023,100
01/02/2023,150
01/03/2023,200
```

## Screenshots 📸

*Project Map*

![Project Map](https://github.com/user-attachments/assets/699243ba-465e-47af-a561-7d7456fcbd18)

*Forecast Generation*

![Forecast Generation](https://github.com/user-attachments/assets/5d3a5260-3089-4aac-99e1-493d0ca1b7bb)
![Image](https://github.com/user-attachments/assets/85ba92e6-7a27-49f4-b494-257c38933e2c)
![Image](https://github.com/user-attachments/assets/cdda008e-a14e-4c1f-9151-dd4f83ec7d12)
![Image](https://github.com/user-attachments/assets/fd6964b5-fbf3-4f96-916f-8947d5982c57)
![Image](https://github.com/user-attachments/assets/b30650ee-389b-4aab-8acf-b64bd1cea4b8)

*Graph Analysis*

![Image Analysis](https://github.com/user-attachments/assets/93a0b02d-7b25-446b-a851-e58b51989500)

*Data Analysis*

![Data Chat](https://github.com/user-attachments/assets/d58a26d3-34fb-4931-a439-29af9f4a7201)
![image](https://github.com/user-attachments/assets/447374a1-06a8-48fd-b0ae-15bd25d842da)

## Author 📍

For any questions or issues, please open an issue on the [@Siddharth Mishra](https://github.com/Sid3503)
