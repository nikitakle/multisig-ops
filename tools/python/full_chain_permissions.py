import requests
import json
import pandas as pd
import os
import re
from dotenv import load_dotenv
from helpers.addresses import get_registry_by_chain_id
from web3 import Web3
from dotmap import DotMap
# from great_ape_safe import GreatApeSafe
import collections

INFURA_KEY = os.getenv('WEB3_INFURA_PROJECT_ID')

w3_by_chain = {
    "mainnet": Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}")),
    "arbitrum": Web3(Web3.HTTPProvider(f"https://arbitrum-mainnet.infura.io/v3/{INFURA_KEY}")),
    "optimism": Web3(Web3.HTTPProvider(f"https://optimism-mainnet.infura.io/v3/{INFURA_KEY}")),
    "polygon": Web3(Web3.HTTPProvider(f"https://polygon-mainnet.infura.io/v3/{INFURA_KEY}")),
    "gnosis": Web3(Web3.HTTPProvider(f"https://rpc.gnosischain.com/"))
}

ALL_CHAINS_MAP = {
    "mainnet": 1,
    "polygon": 137,
    "arbitrum": 42161,
    "optimism": 10,
    "gnosis": 100
}


def monorepo_names_by_address(chain_name):
    r = get_registry_by_chain_id(ALL_CHAINS_MAP[chain_name])  # todo adapt to handle given chain
    monorepo_names = {}
    response = requests.get(
        f"https://raw.githubusercontent.com/balancer-labs/balancer-v2-monorepo/master/pkg/deployments/addresses/{chain_name}.json")
    data = response.json()
    for address, info in data.items():
        monorepo_names[address] = info["name"]
    for name, address in r.balancer.multisigs.items():
        monorepo_names[address] = name
    for name, address in r.balancer.relayers.items():
        monorepo_names[address] = name
    monorepo_names["0xE4a8ed6c1D8d048bD29A00946BFcf2DB10E7923B"] = "GauntletFeeSetter" # TODO figure something better out
    monorepo_names["0x5efBb12F01f27F0E020565866effC1dA491E91A4"] = "GaugeAdder"
    return monorepo_names


def build_chain_permissions_list(chain_name):
    r = get_registry_by_chain_id(ALL_CHAINS_MAP[chain_name])  # TODO make chain sensitive
    results = []
    address_names = monorepo_names_by_address(chain_name)
    action_ids_list = f"https://raw.githubusercontent.com/balancer-labs/balancer-v2-monorepo/master/pkg/deployments/action-ids/{chain_name}/action-ids.json"
    w3 = w3_by_chain[chain_name]
    authorizer = w3.eth.contract(address=r.balancer.Authorizer, abi=json.load(open("./abis/Authorizer.json")))
    try:
        result = requests.get(action_ids_list)
    except requests.exceptions.HTTPError as err:
        print(f"URL: {requests.request.url} returned error {err}")
    input = result.json()
    for deployment, contracts in input.items():
        print(f"Processing {deployment}")
        for contract, data in contracts.items():
            for fx, actionId in data["actionIds"].items():
                numMembers = authorizer.functions.getRoleMemberCount(actionId).call()
                if numMembers > 0:
                    memberAddressList = []
                    memberNameList = []
                    for i in range(0, numMembers, 1):
                        caller = (str(authorizer.functions.getRoleMember(actionId, i).call()))
                        memberAddressList.append(caller)
                        try:
                            memberNameList.append(address_names[caller])
                        except:
                            memberNameList.append("undef")

                        d = {
                            "Fx": fx,
                            "Contract": contract,
                            "Deployment": deployment,
                            "Authorized_Caller_Addresses": memberAddressList,
                            "Authorized_Caller_Names": memberNameList
                        }
                        results.append(d)
    return results


def generate_deployment_deduped_map(permission_data):
    results = {}
    for permission in permission_data:
        contract = permission["Contract"]
        fx = permission["Fx"]
        if contract.endswith("Pool"):
            contract = "Pool"
        if contract.endswith("PoolFactory"):
            contract = "PoolFactory"

        if contract not in results.keys():
            results[contract] = {}
        if fx not in results[contract].keys():
            results[contract][fx] = {
                "callerNames": [],
                "callerAddresses": [],
                "deployments": []
            }
        callerNames = list(permission["Authorized_Caller_Names"])
        callerAddresses = list(permission["Authorized_Caller_Addresses"])
        deployments = [permission["Deployment"]]

        results[contract][fx]["callerNames"] = set(callerNames + list(results[contract][fx]["callerNames"]))
        results[contract][fx]["callerAddresses"] = set(callerAddresses + list(results[contract][fx]["callerAddresses"]))
        results[contract][fx]["deployments"] = set(deployments + list(results[contract][fx]["deployments"]))

    return dict(results)


def deployment_deduped_map_to_list(deployment_map):
    result = []
    for contract, fxdata in deployment_map.items():
        for fx, callers in fxdata.items():
            result.append({
                "function": fx.split("(")[0],
                "contract": contract,
                "callerNames": callers["callerNames"],
                "callerAddresses": callers["callerAddresses"],
                "deployments": callers["deployments"]
            })
    return result



def output_list(permission_data, output_name, chain):
    df = pd.DataFrame(permission_data)
    with open(f"./reports/{output_name}.md", "w") as f:
        df.to_markdown(buf=f, index=False)
    with open(f"./reports/{output_name}.csv", "w") as f:
        df.to_csv(f, index=False)
    registry = monorepo_names_by_address(chain)
    with open(f"./reports/{output_name}-registry.json", "w") as f:
        json.dump(registry, f)
    dedup = pd.DataFrame(deployment_deduped_map_to_list(generate_deployment_deduped_map(permission_data)))
    dedup = dedup.sort_values(by=["function", "contract"])
    with open(f"./reports/{output_name}_deploy_dedup.md", "w") as f:

        dedup.to_markdown(buf=f, index=False)


def main(chain="mainnet"):
    permissions = build_chain_permissions_list(chain)
    with open(f"./reports/perm_dump_{chain}.json", "w") as f:
        json.dump(permissions, f)
    with open(f"./reports/perm_dump_{chain}.json", "r") as f:
        permissions = json.load(f)
        output_list(permissions, f"{chain}-permissions", chain)

if __name__ == "__main__":
    main()
