#It's the I/O documentation for Alert System

#Alert Sys
def Alert_for_three_categories_input(data_in):
	"""
	get data for each type from database.
	format:
		(double value,int type)
	"""
	average_list = [[] for i in range(3)]
	if len(average_list[data_in[1]]) < 20:
		average_list[data_in[1]].append(data_in[0])
	else:
		del(average_list[data_in[1]][0])
		average_list[data_in[1]].append(data_in[0])
	if len(average_list[data_in[1]]) > 20 and exceed_threshold(mean(average_list[data_in[1]])):
		alert_flag[data_in[1]] = 1

def Alert_Output():
	"""
	Compare data with certain threthold
	send flags to user interface module.
	"""
	listen_on(alert_flag);
	if find_alert(alert_flag) != -1:
		alert_type = alert_flag;
		send_alert_message(alert_type) #send message to display devices and alarm alert
