from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import Optional

# 1. Initialize the App
app = FastAPI(
    title="Tech Gadgets API", 
    version="1.0",
    description="A RESTful API for managing tech product inventory - Educational Demo",
    docs_url="/docs",  # Swagger UI endpoint
    redoc_url="/redoc"  # Alternative documentation
)

# 2. Load the Data (Simulating a Database)
# We load this OUTSIDE the functions so it only happens once when the server starts.
try:
    # Ignore the leading comment line in data.csv so headers parse correctly.
    df = pd.read_csv("data.csv", comment="#")
    print(f"✅ Data loaded successfully! {len(df)} products available.")
except FileNotFoundError:
    print("❌ Error: data.csv not found!")
    df = pd.DataFrame() # Create an empty table so the app doesn't crash

# --- ENDPOINTS ---
# An "Endpoint" is a specific URL path (like /items) that triggers a specific Python function.
# It acts as the door through which users access our data.

@app.get("/")
def read_root():
    """Health check endpoint to see if server is running."""
    return {"status": "active", "message": "Welcome to the Tech Gadgets API"}

@app.get("/items")
def get_items(category: Optional[str] = None):
    """
    Get all items, OR filter by category.
    Example: /items?category=Audio
    """
    # Convert dataframe to a list of dictionaries (JSON format)
    data = df.to_dict(orient="records")
    
    # If the user provided a category, filter the list
    if category:
        # We use list comprehension here for a simple filter
        filtered_data = [item for item in data if item['category'].lower() == category.lower()]
        return filtered_data
    
    return data

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    """
    Find a specific item by its unique ID.
    """
    # Filter the dataframe for this ID
    item = df[df['id'] == item_id]
    
    if item.empty:
        raise HTTPException(status_code=404, detail="Item not found")
        
    # Return the first (and only) result
    return item.to_dict(orient="records")[0]