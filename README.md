# Inventory Management App

**Backend:** Flask + SQLite
**Frontend:** React

---

## Setup

1. **Backend**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
python app.py
```

2. **Frontend**

```bash
cd frontend
npm install
npm start
```

---

## Usage

* Access frontend at `http://<raspberrypi-ip>:3000`
* Add items by barcode + quantity
* Delete reduces quantity by 1; deletes item at zero

---

## Notes

* Backend CORS set for frontend IP
* Update IPs in `app.py` and `App.js` accordingly
