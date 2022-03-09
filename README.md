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
 
## Setup ETH node with RPC Endpoint
I first used an infura.io endpoint, but you'll quickly reach the daily limit for large tests.

This public görli seems to work well: 
https://rpc.goerli.mudit.blog/

With geth, you can run a node with a http RPC API. I used `geth --syncmode light --http --http.addr 0.0.0.0 --http.api personal,eth,net,web3,debug --goerli --http.corsdomain "*"` Warning: this exposes the RPC endpoint to remote clients.

## Simulate network delay, packet loss, jitter and more with netem
[Documentation](https://man7.org/linux/man-pages/man8/tc-netem.8.html).

10% packet loss example on wlan0: `sudo tc qdisc add dev wlan0 root netem loss 10%`
