git fetch --all --tags 1> /dev/null
git pull 1> /dev/null

source ~/.bashrc
source ~/.zshrc

conda activate dev

pip config set global.extra-index-url "a"
pip uninstall volive
pip install --upgrade git+https://sha@github.com/volive/volive.git@$GIT_BRANCH 1> /dev/null
