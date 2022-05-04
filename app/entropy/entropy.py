import math
from typing import List
import os
from app.resources.logger import logger


def get_block_entropy(block: bytes, block_size: int) -> float:
    # start counters
    counters = {byte: 0 for byte in range(2 ** 8)}
    for byte in block:
        counters[byte] += 1
    # calculate probabilities for each byte
    probabilities = [counter / block_size for counter in counters.values()]
    # final sum
    entropy = -sum(
        probability * math.log2(probability)
        for probability in probabilities if probability > 0
        )
    return entropy


def get_file_entropy(file_name: str, block_size: int) -> List[float]:
    entropy_detail = []
    f = open(file_name, "rb")
    block = f.read(block_size)
    # get entropy for each block
    while block:
        entropy = get_block_entropy(block, block_size)
        entropy_detail.append(float(f'{entropy:.2f}'))
        block = f.read(block_size)
    f.close()
    return entropy_detail


def get_entropy_summary(entropy_detail: List[float]) -> dict:
    low_entropy_blocks = len([x for x in entropy_detail if x < 2])
    high_entropy_blocks = len([x for x in entropy_detail if x > 7])
    entropy_summary = {
        "low_entropy_blocks": low_entropy_blocks,
        "high_entryopy_blocks": high_entropy_blocks
    }
    return entropy_summary


def delete_saved_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def generate_entropy_report(file_name: str, block_size: int) -> dict:
    try:
        entropy_detail = get_file_entropy(file_name, block_size)
        entropy_summary = get_entropy_summary(entropy_detail)
        response = {
            "entropyDetail": entropy_detail,
            "summary": entropy_summary
        }
        delete_saved_file(file_name)
        return response
    except Exception as e:
        logger.error(f"Exception raised: {e} , deleting saved file.")
        delete_saved_file(file_name)
        raise e
