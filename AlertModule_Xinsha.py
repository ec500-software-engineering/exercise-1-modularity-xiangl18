# Copyright @ Xinsha Wang xinshaww@bu.edu
# Alert Module

#It's the I/O documentation for Alert System

#Alert Sys
def get_bo_data(data):
	if fine_turn > 20:
		bo_flag = 0

	if exceed(data):
		bo_flag += 1
	else:
		fine_turn += 1
		send_data_to_display();

def get_bp_data(data):
	if fine_turn > 20:
		bp_flag = 0

	if exceed(data):
		bp_flag += 1
	else:
		fine_turn += 1
		send_data_to_display();

def get_pul_data(data):
	if fine_turn > 20:
		pul_flag = 0

	if exceed(data):
		pul_flag += 1
	else:
		fine_turn += 1
		send_data_to_display();

def check_flag:
	r1,r2,r3 = 0
	if bo_flag > 100:
		r1 = 1
	if bp_flag > 100:
		r2 = 1	 
	if pul_flag > 100:
		r3 = 1
	return r1*1 + r2*2 + r3*4

def flag_monitor():
	#listen on flags.
	if check_flag() != 0:
		abnormal_ids=find_abnormal(check_flag())
		abnormal_flag = 1

def Alert_Output():
	"""
	Compare data with certain threthold
	send flags to user interface module.
	"""
	listen_on(alert_flag);
	if find_alert(alert_flag) != -1:
		alert_type = alert_flag;
		send_alert_message(alert_type) #send message to display devices and alarm alert
