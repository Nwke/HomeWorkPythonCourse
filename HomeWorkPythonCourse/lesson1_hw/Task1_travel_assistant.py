trip_1 = 10
trip_2 = 20
trip_3 = 30
trip_count = 3
course_euro = 60

flight_cost = 15
cost_per_day = 10

husband = 1500
wife = 2000

family_budget = husband + wife

trip_cost = trip_count * 15 + (trip_1 + trip_2 + trip_3) * cost_per_day
print('Стоимость отпуска в евро: ' + str(trip_cost))
print('Стоимость отпуска в рублях: ' + str(trip_cost * course_euro))

if family_budget < trip_cost:
    print('Бюджета не хватает,стоить поднакопить или пойманить крипту.')
else:
    print('Денег на отпуск хватает.Можно и отдохнуть,если хочется.')

