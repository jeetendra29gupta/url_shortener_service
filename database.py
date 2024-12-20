import sqlite3
from urllib.parse import urlparse


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


def initialize_database():
    """Create the database table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT,
            domain_name TEXT,
            shorten_url TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()


def create_indexes():
    """Create indexes for optimized queries."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE INDEX IF NOT EXISTS idx_domain_name ON url_mapping(domain_name)""")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_short_url ON url_mapping(shorten_url)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_original_url ON url_mapping(original_url)")
    conn.commit()
    conn.close()


def save_shorten_url_into_memory(original_url, shorten_url):
    """Save the shortened URL into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO url_mapping (original_url, domain_name, shorten_url) VALUES (?, ?, ?)",
        (original_url, urlparse(original_url).netloc, shorten_url)
    )
    conn.commit()
    conn.close()


def get_shorten_url_from_memory(original_url):
    """Retrieve the shortened URL from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT shorten_url FROM url_mapping WHERE original_url=?", (original_url,))
    result = cursor.fetchone()
    conn.close()
    return result


def get_original_url_from_memory(shorten_url):
    """Retrieve the original URL from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM url_mapping WHERE shorten_url=?", (shorten_url,))
    result = cursor.fetchone()
    conn.close()
    return result


def get_sorted_domains_metrics():
    """Get the top 3 most frequent domains."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT domain_name, COUNT(domain_name) as counter
        FROM url_mapping
        GROUP BY domain_name
        ORDER BY counter DESC
        LIMIT 3
    """)
    result = cursor.fetchall()
    conn.close()
    return result
