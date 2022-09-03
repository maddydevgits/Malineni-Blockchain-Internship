pragma solidity 0.6.6;

contract fmdemo {
    string private a;
    address owner;
    
    constructor() public // whenever smart contract -> owner
    {
        owner=msg.sender; // msg is a global variable
    }
    
    modifier onlyOwner() 
    {
        require(msg.sender==owner);
        _;
    }
    function setHello(string memory b) onlyOwner public {
        a=b;
    } 
    
    function getHello() public onlyOwner view returns(string memory) {
        return (a);        
    }
    
}
