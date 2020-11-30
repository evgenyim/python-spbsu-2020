"""Hw4."""
from tornado import httpclient
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class MainHandler(RequestHandler):
    """Handler for requests."""

    async def get(self):
        """Override of method which handles requests."""
        init_headers = ['Server', 'Content-Type', 'Date']
        number = self.request.path.split('/')[-1]
        response = await self.get_response(number)
        for header in init_headers:
            self.clear_header(header)
        self.set_status(response.code)
        self.write(response.body)
        self.add_headers(response)

    def add_headers(self, response):
        """Add headers got from response.

        Args:
            response: response from server.
        """
        for header, body in response.headers.get_all():
            # adding this strings would allow to see response body in browser
            # if header == 'Transfer-Encoding':   :noqa E800
            #    continue
            self.add_header(header, body)

    async def get_response(self, number):
        """Get response from target server.

        Args:
            number: additional number for address.

        Returns:
            response: response got fro server
        """
        client = httpclient.AsyncHTTPClient()
        address = 'https://jsonplaceholder.typicode.com/todos/'
        address += number
        response = await client.fetch(address)
        client.close()
        return response


def make_app():
    """Create app with correct routes.

    Returns:
        app: created application.
    """
    return Application([
        (r'/todo/[0-9]+', MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    port_number = 8888
    app.listen(port_number)
    IOLoop.current().start()
