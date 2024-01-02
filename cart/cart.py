import uuid
# 9yvm91ktmttrpi8axlxayuotoha7ufe8
# 7qfmuvqio5ie1b5w8sad219b561o3ea2


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {'fav_number': 13}

        self.cart = cart
