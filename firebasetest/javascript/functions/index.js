const functions = require('firebase-functions');
const admin = require('firebase-admin');
const express = require('express');

// Initialize Firebase Admin SDK
admin.initializeApp({
  credential: admin.credential.cert(require('./serviceAccountKey.json'))
});
const db = admin.firestore();

// Initialize Express app
const app = express();
app.use(express.json());  // For parsing JSON request bodies

// Route to fetch items from Firestore
app.get('/items', async (req, res) => {
  try {
    const itemsRef = db.collection('items');
    const snapshot = await itemsRef.get();

    let itemsList = [];
    snapshot.forEach(doc => {
      itemsList.push(doc.data());
    });

    res.status(200).json({ items: itemsList });
  } catch (error) {
    console.error('Error getting items:', error);
    res.status(500).send('Error retrieving items');
  }
});

// Route to add an item to Firestore
app.post('/add', async (req, res) => {
  const itemName = req.body.item_name;
  
  if (!itemName) {
    return res.status(400).send('Item name is required');
  }

  try {
    await db.collection('items').add({ name: itemName });
    res.status(201).send('Item added successfully');
  } catch (error) {
    console.error('Error adding item:', error);
    res.status(500).send('Error adding item');
  }
});

// Route to delete an item from Firestore
app.delete('/delete/:id', async (req, res) => {
  const itemId = req.params.id;

  try {
    const itemRef = db.collection('items').doc(itemId);
    await itemRef.delete();
    res.status(200).send('Item deleted successfully');
  } catch (error) {
    console.error('Error deleting item:', error);
    res.status(500).send('Error deleting item');
  }
});

// Export the Express app as a Firebase Cloud Function
exports.app = functions.https.onRequest(app);
