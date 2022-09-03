pragma solidity 0.6.6;

contract greatest {
    uint private a=33;
    uint private b=25;
    uint private c=7;
    
    string public m;
    
    function computation() public {
        if(a>b && a>c)
            m='a is greater';
        else if(b>a && b>c)
            m='b is greater';
        else
            m='c is greater';
    }
    
}
