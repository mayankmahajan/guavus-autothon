import os
import json
import datetime
import csv
import sys

try: 
    json_report_path = 'target/artifacts/report.json'

    csv_path = '/tmp/report.csv'
    csv_header = [
        'product_name',
        'component',
        'build_number',
        'date',
        'build_status'
        'category',
        'total',
        'fail',
        'pass',
        'skip',
        'risk',
        'coverage',
        'time'
    ]

    name = 'NA'
    component = 'NA'
    build_number = os.environ['buildNum']
    build_status = 'NA'
    category = 'pytest'
    coverage = 'NA'
    t = datetime.datetime.now()
    print t

    with open(json_report_path, "r") as read_file:
        json_data = json.load(read_file)

    try:
        num_tests = json_data['report']['summary']['num_tests']
    except KeyError:
        num_tests = 'NA'
        pass

    try:
        failed = json_data['report']['summary']['failed']
    except KeyError:
        failed = 'NA'
        pass

    try:
        passed = json_data['report']['summary']['passed']
    except KeyError:
        passed = 'NA'
        pass


    try:
        skipped = json_data['report']['summary']['skipped']
    except KeyError:
        skipped = 'NA'
        pass


    try:
        error_v = json_data['report']['summary']['error']
    except KeyError:
        error_v = 'NA'
        pass


    with open(csv_path, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        line = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(
            name,
            component,
            build_number,
            t,
            build_status,
            category,
            num_tests,
            failed,
            passed,
            skipped,
            error_v,
            coverage,
            t
        )
        print line
        writer.writerow(line)
except:
    print "Unexpected error:", sys.exc_info()[0]