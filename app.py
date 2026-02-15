from fastapi import FastAPI
import pyodbc
import os

app = FastAPI()

def get_connection():
    server = os.getenv("DB_SERVER", "sqlserver")
    database = os.getenv("DB_NAME", "InvoicesDB")
    username = os.getenv("DB_USER", "sa")
    password = os.getenv("DB_PASSWORD")

    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server},1433;"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )

    return pyodbc.connect(connection_string)


# ---------------------------------------------------------
# 1. GET ALL INVOICES
# ---------------------------------------------------------
@app.get("/invoices")
def get_all_invoices():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, CustomerName, InvoiceDate, Amount FROM Invoices")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "customer": row[1],
            "date": str(row[2]),
            "amount": float(row[3])
        }
        for row in rows
    ]


# ---------------------------------------------------------
# 2. GET INVOICES BY CUSTOMER
# ---------------------------------------------------------
@app.get("/invoices/customer/{name}")
def get_invoices_by_customer(name: str):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT Id, CustomerName, InvoiceDate, Amount FROM Invoices WHERE CustomerName = ?"
    cursor.execute(query, (name,))
    rows = cursor.fetchall()
    conn.close()

    return {
        "customer": name,
        "results": [
            {
                "id": row[0],
                "customer": row[1],
                "date": str(row[2]),
                "amount": float(row[3])
            }
            for row in rows
        ]
    }


# ---------------------------------------------------------
# 3. GET INVOICES BY YEAR
# ---------------------------------------------------------
@app.get("/invoices/year/{year}")
def get_invoices_by_year(year: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT Id, CustomerName, InvoiceDate, Amount FROM Invoices WHERE YEAR(InvoiceDate) = ?"
    cursor.execute(query, (year,))
    rows = cursor.fetchall()
    conn.close()

    return {
        "year": year,
        "results": [
            {
                "id": row[0],
                "customer": row[1],
                "date": str(row[2]),
                "amount": float(row[3])
            }
            for row in rows
        ]
    }


# ---------------------------------------------------------
# 4. GET INVOICES BY AMOUNT RANGE
# ---------------------------------------------------------
@app.get("/invoices/range")
def get_invoices_by_range(min: float, max: float):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT Id, CustomerName, InvoiceDate, Amount FROM Invoices WHERE Amount BETWEEN ? AND ?"
    cursor.execute(query, (min, max))
    rows = cursor.fetchall()
    conn.close()

    return {
        "min": min,
        "max": max,
        "results": [
            {
                "id": row[0],
                "customer": row[1],
                "date": str(row[2]),
                "amount": float(row[3])
            }
            for row in rows
        ]
    }
