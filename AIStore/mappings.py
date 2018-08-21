# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:44:01 2018

@author: Vishnu
"""

brand = {
        'Apple': ['apple', 'apple iphone', 'iphone'],
        'Samsung': ['samsung'],
        'Nokia': ['nokia'],
        'Xiaomi': ['xiaomi', 'mi', 'redmi'],
        'Huawei': ['huawei', 'honor', 'honour'],
        'HTC': ['htc'],
        'Blackberry': ['blackberry'],
        'Oppo': ['oppo'],
        'iBRIT': ['ibrit', 'speed x']
        }

mem = {
       '1GB': ['one gb', '1 gb', '1gb', 'onegb'], 
       '2GB': ['two gb', '2 gb', '2gb', 'twogb'],
       '4GB': ['four gb', '4 gb', '4gb', 'fourgb'],
       '8GB': ['eight gb', '8 gb', '8gb', 'eightgb'],
       'No': ['no', 'nah', 'na', 'nop', 'nope', 'dont', "don't", 'not', 
              'confused', 'shoe', 'string', 'low', 'high', 'enough', 'money',
              'cash', 'cost', 'selling', 'sell', 'fund', 'funds', 'spend', 'spending'
              'spent', 'pay', 'payment', 'bucks', 'nothing', 'not aware', 'aware', 'unaware',
              'camera', 'storage', 'battery', 'screen', 'life', 'wide', 'big', 'smart', 'flagship', 'flag ship',
              'flag']
       }

store = {
        '16GB': ['sixteen gb', '16 gb', '16gb', 'sixteengb'],
        '32GB': ['thirty two gb', '32 gb', '32gb', 'thirtytwogb'],
        '64GB': ['sixty four gb', '64 gb', '64gb', 'sixtyfourgb'],
        '128GB': ['one twenty eight gb', '128 gb', '128gb', 'onetwentyeightgb'],
        '256GB': ['two fifty six gb', '256 gb', '256gb', 'twofiftysixgb']
        }

cam = {
       '5MP': ['5 mp', 'five mp', '5mp', 'fivemp'],
       '7MP': ['7 mp', 'seven mp', '7mp', 'sevenmp'],
       '8MP': ['8 mp', 'eight mp', '8mp', 'eightmp'],
       '12MP': ['12 mp', 'twelve mp', '12mp', 'twelvemp'],
       '13MP': ['13 mp', 'thirteen mp', '13mp', 'thirteenmp'],
       '16MP': ['16 mp', 'sixteen mp', '16mp', 'sixteenmp'],
       '20MP': ['20 mp', 'twenty mp', '20mp', 'twentymp'],
       '23MP': ['23 mp', 'twenty three mp', '23mp', 'twentythreemp'],
       '24MP': ['24 mp', 'twenty four mp', '24mp', 'twentyfourmp'],
       '25MP': ['25 mp', 'twenty five mp', '25mp', 'twentyfivemp']
       }

size = {
        '4-inch': ['4 inch', 'four inch', '4inch', 'fourinch'],
        '4.3-inch': ['4.3 inch', '4.3inch'], 
        '4.5-inch': ['4.5 inch', '4.5inch'],
        '4.7-inch': ['4.7 inch', '4.7inch'],
        '5-inch': ['5 inch', 'five inch', '5inch', 'fiveinch'],
        '5.1-inch': ['5.1 inch', '5.1inch'],
        '5.15-inch': ['5.15 inch', '5.15inch'], 
        '5.2-inch': ['5.2 inch', '5.2inch'],
        '5.3-inch': ['5.3 inch', '5.3inch'], 
        '5.5-inch': ['5.5 inch', '5.5inch'],
        '5.6-inch': ['5.6 inch', '5.6inch'],
        '5.7-inch': ['5.7 inch', '5.7inch'], 
        '5.8-inch': ['5.8 inch', '5.8inch'],
        '5.9-inch': ['5.9 inch', '5.9inch'],
        '6-inch': ['6 inch', '6inch'],
        '6.1-inch': ['6.1 inch', '6.1inch'],
        '6.2-inch': ['6.2 inch', '6.2inch'],
        '6.3-inch': ['6.3 inch', '6.3inch'],
        '6.4-inch': ['6.4 inch', '6.4inch'],
        '6.44-inch': ['6.44 inch', '6.44inch'],
        '6.5-inch': ['6.5 inch', '6.5inch']
        }

OS = {
      'Android': ['android', 'android os'],
      'iOS': ['ios', 'ios os']
      }

plans = {
        'Daily': ['daily', '24 hour', 'one day', '1 day', '24 hours'],
        'Weekly': ['weekly', '7 day', '7 days', 'week', 'seven day', 'seven days', 'quickly'],
        'Monthly': ['monthly', 'month', '1 month', '30 day', '30 days', 'mandali', 'manly', 'mowgli', 'sharry mann 3 peg',
                    'month reply', 'mandli']
        }

yesorno = {
            'Yes': ['yes', 'yeah', 'yea', 'yup', 'yap', 'yep', 'international', 'voice', 'data', 'combo', 'maybe', 'may be',
                    'definitely', 'sometimes', 'perhaps', 'can be', 'could be', 'might be', 'might', 'may', 'possibly', 'absolutely',
                    'surely', 'obviously', 'clearly', 'doubtless', 'easily', 'consistently', 'constantly', 'frequently',
                    'occasionally', 'at times', 'at intervals', 'often', 'while', 'on occasion', 'periodically', 'sure', 'surf',
                    'surfing', 'once in a way', 'ofcourse', 'of course', 'plenty', 'excess', 'up'], 
            'No': ['no', 'nah', 'na', 'nop', 'nope', 'dont', "don't", 'not', 
                   'confused', 'shoe', 'string', 'low', 'high', 'enough', 'money',
                   'cash', 'cost', 'selling', 'sell', 'fund', 'funds', 'spend', 'spending'
                   'spent', 'pay', 'payment', 'bucks', 'nothing', 'not aware', 'aware', 'unaware',
                   'thank you', 'thank', 'thanks']
        }

no = {'No': ['no', 'nah', 'na', 'nop', 'nope', 'dont', "don't", 'not', 
             'confused', 'shoe', 'string', 'low', 'high', 'enough', 'money',
             'cash', 'cost', 'selling', 'sell', 'fund', 'funds', 'spend', 'spending'
             'spent', 'pay', 'payment', 'bucks', 'nothing', 'not aware', 'aware', 'unaware']
        }

model = {
    "Oppo F7": ['oppo f7', 'oppo f 7', 'oppo f seven'],
    "Galaxy S9": ['galaxy s9', 'galaxy s 9', 'galaxy s nine', 'galaxy yes 9', 'galaxy yes nine', 's9', 's 9', 
                  's nine'],
    "Galaxy S9+": ['galaxy s9+', 'galaxy s9 +', 'galaxy s 9 +', 'galaxy s nine+', 'galaxy s nine +', 
                   'galaxy yes 9+', 'galaxy yes 9 +', 'galaxy yes nine+', 'galaxy yes nine +', 's9+', 's9 +', 
                   's 9 +', 's 9 plus'],
    "Nokia 8": ['nokia 8', 'nokia eight'],
    "Huawei P20 Pro": ['huawei p20 pro', 'huawei p twenty pro'],
    "Nokia 7+": ['nokia 7+', 'nokia seven plus', 'nokia 7 +', 'nokia seven+', 'nokia seven plus'],
    "Nokia 1": ['nokia 1', 'nokia one'],
    "Galaxy A8+": ['galaxy a8+', 'galaxy a8 +', 'galaxy a eight+', 'galaxy a 8 +', 'galaxy a eight plus',
                   'a8+', 'a 8+', 'a 8 +', 'a eight plus', 'a eight +'],
    "Galaxy A8": ['galaxy a8', 'galaxy a 8', 'galaxy a eight', 'a8', 'a 8', 'a eight'],
    "Nova 3e": ['nova 3e', 'nova 3 e', 'nova three e'],
    "Nokia 2": ['nokia 2', 'nokia two'],
    "HTC M10": ['htc m10', 'htc m 10', 'htc m ten'],
    "Galaxy Note 8": ['galaxy note 8', 'galaxy note8', 'galaxy note eight', 'note 8', 'note8', 'note eight'],
    "Galaxy S8 with Gear VR3": ['galaxy s8 with gear vr3', 'galaxy s8', 'galaxy s eight', 'galaxy s 8',
                                's8', 's 8', 's eight'],
    "Galaxy S8+ with Gear VR3": ['galaxy s8+ with gear vr3', 'galaxy s8+', 'galaxy s 8+', 'galaxy s 8 +',
                                 'galaxy s eight +', 'galaxy s eight plus', 's8+', 's8 +', 's 8 +', 
                                 's eight plus'],
    "Iphone X": ['iphone x', 'iphonex', 'iphone ex'],
    "Iphone 8": ['iphone 8', 'iphone8', 'iphone eight'],
    "Iphone 8 Plus": ['iphone 8 plus', 'iphone8 plus', 'iphone8+', 'iphone 8 +', 'iphone eight +', 
                      'iphone eight plus'],
    "KeyOne": ['keyone', 'key one'],
    "Motion": ['motion'],
    "Mi 5": ['mi 5', 'mi5', 'mi five', 'm i 5', 'm i five'],
    "Mi 5s": ['mi 5s', 'mi 5 s', 'm i 5s', 'm i 5 s', 'mi five s', 'm i five s'],
    "Mi 5s Plus": ['mi 5s plus', 'mi 5s +', 'mi five s plus', 'mi five s+', 'm i 5s plus', 'm i 5s+'],
    "Mi Max 2": ['mi max 2', 'mi max2', 'mi max two', 'm i max2', 'm i max two'],
    "Redmi 3s": ['redmi 3s', 'redmi three s'], 
    "Redmi Note 4": ['redmi note 4', 'redmi note4', 'redmi note four'],
    "Redmi 4X": ['redmi 4x', 'redmi 4 x', 'redmi 4 ex', 'redmi four x', 'redmi four ex'],
    "Redmi Note 3": ["redmi note 3", 'redmi note3', 'redmi note three'],
    "Redmi Note 5A": ['redmi note 5a', 'redmi note five a', 'redmi note five', 'redmi note 5', 'redmi note5'],
    "Nokia 3": ['nokia 3', 'nokia3', 'nokia three'],
    "Nokia 5": ['nokia 5', 'nokia5', 'nokia five'],
    "Nokia 6": ['nokia 6', 'nokia6', 'nokia six'],
    "Huawei Mate 10": ['huawei mate 10', 'huawei mate10', 'huawei mate ten', 'mate 10', 'mate10', 'mate ten'],
    "Huawei Mate 10 Pro": ['huawei mate 10 pro', 'huawei mate10 pro', 'huawei mate ten pro', 'mate 10 pro',
                           'mate10 pro', 'mate ten pro'],
    "Huawei Mate 10 Lite": ['huawei mate 10 lite', 'huawei mate10 lite', 'huawei mate ten lite', 'mate 10 lite', 
                            'mate ten lite', 'mate ten lite'],
    "Huawei P10 Lite": ['huawei p10 lite', 'huawei p 10 lite', 'huawei p ten lite', 'p10 lite', 'p 10 lite',
                        'p ten lite'],
    "Honor 8 Lite": ['honor 8 lite', 'honor eight lite', 'honor8 lite'],
    "Nokia 6.1": ['nokia 6.1'],
    "Speed X": ['speed x', 'speedx']
    }

spec = {'features': ['features', 'specifications', 'specs', 'hightlights', 'highlight', 'price', 'cost']}

low = {'low': ['low', 'less', 'least']}

gsm = {'Postpaid': ['postpaid', 'post paid', 'post-paid'], 'Prepaid': ['prepaid', 'pre paid', 'pre-paid']}

cust = {'New': ['new', 'new customer', 'newcustomer', 'tourist', 'avenue customer', 'avenue', 'amma newcastle',
                'new castle', 'newcastle', 'menu customer', 'menu'], 
        'Existing': ['existing', 'old', 'existing customer', 'old customer', 'timely', 'nexus',
                    'existingcustomer', 'oldcustomer', 'regular', 'previous', 'earlier', 'past', 
                    'ex', 'current', 'ex-customer', 'ex-']}

uae = {'Visitor': ['visitor', 'new', 'new here', 'new to uae', 'no', 'nah', 'na', 'nop', 'nope', 'not', 
                   'foreigner', 'outsider', 'foreign citizen', 'other', 'tourist', 'traveler', 'voyager', 'vacation', 
                   'tripper', 'journeyer', 'journey', 'foreign', 'vacationist', 'sightseer', 'wayfarer', 
                   'passenger', 'commuter', 'wanderer', 'pilgrim', 'traveller', 'nomad', 'pureit', 'obituaries', 'obituary',
                   'ambattur', 'amit used', 'amit tourist', 'hame tourist', 'main tourist'], 
       'Resident': ['resident', 'citizen', 'yes', 'yeah', 'yup', 'yap', 'ya', 'yea', 'iam', 'i am', 'am', 'sure', 
                    'surely', 'obviously', 'clearly', 'doubtless', 'definitely', 'president']}

card = {'Visa': ['visa', 'veesa', 'nisha', 'nisa', 'geyser', 'sheesha'], 
        'Master Card': ['master card', 'mastercard', 'master'], 
        'Other': ['other', 'saved', 'already']}

names = {"Galaxy S9": ['galaxy s9', 'galaxy s 9', 'galaxy s nine', 'galaxy yes 9', 'galaxy yes nine', 's9', 's 9', 's nine'],
         "Galaxy S9+": ['galaxy s9+', 'galaxy s9 +', 'galaxy s 9 +', 'galaxy s nine+', 'galaxy s nine +', 'galaxy yes 9+', 
                        'galaxy yes 9 +', 'galaxy yes nine+', 'galaxy yes nine +', 's9+', 's9 +', 's 9 +', 's 9 plus', 's 9 plus',
                        's9 plus', 'galaxy s9 plus'],
         "Galaxy A8+": ['galaxy a8+', 'galaxy a8 +', 'galaxy a eight+', 'galaxy a 8 +', 'galaxy a eight plus', 'a8+', 
                        'a 8+', 'a 8 +', 'a eight plus', 'a eight +', 'galaxy a8 plus', 'galaxy a 8 plus', 'a8 plus'],
         "Galaxy A8": ['galaxy a8', 'galaxy a 8', 'galaxy a eight', 'a8', 'a 8', 'a eight'],
         "Galaxy Note 8": ['galaxy note 8', 'galaxy note8', 'galaxy note eight', 'note 8', 'note8', 'note eight'],
         "Galaxy S8 with Gear VR3": ['galaxy s8 with gear vr3', 'galaxy s8', 'galaxy s eight', 'galaxy s 8',
                                     's8', 's 8', 's eight'],
         "Galaxy S8+ with Gear VR3": ['galaxy s8+ with gear vr3', 'galaxy s8+', 'galaxy s 8+', 'galaxy s 8 +',
                                      'galaxy s eight +', 'galaxy s eight plus', 's8+', 's8 +', 's 8 +', 
                                      's eight plus', 'galaxy s8 plus', 'galaxy s 8 plus', 's8 plus'],
         "Iphone X": ['iphone x', 'iphonex', 'iphone ex', 'iphone ten', 'iphone 10'],
         "Iphone 8": ['iphone 8', 'iphone8', 'iphone eight'],
         "Iphone 8 Plus": ['iphone 8 plus', 'iphone8 plus', 'iphone8+', 'iphone 8 +', 'iphone eight +', 
                           'iphone eight plus', 'iphone 8 +'],
         "KeyOne": ['keyone', 'key one', 'given'],
         "Motion": ['motion'],
         "100 Dirhams Visitor Line": ["100 dirhams visitor line", "100 dirhams visitor", '100 dirhams line', '100 visitor line', '100 visitor',
                                      '100 line', 'dirham', 'dirhams', '100', 'visitor', 'line'],
         "30 Dirhams Prepaid Data Plan": ["30 dirhams prepaid data plan", '30 dirhams prepaid data', '30 dirhams prepaid plan', 
                                          '30 dirhams data plan', '30 prepaid data plan', '30 prepaid plan', '30 dirhams prepaid', 
                                          '30 data plan', '30 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams'],
         "100 Dirhams Prepaid Data Plan": ["100 dirhams prepaid data plan", '100 dirhams prepaid data', '100 dirhams prepaid plan', 
                                           '100 dirhams data plan', '100 prepaid data plan', '100 prepaid plan', '100 dirhams prepaid', 
                                           '100 data plan', '100 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams'],
         "150 Dirhams Prepaid Data Plan": ["150 dirhams prepaid data plan", '150 dirhams prepaid data', '150 dirhams prepaid plan', 
                                           '150 dirhams data plan', '150 prepaid data plan', '150 prepaid plan', '150 dirhams prepaid', 
                                           '150 data plan', '150 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams'],
         "5 Dirhams Prepaid Data Plan": ["5 dirhams prepaid data plan", '5 dirhams prepaid data', '5 dirhams prepaid plan', 
                                         '5 dirhams data plan', '5 prepaid data plan', '5 prepaid plan', '5 dirhams prepaid', 
                                         '5 data plan', '5 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 'five'],
         "10 Dirhams Prepaid Data Plan": ["10 dirhams prepaid data plan", '10 dirhams prepaid data', '10 dirhams prepaid plan', 
                                          '10 dirhams data plan', '10 prepaid data plan', '10 prepaid plan', '10 dirhams prepaid', 
                                          '10 data plan', '10 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 'ten'],
         "20 Dirhams Prepaid Data Plan": ["20 dirhams prepaid data plan", '20 dirhams prepaid data', '20 dirhams prepaid plan', 
                                          '20 dirhams data plan', '20 prepaid data plan', '20 prepaid plan', '20 dirhams prepaid', 
                                          '20 data plan', '20 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 
                                          'twenty'],
         "50 Dirhams Prepaid Data Plan": ["50 dirhams prepaid data plan", '50 dirhams prepaid data', '50 dirhams prepaid plan', 
                                          '50 dirhams data plan', '50 prepaid data plan', '50 prepaid plan', '50 dirhams prepaid', 
                                          '50 data plan', '50 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 
                                          'fifty'],
         "2 Dirhams Prepaid Data Plan": ["2 dirhams prepaid data plan", '2 dirhams prepaid data', '2 dirhams prepaid plan', 
                                         '2 dirhams data plan', '2 prepaid data plan', '2 prepaid plan', '2 dirhams prepaid', 
                                         '2 data plan', '2 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 
                                         'two'],
         "4 Dirhams Prepaid Data Plan": ["4 dirhams prepaid data plan", '4 dirhams prepaid data', '4 dirhams prepaid plan', 
                                         '4 dirhams data plan', '4 prepaid data plan', '4 prepaid plan', '4 dirhams prepaid', 
                                         '4 data plan', '4 dirhams data plan', 'prepaid', 'data', 'plan', 'dirham', 'dirhams', 
                                         'four', 'for'],
         "40 Dirhams Combo Pack": ["40 dirhams combo pack", '40 dirhams combo', '40 combo pack', '40 dirhams pack', 
                                   '40 combo pack', '40 pack', '40 combo', 'combo', 'pack', 'dirham', 'dirhams', 
                                   'forty', 'fourty'],
         "100 Dirhams Combo Pack": ["100 dirhams combo pack", '100 dirhams combo', '100 combo pack', '100 dirhams pack', 
                                    '100 combo pack', '100 pack', '100 combo', 'combo', 'pack', 'dirham', 'dirhams'],
         "150 Dirhams Combo Pack": ["150 dirhams combo pack", '150 dirhams combo', '150 combo pack', 
                                    '150 combo pack', '150 pack', '150 combo', 'combo', 'pack', 'dirham', 'dirhams'],
         "35 Dirhams Combo Pack": ["35 dirhams combo pack", '35 dirhams combo', '35 combo pack', '35 dirhams pack', 
                                   '35 combo pack', '35 pack', '35 combo', 'combo', 'pack', 'dirham', 'dirhams', 'thirty five'],
         "50 Dirhams Combo Pack": ["50 dirhams combo pack", '50 dirhams combo', '50 combo pack', '50 dirhams pack', 
                                   '50 combo pack', '50 pack', '50 combo', 'combo', 'pack', 'dirham', 'dirhams', 'fifty'],
         "150 Dirhams Pack": ['150 dirhams pack', '150 pack', '150 dirhams', '150', 'pack', 'dirham', 'dirhams'],
         "250 Dirhams Pack": ['250 dirhams pack', '250 pack', '250 dirhams', '250', 'pack', 'dirham', 'dirhams'],
         "500 Dirhams Pack": ['500 dirhams pack', '500 pack', '500 dirhams', '500', 'pack', 'dirham', 'dirhams'],
         "1000 Dirhams Pack": ['1000 dirhams pack', '1000 pack', '1000 dirhams', '1000', 'pack', 'dirham', 'dirhams'],
         'No': ['no', 'nah', 'na', 'nop', 'nope', 'dont', "don't", 'not', 'confused']
         }
