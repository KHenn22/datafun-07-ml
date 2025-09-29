# datafun-07-ml

Northwest Missouri State University Data Analytics Fundamentals — Week 7 (Machine Learning)

This repository contains materials and exercises for Week 7 (machine learning / analysis) module.

## Prerequisites

- Python 3.8 or newer
- pip (Python package installer)
- git (to clone the repository)

## Quick-start (initialize the project)

1. Clone the repository:

```bash
git clone https://github.com/KHenn22/datafun-07-ml
cd datafun-07-ml
```

2. Create and activate a virtual environment (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Start JupyterLab (optional):

```bash
jupyter lab
```

## Quick Python check

After installing dependencies, you can copy and run this small Python snippet to verify key packages are importable:

```python
import sys
import numpy as np
import pandas as pd

print('python', sys.version.split()[0])
print('numpy', np.__version__)
print('pandas', pd.__version__)
```

Copy the block above into a file (for example `check_env.py`) and run:

```bash
python check_env.py
```

## Notes

- This README uses fenced code blocks so commands and small Python examples can be copied directly from the file or from GitHub's rendered view.
- If `pip install -r requirements.txt` fails on binary packages (for example `pyarrow`), consider using conda/mamba or updating pip/setuptools/wheel before retrying.
# datafun-07-ml

Northwest Missouri State University Data Analytics Fundamentals — Week 7 (Machine Learning)

This repository contains materials and exercises for Week 7 (machine learning / analysis) module.


## Prerequisites

- Python 3.8 or newer
- pip (Python package installer)
- git (to clone the repository)

## Quick-start (initialize the project)

1. Clone the repository:

	git clone <https://github.com/KHenn22/datafun-07-ml>
	cd datafun-07-ml
 
2. Create and activate a virtual environment in macOS

	python3 -m venv .venv
	source .venv/bin/activate

3. Upgrade pip and install dependencies:

	pip install --upgrade pip
	pip install -r requirements.txt
