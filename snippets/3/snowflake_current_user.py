import json
import snowflake.connector

# Load config
with open('config.json') as f:
    config = json.load(f)

# Create connection
ctx = snowflake.connector.connect(
    account=config['account'],
    user=config['user'],
    password=config['password'],
    warehouse=config['warehouse'],
    database=config['database'],
    schema=config['schema'],
    role=config.get('rol') or config.get('role')
)

try:
    cs = ctx.cursor()
    cs.execute('SELECT CURRENT_USER()')
    user = cs.fetchone()[0]
    print(f"Current Snowflake user: {user}")
finally:
    cs.close()
    ctx.close()
