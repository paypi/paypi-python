from gql import gql
import asyncio


class User:
    def __init__(self, api_secret, subscriber_secret, session):
        self.api_secret = api_secret
        self.subscriber_secret = subscriber_secret
        self.session = session

    async def make_charge_async(self, charge_identifier, units_used=1):
        make_charge_mutation = gql("""
            mutation makeCharge(
                $charge_ident: String!
                $sub_secret: String!
                $units_used: Int
            ) {
                makeCharge(
                    input: {
                        chargeIdentifier: $charge_ident
                        subscriptionSecret: $sub_secret
                        unitsUsed: $units_used
                    }
                ) {
                    success
                }
            }
        """)

        params = {
            "service_secret": self.api_secret,
            "sub_secret": self.subscriber_secret,
            "charge_ident": charge_identifier
        }

        result = await self.session.execute_async(make_charge_mutation, variable_values=params)

    def make_charge(self, charge_identifier, units_used=1):
        asyncio.run(self.make_charge_async(charge_identifier, units_used))
