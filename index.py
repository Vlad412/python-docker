import os
from dotenv import load_dotenv
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg
from bs4 import BeautifulSoup

load_dotenv()  # set environment variables from .env

database_name = os.getenv("DB_NAME")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
database_host = os.getenv("DB_HOST")
target_url = os.getenv("TARGET_URL")  # no slash at the end


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Flemme ok")


def run_server(port):
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()


run_server(5001)

# Connect to an existing database
with psycopg.connect(
    f"host={database_host} port=5432 dbname={database_name} user={database_user} password={database_password}"
) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute("select * from information_schema.tables where table_name=%s", ("things",))
        val = cur.fetchone()
        if val == False:
            cur.execute(
                """
                CREATE TABLE things (
                    id serial PRIMARY KEY,
                    name text,
                    power int
                    data text)
                """
            )

        cur.execute("SELECT * FROM things")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()
