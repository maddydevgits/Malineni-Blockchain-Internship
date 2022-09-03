pragma solidity 0.6.6;

contract enumerateddemo {
    enum abc {ORANGE, MANGO, APPLE}
    abc choice;
    
    function setChoice() public
    {
        choice=abc.APPLE;
    }
    function getChoice() public view returns(uint) {
        return uint(choice);
    }
    
}
