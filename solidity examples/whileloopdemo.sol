// Program to calculate sum of all the digits
pragma solidity 0.6.6;

contract whileloop {
    uint private m;
    uint public sum=0;
    
    function setValue(uint a) public {
        m=a;
    }
    
    function computation(uint b) private {
        uint dummy;
        while(b>0) // 1 
        {
            dummy=b%10; // 1
            sum+=dummy; // 3+2 = 5+1
            b=b/10; // 0
        }
    }
    
    function returnResult() public returns(uint) {
        computation(m);
        return (sum);
    }
}
