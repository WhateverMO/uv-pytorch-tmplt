docker run -it --gpus all --name cuda12.8 -v /home/zjj/Documents/workspace/zt-zjj-KPConv-PyTorch/:/home/work nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04 bash
<https://hub.docker.com/r/nvidia/cuda>

chsh -s /bin/bash
apt update
apt install sudo vim -y
useradd zjj -p zjj
usermod -a zjj -G sudo
groupadd admin
usermod -a zjj -G admin
mkdir -p /home/zjj
chown -R zjj:zjj /home/zjj
su zjj
chsh -s /bin/bash
cd
ln -s /home/work work

LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
rm -rf lazygit*

BOTTOM_VERSION=$(curl -s "https://api.github.com/repos/ClementTsang/bottom/releases/latest" | grep -Po '"tag_name": "\K[^"]*')
curl -LO "https://github.com/ClementTsang/bottom/releases/download/${BOTTOM_VERSION}/bottom_${BOTTOM_VERSION}-1_amd64.deb"
sudo dpkg -i bottom_${BOTTOM_VERSION}-1_amd64.deb && rm -rf bottom_*

source ~/.bashrc

chsh -s /usr/bin/fish

cd
sudo apt upgrade -y
sudo apt install python3-dev python3-pip python3-tk -y

curl -LsSf <https://astral.sh/uv/install.sh> | sh
source $HOME/.local/bin/env.fish
source $HOME/.local/bin/env

uv tool install nvitop
or
uvx nvitop

uv add torch[cu128] torchvision[cu128] torchaudio[cu128] numpy scikit-learn pyyaml matplotlib mayavi pyqt5
or
uv sync --extra cu128

docker start cuda12.8
docker exec -it -u zjj cuda12.8 fish
