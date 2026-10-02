import sys
import os

# Add project root to path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)

# Change working directory so Flask finds templates/static
os.chdir(root)

from app import app

# Vercel handler
app.debug = False
