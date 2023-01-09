## Welcome to the Balancer Multisig Operations Repo
This repo is used to store payloads uploaded to the multisig, as well as any tooling used to generate such payloads.

### Uploading transaction JSONs as part of Balancer Governance
Balancer Governance requires that a link to a PR request in this repo with a transaction builder JSON is included.

PR's should be to include a single file named `BIP-XXX.json` in the `BIPs` directory where XXX is the number of the BIP.  The PR should include the BIP title as it's commit/pr text.
An example of how to upload such a JSON for a gauge request can be found here: [BIPs/examples/gauge-request](BIPs/Examples/gauge-request)

### Balancer Multisigs
Here are a list of multisigs controlled by the Maxis

| Name                          | Purpose                                                                                                                                 | Chain                                                                                                                                                                                                                                                                           | Address                                    |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Protocol Fees Multisig        | Collect fees, and set A-Factors and Fees on pools (default pool-owner, except on mainnet where a separate multisig is used to set fees. | [MAINNET](https://gnosis-safe.io/app/eth:0x7c68c42De679ffB0f16216154C996C354cF1161B/home), [ARBI](https://gnosis-safe.io/app/arb1:0x7c68c42De679ffB0f16216154C996C354cF1161B/home), [POLYGON](https://gnosis-safe.io/app/matic:0x7c68c42De679ffB0f16216154C996C354cF1161B/home) | 0x7c68c42De679ffB0f16216154C996C354cF1161B |
| Mainnet Fee Setter            | Default pool owner for Mainnet that can set A-Factors and protocol fees.                                                                | [MAINNET](https://gnosis-safe.io/app/eth:0xf4A80929163C5179Ca042E1B292F5EFBBE3D89e6/home)                                                                                                                                                                                       | 0xf4A80929163C5179Ca042E1B292F5EFBBE3D89e6 |
| Gauge Controller(LM Multisig) | Used to manage gauges and Reward Tokens and manage liquidity supplied to multichain (bridge).  New Gauge requests go here.              | [MAINNET](https://gnosis-safe.io/app/eth:0xc38c5f97B34E175FFd35407fc91a937300E33860/home), [ARBI](https://gnosis-safe.io/app/arb1:0xc38c5f97B34E175FFd35407fc91a937300E33860/home), [POLYGON](https://gnosis-safe.io/app/matic:0xc38c5f97B34E175FFd35407fc91a937300E33860/home) | 0xc38c5f97B34E175FFd35407fc91a937300E33860 |
| Linear Pool Control           | Manage limits on Mainnet Linear Pools                                                                                                   | [MAINNET](https://gnosis-safe.io/app/eth:0x75a52c0e32397A3FC0c052E2CeB3479802713Cf4/home)                                                                                                                                                                                       | 0x75a52c0e32397A3FC0c052E2CeB3479802713Cf4 |
| Maxi Operational Payments     | Holds the Maxi Budget and is used to pay people and expenses.                                                                           | [MAINNET](https://gnosis-safe.io/app/eth:0x166f54F44F271407f24AA1BE415a730035637325/home)                                                                                                                                                                                       | 0x166f54F44F271407f24AA1BE415a730035637325 |


### Need Help
You can contact Tritum, Solarcurve or any of the BAL Maxis on the Balancer Discord for help getting your JSON PR submitted.  We can also just do it for you if that's what you'd prefer.