# FPTRACE - First Principles' Trace Processing Toolkit

FPTRACE is a library for analysis of a wide variety of chromatographic
and spectroscopic traces, and deconvolution of Infrared Spectroscopy data.
This package provides tools for implementation of curve-fitting deconvolution
in python, and a web application to run standard analysis operations in a user friendly manner.

## Installation

Currently FPTRACE is not open source, and is a stand alone Flask app.
Often, Flask apps do not require installation as a package. However,
in this case, we want to also put the app into a Docker container, and
for internal modules / imports to work correctly, we need to use
setuptools to package it.

Clone or download the repo.

```bash
git clone https://github.com/brentkendrick/fptrace.git
```

## Install dependencies either locally (for select git repos), or specified versions

### Local, editable installation of packages from github (fpbiolib and chemlabparser)

Clone or download select dependency repo and use setuptools to install the package locally.

With the new pyproject.toml file format, the command python setup.py develop is no longer applicable. The modern alternative is to use pip install -e ., which installs your package in "editable" mode (the equivalent of setup.py develop).

Here's how to do it:
Ensure you have the latest version of pip, setuptools, and wheel in your virtual environment:

```bash
pip install --upgrade pip setuptools wheel
```

To install a dependency package in editable mode (note fpbiolib is public, but chemlabparser
is private and requires a github access token for the build
and in the repository Secrets-GH_SCOPED_TOKEN, request help from brent.kendrick@fp-biopharma.com
if needed):

clone the repository, e.g. for chemlabparser

```bash
git clone https://github.com/brentkendrick/chemlabparser.git
```

Line in a requirements.txt file (assumes chemlabparser was cloned to the indicated path)

```bash
-e /Users/brent/code/lib/chemlabparser
```

Or, in your dependency package directory, run:

```bash
pip install -e .
```

This command will install your package in a way that allows you to modify the source code and immediately see changes without needing to reinstall the package.

### Installation of a specific version (good for production)

(chemlabparser requires git access token, it will prompt for this
as a password request during pip install (no need to create
a system variable for local installs). You will pass it as
an arg for docker builds)

```bash
pip install fpbiolib @ git+https://github.com/brentkendrick/fpbiolib@v0.5.2
pip install chemlabparser @ git+https://<GH_SCOPED_TOKEN>@github.com/brentkendrick/chemlabparser@v0.5.2
```

Lines in a requirements.txt file

```bash
fpbiolib @ git+https://github.com/brentkendrick/fpbiolib@v0.5.2
chemlabparser @ git+https://<GH_SCOPED_TOKEN>@github.com/brentkendrick/chemlabparser@v0.5.2
```

Install all packages using requirements.txt

```bash
pip install -r requirements.txt
```

### Package fptrace so local imports will work

In the fptrace project directory, run:

```bash
pip install -e .
```

## Usage

## Running the app locally

### Ensure redis is running

Start redis on your local machine:

```bash # linux
sudo service redis-server start
```

or

```bash # mac using homebrew
brew services start redis
```

go to root directory of this app and run:

```bash
python run.py
```

(note: trying to run the app with `python dash_df_plot/app.py` will prevent relative imports to work,
because when you run a file directly, its context changes, and it is no longer treated as part of the package.
However, you can run it as a module with `python -m dash_df_plot.app` )

Or, with gunicorn:

```bash
gunicorn -c "python:dash_df_plot.config.gunicorn" "run:server"
```

## With Docker

### Ensure redis is stopped

Stop redis on your local machine:

```bash # linux
sudo service redis-server stop
```

or

```bash # mac using homebrew
brew services stop redis
```

Open a terminal configured to run Docker, navigate to the folder containing the docker-compose.yml file. To build the images, run (must use intel build for images to run on EC2):

Using the docker-compose.yml file (preferred, since redis is conveniently linked)
If issues appear with build, try adding the flag --no-cache after docker compose build

```bash
docker compose build
```

NOTE: building with docker compose will typically use the directory name (unless project name is
otherwise specified), and then a dash followed by the name listed in the relevant docker-compose section.
You probably want to tag it like the following if you are using it in other docker compose instances
that call for the fptrace:latest images:

```bash
docker tag fptrace-fptrace:latest fptrace:latest
```

Now, to run:

```bash
docker compose up
```

and go to: http://localhost:5000/fptrace/

Or,

```bash
docker build -t fptrace .
```

Now, to run:

```bash
docker run -p 5000:5000 fptrace
```

## Deploy docker image to AWS ECR

This is normally done via the Github automated actions using the
.github/workflows/norbi_build_deploy.yml file.

The manual process is:

```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 979711578039.dkr.ecr.us-east-2.amazonaws.com
docker tag fptrace:latest 979711578039.dkr.ecr.us-east-2.amazonaws.com/fptrace:latest
docker push 979711578039.dkr.ecr.us-east-2.amazonaws.com/fptrace:latest
```

## Troubleshooting

On Mac, may need to use a different port or disable Airplay Receiver which uses port 5000. System Settings > General > AirDrop & Handoff > AirPlay Receiver. To find what is using port 5000

```bash
lsof -i tcp:5000
```

With this error: ModuleNotFoundError: No module named 'fptrace'.  
Make sure to install fptrace as local package: pip install -e .

### Callback errors

All callback return values must be in a JSON serializable form. These are
usually in the form of a simple string, a list of strings / numbers, or a
dictionary of strings/numbers.

The following error occurs if you pass a python object like None,
rather than "None" in a dictionary callback value, such as in:

return {["label": "Label 1"], ["value": None]}

Gives the following error:
Converting circular structure to JSON
--> starting at object with constructor 'BaseTreeContainer'
| property '\_reactInternalFiber' -> object with constructor 'FiberNode'
--- property 'stateNode' closes the circle

Whereas:
return {["label": "Label 1"], ["value": "None"]}

works just fine.

### Sphinx documentation generation

For detailed documentation please read the sphinx documentation. This
documentation can be built using the following.

```bash
sphinx-build doc/source FPTRACE/doc
```

This will output HMTL files in the FPTRACE/doc directory which contains detailed
information about what deconvolution algorithms have been implemented, how to
use the io functionality and much more. This is important as the application
serves these html files as static files.

Getting the following error when running docker compose up:

Fatal error loading the DB: Invalid argument. Exiting.

Fix: Clear the Redis Volume (If Persistent Storage is Used)

If you’re using a persistent volume, try clearing it to rule out data corruption:

    1.	Stop your containers with -v flag:

    ```bash
    docker compose down -v
    ```

Error with docker compose build, try doing it with no cache.

```bash
docker compose build --no-cache
```

# Updating to latest package versions

1.  Create a new virtual environment and do a `pip install -r requirements.txt`. To find outdated python packages run:

```bash
pip3 list --outdated
```

Manually update the requirements.txt file with the latest versions. Run appropriate app tests to verify.

Run a pip freeze to get a complete list of dependency versions (helpful for troubleshooting)

```bash
pip3 freeze -r requirements.txt > requirements.lock
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT license, Copyright 2024 First Principles Biopharma

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# If the app requires celery worker - see below

go to fptrace directory of this app and run:

```bash
celery -A app.celery_app worker --loglevel=INFO --concurrency=2
```

project/
├── run.py
├── dash_df_plot/
│ ├── **init**.py
│ ├── app.py
│ ├── ids.py
│ ├── utils.py
| ├── \_version.py
│ └── config/
│ ├── **init**.py
│ ├── settings.py
│ └── gunicorn.py
├── pyproject.toml
└── requirements.txt
