import TRCore, sched, time, mechanize

s = sched.scheduler(time.time, time.sleep)



def raid():
	b = mechanize.Browser()
	TRCore.login("http://tx3.travian.fr/", "", "")
	r = TRCore.raid("raidlist.txt")
	while True:
		try:
			r.next()
		except:
			break

raid()

i = 0
while i < 4:
	s.enter(2640, 1, raid, ())
	s.run()
	i += 1
