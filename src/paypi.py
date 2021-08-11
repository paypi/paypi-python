from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from user import User
import asyncio

# DEFAULT_HOST = "http://localhost:8080"
# DEFAULT_BASE_PATH = "/graphql"
DEFAULT_HOST = "https://api.paypi.dev:443"
DEFAULT_BASE_PATH = "/graphql"


class UserKeyNotValid(Exception):
    pass


class PayPI:
    def __init__(self, key, host=DEFAULT_HOST, base_path=DEFAULT_BASE_PATH):
        self.key = key
        self.connection_string = f"{host}{base_path}"
        self.transport = AIOHTTPTransport(url=self.connection_string)
        self.session = Client(transport=self.transport)

    async def authenticate_async(self, subscriber_secret):
        authenticate_client_mutation = gql("""
            mutation AuthenticateClient(
                $service_secret: String!
                $sub_secret: String!
            ) {
                checkSubscriberSecret(
                    input: {
                        serviceSecret: $service_secret
                        subscriptionSecret: $sub_secret
                    }
                ) {
                    isAuthed
                }
            }
        """)

        params = {
            "service_secret": self.key,
            "sub_secret": subscriber_secret
        }

        result = await self.session.execute_async(authenticate_client_mutation, variable_values=params)

        if not result['checkSubscriberSecret']['isAuthed']:
            raise UserKeyNotValid("Provided user key is not valid")

        return User(self.key, subscriber_secret, self.session)

    def authenticate(self, subscriber_secret):
        return asyncio.run(self.authenticate_async(subscriber_secret))
