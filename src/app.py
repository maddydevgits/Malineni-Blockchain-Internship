from flask import Flask,render_template, redirect, request
from web3 import Web3, HTTPProvider
from ca import *
import json
from SendEmail import *
import time

def connect_with_blockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:8545'))
    if(acc==0):
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    compiled_contract_path='../build/contracts/hotel.json'
    deployed_contract_address=hotelContractAddress

    with open(compiled_contract_path) as file:
        contract_json=json.load(file)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)
    return contract, web3

app=Flask(__name__)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/rooms-tariff')
def roomstariff():
    return render_template('rooms-tariff.html')

@app.route('/room-details')
def roomdetails():
    return render_template('room-details.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/bookRoom',methods=['GET','POST'])
def bookRoom():
    walletaddr=request.form['walletaddr']
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    rooms=int(request.form['rooms'])
    adults=int(request.form['adults'])
    date=int(request.form['date'])
    month=int(request.form['month'])
    year=int(request.form['year'])
    message=(request.form['message'])
    print(walletaddr,name,email,phone,rooms,adults,date,month,year,message)
    contract,web3=connect_with_blockchain(0)
    tx_hash=contract.functions.bookRoom(walletaddr,name,email,phone,rooms,adults,date,month,year,message).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    verifyIdentity(email)
    while True:
        try:
            a=sendmessage('Rooms Booked at Hotel Holiday Crown, Dubai',walletaddr,name,phone,rooms,adults,date,month,year,email)
            if(a):
                break
            else:
                continue
        except:
            time.sleep(10)
    return render_template('index.html')

@app.route('/customer')
def customers():
    data=[]
    contract,web3=connect_with_blockchain(0)
    _customers,_names,_emails,_phones,_rooms,_adults,_dates,_months,_years,_messages=contract.functions.viewRooms().call()
    for i in range(len(_customers)):
        dummy=[]
        dummy.append(_customers[i])
        dummy.append(_names[i])
        dummy.append(_emails[i])
        dummy.append(_phones[i])
        dummy.append(_rooms[i])
        dummy.append(_adults[i])
        dummy.append(str(_dates[i])+'/'+str(_months[i])+'/'+str(_years[i]))
        dummy.append(_messages[i])
        data.append(dummy)
    l=len(data)
    return render_template('customers.html',dashboard_data=data,len=l)

if __name__=="__main__":
    app.run(debug=True)