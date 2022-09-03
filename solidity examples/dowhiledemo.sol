pragma solidity 0.6.6;

contract dowhile {
    uint private m;
    uint public sum=0;
    
    function setValue(uint a) public {
        m=a;
    }
    
    function computation() public {
        uint dummy;
        uint b;
        b=m;
        do
        {
            dummy=b%10;
            sum+=dummy;
            b=b/10;
        }while(b>0);
    }
}
