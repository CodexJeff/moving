# ============================================================
#
# Student Name (as it appears on cuLearn): Jeff Jose
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a3 import *

def decision_making_function(e):  # 'e' IS THE SHAPE ARGUMENT YOU MUST PASS TO YOUR PERMITTED FUNCTIONS

	condition_for_sending_down =  wrapped_in_a_circle(e) and is_colored_purple(e) or wrapped_in_a_triangle(e) and is_colored_blue(e)
	condition_for_sending_left =  wrapped_in_a_diamond(e) and is_colored_orange(e) or wrapped_in_a_square(e) and is_colored_green(e) and divides_evenly_by(e, 3) or wrapped_in_a_square(e) and is_colored_orange(e) and divides_evenly_by(e, 3)
	condition_for_sending_right = wrapped_in_a_circle(e) and is_colored_orange(e) or wrapped_in_a_triangle(e) and is_colored_green(e)
	
	return (condition_for_sending_down, condition_for_sending_left, condition_for_sending_right)

	
run_the_program(decision_making_function)
