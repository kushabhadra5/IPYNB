echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda  create --prefix env python=3.10 -y
echo [$(date)]: "**********************************"
echo [$(date)]: "Activating conda env"
source activate ./env
echo [$(date)]: "**********************************"
echo [$(date)]: "Installing dev requirements"
pip install -r requirements.txt
echo [$(date)]: "**********************************"
echo [$(date)]: "END"