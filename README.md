tap_rest_fast_api

Create 3 Simple Python Services:

    Users Service -> Which will deal with users and users only. It should support CRUD for users

    Address Service -> It would keep all of the addresses of the user. One user can have multiple addresses. It should also support CRUD.

    Transaction service -> It would keep a record of all of the transactions based on a user ID -> It would also communicate with the 3rd Party API from my service, make sure you have implemented the correct mechanism for retries and delays.

Please make sure to implement as much as possible from today’s lectures. DTOs would be welcomed too. The general behaviour of the infrastructure should be like follows. If I create a new user, I should be able to provide an address for them in the user service endpoint. When I try to get an user that exists I’d like to receive the recent transactions, the user first and last name + his ID. The Transaction Service should have query parameters that would dictate how many transactions I can get. Transations should be sorted by date. (edited)# tap_rest_fastapi
