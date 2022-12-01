from math import trunc
plan=int(input('What is your plan: '))
extras=int(input('How many extras per month: '))
avgpoints=float(input('Average number of points per class: '))
months=int(input('Number of months to model: '))
plancost = 0
extrascost = 0
if plan == 20:
  plancost = 49
if plan == 30:
  plancost = 69
if plan == 34:
  plancost = 79
if plan == 50:
  plancost = 109
if plan == 54:
  plancost = 119
if plan == 80:
  plancost = 170
if extras == 2:
  extrascost = 5
if extras == 10:
  extrascost = 25
if extras == 25:
  extrascost = 55
if extras == 50:
  extrascost = 95
maxclasses = 8
totpoints=0
curpoints=0
totcost=0
totclasses=0
for month in range(1,months+1):
  monthpoints = plan+extras
  # so we get an extra (plan+extras) points
  totpoints=totpoints+monthpoints
  totcost=totcost+(plancost+extrascost)
  # calculate rollover
  if curpoints > plan:
    curpoints = plan
  curpoints = curpoints + monthpoints
  maxclasses = trunc(curpoints/avgpoints)
  totclasses = totclasses+maxclasses
  curpoints = curpoints-(maxclasses*avgpoints)
  print("M={month} Points at end: {curpoints} Classes in month: {maxclasses}".format(month=month,curpoints=curpoints,maxclasses=maxclasses))

costperclass=float(float(totcost)/float(totclasses))
print("Total - Points: {totpoints} Classes: {totclasses} Cost: {totcost} Cost per class: {costperclass}".format(totpoints=totpoints,totclasses=totclasses,totcost=totcost,costperclass=costperclass))


