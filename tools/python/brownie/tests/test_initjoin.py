import brownie
import time
import pytest


def test_deploy(deploy):
    return


def test_create_pool(pool):
    return


def test_init_join(helper, ldo, weth, pool, caller, unordered_token_list):
    ldo.approve(helper, 1000000000000, {"from": caller})
    weth.approve(helper, 100000000000, {"from": caller})
    tx = helper.initJoinWeightedPool(pool.getPoolId(), unordered_token_list, [1000000000, 100000], {'from': caller})
    assert pool.balanceOf(caller) > 0
    assert False
    return tx


