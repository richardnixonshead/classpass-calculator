from math import trunc
# This one takes how many classes you want to do per month, and avg points per class, and works out cheapest
classes=int(input('How many classes do you want to do: '))
avgpoints=float(input('Average number of points per class: '))
curpoints=int(input('How many points do you have: '))
plans=[{'cost': 49, 'points': 20}, {'cost': 69, 'points': 30}, {'cost': 79, 'points': 34},{'cost':109, 'points':50},{'cost':119,'points':54},{'cost':170,'points':80}]
extras=[{'cost': 5, 'points': 2},{'cost':25,'points':10},{'cost':55,'points':25},{'cost':95,'points':50},{'cost':0,'points':0}]
totpoints=0
totcost=0
totclasses=0
mincost=999
minpoints=-1
minextras=-1
minrempoints=-1

for plan in plans:
  plancost=plan['cost']
  planpoints=plan['points']
  for extra in extras:
    extrascost=extra['cost']
    extraspoints=extra['points']
    # okay, so we can roll over up to planpoints
    if curpoints > planpoints:
      initialpoints = planpoints
    else:
      initialpoints = curpoints
    points = initialpoints + planpoints + extraspoints
    print("Doing {planpoints} with {extraspoints}. Starting with {initialpoints} we have {points} to use".format(planpoints=planpoints,extraspoints=extraspoints,initialpoints=initialpoints,points=points))
    totcost = plancost + extrascost
    pointsrequired = avgpoints*classes
    if (pointsrequired > points):
      # can't do this combination
      print("Can't do {planpoints} with {extraspoints}".format(planpoints=planpoints,extraspoints=extraspoints))
      continue
    if totcost < mincost:
      minpoints = planpoints
      minextras = extraspoints
      mincost = totcost
      minrempoints = points - pointsrequired

print("Cheapest way to do it is {minpoints} plan with {minextras} extras for {mincost}. You'll have {minrempoints} remaining".format(minpoints=minpoints,minextras=minextras,mincost=mincost,minrempoints=minrempoints))


