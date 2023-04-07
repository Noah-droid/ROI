# subscription/views.py
from ussd.core import UssdView

class SubscriptionView(UssdView):
    def get(self, req):
        # This is the first screen the user will see
        self.session['screen'] = 'start'
        self.session.save()
        return 'Welcome to our subscription service.\n1. Subscribe\n2. Unsubscribe'

    def post(self, req):
        user_input = req.POST.get('text')
        if self.session['screen'] == 'start':
            if user_input == '1':
                # User wants to subscribe
                self.session['screen'] = 'subscribe'
                self.session.save()
                return 'Enter your phone number:'
            elif user_input == '2':
                # User wants to unsubscribe
                self.session['screen'] = 'unsubscribe'
                self.session.save()
                return 'Enter your phone number:'
            else:
                # User entered an invalid option
                return 'Invalid option. Please try again.'

        elif self.session['screen'] == 'subscribe':
            # Here you can add your code to subscribe the user
            # For example, you can add the user's phone number to a database
            return 'Thank you for subscribing!'

        elif self.session['screen'] == 'unsubscribe':
            # Here you can add your code to unsubscribe the user
            # For example, you can remove the user's phone number from the database
            return 'You have been unsubscribed. Goodbye!'
