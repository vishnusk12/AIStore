# -*- coding: utf-8 -*-
'''
Created on 01-Jun-2018

@author: Vishnu
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .config import create_cache
from .model import build_model
from .queries import welcome, assist_yes, assist_no, choice, sry_mobile
from .queries import sry_mobile_rec, gsm_select, mobile_rec, offer_gsm_also
from .queries import sry_prepaid, sry_postpaid, prepaid_rec, postpaid_rec
from .queries import bill, assistance, plan_select, fillers, res
import random
import dill
import base64
import pymongo
from pymongo import MongoClient

connection = MongoClient('52.221.4.121', 38128)
db = connection.etisalat

@permission_classes((permissions.AllowAny,))
class Bot(viewsets.ViewSet):
    def create(self, request):
        CACHE_ID = 'CONSTANT5'
        question = request.data
        if 'user_id' in question:
            CACHE_ID = question['user_id']
        req_cache = create_cache(CACHE_ID)
        print 'asdfg', req_cache
        if question['messageSource'] == 'userInitiatedReset':
            req_cache.delete()
            question['messageSource'] = 'messageFromBot'
            question['filter'] = 'normal'
            question['messageText'] = [[random.choice(welcome)], 
                                       ['Are you a New Customer or an Existing Customer?']]
            return Response(question)
        kern = dill.loads(base64.b64decode(req_cache.user.aiml_kernel))
        print 'kern', kern
        question = build_model(question, kern, req_cache.cache)
        if 'property' in question:
            req_cache.cache = question['property']
            req_cache.user.aiml_kernel = base64.b64encode(dill.dumps(kern))
            req_cache.user.save()
            req_cache.save()
        if str({key: value for d in question["property"] for key, value in d.items()}.has_key('Features'))=='False' and \
        str({key: value for d in question["property"] for key, value in d.items()}.has_key('Name'))=='False' and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Model') and \
        question['messageSource'] == 'MobileSpecific':
            new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
            new_question = list(filter(None, new_question))
            data = list(db.mobile.find({'Model': \
                                        str({key: value for d in new_question for key, value in d.items()}['Model'].title())}))
            [i.pop('_id') for i in data]
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], 
                                           [str({key: value for d in new_question for key, value in d.items()}['Model'].title()) \
                                            + random.choice(choice)], 
                                           ['I will alert one of our sales person to help you in selecting one.'], 
                                           [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                           ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['product'] = 'yes'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_mobile)], [random.choice(offer_gsm_also)], 
                                           [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    else:
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Model') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Features') and \
        question['messageSource'] == 'MobileSpecific':
            new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
            new_question = list(filter(None, new_question))
            data = list(db.mobile.find({'Model': \
                                        str({key: value for d in new_question for key, value in d.items()}['Model'].title())}))
            [i.pop('_id') for i in data]
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], 
                                           ['The following are the specifications of your' + ' ' + \
                                            str({key: value for d in new_question for key, value in d.items()}['Model'].title()) + \
                                            '.' ], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                           ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['product'] = 'yes'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_mobile)], [random.choice(offer_gsm_also)], 
                                           [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    else:
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Top') and \
        question['messageSource'] == 'MobileSpecific':
            new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
            new_question = list(filter(None, new_question))
            data = list(db.mobile.find({}).sort('Price', pymongo.DESCENDING))
            data = data[:3]
            [i.pop('_id') for i in data]
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], [random.choice(mobile_rec)], [random.choice(offer_gsm_also)], 
                                           [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['product'] = 'yes'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                           [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    else:
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Low') and \
        question['messageSource'] == 'MobileSpecific':
            new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
            new_question = list(filter(None, new_question))
            data = list(db.mobile.find({}).sort('Price', pymongo.ASCENDING))
            data = data[:3]
            [i.pop('_id') for i in data]
            models = [i['Model'] for i in data]
            models = ', '.join(models)
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], ['The following are the low budget smartphones available here.'], 
                                           ['Please select your preferred model from' + ' ' + models + '.']]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'itemname'
                reply = question
                try:
                    if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Thank You for selecting' + ' ' \
                                                    + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                    + '.'], 
                                                   [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                   ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['product'] = 'yes'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'MobileSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                   ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'no':
                                question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['action'] = 'stop'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'yes':
                                question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'MobileSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                        question['messageText'] = [["Sorry I didn't get you."], 
                                                   ['Please select your preferred model from' + ' ' + models + '.']]
                        question['data'] = data
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'itemname'
                        reply = question
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                           [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'MobileSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'no':
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'yes':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Specifications') and \
        {key: value for d in question["property"] for key, value in d.items()}['Specifications'].has_key('RAM') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Price') and \
        question['messageSource'] == 'MobileSpecific':
            if str({key: value for d in question["property"] for key, value in d.items()}['RAM']) == 'No' and \
            str({key: value for d in question["property"] for key, value in d.items()}['Price']) != 'No'  and \
            question['messageSource'] == 'MobileSpecific':
                new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
                new_question = list(filter(None, new_question))
                pipeline = [{"$match": {'Price':{'$lte': int({key: value for d in new_question for key, value in d.items()}['Price'])}}}, 
                            {'$sort': {'Price': -1}}]
                data = list(db.mobile.aggregate(pipeline))
                data = data[:3]
                data = random.sample(data, len(data))
                [i.pop('_id') for i in data]
                models = [i['Model'] for i in data]
                models = ', '.join(models)
                if len(data) != 0:
                    question['messageText'] = [['Thank You.'], 
                                               ['The following are the recommended mobile phones within your budget of' + ' '  \
                                                +  str({key: value for d in new_question for key, value in d.items()}['Price']) \
                                                + ' ' + 'Dirhams.'],
                                               ['Please select your preferred model from' + ' ' + models + '.']]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'itemname'
                    reply = question
                    try:
                        if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Thank You for selecting' + ' ' \
                                                        + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                        + '.'], 
                                                       [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['product'] = 'yes'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'normal'
                                    question['action'] = 'citizen'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], \
                                                       [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'no':
                                    question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['action'] = 'stop'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'yes':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                            question['messageText'] = [["Sorry I didn't get you."], 
                                                       ['Please select your preferred model from' + ' ' + models + '.']]
                            question['data'] = data
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'itemname'
                            reply = question
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
                else:
                    question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                               [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'quest'
                    reply = question
                    try:
                        if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                            question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'no':
                            question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            question['action'] = 'stop'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'yes':
                            question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                       [random.choice(res)]]
                            question['messageSource'] = 'BillSpecific'
                            question['filter'] = 'citizen'
                            question['action'] = 'invoice'
                            question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
            elif str({key: value for d in question["property"] for key, value in d.items()}['RAM']) == 'No' and \
            str({key: value for d in question["property"] for key, value in d.items()}['Price']) == 'No' and \
            question['messageSource'] == 'MobileSpecific':
                new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
                new_question = list(filter(None, new_question))
                data = list(db.mobile.find({}).sort('Price', pymongo.DESCENDING))
                data = data[:3]
                data = random.sample(data, len(data))
                [i.pop('_id') for i in data]
                models = [i['Model'] for i in data]
                models = ', '.join(models)
                if len(data) != 0:
                    question['messageText'] = [['Thank You.'], [random.choice(mobile_rec)], 
                                               ['Please select your preferred model from' + ' ' + models + '.']]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'itemname'
                    reply = question
                    try:
                        if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Thank You for selecting' + ' ' \
                                                        + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                        + '.'], 
                                                       [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['product'] = 'yes'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                    question['messageText'] = [['Thank you.'], 
                                                               ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], 
                                                       [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'no':
                                    question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['action'] = 'stop'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'yes':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                            question['messageText'] = [["Sorry I didn't get you."], 
                                                       ['Please select your preferred model from' + ' ' + models + '.']]
                            question['data'] = data
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'itemname'
                            reply = question
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
                else:
                    question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                               [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'quest'
                    reply = question
                    try:
                        if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                            question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'no':
                            question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            question['action'] = 'stop'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'yes':
                            question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                       [random.choice(res)]]
                            question['messageSource'] = 'BillSpecific'
                            question['filter'] = 'citizen'
                            question['action'] = 'invoice'
                            question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Specifications') and \
        {key: value for d in question["property"] for key, value in d.items()}['Specifications'].has_key('Brand') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Price') and \
        question['messageSource'] == 'MobileSpecific':
            if str({key: value for d in question["property"] for key, value in d.items()}['Price']) != 'No':
                new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
                new_question = list(filter(None, new_question))
                pipeline = [{"$match": {'Price':{'$lte': int({key: value for d in new_question for key, value in d.items()}['Price'])}, 
                                        'Brand': str({key: value for d in new_question for key, value in d.items()}['Brand'])}}, 
                            {'$sort': {'Price': -1}}]
                data = list(db.mobile.aggregate(pipeline))
                data = data[:3]
                [i.pop('_id') for i in data]
                models = [i['Model'] for i in data]
                models = ', '.join(models)
                if len(data) != 0:
                    question['messageText'] = [['Thank You.'], ['The following are the recommended' + ' '+ \
                                                                str({key: value for d in new_question for key, value in d.items()}['Brand']).title() \
                                                                + ' ' + 'phones within your budget of' + ' '  +  \
                                                                str({key: value for d in new_question for key, value in d.items()}['Price']) + ' ' + 'Dirhams.'], 
                                               ['Please select your preferred model from' + ' ' + models + '.']]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'itemname'
                    reply = question
                    try:
                        if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Thank You for selecting' + ' ' \
                                                        + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                        + '.'], 
                                                       [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['product'] = 'yes'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                    question['messageText'] = [['Thank you.'], 
                                                               ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'no':
                                    question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['action'] = 'stop'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'yes':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                            question['messageText'] = [["Sorry I didn't get you."], 
                                                       ['Please select your preferred model from' + ' ' + models + '.']]
                            question['data'] = data
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'itemname'
                            reply = question
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
                else:
                    question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                               [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'quest'
                    reply = question
                    try:
                        if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                            question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'no':
                            question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            question['action'] = 'stop'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'yes':
                            question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                       [random.choice(res)]]
                            question['messageSource'] = 'BillSpecific'
                            question['filter'] = 'citizen'
                            question['action'] = 'invoice'
                            question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
            elif str({key: value for d in question["property"] for key, value in d.items()}['Price']) == 'No':
                new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
                new_question = list(filter(None, new_question))
                pipeline = [{"$match": {'Brand': str({key: value for d in new_question for key, value in d.items()}['Brand'])}}]
                data = list(db.mobile.aggregate(pipeline))
                data = data[:3]
                [i.pop('_id') for i in data]
                models = [i['Model'] for i in data]
                models = ', '.join(models)
                if len(data) != 0:
                    question['messageText'] = [['Thank You.'], ['The following are the recommended' + ' ' \
                                                                + str({key: value for d in new_question for key, value in d.items()}['Brand']).title() \
                                                                + ' ' + 'phones.'], 
                                               ['Please select your preferred model from' + ' ' + models + '.']]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'itemname'
                    reply = question
                    try:
                        if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Thank You for selecting' + ' ' \
                                                        + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                        + '.'], 
                                                       [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['product'] = 'yes'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                    question['messageText'] = [['Thank you.'], 
                                                               ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'no':
                                    question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['action'] = 'stop'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'yes':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                            question['messageText'] = [["Sorry I didn't get you."], 
                                                       ['Please select your preferred model from' + ' ' + models + '.']]
                            question['data'] = data
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'itemname'
                            reply = question
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
                else:
                    question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                               [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'quest'
                    reply = question
                    try:
                        if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                            question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'no':
                            question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            question['action'] = 'stop'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'yes':
                            question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                       [random.choice(res)]]
                            question['messageSource'] = 'BillSpecific'
                            question['filter'] = 'citizen'
                            question['action'] = 'invoice'
                            question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Specifications') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Price') and \
        question['messageSource'] == 'MobileSpecific':
            if str({key: value for d in question["property"] for key, value in d.items()}.has_key('Name'))=='False':
                new_question = [{k: v for k, v in d.items() if k != 'Specifications'} for d in question["property"]]
                new_question = list(filter(None, new_question))
                pipeline = [{"$match": {}}]
                new_dict = {k:v for element in new_question for k,v in element.items()}
                pipeline[0]["$match"].update(new_dict)
                data = list(db.mobile.aggregate(pipeline))
                data = data[:3]
                [i.pop('_id') for i in data]
                models = [i['Model'] for i in data]
                models = ', '.join(models)
                if len(data) != 0:
                    question['messageText'] = [['Thank You.'], [random.choice(mobile_rec)], 
                                               ['Please select your preferred model from' + ' ' + models + '.']]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'itemname'
                    reply = question
                    try:
                        if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Thank You for selecting' + ' ' \
                                                        + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                        + '.'], 
                                                       [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['product'] = 'yes'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                    question['messageText'] = [['Thank you.'], 
                                                               ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                            question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                       ["Say Yes to continue and No to Stop."]]
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'quest'
                            reply = question
                            try:
                                if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                    question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'no':
                                    question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                    question['messageSource'] = 'messageFromBot'
                                    question['filter'] = 'normal'
                                    question['action'] = 'stop'
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                                elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                                and str(request.data['product']) == 'yes':
                                    question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                               [random.choice(res)]]
                                    question['messageSource'] = 'BillSpecific'
                                    question['filter'] = 'citizen'
                                    question['action'] = 'invoice'
                                    question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                    reply = question
                                    req_cache.delete()
                                    return Response(reply)
                            except:
                                question['messageSource'] = 'MobileSpecific'
                                reply = question
                                return Response(reply)
                        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                        str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                            question['messageText'] = [["Sorry I didn't get you."], 
                                                       ['Please select your preferred model from' + ' ' + models + '.']]
                            question['data'] = data
                            question['messageSource'] = 'MobileSpecific'
                            question['filter'] = 'itemname'
                            reply = question
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
                else:
                    question['messageText'] = [[random.choice(sry_mobile_rec)], [random.choice(offer_gsm_also)], 
                                               [random.choice(gsm_select)], ["Say Yes to continue and No to Stop."]]
                    question['data'] = data
                    question['messageSource'] = 'MobileSpecific'
                    question['filter'] = 'quest'
                    reply = question
                    try:
                        if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                            question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'no':
                            question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                            question['messageSource'] = 'messageFromBot'
                            question['filter'] = 'normal'
                            question['action'] = 'stop'
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                        elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                        and str(request.data['product']) == 'yes':
                            question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                       [random.choice(res)]]
                            question['messageSource'] = 'BillSpecific'
                            question['filter'] = 'citizen'
                            question['action'] = 'invoice'
                            question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                            reply = question
                            req_cache.delete()
                            return Response(reply)
                    except:
                        question['messageSource'] = 'MobileSpecific'
                        reply = question
                        return Response(reply)
            else:
                try:
                    if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Thank You for selecting' + ' ' \
                                                    + str({key: value for d in question["property"] for key, value in d.items()}['Name']) \
                                                    + '.'], 
                                                   [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                   ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['product'] = 'yes'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                question['messageText'] = [['Thank you.'], 
                                                           ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'MobileSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Okay.'], [random.choice(offer_gsm_also)], [random.choice(gsm_select)], 
                                                   ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [[random.choice(plan_select)], ["Prepaid or Postpaid?"]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'no':
                                question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['action'] = 'stop'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'yes':
                                question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'MobileSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                        question['messageText'] = [["Sorry I didn't get you."], 
                                                   ['Please select your preferred model from' + ' ' + models + '.']]
                        question['data'] = data
                        question['messageSource'] = 'MobileSpecific'
                        question['filter'] = 'itemname'
                        reply = question
                        return Response(reply)
                except:
                    question['messageSource'] = 'MobileSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Plan_type') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Plan') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Data') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Voice') and \
        question['messageSource'] == 'GSMSpecific':
            pipeline = [{"$match": {'Plan': str({key: value for d in question["property"] for key, value in d.items()}['Plan']),
                                    'Data': str({key: value for d in question["property"] for key, value in d.items()}['Data']), 
                                    'International Call': str({key: value for d in question["property"] for key, value in d.items()}['Voice'])}}]
            data = list(db.prepaid.aggregate(pipeline))
            data = data[:3]
            data = random.sample(data, len(data))
            [i.pop('_id') for i in data]
            [i.pop('International Call') for i in data]
            [i.pop('Data') for i in data]
            [i.pop('Plan') for i in data]
            models = [i['Name'] for i in data]
            models = list(set(models))
            models = ', '.join(models)
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], [random.choice(prepaid_rec)], 
                                           ['Please select your preferred plan from' + ' ' + models + '.']]
                question['data'] = data
                question['messageSource'] = 'GSMSpecific'
                question['filter'] = 'itemname'
                reply = question
                try:
                    if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Thank You for selecting a prepaid plan.'], 
                                                   [random.choice(assistance)], ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [random.choice(assist_yes)]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['product'] = 'yes'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                question['messageText'] = [['Thank you.'], 
                                                           ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'GSMSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Okay.'], [random.choice(assistance)], ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [random.choice(assist_yes)]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'no':
                                question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['action'] = 'stop'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'yes':
                                question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'GSMSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                        question['messageText'] = [["Sorry I didn't get you."], 
                                                   ['Please select your preferred plan from' + ' ' + models + '.']]
                        question['data'] = data
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'itemname'
                        reply = question
                        return Response(reply)
                except:
                    question['messageSource'] = 'GSMSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_prepaid)], [random.choice(assistance)], 
                                           ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'GSMSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [random.choice(assist_yes)]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'no':
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'yes':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'GSMSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Plan_type') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('International') and \
        {key: value for d in question["property"] for key, value in d.items()}.has_key('Data') and \
        question['messageSource'] == 'GSMSpecific':
            pipeline = [{"$match": {'International Calls': str({key: value for d in question["property"] for key, value in d.items()}['International']),
                                    'Data': str({key: value for d in question["property"] for key, value in d.items()}['Data'])}}]
            data = list(db.postpaid.aggregate(pipeline))
            data = data[:3]
            data = random.sample(data, len(data))
            [i.pop('_id') for i in data]
            [i.pop('International Calls') for i in data]
            [i.pop('Data') for i in data]
            models = [i['Name'] for i in data]
            models = list(set(models))
            models = ', '.join(models)
            if len(data) != 0:
                question['messageText'] = [['Thank You.'], [random.choice(postpaid_rec)], 
                                           ['Please select your preferred plan from' + ' ' + models + '.']]
                question['data'] = data
                question['messageSource'] = 'GSMSpecific'
                question['filter'] = 'itemname'
                reply = question
                try:
                    if {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Thank You for selecting a postpaid plan.'], 
                                                   [random.choice(assistance)], ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [random.choice(assist_yes)]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['product'] = 'yes'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No':
                                question['messageText'] = [['Thank you.'], 
                                                           ['Displayed is your invoice for the purchase.'], [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'GSMSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') \
                    and str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'No' and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) != 'invalid':
                        question['messageText'] = [['Okay.'], [random.choice(assistance)], 
                                                   ["Say Yes to continue and No to Stop."]]
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'quest'
                        reply = question
                        try:
                            if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                                question['messageText'] = [random.choice(assist_yes)]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'no':
                                question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                                question['messageSource'] = 'messageFromBot'
                                question['filter'] = 'normal'
                                question['action'] = 'stop'
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                            elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                            and str(request.data['product']) == 'yes':
                                question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                           [random.choice(res)]]
                                question['messageSource'] = 'BillSpecific'
                                question['filter'] = 'citizen'
                                question['action'] = 'invoice'
                                question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                                reply = question
                                req_cache.delete()
                                return Response(reply)
                        except:
                            question['messageSource'] = 'GSMSpecific'
                            reply = question
                            return Response(reply)
                    elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Name') and \
                    str({key: value for d in question["property"] for key, value in d.items()}['Name']) == 'invalid':
                        question['messageText'] = [["Sorry I didn't get you."], 
                                                   ['Please select your preferred plan from' + ' ' + models + '.']]
                        question['data'] = data
                        question['messageSource'] = 'GSMSpecific'
                        question['filter'] = 'itemname'
                        reply = question
                        return Response(reply)
                except:
                    question['messageSource'] = 'GSMSpecific'
                    reply = question
                    return Response(reply)
            else:
                question['messageText'] = [[random.choice(sry_postpaid)], [random.choice(assistance)], 
                                           ["Say Yes to continue and No to Stop."]]
                question['data'] = data
                question['messageSource'] = 'GSMSpecific'
                question['filter'] = 'quest'
                reply = question
                try:
                    if str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'Yes':
                        question['messageText'] = [random.choice(assist_yes)]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'no':
                        question['messageText'] = [['Thank You.'], [random.choice(assist_no)]]
                        question['messageSource'] = 'messageFromBot'
                        question['filter'] = 'normal'
                        question['action'] = 'stop'
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                    elif str({key: value for d in question["property"] for key, value in d.items()}['Question']) == 'No'\
                    and str(request.data['product']) == 'yes':
                        question['messageText'] = [['Thank you.'], ['Displayed is your invoice for the purchase.'], 
                                                   [random.choice(res)]]
                        question['messageSource'] = 'BillSpecific'
                        question['filter'] = 'citizen'
                        question['action'] = 'invoice'
                        question['url'] = ['https://academy.getjobber.com/wp-content/uploads/2017/01/WhatIsAnInvoice-926x500_c.png']
                        reply = question
                        req_cache.delete()
                        return Response(reply)
                except:
                    question['messageSource'] = 'GSMSpecific'
                    reply = question
                    return Response(reply)
        elif {key: value for d in question["property"] for key, value in d.items()}.has_key('Citizenship') \
        and {key: value for d in question["property"] for key, value in d.items()}.has_key('Card') \
        and question['messageSource'] == 'BillSpecific':
            question['messageText'] = [[random.choice(fillers)], [random.choice(bill)], ['Thank You.'],
                                       [random.choice(assist_no)]]
            question['messageSource'] = 'messageFromBot'
            question['filter'] = 'normal'
            question['hold'] = 'hold'
            question['action'] = 'stop'
            reply = question
            return Response(reply)
        else:
            reply = question
        return Response(reply)
