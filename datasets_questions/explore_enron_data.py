#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data.keys())

pois = [person_name for person_name in enron_data.keys() if enron_data[person_name]['poi']==1]
print pois
print 'There are {} POIs'.format(len(pois))

print 'James Prentice had {} stock'.format(enron_data['PRENTICE JAMES']['total_stock_value'])
print 'Wesley  Colwell wrote {} emails to POIs'.format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
leaders = ['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S']
print 'Jeffrey Skilling exercised {} stock options'.format(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print '{} took home the most money. He got {}'.format(
	max(leaders, key = lambda x: enron_data[x]['total_payments']),
	max([enron_data[x]['total_payments'] for x in leaders]))
print '{} people have a defined salary'.format(len([x for x in enron_data.keys() if enron_data[x]['salary'] != 'NaN']))
print '{} people have a defined email address'.format(len([x for x in enron_data.keys() if enron_data[x]['email_address'] != 'NaN']))

print '{} of the people are missing total payments'.format(float(len([x for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN'])) / len(enron_data.keys()))
print '{} of the POIs are missing total payments'.format(float(len([x for x in pois if enron_data[x]['total_payments'] == 'NaN'])))