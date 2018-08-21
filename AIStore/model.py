# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:06:29 2018

@author: Vishnu
"""

from .config import get_RAM, get_storage, get_frontcam, get_backcam, get_brand
from .config import get_size, get_os, get_budget, get_quest, get_model, get_spec, get_low
from .config import get_plan, get_data, get_voice, get_combo, get_plantype, get_international
from .config import intent_classifier, get_customer, get_citizen, get_card, get_name
from .queries import budget, specs, plan, data, international, new_customer, existing_customer 
from .queries import res, offer_mobile, gsm, helping, offer_gsm, offer_postpaid, offer_prepaid
from .queries import apple_range, samsung_range, blackberry_range, card_new
from .queries import price_range, visitor, fallback, fillers, plan_select
import random

def generate_reply_card(entity, reply, entity_list_available):
    if entity == 'Card':
        new_question = list(filter(None, reply['property']))
        if str({key: value for d in reply['property'] for key, value in d.items()}['Citizen']) == 'Resident' and \
        len(new_question) == 2:
            reply['messageText'] = [[random.choice(fillers)], ['Please Scan your Emirates ID. And, mention "DONE" to proceed further.'], ['Thank You.'], 
                                    [random.choice(card_new)]]
            reply['messageSource'] = 'BillSpecific'
            reply['filter'] = 'card'
            reply['hold'] = 'hold'
            return reply
        elif str({key: value for d in reply['property'] for key, value in d.items()}['Citizen']) == 'Visitor' and \
        len(new_question) == 2:
            reply['messageText'] = [[random.choice(fillers)], [random.choice(visitor)], [random.choice(card_new)]]
            reply['messageSource'] = 'BillSpecific'
            reply['filter'] = 'card'
            return reply
        else:
            reply['messageText'] = [["Sorry. I didn't understand."], ["Could you please repeat which card you are going to use?"]]
            reply['messageSource'] = 'BillSpecific'
            reply['filter'] = 'card'
            return reply
            
def generate_reply_mobile(entity, reply, entity_list_available):
    if entity == 'Price':
        if {key: value for d in reply["property"] for key, value in d.items()}.has_key('Brand'):
            new_question = list(filter(None, reply['property']))
            if str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Apple' and \
            len(new_question) == 3 and {key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer') or \
            str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Apple' \
            and len(new_question) == 2 and str({key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer')) == 'False': 
                first_reply = ['Choosing ' + str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a good option.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a fine selection.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a nice choice.']
                reply['messageText'] = [[random.choice(fillers)], [random.choice(first_reply)], 
                                        [random.choice(apple_range)], [random.choice(budget)]]
                reply['messageSource'] = 'MobileSpecific'
                reply['filter'] = 'price'
                return reply
            elif str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Samsung' and \
            len(new_question) == 3 and {key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer') or \
            str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Samsung' \
            and len(new_question) == 2 and str({key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer')) == 'False': 
                first_reply = ['Choosing ' + str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a good option.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a fine selection.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a nice choice.']
                reply['messageText'] = [[random.choice(fillers)], [random.choice(first_reply)], 
                                        [random.choice(samsung_range)], [random.choice(budget)]]
                reply['messageSource'] = 'MobileSpecific'
                reply['filter'] = 'price'
                return reply
            elif str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Blackberry' and \
            len(new_question) == 3 and {key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer') or \
            str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) == 'Blackberry' \
            and len(new_question) == 2 and str({key: value for d in reply["property"] for key, value in d.items()}.has_key('Customer')) == 'False': 
                first_reply = ['Choosing ' + str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a good option.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a fine selection.', 
                               str({key: value for d in reply["property"] for key, value in d.items()}['Brand'].title()) \
                               + ' is a nice choice.']
                reply['messageText'] = [[random.choice(fillers)], [random.choice(first_reply)], 
                                        [random.choice(blackberry_range)], [random.choice(budget)]]
                reply['messageSource'] = 'MobileSpecific'
                reply['filter'] = 'price'
                return reply
            else:
                reply['messageText'] = [["Sorry. I didn't understand."], 
                                        ["Could you please specify your budget?"]]
                reply['messageSource'] = 'MobileSpecific'
                reply['filter'] = 'price'
                return reply
        else:
            reply['messageText'] = [[random.choice(fillers)], [random.choice(price_range)], 
                                    [random.choice(budget)]]
            reply['messageSource'] = 'MobileSpecific'
            reply['filter'] = 'price'
            return reply
            
def generate_reply_postpaid(entity, reply, entity_list_available):
    if entity == 'International':
        reply['messageText'] = [[random.choice(fillers)], [random.choice(international)]]
        reply['messageSource'] = 'GSMSpecific'
        reply['filter'] = 'normal'
        return reply

def generate_reply_prepaid(entity, reply, entity_list_available):
    if entity == 'Data':
        reply['messageText'] = [[random.choice(fillers)], [random.choice(data)]]
        reply['messageSource'] = 'GSMSpecific'
        reply['filter'] = 'data'
        return reply
    elif entity == 'Voice':
        reply['messageText'] = [[random.choice(fillers)], [random.choice(international)]]
        reply['messageSource'] = 'GSMSpecific'
        reply['filter'] = 'normal'
        return reply

def build_model(question, kern, ent_list):
    kernel_reply = kern.respond(question['messageText'])
    if not "Sorry, I didn't get you.." in kernel_reply:
        response = {}
        response['property'] = []
        response['messageText'] = [kernel_reply]
        response['messageSource'] = 'messageFromBot'
        response['filter'] = 'normal'
        return response
    else:
        response = {}
        response['property'] = []
        response['property'].extend(ent_list)
        intent_label = intent_classifier(question['messageText'])
        print intent_label
        if intent_label == 1 or question['messageSource'] == 'MobileSpecific':
            response['property'] = get_brand(question['messageText'], response['property'])
            response['property'] = get_model(question['messageText'], response['property'])
            response['property'] = get_spec(question['messageText'], response['property'])
            response['property'] = get_low(question['messageText'], response['property'])
            if question['filter'] == 'specs':
                response['property'] = get_RAM(question['messageText'], response['property'])
            response['property'] = get_storage(question['messageText'], response['property'])
            response['property'] = get_frontcam(question['messageText'], response['property'])
            response['property'] = get_backcam(question['messageText'], response['property'])
            response['property'] = get_size(question['messageText'], response['property'])
            response['property'] = get_os(question['messageText'], response['property'])
            if question['filter'] == 'price':
                response['property'] = get_budget(question['messageText'], response['property'])
            if question['filter'] == 'quest':   
                response['property'] = get_quest(question['messageText'], response['property'])
            if question['filter'] == 'itemname':
                response['property'] = get_name(question['messageText'], response['property'])
            specs_list = ['Brand', 'Features', 'Model', 'RAM', 'Storage', 
                          'Front Cam', 'Back Cam', 'Screen Size', 'OS', 'Top', 'Low']
            dict_property = {}
            for i in response['property']:
                for j in specs_list:
                    if j in i:
                        dict_property['Specifications'] = i
            response['property'].append(dict_property)
            entity_list = ['Specifications', 'Price']
            entity_dict_available = {k:v for d in response['property'] for k,v in d.items()}
            entity_list_available = list(entity_dict_available.keys())
            entity_list = [i for i in entity_list if i not in entity_list_available]
            for i in entity_list:
                if i == 'Specifications' :
                    if len(response['property'])<=2 and {key: value for d in response["property"] for key, value in d.items()}.has_key('Customer') \
                    or len(response['property'])<=1 and str({key: value for d in response["property"] for key, value in d.items()}.has_key('Customer')) == 'False':
                        response['messageText'] = [[random.choice(fillers)], [random.choice(offer_mobile)], 
                                                   [random.choice(specs)]]
                        response['messageSource'] = 'MobileSpecific'
                        response['filter'] = 'specs'
                        return response
                    else:
                        response['messageText'] = [["Sorry. I didn't understand."], 
                                                   ["Could you please repeat your brand preference?"]]
                        response['messageSource'] = 'MobileSpecific'
                        response['filter'] = 'specs'
                        return response
                elif i not in entity_list_available:
                    response = generate_reply_mobile(i, response, entity_list_available)
                    response['messageSource'] = 'MobileSpecific'
                    return response
                else:
                    continue
            response['messageSource'] = 'MobileSpecific'
            return response
        elif intent_label == 2 or question['messageSource'] == 'GSMSpecific':
            if question['filter'] == 'normal':
                response['property'] = get_plantype(question['messageText'], response['property'])
                response['property'] = get_plan(question['messageText'], response['property'])
            if question['filter'] == 'data':
                response['property'] = get_data(question['messageText'], response['property'])
            if question['filter'] == 'combo':
                response['property'] = get_combo(question['messageText'], response['property'])
            if question['filter'] == 'quest':
                response['property'] = get_quest(question['messageText'], response['property'])
            if question['filter'] == 'itemname':
                response['property'] = get_name(question['messageText'], response['property'])
            try:
                if str({key: value for d in response['property'] for key, value in d.items()}['Plan_type']) == 'Postpaid':
                    if question['filter'] == 'normal':
                        response['property'] = get_international(question['messageText'], response['property'])
                    entity_list = ['Data', 'International']
                    entity_dict_available = {k:v for d in response['property'] for k,v in d.items()}
                    entity_list_available = list(entity_dict_available.keys())
                    entity_list = [i for i in entity_list if i not in entity_list_available]
                    for i in entity_list:
                        if i == 'Data':
                            response['messageText'] = [[random.choice(fillers)], 
                                                       [random.choice(offer_postpaid)], [random.choice(data)]]
                            response['messageSource'] = 'GSMSpecific'
                            response['filter'] = 'data'
                            return response
                        elif i not in entity_list_available:
                            response = generate_reply_postpaid(i, response, entity_list_available)
                            response['messageSource'] = 'GSMSpecific'
                            return response
                        else:
                            continue
                    response['messageSource'] = 'GSMSpecific'
                    return response
                elif str({key: value for d in response['property'] for key, value in d.items()}['Plan_type']) == 'Prepaid':
                    if question['filter'] == 'normal':
                        response['property'] = get_voice(question['messageText'], response['property'])
                    specs_list = ['Plan']
                    dict_property = {}
                    for i in response['property']:
                        for j in specs_list:
                            if j in i:
                                dict_property['Plans'] = i
                    response['property'].append(dict_property)
                    entity_list = ['Plans', 'Data', 'Voice']
#                     entity_list = ['Plan', 'Data', 'Voice']
                    entity_dict_available = {k:v for d in response['property'] for k,v in d.items()}
                    entity_list_available = list(entity_dict_available.keys())
                    entity_list = [i for i in entity_list if i not in entity_list_available]
                    for i in entity_list:
                        if i == 'Plans':
                            if len(response['property'])<=3 and {key: value for d in response["property"] for key, value in d.items()}.has_key('Customer') \
                            or len(response['property'])<=2 and str({key: value for d in response["property"] for key, value in d.items()}.has_key('Customer')) == 'False':
                                response['messageText'] = [[random.choice(fillers)], 
                                                           [random.choice(offer_prepaid)], [random.choice(plan)]]
                                response['messageSource'] = 'GSMSpecific'
                                response['filter'] = 'normal'
                                return response
                            else:
                                response['messageText'] = [["Sorry. I didn't understand."], 
                                                           ["Could you please repeat?"]]
                                response['messageSource'] = 'GSMSpecific'
                                response['filter'] = 'normal'
                                return response
                        elif i not in entity_list_available:
                            response = generate_reply_prepaid(i, response, entity_list_available)
                            response['messageSource'] = 'GSMSpecific'
                            return response
                        else:
                            continue
                    response['messageSource'] = 'GSMSpecific'
                    return response
            except:
                response['messageText'] = [[random.choice(fillers)], [random.choice(offer_gsm)], 
                                           [random.choice(gsm)], ['Postpaid or Prepaid?']]
                response['messageSource'] = 'GSMSpecific'
                response['filter'] = 'normal'
                return response
        elif intent_label == 5:
            response['property'] = get_customer(question['messageText'], response['property'])
            entity_list = ['Customer']
            entity_dict_available = {k:v for d in response['property'] for k,v in d.items()}
            entity_list_available = list(entity_dict_available.keys())
            entity_list = [i for i in entity_list if i not in entity_list_available]
            for i in entity_list:
                if i == 'Customer':
                    response['messageText'] = ['Are you a New Customer or an Existing customer?']
                    response['messageSource'] = 'messageFromBot'
                    response['filter'] = 'normal'
                    return response
                else:
                    continue
            try:
                if str({key: value for d in response['property'] for key, value in d.items()}['Customer']) == 'New':
                    response['messageText'] = [[random.choice(fillers)], [random.choice(new_customer)], 
                                               [random.choice(helping)]]
                    response['messageSource'] = 'messageFromBot'
                    response['filter'] = 'normal'
                    return response
                elif str({key: value for d in response['property'] for key, value in d.items()}['Customer']) == 'Existing':
                    response['messageText'] = [[random.choice(fillers)], [random.choice(existing_customer)], 
                                               [random.choice(helping)]]
                    response['messageSource'] = 'messageFromBot'
                    response['filter'] = 'normal'
                    return response
            except:
                response['messageSource'] = 'messageFromBot'
                return response 
        elif intent_label == 6 or question['messageSource'] == 'BillSpecific':
            if question['filter'] == 'card':
                response['property'] = get_card(question['messageText'], response['property'])
            if question['filter'] == 'citizen':
                response['property'] = get_citizen(question['messageText'], response['property'])
            if question['filter'] == 'quest':     
                response['property'] = get_quest(question['messageText'], response['property'])
            specs_list = ['Citizen']
            dict_property = {}
            for i in response['property']:
                for j in specs_list:
                    if j in i:
                        dict_property['Citizenship'] = i
            response['property'].append(dict_property)
            entity_list = ['Citizenship', 'Card']
            entity_dict_available = {k:v for d in response['property'] for k,v in d.items()}
            entity_list_available = list(entity_dict_available.keys())
            entity_list = [i for i in entity_list if i not in entity_list_available]
            for i in entity_list:
                if i == 'Citizenship':
                    if len(response['property']) == 0:
                        response['messageText'] = [[random.choice(fillers)], [random.choice(res)]]
                        response['messageSource'] = 'BillSpecific'
                        response['filter'] = 'citizen'
                        return response
                    else:
                        response['messageText'] = [["Sorry. I didn't understand."], 
                                                   ["Could you please confirm if you are a UAE resident?"],
                                                   ["Please say Yes or No."]]
                        response['messageSource'] = 'BillSpecific'
                        response['filter'] = 'citizen'
                        return response
                elif i not in entity_list_available:
                    response = generate_reply_card(i, response, entity_list_available)
                    response['messageSource'] = 'BillSpecific'
                    return response
                else:
                    continue
            response['messageSource'] = 'BillSpecific'
            return response 
        elif intent_label == 7:
            response['messageText'] = [["That's okay."], [random.choice(offer_gsm)], 
                                       [random.choice(plan_select)], ["Prepaid or Postpaid?"]]
            response['messageSource'] = 'messageFromBot'
            response['filter'] = 'normal'
            return response
        elif intent_label == 8:
            response['messageText'] = [["That's okay."], [random.choice(offer_mobile)], 
                                       ["What would you like?"]]
            response['messageSource'] = 'messageFromBot'
            response['filter'] = 'normal'
            return response
        else:
            response['messageText'] = [random.choice(fallback)]
            response['messageSource'] = 'messageFromBot'
            response['filter'] = 'normal'
            return response
