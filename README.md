# Online Shop (Django)

This is a simple online shop website made with Django as a school project.
The project is not commercial and was created only for learning purposes.

What is this project about?

* Users can register and log in
* Users can add products
* Each product belongs to the user who created it
* Products have name, price, description, stock and image
* There is a basic order system (models only)
  
--- How to run the project:
### 1. Clone the repository

git clone <repository_url>


### 2. Create a virtual environment

python -m venv venv


### 3. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac / Linux:

source venv/bin/activate


### 4. Install dependencies

pip install -r requirements.txt

### 5. Apply migrations

python manage.py migrate

### 6. Run the server

python manage.py runserver

### 7. Open in browser

Go to:

```
http://127.0.0.1:8000/
```

---

## Notes

* `venv`, database file and media files are not included in the repository
* This project was made for educational purposes

---

Author: Anna
