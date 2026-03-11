import sys
import os

# Add the parent directory to the path so it can find db_manager, auth, etc.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app

# Vercel requires the app object to be available here.
