# DataMuleIoT
Proof of Concept of Data Mules using IoT devices over a State Channel Network


## Create Ethereum account(s)
Install geth.
For Raspberry Pi Zero:
I installed geth with from https://geth.ethereum.org/downloads/, using the "arm-v6" arch.
My Pi Zero struggled with geth account creation, crashing after running out of memory. The account was however created and valid.

geth account new --keystore $HOME/.ethereum/keystore/

## Get testnet ETH on Görli
Most faucets have dried up. As of March 2022, the testnet faucet at https://app.mycrypto.com/faucet works. You only need to complete a quick Captcha, however you only get 0.01 ETH at a time. I added one account on MetaMask, accumulated the daily max faucet ETH on mycrypto and distributed the ETH to the accounts I was planning to use.

## Install Raiden
To install on raspberry pi as well as pc,
`pip install raiden` can be used. This might take some time since there might not be a prebuilt wheel for the pi arch. 
Raiden binary path needs to be added to PATH to launch. Adding to ~/.bashrc is one solution. Add export PATH=/home/pi/.local/bin:$PATH to the end of ~/.bashrc (replace pi with username).
 
