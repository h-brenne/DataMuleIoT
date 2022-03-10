from raiden_api_client.exceptions import (
    RaidenAPIConflictException
)
from raiden_api_client.wrapper import RaidenAPIWrapper

ADDRESS = "0x3860601ba03e0B42410712d47c0622cEF5166844"
URL = "0.0.0.0"
PORT = "5001"

amount = 100000000000000000000 # 100 tokens

TOKEN_TT2 = "0x59105441977ecD9d805A4f5b060E34676F50F806" 
TOKEN_SVT = "0x5Fc523e13fBAc2140F056AD7A96De2cC0C4Cc63A" 

rdn = RaidenAPIWrapper(ip=URL, port=PORT)

print(rdn.mint_tokens(token=TOKEN_TT2, receiver=ADDRESS, amount=amount))
print(rdn.mint_tokens(token=TOKEN_SVT, receiver=ADDRESS, amount=amount))
