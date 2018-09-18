# Custom Script for Linux

# Update OS sources
apt update -y

# Install Python 
apt install python3
pip install pipenv

# Setup Pl^g location
mkdir /plug && cd /plug

# install Pl^g
pipenv shell

pipenv install -e git+ssh://git@github.com/plugblockchain/plug@master#egg=plug_framework

pipenv install -e git+ssh://git@github.com/plugblockchain/plug.demo@master#egg=plug_demo


# Configure Pl^g Node
cat <<EOF > node.yaml
plug:
  network_id: plug.demo.balance
  max_block_size: 100

  registry:
    plugins:
    - plug_demo.balance.BalancePlugin

  initial_state:
    plug_demo.balance.BalanceModel:
      137i7u2nxUod3ctEdPe5rN6EHCa8X64rBW:
          balance: 100
      1MunZQ7AUnjBLjTeUYU7hM2r9aTM3KYjYn:
          balance: 100
EOF

# Initialize 
nodeplug-dev create-network -n1 node.yaml -d ./nodes
cd nodes/node_0
plug run
