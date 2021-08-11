from paypi import PayPI
import asyncio

api_secret = "<API SECRET>"
subscriber_secret = "<SUBSCRIBER SECRET>"
charge_id = "<CHARGE ID>"

paypi = PayPI(api_secret, host="http://localhost:8080")
user = paypi.authenticate(subscriber_secret)
user.make_charge(charge_id)
