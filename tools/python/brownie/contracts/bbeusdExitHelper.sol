// SPDX-License-Identifier: MIT

pragma solidity 0.8.16;
import "interfaces/balancer/vault/IVault.sol";
import "interfaces/balancer/pool-stable/IComposableStablePool.sol";
import "interfaces/balancer/pool-linear/ILinearPool.sol";
import "@openzeppelin/contracts/access/Ownable.sol";




/**
 * @title The WeightedPool v4 create and join helper
 * @author tritium.eth
 * @notice This contract attempts to make creating and initjoining a pool easier from etherscan
 */
contract bbeUsdExitHelper is Ownable {
    IVault public constant vault = IVault(0xBA12222222228d8Ba445958a75a0704d566BF2C8);
    IComposableStablePool public constant bbeusd = IComposableStablePool(0x50Cf90B954958480b8DF7958A9E965752F627124);
    ILinearPool public constant bbeusdt = ILinearPool(0x3C640f0d3036Ad85Afa2D5A9E32bE651657B874F);
    ILinearPool public constant bbeusdc = ILinearPool(0xD4e7C1F3DA1144c9E2CfD1b015eDA7652b4a4399);
    ILinearPool public constant bbedai = ILinearPool(0xeB486AF868AeB3b6e53066abc9623b1041b42bc0);


    struct UserBalanceOp {
        uint8 kind;
        address asset;
        uint256 amount;
        address sender;
        address payable recipient;
    }

    function exitLinearPool(address token) private {
        ILinearPool pool = ILinearPool(token);
        address[] memory poolTokens;
        (poolTokens, uint256[], uint256) = vault.getPoolTokens(pool.getPoolId());
        uint256  amount = pool.balanceOf(address(this));
        bytes memory userData = abi.encode(255, amount);
        vault.exitPool(pool.getPoolId(), address(this), address(this), (poolTokens, [0,0,0], userData, true));
    }

     /**
      * @notice Burn bbeusd tokens, extract available unfrozen stablecoinz and send to sender. Leave frozen e-tokens as internal user balances in the vault   At least amount of bbeusd tokens must be approved to the helper.
     * @param amount The number of BPTs to extract, or 0 for all of them.
     */
    function emergenceExit (uint256 amount) public {
        // define stuff here for cheaper gas?
        address[] memory bbeusdPoolTokens = [address(bbeusdt), address(bbeusd), address(bbeusdc), address(bbedai)];
        address[] memory withdrawTokens = [0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48, 0xdAC17F958D2ee523a2206206994597C13D831ec7, 0x6B175474E89094C44Da98b954EedeAC495271d0F];

        uint256 extractAmountWei;
        if(amount == 0){
            extractAmountWei = bbeusd.balanceOf(msg.sender);
        } else
        {
            extractAmountWei = amount * 1e18;
        }


        // Make sure both the contract and the wallet are in expected state before we start.
        require(extractAmountWei <= bbeusd.balanceOf(msg.sender), "Amount is more than Balance");
        require(extractAmountWei <= bbeusd.allowance(msg.sender, address(this)), "Amount is more tha allowance to helper");
        require(bbeusd.balanceOf(address(this)) == 0, "Already bbeusd in the helper, need cleanup");
        require(bbeusdt.balanceOf(address(this)) == 0, "Already bbeusdt in the helper, need cleanup");
        require(bbeusdc.balanceOf(address(this)) == 0, "Already bbeusdc in the helper, need cleanup");
        require(bbedai.balanceOf(address(this)) == 0, "Already bbedai in the helper, need cleanup");

        uint256[] memory amounts = vault.getInternalBalancers(address(this));
        for (uint8 i=0; i<amounts.length; amounts++){
            require(amounts[i] == 0, "Already internal balances in the helper, need cleanup");
        }

        // Get out of bbeUSD - The 255 as the first argument represents an emergency exit
        bytes memory userData = abi.encode(255, extractAmountWei);
        vault.exitPool(bbeusd.getPoolId(), address(this), msg.sender, (bbeusdPoolTokens, [0,0,0,0], userData, false));

        //exit linear pool tokens to internal balances
        exitLinearPool(bbedai);
        exitLinearPool(bbeusdc);
        exitLinearPool(bbeusdt);

        //wd from vault
        UserBalanceOp[] memory oplist = new UserBalanceOp[](withdrawTokens.length);
        for (uint8 i=0; i<withdrawTokens.length; i++) {
            UserBalanceOp memory op;
            op.kind =1;
            op.asset = withdrawTokens[i];
            op.amount = amounts[i];
            op.sender = address(this);
            op.recipient = msg.sender;
            oplist[i] = op;
        }
        vault.managePoolBalance(oplist);
        require(bbeusd.balanceOf(address(this)) == 0, "Leftover bbeusd in the helper.");
        require(bbeusdt.balanceOf(address(this)) == 0, "Leftover bbeusdt in the helper");
        require(bbeusdc.balanceOf(address(this)) == 0, "Leftover bbeusdc in the helper");
        require(bbedai.balanceOf(address(this)) == 0, "Leftover bbedai in the helper");
        amounts = vault.getInternalBalancers(address(this));
        for (uint8 i=0; i<amounts.length; amounts++){
            require(amounts[i] == 0, "Leftover internal balances in the helper");
        }
    }

    function withdrawInternalToHelper(address[] memory tokens) external onlyOwner {
        UserBalanceOp[] memory oplist = new UserBalanceOp[](tokens.length);
        uint256[] memory amounts = vault.getInternalBalancers(address(this));
        for (uint8 i=0; i<tokens.length; i++) {
            UserBalanceOp memory op;
            op.kind = 1;
            op.asset = tokens[i];
            op.amount = amounts[i];
            op.sender = address(this);
            op.recipient = address(this);
            oplist[i] = op;
        }
        vault.managePoolBalance(oplist);
    }

      /**
   * @notice Sweep the full contract's balance for a given ERC-20 token
   * @param token The ERC-20 token which needs to be swept
   * @param payee The address to pay
   */
  function sweep(address token, address payee) external onlyOwner {
    uint256 balance = IERC20(token).balanceOf(address(this));
    IERC20(token).transfer(payee, balance);
  }

}