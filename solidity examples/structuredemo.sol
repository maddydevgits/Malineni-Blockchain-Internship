pragma solidity 0.6.6;

contract structuredemo {
    struct madhu
    {
        string a;
        uint b;
    }
    
    madhu abc;
    
    function setValues() public
    {
        abc.a='Hello';
        abc.b=3;
    }
    
    function getResult() view public returns(string memory) {
        return(abc.a);
    }
    
}
