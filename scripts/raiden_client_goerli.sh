#!/bin/bash
raiden --eth-rpc-endpoint "ETH_ENDPOINT_HERE(node)" --network-id 5 --accept-disclaimer --development-environment unstable --environment-type development --api-address 0.0.0.0:5001 --pathfinding-service-address https://pfs.transport01.raiden.network

