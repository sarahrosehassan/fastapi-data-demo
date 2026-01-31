# 🚀 Building a Data-Driven Backend API with FastAPI

**CPS 730 Technical Demo | Group 6**
*A hands-on guide to building a modern, high-performance REST API using Python, FastAPI, and Pandas.*

---

## 📖 1. Overview
In this tutorial, we will demonstrate how to build a scalable backend service that ingests structured data (CSV) and serves it via a fast, well-documented API. We use **FastAPI** for the web framework and **Pandas** for efficient server-side data processing.

**What you will learn:**
- How to structure a modern Python backend project.
- How to load and query CSV datasets efficiently using Pandas.
- How to validate incoming data requests using Pydantic models.
- How to handle errors and generate automatic documentation (OpenAPI/Swagger).

---

## 🛠 2. Prerequisites & Setup
Before starting, ensure you have the following installed:
* **Python 3.9+**
* **Docker Desktop** (Optional, for the deployment step)
* **A sample CSV file** (We will provide `data.csv` in the repo)

### Installation
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/fastapi-data-demo.git](https://github.com/your-username/fastapi-data-demo.git)
    cd fastapi-data-demo
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Your `requirements.txt` should include: `fastapi`, `uvicorn`, `pandas`, `pydantic`)*

---

## 💻 3. Tutorial Walkthrough

### Step 1: The Basic FastAPI Server
Create a file called `main.py`. This initializes the app and the automatic documentation.

```python
from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Data Service API", version="1.0")

# Load data on startup
df = pd.read_csv("data.csv")

@app.get("/")
def read_root():
    return {"status": "active", "service": "Data Processing API"}
