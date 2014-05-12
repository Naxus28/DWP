import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
the_cal = cal.formatmonth(2013, 1, 0, 0)

#print the_cal

html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
the_html_cal = html_cal.formatmonth(2013, 1)

#print the_html_cal

# for i in cal.itermonthdays(2014,5):
#     print i
#
# for month in calendar.month_name:
#     print month
#
# for day in calendar.day_name:
#     print day

for m in range(1, 13):
    #print m
    cal = calendar.monthcalendar(2013, m)

    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]

    print "%10s %2d" % (calendar.month_name[m], meet_day)
    # print cal

# cal1 = calendar.monthcalendar(2013, 2)
# print cal1
