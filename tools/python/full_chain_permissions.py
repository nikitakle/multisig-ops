import requests
import json
import pandas as pd
import os
import re
from dotenv import load_dotenv
from helpers.addresses import get_registry_by_chain_id
from web3 import Web3
from dotmap import DotMap
#from great_ape_safe import GreatApeSafe

INFURA_KEY  = os.getenv('WEB3_INFURA_PROJECT_ID')

w3_by_chain ={
    "mainnet": Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}")),
    "arbitrum": Web3(Web3.HTTPProvider(f"https://arbitrum-mainnet.infura.io/v3/{INFURA_KEY}")),
    "optimism": Web3(Web3.HTTPProvider(f"https://optimism-mainnet.infura.io/v3/{INFURA_KEY}")),
    "polygon": Web3(Web3.HTTPProvider(f"https://polygon-mainnet.infura.io/v3/{INFURA_KEY}")),
    "gnosis" :Web3(Web3.HTTPProvider(f"https://rpc.gnosischain.com/"))
}


def monorepo_names_by_address(chain_name):
    r = get_registry_by_chain_id(1) #todo adapt to handle given chain
    monorepo_names = {}
    response = requests.get(
        f"https://raw.githubusercontent.com/balancer-labs/balancer-v2-monorepo/master/pkg/deployments/addresses/{chain_name}.json")
    data = response.json()
    for address, info in data.items():
        monorepo_names[address] = info["name"]
    for name, address in r.balancer.multisigs.items():
        print(name)
        monorepo_names[address] = name
    return monorepo_names



def build_chain_permissions_list(chain_name):
    r = get_registry_by_chain_id(1) #TODO make chain sensitive
    results= []
    address_names = monorepo_names_by_address(chain_name)
    action_ids_list = f"https://raw.githubusercontent.com/balancer-labs/balancer-v2-monorepo/master/pkg/deployments/action-ids/{chain_name}/action-ids.json"
    w3 = w3_by_chain[chain_name]
    authorizer=w3.eth.contract(address=r.balancer.Authorizer, abi=json.load(open("./abis/Authorizer.json")))
    try:
        result = requests.get(action_ids_list)
    except requests.exceptions.HTTPError as err:
        print(f"URL: {requests.request.url} returned error {err}")
    input = result.json()
    for deployment, contracts in input.items():
        print (f"Processing {deployment}")
        for contract, data in contracts.items():
            for fx, actionId in data["actionIds"].items():
                numMembers = authorizer.functions.getRoleMemberCount(actionId).call()
                if numMembers >0:
                    memberAddressList = []
                    memberNameList= []
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
                            "Authorized _Caller_Names": memberNameList
                        }
                        results.append(d)
    return results

def output_list(permission_data, output_name):
    df = pd.DataFrame(permission_data)
    with open(f"./reports/{output_name}.md", "w") as f:
        df.to_markdown(buf=f, index=False)
    with open(f"./reports/{output_name}.csv", "w") as f:
        df.to_csv(f, index=False)
    registry = monorepo_names_by_address("mainnet")
    with open(f"./reports/{output_name}-registry.json", "w") as f:
        json.dump(registry, f)

def main():
    #permissions = build_chain_permissions_list("mainnet")
    #with open(f"./reports/perm_dump_mainnet.json", "w") as f:
    #    json.dump(permissions, f)
    with open(f"./reports/perm_dump_mainnet.json", "r") as f:
        output_list(json.load(f), "mainnet-permissions")


if __name__ == "__main__":
    main()


