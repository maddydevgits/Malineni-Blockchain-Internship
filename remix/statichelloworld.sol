pragma solidity 0.8.13; // which tells about the solidity version

contract HelloWorld {    // creating contract with the name hello wolrd 
    string s="hello world";   // creating one varible with static text as hello wolrd 
    function sample() public view returns (string memory) {  //created function as sample with public acces specifier 
        return s;                                             // returing variable 
    }  
}
