import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "foodbridge")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

SMTP_SERVER = os.getenv("SMTP_SERVER", "mail.local")
SMTP_PORT = int(os.getenv("SMTP_PORT", "25"))
DEFAULT_SENDER = os.getenv("DEFAULT_SENDER", "noreply@foodbridge.local")
ADMIN_ALERT_EMAIL = os.getenv("ADMIN_ALERT_EMAIL", "ops@foodbridge.local")

REPORT_OUTPUT = "./data/daily_report.txt"
MAX_ROUTE_STOPS = 12
ENABLE_SMS = True
