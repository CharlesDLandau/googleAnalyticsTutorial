# Analytics Scripting With Python

## Prerequisites

Python >= 3.6
`virtualenv`


## Setup:

Clone this repo:

```
git clone https://github.com/CharlesDLandau/googleAnalyticsTutorial.git

```

Create a virtualenv:

```virtualenv venv --no-site-packages

// bash
source venv/bin/activate

// cmd
call venv/scripts/activate

```

Install dependencies:

```
pip install -r requirements.txt
```

Setup kernel

```
python -m ipykernel install --user --name venv --display-name "venv"
```

Launch jupyter lab

```
jupyter lab
```

**Note:** If a browser tab does not spawn, the output of this command will have a URL you can cut and paste.

Launch the tutorial notebook:

[](./assets/launch_jupyter.png)

You can select the kernel we built with menu options `Kernel>Change Kernel` and selecting it by name ("venv" in our example command above.)

