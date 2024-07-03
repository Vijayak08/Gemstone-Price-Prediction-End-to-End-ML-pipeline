echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"

conda create --prefix ./testvenv python=3.8 -y

echo [$(date)]: "activating the environment"

source activate ./testvenv

echo [$(date)]: "Installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)]: "END"