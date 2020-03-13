'''
    vngshare - Vserver-like Notebook Grader Share
    Similar to vserver; allows easy testing.
'''

# pylint: disable=abstract-method
# pylint: disable=function-redefined
# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import

import sys
from ngshare import *

class MockAuth(HubAuthenticated):
    '''
        Mock class substituting HubAuthenticated
    '''
    def get_login_url(self):
        return 'http://example.com/'

    def get_current_user(self):
        if type(self).__name__ in ('HomePage', 'Favicon', 'InitDatabase'):
            user = self.get_argument('user', 'user')
        else:
            user = self.get_argument('user')
        return {'name': user}

MyRequestHandler.__bases__ = (MockAuth, RequestHandler, MyHelpers)

def main():
    'Main function'
    parser = argparse.ArgumentParser(
        description='vngshare, Vserver-like ngshare (Notebook Grader Share)')
    parser.add_argument('--prefix', help='URL prefix', default='/api/')
    parser.add_argument('--no-debug', help='disable debug', action='store_true')
    parser.add_argument('--database', help='database url',
                        default='sqlite:////tmp/ngshare.db')
    parser.add_argument('--host', help='bind hostname', default='127.0.0.1')
    parser.add_argument('--port', help='bind port', type=int, default=12121)
    args = parser.parse_args()

    app = MyApplication(args.prefix, args.database, debug=not args.no_debug)

    http_server = HTTPServer(app)
    http_server.listen(args.port, args.host)

    print('Starting vngshare (Vserver-like Notebook Grader Share)')
    print('Database file is %s' % repr(args.database))
    print('Please go to http://%s:%d/api/' % (args.host, args.port))
    IOLoop.current().start()

if __name__ == '__main__':
    main()
