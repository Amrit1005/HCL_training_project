from fastapi import FastAPI 
from data import product
from database import getData , add_data , update_data , delete_data
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)
# products=[
#     product(id=1,name='Laptop',description='Lenovo Ideapad Gaming 3',price=70000,quantity=10),
#     product(id=2,name='Laptop',description='Apple Mac M4',price=170000,quantity=12),
#     product(id=3,name='Laptop',description='HP ',price=40000,quantity=90),
#     product(id=4,name='Laptop',description='Dell',price=45000,quantity=100)
#     ]

@app.get('/')
def getHome():
    return "welcome to HCL tech here "

# @app.get('/newPage')
# def getData():
#     return "welcome to new Page...."

@app.get('/products/')
def all_Products():
    return getData()

@app.get('/products/{id}')
def get_Products(id:int):
    products = getData()
    for i in products:
        if i.id==id:
            return i
    return "404 Product not found"

@app.post('/products/')
def add_product(product:product):
    return add_data(product)

@app.put('/products/{id}')
def update_product(id:int,product:product):
    return update_data(id,product)

@app.delete('/products/{id}')
def delete_product(id:int):
    return delete_data(id)

''' 
# Import the FastAPI class to create the web application instance.
from fastapi import FastAPI

# Import the 'product' class/model from a local module named 'data'.
# This class is used to instantiate product objects with fields like id, name, etc.
from data import product

# Create a FastAPI application instance.
# This 'app' object is the central ASGI application that defines routes and handles requests.
app = FastAPI()

# Define an in-memory list to act as a simple "database" of products.
# Using a list keeps the example lightweight without external dependencies like SQL.
listOfproducts = [
    # Each element is an instance of the 'product' class with predefined attributes.
    # This pre-populates the list with sample data for testing the API.
    product(id=1, name="Laptop", description="Dell laptop", price=150, quantity=10),
    product(id=2, name="Laptop", description="HP laptop", price=250, quantity=15),
    product(id=3, name="Table", description="Ikea", price=350, quantity=16),
    product(id=4, name="Mobile", description="Samsung phone", price=450, quantity=13),
]

# Register a GET route at the root path '/'.
# When a client sends a GET request to '/', FastAPI calls this function.
@app.get("/")
def getData():
    # Return a simple string response as the body of the HTTP response.
    # FastAPI will serialize this to JSON automatically (as a plain string).
    return "Welcome to Home page"

# Register a GET route at '/newPage'.
# This demonstrates adding multiple endpoints to the application.
@app.get("/newPage")
def newPageData():
    # Return a greeting string for the '/newPage' endpoint.
    return "Welocme to new page"

# Register a GET route at '/all_listOfproducts' to fetch all products.
@app.get("/all_listOfproducts")
def get_listOfproducts():
    # Return the entire in-memory list of product objects.
    # FastAPI will attempt to serialize each object; if 'product' is a Pydantic model, this is automatic.
    return listOfproducts

# Register a GET route with a path parameter 'id' to fetch a single product.
# The '{id}' segment in the path captures the value from the URL.
@app.get("/products/{id}")
def get_listOfproducts(id: int):
    # Iterate over each product in the list to find a matching ID.
    for i in listOfproducts:
        # Check if the current product's 'id' matches the requested 'id'.
        if i.id == id:
            # If found, return the product object as the response.
            return i
    # If no product matches the given 'id', return a not-found message.
    # Consider returning a JSON dict or raising HTTPException for better API semantics.
    return "404 Product not found"

# Register a POST route at '/products' to add a new product.
@app.post("/products")
def add_product(product: product):
    # The function parameter 'product' is typed as the 'product' class.
    # FastAPI parses the request body into this object, enforcing the expected fields.
    # Append the new product object to the in-memory list.
    listOfproducts.append(product)
    # Return a success message indicating the product was added.
    return "Product added successfully"

# Register a PUT route at '/products/{id}' to update an existing product by ID.
@app.put("/products/{id}")
def update_product(id: int, product: product):
    # Iterate over indices to allow assignment into the list when a match is found.
    for i in range(len(listOfproducts)):
        # Check if the product at index 'i' has the same 'id' as the path parameter.
        if listOfproducts[i].id == id:
            # Replace the existing product with the new 'product' object from the request body.
            listOfproducts[i] = product
            # Return a success message indicating the update was performed.
            return "Product updated successfully"
    # If no product with the given 'id' exists, return a not-found message.
    return "Product not found"

# Register a DELETE route at '/products/{id}' to remove a product by ID.
# Note: Including '{id}' in the path makes the endpoint RESTful and unambiguous.
@app.delete("/products/{id}")
def delete_product(id: int):
    # Iterate over indices to safely delete by position using 'del' or 'pop'.
    for i in range(len(listOfproducts)):
        # Check if the product at index 'i' matches the requested 'id'.
        if listOfproducts[i].id == id:
            # Delete the product from the list to remove it from the "database".
            del listOfproducts[i]
            # Return a success message indicating deletion.
            return "Product Deleted successfully"
    # If no matching product is found, return a not-found message.
    return "Product not found"
    p'''