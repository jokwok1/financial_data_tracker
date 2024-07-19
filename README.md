## README

### What the Program Does
1. Users can register or log in to their accounts.
2. After logging in, users can view their financial data of their previous transactions.
3. Users can upload a CSV with new transactions, which will be saved and financial data will be extracted.
4. The home page will be updated with new chart data of their collated transactions based on category.
5. CSV file should be in the following format:
    - Columns: "Date, Category, Amount"
    - Each row represents an entry with these columns filled.

### Running the Application
This web application consists of a Django backend and a React frontend. To run the application, follow these steps:

1. In VSCode, open the folder `Financial Data Tracker`, and open the terminal in VSCode.
2. Navigate to the Backend Directory:
    ```bash
    cd backend
    ```
3. Activate Virtual Environment:
    ```bash
    venv\Scripts\activate
    ```
4. Install Dependencies (if required):
    ```bash
    pip install -r requirements.txt
    ```
5. Apply Migrations (if required):
    ```bash
    python manage.py makemigrations 
    python manage.py migrate
    ```
6. Run Django Development Server:
    ```bash
    python manage.py runserver
    ```
7. Ensure you have Node.js installed.
8. Open a new Terminal and navigate to the Frontend Directory:
    ```bash
    cd frontend
    ```
9. Install Dependencies:
    ```bash
    npm install
    ```
10. Start the Development Server:
    ```bash
    npm run dev
    ```

Frontend will be run at `http://localhost:5173/` while the backend will be run at `http://127.0.0.1:8000/`.
