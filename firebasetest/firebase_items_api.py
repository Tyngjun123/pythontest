from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Create a FastAPI instance, command 2nd app is this one
app = FastAPI()

# Route to get all items from the "items" collection in Firebase Firestore
@app.get("/items")
async def get_items():
    # Query Firebase Firestore
    items_ref = db.collection('items')
    docs = items_ref.stream()

    items_list = []
    for doc in docs:
        # Convert Firestore document to dictionary and append to the list
        items_list.append(doc.to_dict())

    # Return the list of items as a JSON response
    return {"items": items_list}

# Start FastAPI using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

#run this command for this api
# uvicorn firebase_items_api:app --reload

#navigate to my directory
# cd C:\Users\Admin\Desktop\firebasetest


