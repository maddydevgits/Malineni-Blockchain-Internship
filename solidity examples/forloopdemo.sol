pragma solidity 0.6.6;

contract forloopdemo {
    uint private m;
    uint public factorial=1;
    
    function setValue(uint a) public {
        m=a;    
    }
    
    function computation() public {
        uint i;
        for(i=1;i<=m;i++) // i = 4, 4<=3
        {
            factorial*=i; // 1*2*3
        }
    }
}
