# 🚀 Building a Data-Driven Backend API with FastAPI
**CPS 730 Technical Demo | Group 6**
*A hands-on guide to building a modern, high-performance REST API using Python, FastAPI, and Pandas.*

 ## 1. Overview
In this tutorial, we will demonstrate how to build a scalable backend service that ingests structured data (CSV) and serves it via a fast, well-documented API. We use **FastAPI** for the web framework and **Pandas** for efficient server-side data processing.

**What you will learn:**
- How to structure a modern Python backend project.
- How to load and query CSV datasets efficiently using Pandas.
- How to validate incoming data requests using Pydantic models.
- How to handle errors and generate automatic documentation (OpenAPI/Swagger).
  
 ## 2. Prerequisites & Setup
Before starting, ensure you have the following installed:
* **Python 3.9+**
* **Docker Desktop** (Optional, for the deployment step)
* **A sample CSV file** (We have provided `data.csv` in the repo)

### Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/sarahrosehassan/fastapi-data-demo.git
    cd fastapi-data-demo
    ```

2.  **Create a Virtual Environment**
    *This creates an isolated "sandbox" for our project so our tools don't conflict with other projects on your computer.*

    **A. Build the Environment (Run once)**
    ```bash
    # Windows
    python -m venv venv
    ```

    ```bash
    # Mac/Linux
    python3 -m venv venv
    ```

    **B. Turn the Environment ON (Run every time you open a terminal)**
    ```bash
    # Windows:
    .\venv\Scripts\activate

    # Mac/Linux:
    source venv/bin/activate
    ```
    *(Tip: You will know it worked if you see `(venv)` appear at the start of your terminal line!)*

3.  **Install Dependencies**
    ```bash
    python -m pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` includes: `fastapi`, `uvicorn`, `pandas`, `pydantic`)*

 ## 3. Tutorial Walkthrough


 ## 4. Verification & Expected Outputs


 ## 5. Troubleshooting (Common Issues)


 ## 6. Clean-up


 ## 7. References
