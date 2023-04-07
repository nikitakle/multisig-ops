import brownie
import time
import pytest


def test_deploy(deploy):
    return


def test_create_pool(pool):
    return


def test_init_join_unordered(helper, ldo, weth, pool, caller, unordered_token_list):
    ldo.approve(helper, 1000000000000, {"from": caller})
    weth.approve(helper, 100000000000, {"from": caller})
    with brownie.reverts("BAL#520"):
        tx = helper.initJoinWeightedPool(pool.getPoolId(), unordered_token_list, [1000000000, 100000], {'from': caller})


def test_init_join_ordered(helper, ldo, weth, pool, caller, ordered_token_list):
    ldo.approve(helper, 20*10**18, {"from": caller})
    weth.approve(helper, 100000000000, {"from": caller})
    tx = helper.initJoinWeightedPool(pool.getPoolId(), ordered_token_list, [1000000000, 100000], {'from': caller})
    assert pool.balanceOf(caller) > 0
    return tx

def test_init_join_use_orderer(helper, ldo, weth, pool, caller):
    weth.approve(helper, 10000000, {"from": caller})
    ldo.approve(helper, 1000000000, {"from": caller})
    tokens = [weth, ldo]
    amounts = [10000000, 1000000000]
    sortTokens, sortAmounts = helper.sortAmountsByAddresses(tokens, amounts)
    tx = helper.initJoinWeightedPool(pool.getPoolId(), sortTokens, sortAmounts, {'from': caller})
    assert pool.balanceOf(caller) > 0
    return tx

def test_create_and_join(helper, ldo, weth, caller, ordered_token_list):
    weth.approve(helper, 10000000, {"from": caller})
    ldo.approve(helper, 1000000000, {"from": caller})
    tokens = [weth, ldo]
    amounts = [10000000, 1000000000]
    sortTokens, sortAmounts = helper.sortAmountsByAddresses(tokens, amounts)
    tx = helper.createAndJoinWeightedPool("LDO/WETH", "B-50LDO-50WETH", sortTokens, [], sortAmounts, [50,50], 300, b"how 'bout some pepper?")
    return tx