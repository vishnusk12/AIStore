# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:15:20 2018

@author: Vishnu
"""

budget = ['What is your price range like?', 'How much has been budgeted for the purchase?',
          'What is the price range you have in mind?', 'Could you please state your budget for the purchase?', 
          "What’s your budget like for the purchase?", 
          "How much have you budgeted for the purchase?", 
          'What budget do you have in mind?', 
          'Have you decided a budget for this purchase? If so, could you please elaborate.', 
          'Do you have a price range in mind? If so, could you please specify.',
          'Would you like to specify your budget? If so, would you please mention it.']

specs = ['Do you have any specific brand in mind? If so, could you please specify.', 
         'Are you looking for some specific brand? If so, could you please mention it.', 
         'Have you thought of any brand in mind? If so, could you please specify.', 
         'Do you have any particular phone that you are looking for? If so, could you please mention it.'
         ]

plan = ['What plan do you prefer? A Daily plan or a Weekly plan or Monthly plan?',
        'What plan would you like to have? Daily plan or Weekly plan or Monthly plan?',
        'Please select from the plans. Daily plan or Weekly plan or Monthly plan?', 
        'Please select your preferred choice: Daily , Weekly or Monthly plans?',
        'We have a daily, weekly and monthly plan. Which would you prefer.?',
        'You could choose between a daily, weekly and a monthly plan. Which would you like.?',
        'We have a daily, weekly and a monthly plan. Which would you like to go with.?',
        'Which plan works for you the best.? Daily, weekly or monthly.?', 
        'What kind of plan would you prefer? Daily, weekly or monthly.?',
        'We have a daily, weekly and a monthly plan available. Which would you prefer.?', 
        'We have a daily, weekly and a monthly plan. Which of these would you like.?']

data = ['Are you a regular user of data?', 'Do you use mobile data regularly?', 
        'Do you use a lot of data regularly?', 'Would you regularly use a lot of mobile data?', 
        'Do you frequently use mobile data?', 'Do you use mobile data frequently?', 'Do you use mobile data a lot?']

voice = ['Do you use voice calls regularly?', 'Are you a person who regularly uses voice calls?', 
         'Do you use voice calls daily?', 'Do you use voice calling frequently?', 
         'Are you a regular user of voice call?', 'Do you make voice calls frequently?', 
         'On an average, do you make a lot of voice calls in your day to day life?', 'Do you make a lot of voice calls daily?']

international = ['Do you use international calls regularly?', 'Are you a person who regularly uses international calls?', 
                 'Do you use the international calling facility regularly?', 'Do you use international calling facility frequently?', 
                 'Do you make international calls frequently?', 
                 'On an average, do you make a lot of international calls in your day to day life?', 
                 'Do you make a lot of international calls daily?']

welcome = ['Hi! Etisalat welcomes you to the AI Store.', 
           'Hello! Welcome to Etisalat AI Store.',
           'Good day! Etisalat welcomes you to the AI Store.',
           'Hello! Etisalat welcomes you to the AI Store.'
           ]

assist_yes =  ['What else do you need?', 'What would you like to add?', 'What else do you want?', 
               'What else do you require?', 'What more do you want?', 
               'What else can I help you with?']

assistance = ['Is there anything else that I can help you with?', 
              'May I help you with anything else?', 'Is there anything else I can do for you?', 
              'Do you need any more assistance now?', 
              'Would you like me to assist you with anything else?', "Would you like to have more assistance?"]

assist_no = ['Hope to serve you again! Have a good day.', 
             'Bye for now. Hope to see you soon!', 
             'Bye for now. Looking forward to serving you again.', 
             'Great to have had you here. See you later.',
             'Hope to talk to you again.', 
             'Bye for now. Have a good day.',
             'Have a good day. Bye', 'Have a great day. Bye', 
             'Have a good day. See you later.',
             'Hope to see you soon. Bye.']

choice = [' is indeed a good decision.', ' is indeed an excellent choice.', ' is indeed a wonderful selection.', ' is indeed a good choice.',
          ' is certainly one of the most popular phones in the market right now', ' is a great choice', ' is indeed our most popular choice.',
          ' is a superb selection.']

price_range = ['We have a range of mobile phones of brands like Apple, Samsung and Blackberry ranging from 1700 to 3900 Dirhams.',
               'We have smart phones of Apple, Samsung and Blackberry from a price range of 1700 to 3900 Dirhams.',
               'We have different brands of mobile phones like Samsung, Apple and Blackberry from a budget of 1700 to 3900 Dirhams.'
               ]

apple_range = ['We have Apple iPhones ranging from 2600 to 3900 Dirhams.',
               'We have different iPhones of Apple from a price range of 2600 to 3900 Dirhams.',
               'We have mobile phones of Apple from a budget of 2600 to 3900 Dirhams.'
               ]

samsung_range = ['We have different models of Samsung mobile phones ranging from 1800 to 3400 Dirhams.',
                 'We have smart phones of Samsung from a price range of 1800 to 3400 Dirhams.',
                 'We have Samsung mobile phones from a budget of 1800 to 3400 Dirhams.'
                ]

blackberry_range = ['We have mobile phones of Blackberry ranging from 1700 to 2000 Dirhams.',
                    'We have Blackberry smart phones from a price range of 1700 to 2000 Dirhams.',
                    'We have different models of Blackberry mobile phones from a budget of 1700 to 2000 Dirhams.'
                    ]

card = ['What type of card do you want to use? A Visa card, a Master card or your already saved card as in our records?', 
        'What type of card are you going to use? Visa, Master Card or one of your already saved cards?',
        'Which card would you like to use? Visa, Master Card or one of your saved card?']

card_new = ['What type of card do you want to use? Visa or Master Card?', 
            'What type of card are you going to use? A Visa or Master Card?',
            'Which card would you like to use? Visa or Master Card?']

res = ['Are you a UAE resident?']

gsm = ['What would you like to have?', 'What type of GSM plan are you looking for?',  
       'What kind of GSM plan do you need?', 'What kind of GSM plan would you like?',
       'What kind of GSM plan would you like to take?' , 'What kind of GSM plan would you like to select?',
       'Which type of GSM plan would you like to have?', 'Which one do you like to choose?']

offer_mobile = ['We offer top class Mobile Phones of Apple, Samsung and Blackberry.', 
                'We provide the best in class mobile phones of Apple, Samsung and Blackberry.',
                'We have the latest smartphones of Apple, Samsung and Blackberry.']

offer_gsm = ['There are a lot of prepaid and postpaid GSM plans available here.', 
             'We provide a lot of postpaid and prepaid plans.',
             'We offer many prepaid and postpaid plans.', 'We have good prepaid and postpaid plans.', 
             'We have different prepaid and postpaid plans.']

offer_gsm_also = ['We also provide a lot of postpaid and prepaid plans.',
                  'We also offer many prepaid and postpaid plans.', 'We also have a good number of prepaid and postpaid plans.', 
                  'We also have different prepaid and postpaid plans.']

offer_prepaid = ['We have many exciting prepaid offers.', 'There are a plenty of interesting prepaid offers.',
                 'There are a lot of exciting prepaid offers.']

offer_postpaid = ['We have many exciting postpaid offers.', 'There are plenty of exciting postpaid offers.',
                  'There are a lot of exciting postpaid offers.']

new_customer = ['Welcome to the store. We are glad that you selected Etisalat.', 
                'Thank you for choosing Etisalat.', 
                'Etisalat welcomes you to the AI store. Thank you for giving us an opportunity.']

existing_customer = ['Welcome back! We are happy to see you again!', 
                     'Welcome back! We are glad that you preferred Etisalat again!', 
                     'Welcome back! Thank you for giving us another opportunity to serve you!']

visitor = ['Welcome to UAE. Hope you are having a nice time here in UAE. Thank you for visiting Etisalat.', 
           'Welcome to UAE. Hope you are enjoying your stay here.Thank you for dropping in at the Etislat AI Store.']

helping = ['How may I help you?', 'How can I be of help to you today?', 'How shall I help you?', 
           'How may I assist you?', 'How can I help you today?', 'How may I help you today?', 
           'How may I be of service today?']

bill = ['We have an EPM self service machine. You can use it for the Bill payment. Please mention "DONE" to complete the transaction.', 
        'We have an EPM self service machine. You can use it for your payments. Please mention "DONE" to close the transaction.']

sry_mobile = ["I am so sorry. We don't have that mobile phone with us now.", 
              "We are very sorry but we don't have that mobile phone with us now.",
              "I’m sorry to say that we don't have that particular make or model with us.",
              "I’m afraid we don’t have what you’re looking for right now. Sorry about that."]

sry_mobile_rec = ["I am so sorry. Currently we don't have any mobile phones matching your mentioned requirements.",
                  "We are very sorry. Currently we don't have a mobile phone matching to your requirements.",
                  "Our apologies to you. We do not have any phone that matches your brand preference or budget right now.",
                  "I'm afraid we don't have what you're looking for right now. Sorry about that."]

sry_prepaid = ["Sorry. We regret to say that we don't have any prepaid plans matching your needs.",
               "Sorry, at the moment we don’t have any prepaid plans that match your needs.",
               "Sorry. We don't have any prepaid plans matching your preferences."]

sry_postpaid = ["Sorry. We regret to say that we don't have any postpaid plans matching your needs.",
                "Sorry, at the moment we don’t have any postpaid plans that match your needs.",
                "Sorry. We don't have any postpaid plans matching your preferences."]

prepaid_rec = ['The following are the recommended prepaid plans.', 
               'Based on your responses, here are the prepaid plans we feel could work best for you.',
               'Here are some prepaid plans that we feel would be suitable for you.']

postpaid_rec = ['The following are the recommended postpaid plans.', 
                'Based on your responses, here are the postpaid plans we feel could work best for you.',
                'Here are some postpaid plans that we feel would be suitable for you.']

mobile_rec = ['The following are the recommended mobile phones.',
              'The following are some of the mobile phones that we recommend.', 
              'Here is a list of some of the best smartphones available with us.']

fallback = ["I'm really sorry! I didn't understand what you said.",
            "I'm really sorry!I don't think I may be able to help you with that.", 
            "Oops. I’m so sorry. Currently I’m not aware of that.",
            "I am so sorry, I don't know much about it."]

fillers = ['Okay.', 'Great.', 'Cool.', 'Awesome.', 'Well.', "That's Good.", 'Excellent.']

gsm_select = ['Would you like to select any GSM prepaid or postpaid plans?', 
              'Would you be interested to buy a GSM prepaid or postpaid plan?',
              'Do you want to avail any GSM prepaid or postpaid plans?', 
              'Do you wish to have any GSM postpaid or prepaid plans?',
              'Are you interested in purchasing any GSM postpaid or prepaid plans?']

plan_select = ['Okay. Which GSM plan would you like to select?', 'Fine, which GSM plan do you prefer?']
