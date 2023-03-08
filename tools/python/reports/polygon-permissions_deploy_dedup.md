| function                          | contract                                       | callerNames                                 | callerAddresses                                                                                                                                                                          | deployments                                                                                                                    |
|:----------------------------------|:-----------------------------------------------|:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| addPoolFactory                    | PoolRecoveryHelper                             | {'undef'}                                   | {'0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                                                                           | {'20221123-pool-recovery-helper'}                                                                                              |
| addTokenToGauge                   | ChildChainGaugeTokenAdder                      | {'lm'}                                      | {'0xc38c5f97B34E175FFd35407fc91a937300E33860'}                                                                                                                                           | {'20220527-child-chain-gauge-token-adder'}                                                                                     |
| add_reward                        | ChildChainStreamer                             | {'ChildChainGaugeTokenAdder'}               | {'0x1554ee754707D5C93b7934AF404747Aba521Aaf2'}                                                                                                                                           | {'20220413-child-chain-gauge-factory'}                                                                                         |
| batchSwap                         | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| denylistToken                     | ProtocolFeesWithdrawer                         | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220517-protocol-fee-withdrawer'}                                                                                           |
| disable                           | AaveLinearPoolFactory                          | {'undef', 'emergency'}                      | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                             | {'20220817-aave-rebalanced-linear-pool', '20230206-aave-rebalanced-linear-pool-v4', '20221207-aave-rebalanced-linear-pool-v3'} |
| disable                           | ComposableStablePoolFactory                    | {'undef', 'emergency'}                      | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                             | {'20221122-composable-stable-pool-v2', '20230206-composable-stable-pool-v3', '20220906-composable-stable-pool'}                |
| disable                           | ERC4626LinearPoolFactory                       | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20230206-erc4626-linear-pool-v3'}                                                                                            |
| disable                           | ManagedPoolFactory                             | {'undef', 'emergency'}                      | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                             | {'20221021-managed-pool'}                                                                                                      |
| disable                           | NoProtocolFeeLiquidityBootstrappingPoolFactory | {'undef', 'emergency'}                      | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                             | {'20211202-no-protocol-fee-lbp'}                                                                                               |
| disable                           | WeightedPoolFactory                            | {'undef', 'emergency'}                      | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                             | {'20220908-weighted-pool-v2', '20230206-weighted-pool-v3'}                                                                     |
| disable                           | YearnLinearPoolFactory                         | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20230213-yearn-linear-pool'}                                                                                                 |
| enableRecoveryMode                | AaveLinearPool                                 | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220817-aave-rebalanced-linear-pool', '20221207-aave-rebalanced-linear-pool-v3'}                                            |
| enableRecoveryMode                | ComposableStablePool                           | {'PoolRecoveryHelper', 'emergency'}         | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0x495F696430F4A51F7fcB98FbE68a9Cb7A07fB1bA'}                                                                                             | {'20230206-composable-stable-pool-v3', '20221122-composable-stable-pool-v2', '20220906-composable-stable-pool'}                |
| enableRecoveryMode                | StablePool                                     | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220609-stable-pool-v2'}                                                                                                    |
| enableRecoveryMode                | WeightedPool                                   | {'PoolRecoveryHelper', 'emergency'}         | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846', '0x495F696430F4A51F7fcB98FbE68a9Cb7A07fB1bA'}                                                                                             | {'20220908-weighted-pool-v2', '20230206-weighted-pool-v3'}                                                                     |
| exitPool                          | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| joinPool                          | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| manageUserBalance                 | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| notify_reward_amount              | ChildChainStreamer                             | {'undef'}                                   | {'0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                                                                           | {'20220413-child-chain-gauge-factory'}                                                                                         |
| pause                             | AaveLinearPool                                 | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220817-aave-rebalanced-linear-pool'}                                                                                       |
| pause                             | ComposableStablePool                           | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20221122-composable-stable-pool-v2', '20230206-composable-stable-pool-v3', '20220906-composable-stable-pool'}                |
| pause                             | WeightedPool                                   | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220908-weighted-pool-v2', '20230206-weighted-pool-v3'}                                                                     |
| removePoolFactory                 | PoolRecoveryHelper                             | {'undef'}                                   | {'0xf9D6BdE5c2eef334AC88204CB2eEc07111DCBA97'}                                                                                                                                           | {'20221123-pool-recovery-helper'}                                                                                              |
| setFeeTypePercentage              | ProtocolFeePercentagesProvider                 | {'undef'}                                   | {'0xd2bD536ADB0198f74D5f4f2Bd4Fe68Bae1e1Ba80'}                                                                                                                                           | {'20220725-protocol-fee-percentages-provider'}                                                                                 |
| setFlashLoanFeePercentage         | ProtocolFeesCollector                          | {'ProtocolFeePercentagesProvider'}          | {'0x42AC0e6FA47385D55Aff070d79eF0079868C48a6'}                                                                                                                                           | {'20210418-vault'}                                                                                                             |
| setRelayerApproval                | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| setSwapFeePercentage              | AaveLinearPool                                 | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220817-aave-rebalanced-linear-pool', '20230206-aave-rebalanced-linear-pool-v4'}                                            |
| setSwapFeePercentage              | ComposableStablePool                           | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20221122-composable-stable-pool-v2', '20230206-composable-stable-pool-v3', '20220906-composable-stable-pool'}                |
| setSwapFeePercentage              | ERC4626LinearPool                              | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20230206-erc4626-linear-pool-v3'}                                                                                            |
| setSwapFeePercentage              | ProtocolFeesCollector                          | {'undef', 'ProtocolFeePercentagesProvider'} | {'0xd2bD536ADB0198f74D5f4f2Bd4Fe68Bae1e1Ba80', '0x42AC0e6FA47385D55Aff070d79eF0079868C48a6'}                                                                                             | {'20210418-vault'}                                                                                                             |
| setSwapFeePercentage              | StablePool                                     | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220609-stable-pool-v2', '20210624-stable-pool'}                                                                            |
| setSwapFeePercentage              | WeightedPool                                   | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220908-weighted-pool-v2', '20230206-weighted-pool-v3'}                                                                     |
| setSwapFeePercentage              | YearnLinearPool                                | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20230213-yearn-linear-pool'}                                                                                                 |
| setTargets                        | AaveLinearPool                                 | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220817-aave-rebalanced-linear-pool', '20230206-aave-rebalanced-linear-pool-v4'}                                            |
| setTargets                        | ERC4626LinearPool                              | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20230206-erc4626-linear-pool-v3'}                                                                                            |
| setTargets                        | YearnLinearPool                                | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20230213-yearn-linear-pool'}                                                                                                 |
| set_rewards                       | RewardsOnlyGauge                               | {'ChildChainGaugeTokenAdder'}               | {'0x1554ee754707D5C93b7934AF404747Aba521Aaf2'}                                                                                                                                           | {'20220413-child-chain-gauge-factory'}                                                                                         |
| startAmplificationParameterUpdate | ComposableStablePool                           | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20221122-composable-stable-pool-v2', '20230206-composable-stable-pool-v3', '20220906-composable-stable-pool'}                |
| startAmplificationParameterUpdate | StablePool                                     | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220609-stable-pool-v2', '20210624-stable-pool'}                                                                            |
| stopAmplificationParameterUpdate  | ComposableStablePool                           | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20221122-composable-stable-pool-v2', '20230206-composable-stable-pool-v3', '20220906-composable-stable-pool'}                |
| stopAmplificationParameterUpdate  | StablePool                                     | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220609-stable-pool-v2', '20210624-stable-pool'}                                                                            |
| swap                              | Vault                                          | {'BalancerRelayer'}                         | {'0x28A224d9d398a1eBB7BA69BCA515898966Bb1B6b', '0x4574ccBcC09A00C9eE55fB92Fe353699A4fA800e', '0xcf6a66E32dCa0e26AcC3426b851FD8aCbF12Dac7', '0xF537dDd7f4cc72C6C08866b62EAe9378f1F62da8'} | {'20210418-vault'}                                                                                                             |
| unpause                           | AaveLinearPool                                 | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220817-aave-rebalanced-linear-pool'}                                                                                       |
| unpause                           | ComposableStablePool                           | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220906-composable-stable-pool', '20221122-composable-stable-pool-v2'}                                                      |
| unpause                           | WeightedPool                                   | {'emergency'}                               | {'0x3c58668054c299bE836a0bBB028Bee3aD4724846'}                                                                                                                                           | {'20220908-weighted-pool-v2'}                                                                                                  |
| withdrawCollectedFees             | ProtocolFeesCollector                          | {'ProtocolFeesWithdrawer'}                  | {'0xEF44D6786b2b4d544b7850Fe67CE6381626Bf2D6'}                                                                                                                                           | {'20210418-vault'}                                                                                                             |
| withdrawCollectedFees             | ProtocolFeesWithdrawer                         | {'feeManager'}                              | {'0x7c68c42De679ffB0f16216154C996C354cF1161B'}                                                                                                                                           | {'20220517-protocol-fee-withdrawer'}                                                                                           |