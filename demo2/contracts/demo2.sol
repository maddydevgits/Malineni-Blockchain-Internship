// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract demo2 {
  string m;

  function insertmessage(string memory a) public {
    m=a;
  }
  function viewmessage() public view returns(string memory){

    return m;
  }

}
