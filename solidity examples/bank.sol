pragma solidity 0.6.6;

contract klhmadhu {
    
    uint private bal=0; // state
    
    function reviewBalance() public view returns (uint) {
        return (bal);
    }
    
    function depositMoney(uint m) public {
        bal+=m;
    }
    
    function withdrawMoney(uint m) public returns(bool) {
        if(bal>=m) {
            bal-=m;
            return true;
        }        
        else {
            return false;
        }
    }
}
