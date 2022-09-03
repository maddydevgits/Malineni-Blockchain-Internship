/*
    Demo Program
*/
pragma solidity 0.6.6;

// We are creating a contract
contract madblocks {
    uint private m; // m - var, public - scope, uint - datatype
    // m - state variable (public) - uint - uint256
    // uint8 - 8 bits 
    // uint - 256 bits
    
    // logic to assign a value to it.
    // m=30 
    
    function setValue(uint a) public {
        m=a; // the value of a is assigned to m
        // a is local variable, m is state variable
    }
    
    function getValue() public view returns(uint) {
        return(m);
    }
}
