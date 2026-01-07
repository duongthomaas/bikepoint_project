# TfL BikePoint Data Extractor

A robust Python script to fetch live docking station data from the Transport for London (TfL) BikePoint API. This tool downloads the full dataset of bike points, saves it as a timestamped JSON file, and maintains detailed execution logs.

## 🚀 Features

* **Live Data Extraction**: Connects to the `BikePoint_GetAll` endpoint.
* **Automatic Logging**: Generates detailed log files in a `logs/` directory to track success, warnings, and errors.
* **Data Archiving**: Saves raw data in a `data/` directory with timestamped filenames (e.g., `2024-01-01 12-00-00.json`).
* **Robust Error Handling**:
    * **Retry Logic**: Automatically retries 3 times if the server returns a 5xx error or connection fails.
    * **Timeout Safety**: Includes a 10-second timeout to prevent the script from hanging.
    * **Status Checks**: Distinguishes between client errors (4xx) and server errors (5xx).

## 🛠️ Prerequisites

* Python 3.x
* `requests` library

## 📦 Installation

1.  **Clone the repository** (or download the script):
    ```bash
    git clone [https://github.com/yourusername/tfl-bike-extractor.git](https://github.com/yourusername/tfl-bike-extractor.git)
    cd tfl-bike-extractor
    ```

2.  **Install dependencies**:
    ```bash
    pip install requests
    ```

## 🏃 Usage

Run the script directly from your terminal:

```bash
python your_script_name.py
