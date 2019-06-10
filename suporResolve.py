#!/usr/bin/env python
# -*- encoding : utf-8 -*-

import os
import re

SUPOR_REGEX = {
	'UI_Identity' : re.compile(r'\b(user(\s?name|\sid)((\sor\s|/)e-?mail)?|e-?mail(\sor\s|/)user(\s)?name|nick\s*name|moniker|cognomen|sobriquet|soubriquet|byname)\b'),
	'UI_Credential' : re.compile(r'\b(pin(code|\s(code|number|no|#))?|personal\sidentification\s(number|no)|password(s)?|passwort|watchword|parole|countersign|(security\s)?passcode)\b'),
	'UI_Contact' : re.compile(r'\b((phone:)?e-?mail|e-?mail(\s)?address(es)?|(mobile\s|tele|cell|your\s)?phone(\s(no|number|#))?|mobile\s(no|number|#)|gmail|contact(s|\sname)|fax)\b'),
	'UI_Account' : re.compile(r'\b((your\s)?login(\s(credential|certificat(e|ion))(s)?)?|regist(er|ration|ry)|user\s(authentication|hallmark|assay(\s|-)mark)|sign(ing)?\s(in|up)|check\sin|log(-|\s+)(in|on)(to)?)\b'),
	'UI_CreditCard' : re.compile(r'\b(((credit|charge|my|your)( |\s)?)?card( |\s)?(number|no|#|information|statement)|(credit|charge)( |\s)?card|cvc(( |\s)+code)?)\b'),
	'UI_SSN' : re.compile(r'\b(((digits\s)?of\s)?ssn|tin|(federal|national)\s(id|identity)|(your\s)?social\ssec(urity)?(\s(number|no|#))?)\b'),
	'UI_Protection' : re.compile(r'\b(security\s(answer|code|token|item)|enter\syour\s(answer|reply|response)|(identification|designation)\s(code|number|no)|activation\s(code|number|no)|financial\sinstitution)\b'),
	'UI_PersonalInfo' : re.compile(r'\b((first|last)(\s)?name|age|sex|gender|birth(\s)?(date|day)?|date\sof\birth|interests|dropbox|facebook|address(es)?)\b'),
	'UI_Health' : re.compile(r'\b(weight|height|health|cholesterol|glucose|obese|calories|kcal|doctor|blood(\stype)?)\b'),
	'UI_FinancialInfo' : re.compile(r'\b(repayment|(payment(s)?|deposit|loan)(\samount)?|income|expir(y|ation)(\sdate)?|paypal|banking|debit|mortgage|taxable|(down|monthly)\spayment|payment\s(information|details)|cardholder\'s\sname|billing\saddress|opening\sbalance)\b')
}

# What percentage of applications have these ambiguous terms?

def SUPOR_SEMRES(hint, text, label):
	val = SUPOR_STOCK_SEMRES(hint)
	if val is not None:
		return val
	val = SUPOR_STOCK_SEMRES(text)
	if val is not None:
		return val
	return SUPOR_STOCK_SEMRES(label)

def SUPOR_STOCK_SEMRES(txt):
	if txt is None:
		return None
	tags = []
	for val in SUPOR_REGEX.keys():
		if SUPOR_REGEX[val].match(txt.lower()):
			tags.append(val)
	return tags if len(tags) > 0 else None

def getLayoutFiles():
	FILENAME = 'LAYOUT_FILES.txt'
	if os.path.isfile(FILENAME):
		return [line.strip() for line in open(FILENAME, 'r')]
	return [] 


if __name__ == '__main__':
	while True:
		strval = raw_input('Enter a string to resolve using SUPOR: ')
		print SUPOR_SEMRES(strval, strval,strval)
		
