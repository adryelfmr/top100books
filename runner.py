import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "top100.py"]
sys.exit(stcli.main())