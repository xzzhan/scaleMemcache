#!/usr/bin/python

import memcache
import time

#Create a client
servers = ['128.148.16.164:11211', '128.148.16.165:11211', '128.148.16.178:11211'];
mc = memcache.Client(servers);

#Make files to record results
file1 = open('server1.txt', 'w');
file2 = open('server2.txt', 'w');
file3 = open('server3.txt', 'w');

file1.write('bytes_written\ttotal_items\tcurr_connections\tthreads\tcmd_set\tcmd_get\tget_misses\tget_hits\tbytes_read\n');
file2.write('bytes_written\ttotal_items\tcurr_connections\tthreads\tcmd_set\tcmd_get\tget_misses\tget_hits\tbytes_read\n');
file3.write('bytes_written\ttotal_items\tcurr_connections\tthreads\tcmd_set\tcmd_get\tget_misses\tget_hits\tbytes_read\n');

#Record stats
while(1):
	stats = mc.get_stats();

	cur_serv_stats = stats[0][1];
	bytes_written = cur_serv_stats['bytes_written'];
	total_items = cur_serv_stats['total_items'];
	curr_items = cur_serv_stats['curr_items']; 
        curr_connections = cur_serv_stats['curr_connections'];
	threads = cur_serv_stats['threads'];
	cmd_set = cur_serv_stats['cmd_set'];
	cmd_get = cur_serv_stats['cmd_get'];
	get_misses = cur_serv_stats['get_misses'];
	get_hits = cur_serv_stats['get_hits'];
	bytes_read = cur_serv_stats['bytes_read'];
	file1.write(bytes_written+'\t'+total_items+'\t'+curr_connections+'\t'+threads+'\t'+cmd_set+'\t'+cmd_get+'\t'+get_misses+'\t'+get_hits+'\t'+bytes_read+'\t'+curr_items+'\n');
	
	cur_serv_stats = stats[1][1];
	bytes_written = cur_serv_stats['bytes_written'];
	total_items = cur_serv_stats['total_items'];
        curr_items = cur_serv_stats['curr_items'];
	curr_connections = cur_serv_stats['curr_connections'];
	threads = cur_serv_stats['threads'];
	cmd_set = cur_serv_stats['cmd_set'];
	cmd_get = cur_serv_stats['cmd_get'];
	get_misses = cur_serv_stats['get_misses'];
	get_hits = cur_serv_stats['get_hits'];
	bytes_read = cur_serv_stats['bytes_read'];
	file2.write(bytes_written+'\t'+total_items+'\t'+curr_connections+'\t'+threads+'\t'+cmd_set+'\t'+cmd_get+'\t'+get_misses+'\t'+get_hits+'\t'+bytes_read+'\t'+curr_items+'\n');
	
	cur_serv_stats = stats[2][1];
	bytes_written = cur_serv_stats['bytes_written'];
	total_items = cur_serv_stats['total_items'];
        curr_items = cur_serv_stats['curr_items'];
	curr_connections = cur_serv_stats['curr_connections'];
	threads = cur_serv_stats['threads'];
	cmd_set = cur_serv_stats['cmd_set'];
	cmd_get = cur_serv_stats['cmd_get'];
	get_misses = cur_serv_stats['get_misses'];
	get_hits = cur_serv_stats['get_hits'];
	bytes_read = cur_serv_stats['bytes_read'];
	file3.write(bytes_written+'\t'+total_items+'\t'+curr_connections+'\t'+threads+'\t'+cmd_set+'\t'+cmd_get+'\t'+get_misses+'\t'+get_hits+'\t'+bytes_read+'\t'+curr_items+'\n');

	file1.flush();
	file2.flush();
	file3.flush();	
	time.sleep(5);


