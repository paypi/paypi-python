from paypi import PayPI
import asyncio

api_secret = "<API SECRET>"
subscriber_secret = "<SUBSCRIBER SECRET>"
charge_id = "<CHARGE ID>"

paypi = PayPI(api_secret)
user = paypi.authenticate_sync(subscriber_secret)
user.make_charge_sync(charge_id)
