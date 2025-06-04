import React, { useEffect, useState } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [barcode, setBarcode] = useState('');
  const [quantity, setQuantity] = useState(1);
  const API_BASE = "http://192.168.1.155:5000";

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = () => {
    fetch(`${API_BASE}/items`)
      .then(res => res.json())
      .then(setItems)
      .catch(console.error);
  };

  const handleAdd = () => {
    if (!barcode.trim()) {
      alert("Please enter a barcode");
      return;
    }

    fetch(`${API_BASE}/items`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ barcode, quantity: parseInt(quantity, 10) || 1 })
    })
      .then(res => res.json())
      .then(() => {
        fetchItems();
        setBarcode('');
        setQuantity(1);
      })
      .catch(console.error);
  };

  const handleDelete = (barcodeToDelete) => {
    fetch(`${API_BASE}/items/${barcodeToDelete}`, {
      method: 'DELETE'
    })
      .then(res => res.json())
      .then(() => fetchItems())
      .catch(console.error);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Inventory</h1>

      <div style={{ marginBottom: 20 }}>
        <input
          type="text"
          placeholder="Barcode"
          value={barcode}
          onChange={e => setBarcode(e.target.value)}
          style={{ marginRight: 10 }}
        />
        <input
          type="number"
          min="1"
          value={quantity}
          onChange={e => setQuantity(e.target.value)}
          style={{ width: 60, marginRight: 10 }}
        />
        <button onClick={handleAdd}>Add / Update Item</button>
      </div>

      <ul>
        {items.map(item => (
          <li key={item.barcode} style={{ marginBottom: 8 }}>
            {item.barcode} - Qty: {item.quantity}{' '}
            <button onClick={() => handleDelete(item.barcode)}>Delete One</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

