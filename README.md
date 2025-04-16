# mm - move mouse
This OSX software moves mouse cursor by 1 pixel up every ~50-60 seconds

## Installation setup

> Make sure python3 and pip are installed. It is recommended to use hombrew to install python.

1. Create a virtual environment 
```bash
python3 -m venv venv
```

2. Activate the virtual environment
```bash
source venv/bin/activate
```

3. Install pyautogui within virtual environment
```bash
pip install pyautogui
```

4. Make sure mm.sh has executible flag set up
```bash
chmod +x mm.sh
```

5. Run the mm

Once virtual environment is activated within shell you can run it directly with:
```bash
python3 mm.py
```

You can also do bash script that activates virtual environment and runs python script automatically:

```bash
mm.sh
```