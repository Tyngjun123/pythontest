from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    items_ref = db.collection('items')
    items = items_ref.get()
    items_list = [{'id': item.id, 'name': item.to_dict()['name']} for item in items]  # Include 'id' for deletion
    return render_template('index.html', items=items_list)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('item_name')
    if item_name:
        db.collection('items').add({'name': item_name})
    return redirect(url_for('index'))

@app.route('/delete/<item_id>', methods=['POST'])
def delete_item(item_id):
    db.collection('items').document(item_id).delete()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
