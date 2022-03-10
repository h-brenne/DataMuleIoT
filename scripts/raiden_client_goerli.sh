#!/bin/bash
raiden --eth-rpc-endpoint http://127.0.0.1:8545 --network-id 5 --accept-disclaimer --development-environment unstable --environment-type development --api-address 0.0.0.0:$1 --pathfinding-service-address https://pfs.transport01.raiden.network

