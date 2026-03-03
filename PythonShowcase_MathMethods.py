### Python Showcase Math Methods ###
print("Beginning of the Python Math Methods Showcase\n\n\n")

import math


Math_ArcCosine_def = "Math Arc Cosine: The math.acos() method returns the arc cosine value of a number. Note: The parameter passed in math.acos() must lie between -1 to 1. Tip: math.acos(-1) will return the value of PI."
print(f"\n{Math_ArcCosine_def}")
print("    # Return the arc cosine of numbers")
print(f"        print(math.acos(0.55)) = {math.acos(0.55)}")
print(f"        print(math.acos(-0.55)) = {math.acos(-0.55)}")
print(f"        print(math.acos(0)) = {math.acos(0)}")
print(f"        print(math.acos(1)) = {math.acos(1)}")
print(f"        print(math.acos(-1)) = {math.acos(-1)}")




Math_InverseCosine_def = "Math Inverse Cosine: The math.acosh() method returns the inverse hyperbolic cosine of a number. Note: The parameter passed in acosh() must be greater than or equal to 1."
print(f"\n{Math_InverseCosine_def}")
print("    # Return the inverse hyperbolic cosine of different numbers")
print(f"        print(math.acosh(7)) = {math.acosh(7)}")
print(f"        print(math.acosh(56)) = {math.acosh(56)}")
print(f"        print(math.acosh(2.45)) = {math.acosh(2.45)}")
print(f"        print(math.acosh(1)) = {math.acosh(1)}")





Math_ArcSine_def = "Math Arc Sine: The math.asin() method returns the arc sine of a number. Note: The parameter passed in math.asin() must lie between -1 to 1. Tip: math.asin(1) will return the value of PI/2, and math.asin(-1) will return the value of -PI/2."
print(f"\n{Math_ArcSine_def}")
print("    # Return the arc sine of numbers")
print(f"        print(math.asin(0.55)) = {math.asin(0.55)}")
print(f"        print(math.asin(-0.55)) = {math.asin(-0.55)}")
print(f"        print(math.asin(0)) = {math.asin(0)}")
print(f"        print(math.asin(1)) = {math.asin(1)}")
print(f"        print(math.asin(-1)) = {math.asin(-1)}")




Math_InverseArcSine_def = "Math Inverse Sine: The math.asinh() method returns the inverse hyperbolic sine of a number."
print(f"\n{Math_InverseArcSine_def}")
print("    # Return the hyperbolic arc sine value of numbers")
print(f"        print(math.asinh(7)) = {math.asinh(7)}")
print(f"        print(math.asinh(56)) = {math.asinh(56)}")
print(f"        print(math.asinh(2.45)) = {math.asinh(2.45)}")
print(f"        print(math.asinh(1)) = {math.asinh(1)}")
print(f"        print(math.asinh(0.5)) = {math.asinh(0.5)}")
print(f"        print(math.asinh(-10)) = {math.asinh(-10)}")





Math_ArcTangent_def = "Math Arc Tangent: The math.atan() method returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians. Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated."
print(f"\n{Math_ArcTangent_def}")
print("    #find the arctangent of some values")
print(f"        print(math.atan(0.39)) = {math.atan(0.39)}")
print(f"        print(math.atan(67)) = {math.atan(67)}")
print(f"        print(math.atan(-21)) = {math.atan(-21)}")





Math_ArcTangent_XY_def = "Math Arc Tangent XY: The math.atan2() method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y). The returned value is between PI and -PI."
print(f"\n{Math_ArcTangent_XY_def}")
print("    # Return the arc tangent of y/x in radians")
print(f"        print(math.atan2(8, 5)) = {math.atan2(8, 5)}")
print(f"        print(math.atan2(20, 10)) = {math.atan2(20, 10)}")
print(f"        print(math.atan2(34, -7)) = {math.atan2(34, -7)}")
print(f"        print(math.atan2(-340, -120)) = {math.atan2(-340, -120)}")





Math_InverseHyperbolicTangent_def = "Math Inverse Hyperbolic Tangent: The math.atanh() method returns the inverse hyperbolic tangent of a number. Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99."
print(f"\n{Math_InverseHyperbolicTangent_def}")
print("    #print the hyperbolic arctangent of different numbers")
print(f"        print(math.atanh(0.59)) = {math.atanh(0.59)}")
print(f"        print(math.atanh(-0.12)) = {math.atanh(-0.12)}")
print(f"        print(math.atanh(0.99)) = {math.atanh(0.99)}")




Math_Ceiling_def = "Math Ceiling: The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result. Tip: To round a number DOWN to the nearest integer, look at the math.floor() method."
print(f"\n{Math_Ceiling_def}")
print("    # Round a number upward to its nearest integer")
print(f"        print(math.ceil(1.4)) = {math.ceil(1.4)}")
print(f"        print(math.ceil(5.3)) = {math.ceil(5.3)}")
print(f"        print(math.ceil(-5.3)) = {math.ceil(-5.3)}")
print(f"        print(math.ceil(22.6)) = {math.ceil(22.6)}")
print(f"        print(math.ceil(10.0)) = {math.ceil(10.0)}")



Math_CombinationsPossible_def = "Math Combinations Possible: The math.comb() method returns the number of ways picking k unordered outcomes from Math_Comb_n possibilities, without repetition, also known as combinations. Note: The parameters passed in this method must be positive integers."
print(f"\n{Math_CombinationsPossible_def}")
Math_Comb_n = 7
Math_Comb_k = 5
print("    # Initialize the number of items to choose from")
print("    Math_Comb_n = 7")
print("    # Initialize the number of possibilities to choose")
print("    Math_Comb_k = 5")
print("    # Print total number of possible combinations")
print(f"        print(math.comb(Math_Comb_n, Math_Comb_k)) = {math.comb(Math_Comb_n, Math_Comb_k)}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")




# DEF = ""
#
# print(f"\Math_Comb_n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")



print("\n\n\nEnd of the Python Math Methods Showcase")

