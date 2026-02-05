# 📱 Tech Products API (Backend Demo)

## ⚡ Quick Start
For experienced users who want to get started immediately:

**Mac / Linux:**
```bash
./setup.sh  # Install everything
./start.sh  # Start the server
```

**Windows:**
```bash
setup.bat  # Install everything
start.bat  # Start the server
```

Then open http://127.0.0.1:8000/docs in your browser.

---

## 1. Overview
This project demonstrates a high-performance REST API backend built with **Python**, **FastAPI**, and **Pandas**. It simulates an e-commerce inventory system where users can:
* **Retrieve** a full list of tech products.
* **Filter** products by category (e.g., "Audio", "Monitors").
* **Lookup** specific items by their unique ID.

**Tech Stack:**
* **FastAPI:** For handling HTTP requests and routing.
* **Pandas:** For efficient in-memory data processing (simulating a database).
* **Uvicorn:** As the ASGI server to run the application.

---

## 2. Key Technologies Explained

### What is a REST API?
REST (Representational State Transfer) is an architectural style for building web services. A REST API allows different applications to communicate over HTTP using standard methods (GET, POST, PUT, DELETE). In this project, we use GET requests to retrieve product data.

### Why FastAPI?
FastAPI is a modern Python web framework that's significantly faster than alternatives like Flask or Django. It automatically generates interactive API documentation (Swagger UI), validates data types, and provides async support for high-performance applications.

### What is Swagger/OpenAPI?
Swagger UI is an interactive documentation interface that FastAPI generates automatically. It lets you test API endpoints directly in your browser without writing any frontend code or using tools like Postman.

### Role of Pandas
Pandas is typically used for data analysis, but here it serves as an in-memory database. It loads the CSV file and allows fast filtering and querying operations, simulating what a real database would do.

---

## 3. Prerequisites & Setup Instructions

### Prerequisites
* **Python 3.8+** 
  * **Mac / Linux:** Verify with `python3 --version`
  * **Windows:** Verify with `python --version`

### Installation & Setup

**Step 1: Prepare the Files**
Ensure the following files are in your project folder:
* `main.py` (Application logic)
* `data.csv` (Data source)
* `requirements.txt` (Dependencies)

**Step 2: Create Virtual Environment**
Run the command for your operating system to create an isolated sandbox:

* **Mac / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

* **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
(You should see `(venv)` appear at the start of your terminal line).

**Step 3: Install Dependencies**
```bash
python -m pip install -r requirements.txt
```

**Step 4: Start the Server**
```bash
uvicorn main:app --reload
```
You should see: `Uvicorn running on http://127.0.0.1:8000`

![Server Running](images/server-running.png)

Visiting http://127.0.0.1:8000 will only show a raw JSON message.

---

## 4. Tutorial Walkthrough
We use the automatic Swagger UI to test the API without needing a frontend.

**Step 1: Open the Interface**  
Navigate to http://127.0.0.1:8000/docs in your browser.

![Swagger UI Main Page](images/swagger-ui-main.png)

**Step 2: Get All Items**
1. Click on the blue bar **GET /items**.
2. Click **Try it out** -> **Execute**.
3. **Result:** The API returns a JSON list of all products from `data.csv`.

![Get All Items Response](images/get-all-items-response.png)

**Step 3: Filter by Category**
1. In the `category` parameter field, type: `Audio`
2. Click **Execute**.
3. **Result:** The API returns only the "Sony Noise Cancelling Headphones".

![Filter by Category Response](images/filter-by-category-response.png)

**Step 4: Lookup Specific Item**
1. Scroll to **GET /items/{item_id}**.
2. Click **Try it out**.
3. Enter ID: `106` (Apple Watch).
4. Click **Execute**.
5. **Result:** The API returns details for the "Smart Watch Series 7".

![Get Item by ID Response](images/get-item-by-id-response.png)

---

## 5. Troubleshooting

**Error: "Module not found: pandas"**
* **Cause:** You are not inside the virtual environment.
* **Fix:** Run `source venv/bin/activate` (Mac) or `.\venv\Scripts\activate` (Windows).

**Error: "command not found: uvicorn"**
* **Cause:** Dependencies were installed globally or not at all.
* **Fix:** Activate the venv and run `pip install -r requirements.txt` again.

**Error: "Address already in use"**
* **Cause:** Another instance of the server is running.
* **Fix:** Close other terminal windows or change the port: `uvicorn main:app --reload --port 8001`.

---

## 6. Clean-up
To properly close the project when finished:

1. **Stop the Server:** Go to your terminal and press `Ctrl + C`.

2. **Exit the Environment:** Type the following command to leave the virtual sandbox:
   ```bash
   deactivate
   ```

3. **(Optional) Delete Environment:** If you want to save space, you can delete the `venv` folder safely. It can always be recreated using the Setup Instructions.

---

## 7. References
* **FastAPI Documentation:** https://fastapi.tiangolo.com/
* **Pandas Documentation:** https://pandas.pydata.org/docs/
* **Uvicorn Deployment:** https://www.uvicorn.org/
* **Python venv Module:** https://docs.python.org/3/library/venv.html
