# consists blocks
# blocks consist transactions
# blocks are connected through hashing
        # unique digital fingerprint(hash) - transaction + previous blocks fingerprint(hash)
from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Ivan",
                                                     "Maria sent 5 BTC to Jenny",
                                                     "Satoshi sent 5 BTC to Hal Finney"])
# genesis_block.block_hash -> second_block.previous_block
second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz"])
third_block = Block(second_block.block_hash, ["A to C 5 BTC",
                                               "G to D 4 BTC"])

print("genesis_block.block_hash:\n", genesis_block.block_hash)
print("second_block.block_hash:\n", second_block.block_hash)
print("third_block.block_hash:\n", third_block.block_hash)

print("\ngenesis_block.block_hash == second_block.previous_hash:\n", genesis_block.block_hash == second_block.previous_hash)
print("\nsecond_block.block_hash == third_block.previous_hash:\n", second_block.block_hash == third_block.previous_hash)