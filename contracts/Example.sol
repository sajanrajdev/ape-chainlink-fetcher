// SPDX-License-Identifier: MIT

pragma solidity 0.8.12;
contract Example {

    function test() external pure returns(uint256) {
        // will return type(uint256).max

        uint256 x = 0;
        unchecked { x--; }

        return x;
    }
}