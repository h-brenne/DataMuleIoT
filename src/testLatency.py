import time
import numpy as np
import pickle
from raiden_api_client.exceptions import (
    RaidenAPIConflictException
)
from raiden_api_client.wrapper import RaidenAPIWrapper
def ping_pong_transaction(rdn, rdn2, PARTNER, PARTNER2, TOKEN_ADDR):
    success = False
    start_ping = time.time()
    while(not success):
        try:
            result = rdn.transfer(amount=10000000000005, partner=PARTNER2, token=TOKEN_ADDR)
            success = True
        except KeyboardInterrupt:
            exit()
        except:
            pass
    end_ping = time.time()
    print(result)

    success = False
    start_pong = time.time()
    while(not success):
        try:
            result = rdn2.transfer(amount=10000000000005, partner=PARTNER, token=TOKEN_ADDR)
            success = True
        except KeyboardInterrupt:
            exit()
        except:
            pass
    end_pong = time.time()

    transfer_times = [end_ping-start_ping, end_pong-start_pong]
    print(transfer_times)
    return transfer_times
def analyze_ping_pong_transactions(latencies):
    latencies = np.array(latencies)
    sum = np.sum(latencies, axis=0)
    mean = np.mean(latencies, axis=0)
    var = np.var(latencies, axis=0)

    total_transactions = latencies.size
    total_time = sum[0]+sum[1]
    average_time = np.mean(latencies)
    time_variance = np.var(latencies)

    total_time_way1 = sum[0]
    total_time_way2 = sum[1]
    average_time_way1 = mean[0]
    average_time_way2 = mean[1]
    time_variance_way1 = var[0]
    time_variance_way2 = var[1]

    print("Number of transactions: %d, Total transaction time: %f" % (total_transactions, total_time))
    print("Average transaction time: %f, Transaction time variance:%f" % (average_time, time_variance))
    print("Average transaction time way 1: %f, Average transaction time way 2: %f" % (average_time_way1, average_time_way2))
    print("Transaction time variance way 1: %f, Transaction time variance way 2: %f" % (time_variance_way1, time_variance_way2))
URL = "0.0.0.0"
URL_RPI_ZERO = "raspberrypi.local"
PORT_RPI = "5001"
PORT = "5001"
PORT2 = "5004"
#TOKEN = "0xC563388e2e2fdD422166eD5E76971D11eD37A466" #TTT 1
TOKEN_ADDR = "0x59105441977ecD9d805A4f5b060E34676F50F806" #TTT 2
#TOKEN = "0x5Fc523e13fBAc2140F056AD7A96De2cC0C4Cc63A" #SVT
#PARTNER = "0x1F916ab5cf1B30B22f24Ebf435f53Ee665344Acf"  # Raiden Hub
#PARTNER_RPI_ZERO = "0xbe419547448aD3561f8cbA0ad14a12b51F16C873" #rpi_zero
PARTNER_RPI_ZERO = "0x3860601ba03e0B42410712d47c0622cEF5166844" #rpi_zero

#PARTNER = "0x057257D80088f7D1DFAA271Db62c03b37CAA5d3B" #N2
PARTNER1 = "0x3f3208313884345393f33EC65FdFbbc44766Db22" #N3
PARTNER2 = "0x0065643F974F027931c19B9f01E21512a8E46BE9" #N4
PARTNER3 = "0x1B9C969016C073858e075e3102d99e60Bfc00B9E"
PARTNER4 = "0xb43d49253718E20a7cf1F208Ab4CD3AD96467c9C"
rdn = RaidenAPIWrapper(ip=URL, port=PORT)
rdn2 = RaidenAPIWrapper(ip=URL, port=PORT2)

latencies = []
for i in range(20):
    latencies.append(ping_pong_transaction(rdn, rdn2, PARTNER1, PARTNER4, TOKEN_ADDR))
analyze_ping_pong_transactions(latencies)

with open("latencies_pc_loss_50", 'wb') as out:
    pickle.dump(latencies, out, pickle.HIGHEST_PROTOCOL)
