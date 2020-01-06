{"changed":true,"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","value":"from django import forms \nfrom .models import Order, OrderLineItem\n\nclass MakePaymentForm(forms.Form):\n    \n    MONTH_CHOICES = [(i,i) for i in range(1,12)]\n    YEAR_CHOICES = [(i,i) for i in range (2017,2036)]\n    \n    credit_card_number = forms.CharField(label=\"Credit Card Number\", required = False)\n    cvv = forms.CharField(label='Security code (CVV)', required = False)\n    expiry_month = forms.ChoiceField(label=\"Month\", choices=MONTH_CHOICES, required=False)\n    expiry_year = forms.ChoiceField(label=\"Year\", choices=YEAR_CHOICES, required=False)\n    stripe_id = forms.CharField(widget=forms.HiddenInput)\n    \n    \n    \nclass OrderForm(forms.ModelForm):\n    class Meta: \n        model = Order\n        fields = ('full_name','phone_number', 'country', 'postcode', 'town_or_city','street_address1', 'street_address2', 'country')","undoManager":{"mark":-2,"position":1,"stack":[[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":3},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":57},"end":{"row":12,"column":57},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1578340304333}