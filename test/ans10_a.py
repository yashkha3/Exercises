def endcalc(a, b, c, d, e, f, g):
	opera_hour = a + d
	opera_minute = b + e
	opera_seconds = c + f


	while opera_seconds >= 60:
		opera_seconds = opera_seconds - 60
		opera_minute = opera_minute + 1

	while opera_minute >= 60: 
		opera_minute = opera_minute - 60
		opera_hour = opera_hour + 1

	if opera_hour >= 12:
		opera_hour = opera_hour - 12
		if g == "AM":
			g = "PM"

		elif g == "PM":
			g = "AM"

	print(f"\n\n                 Opera will end at  { opera_hour }:{ opera_minute }:{ opera_seconds } { g }")


sh = int(input(" Enter Starting Hour   : "))
sm = int(input(" Enter Starting Minute : "))
ss = int(input(" Enter Starting Second : "))
gt = input("\n\n Enter AM or PM        :").upper()

rh = int(input("\n\n\n Enter Total Duration Hour     : "))
rm = int(input(" Enter Total Duration Minute   : "))
rs = int(input(" Enter Total Duration Second   : "))

if sh and rh <= 12:
	if sm and rm <= 60:
		endcalc(sh, sm, ss, rh, rm, rs, gt)
else:
	print("Wrong Timing Given")	
