import brownie
import time
import pytest


def test_deploy(deploy):
    return


def test_create_pool(pool):
    return


def test_init_join(helper, pool, caller, token_list):
    tx = helper.initJoinWeightedPool(pool.getPoolId(), token_list, [10000000, 100000], {'from': caller})
    return tx

