pragma solidity 0.6.6;

contract arraydemo {
    uint[3] private a;
    
    function setValues() public {
        a[0]=22;
        a[1]=21;
        a[2]=20;
    }
    function getValues(uint i) public view returns(uint) {
        return(a[i]);
    }
}
