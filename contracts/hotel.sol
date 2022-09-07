// SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity >=0.4.22 <0.9.0;

contract hotel {

  address[] _customers;
  string[] _names;
  string[] _emails;
  string[] _phones;
  uint[] _rooms;
  uint[] _adults;
  uint[] _dates;
  uint[] _months;
  uint[] _years;
  string[] _messages;
  
  function bookRoom(address customer,string memory name, string memory email, string memory phone, uint room, uint adult, uint date, uint month, uint year, string memory message) public {

    _customers.push(customer);
    _names.push(name);
    _emails.push(email);
    _phones.push(phone);
    _rooms.push(room);
    _adults.push(adult);
    _dates.push(date);
    _months.push(month);
    _years.push(year);
    _messages.push(message);
  }

  function viewRooms() public view returns (address[] memory, string[] memory, string[] memory, string[] memory, uint[] memory, uint[] memory, uint[] memory, uint[] memory, uint[] memory, string[] memory) {
    return(_customers,_names,_emails,_phones,_rooms,_adults,_dates,_months,_years,_messages);
  }
}
