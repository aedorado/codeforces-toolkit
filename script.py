import os
import shutil

contest_id = raw_input('Enter contest id : ')
ext = raw_input('Enter filename extension : ')

contest_id = contest_id.strip()
ext = ext.strip()

if not os.path.exists('contest/' + contest_id):
	os.mkdir('contest/' + contest_id)

open('contest/' + contest_id + '/input', 'w')
for filename in range(ord('A'), ord('F')):
	shutil.copy('templates/' + ext, 'contest/' + contest_id + '/' + contest_id + chr(filename) + '.' + ext)
