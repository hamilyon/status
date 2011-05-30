#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.gravitydev.com/project/1984/stories/3#task-6

from xml.dom.minidom import parse
import httplib
import sys

#xml hacks
# theirs
jobs = lambda v : v.documentElement.getElementsByTagName('job') 
props = lambda job:(job.getElementsByTagName('title')[0].firstChild.nodeValue , job.getElementsByTagName('region')[0].firstChild.nodeValue, job.getElementsByTagName('code')[0].firstChild.nodeValue)

#ours
vacancies_hh = lambda v : v.documentElement.getElementsByTagName('vacancy')  
props_hh = lambda job:(job.getElementsByTagName('name')[0].firstChild.nodeValue , job.getElementsByTagName('region')[0].getAttribute('id'), job.getAttribute('id'))
#<vacancy id="3732100">
#'name'
#region id="1"

#[0].firstChild.nodeValue
#(title, region, code) = props (job)

def interact():
    while (True):
        print 'command [q(quit) | l(log)N | d(diff)N | m(merge)N | r(revert) | u(update)]: ',
        command = sys.stdin.readline()[:-1]

def answer(question):
    print question,
    return sys.stdin.readline()[:-1]

def get_vacancies_from_vtb(server, url ):
	h1 = httplib.HTTPConnection(server)
	h1.request('GET', url)
	r2 = h1.getresponse()
	return parse(r2)

def get_our_vtb_vacancies(server, url ):
	h1 = httplib.HTTPConnection(server)
	h1.request('GET', url)
	r2 = h1.getresponse()
	return parse(r2)
	
def compare_and_mix(table_vtb_vac, table_our_vac):
	table_our_vac.sort(key = lambda x: x[1])
	table_vtb_vac.sort(key = lambda x: x[1])
	
	result = []
	
	for o in table_our_vac :
		add = True
		for v in table_vtb_vac[:]:
			if o[0].strip() == v[0].strip():
				#~ print '1st' , 
				#~ print o[0].encode('utf-8'),
				#~ print v[0].encode('utf-8')
				
				if (o[0].strip() == v[0].strip() and
					o[1] == v[1]):
					result.append((o[2], v[0], v[1], v[2],))
					table_vtb_vac.remove(v)
					add = False
				else:
					#~ print o[1] + ' != ' + v[1]
					pass
		if add: 
			result.append((o[2],o[0], o[1], None))
	
	for v in table_vtb_vac[:]:
		result.append((None,v[0], v[1],v[2],))
	
	return result
	
def print_three_lists(data, columns=None):
	columns = columns or [0,1,2,3]
	separator = ','
	list_owrs, list_theirs, list_both = [],[],[]
	for row in data:
		
		if row[0]!=None and row[3]!=None:
			list_both.append(row)
		elif row[0]!=None:
			list_owrs.append(row)
		elif row[3]!=None:
			list_theirs.append(row)

	print 'вакансии есть только у HH:'
	print_list(list_owrs,columns)
	print '----=====----'
	print 'вакансии есть только у ВТБ:'
	print_list(list_theirs,columns)
	print '----=====----'
	print 'вакансии есть у обоих:'
	print_list(list_both,columns)

def print_(x):
        print x

def print_list(data, columns):
        for x in data: 
                print ',\t'.join(list(gt(x,columns)))
                        #print_()) 

def gt(lst, cols):
        for c in cols:
                yield encode(or_null(lst[c]))

or_empty = lambda x: x or "" 

or_null = lambda x: x or "null"

encode = lambda x : x.encode('utf-8')

def main():
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option('-i', '--insert', dest='insert', action='store_true', help='in sql-friendly format')
        parser.add_option('-f', '--full', dest='full', action='store_true', help='display all information in table')
        (options, _) = parser.parse_args()
        if bool(options.insert) and bool(options.full):
                print "choose -i or -f"
                sys.exit(2)
        
        
        #new_vtb_vac = get_vacancies_from_vtb('job71.kadry.ru','/cgi-bin/ext/active_public_jobs_xml')
        new_vtb_vac = get_vacancies_from_vtb('192.168.0.199:807','/hh-static/active_public_jobs_xml.xml')
        old_our_vacancies = get_our_vtb_vacancies('api.hh.ru','/1/xml/vacancy/employer/4181/')
        table_vtb_vac = [props(j) for j in jobs(new_vtb_vac)]
        #print len(table_vtb_vac)
        table_our_vac = [props_hh(v) for v in vacancies_hh(old_our_vacancies)]
        #~ import pprint 
        #~ pprint.pprint(table_our_vac)
        data = compare_and_mix(table_vtb_vac, table_our_vac)
        if options.insert:
                print_three_lists(data, [0,3])
                return
        elif options.full:
                print_three_lists(data, [0,3,1,2])
        #~ else:
                #~ print_three_lists(data, [0,3,1,2])
        print_three_lists(data, [0,3,1,2])


if __name__ == "__main__":
        main()
