"""
reads in master accounts file
then applies all days transactions from merged trans file
to the master accounts fiel

master accoutsn file
acc num balance acc name

must be in ascending order

at end must produce new validaccounts file


reads in merged trans file
ends in 00
for each line perform said transaciton on master accounts

constraints
no negative balances
deleted account has zero balance, dpes it disappear
created account should not have existing acc num,, 2 create same number
nam egiven for delete myst have a mathcing name

constraint fails and the fatal error stop
"""