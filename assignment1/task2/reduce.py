#!/usr/bin/env python
import sys
import csv
parkArray = [
    'summons_number',
    'issue_date',
    'violation_code',
    'violation_county',
    'violation_description',
    'violation_location',
    'violation_precinct',
    'violation_time',
    'time_first_observed',
    'meter_number',
    'issuer_code',
    'issuer_command',
    'issuer_precinct',
    'issuing_agency',
    'plate_id',
    'plate_type',
    'registration_state',
    'street_name',
    'vehicle_body_type',
    'vehicle_color',
    'vehicle_make',
    'vehicle_year'
]

openArray = [
    'summons_number',
    'plate',
    'license_type',
    'county',
    'state',
    'precinct',
    'issuing_agency',
    'violation',
    'violation_status',
    'issue_date',
    'violation_time',
    'judgment_entry_date',
    'amount_due',
    'payment_amount',
    'penalty_amount',
    'fine_amount',
    'interest_amount',
    'reduction_amount'
]

def format(s):
	return str(s).replace('(', '').replace(')', '').replace("'", '')

def formatOut(key, value):
		return '{0}\t{1}'.format(format(key), format(value))

def parkId(value):
    return parkArray.index(value)

def openId(value):
    return openArray.index(value)

preKey = None
preValue = 0
for line in sys.stdin:
	key, value = line.split('\t', 1)
	value = value.strip()

	if key == preKey:
		preValue += 1
	else:
		if preKey:
			print('{}\t{}'.format(preKey, preValue))
		preKey = key
		preValue = 1

if preKey:
	print('{}\t{}'.format(preKey, preValue))

		




