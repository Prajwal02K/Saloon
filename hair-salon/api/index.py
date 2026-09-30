import sys
import os

# Add the project root to Python path so Flask can find all modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel needs the app object named 'app'
handler = app
