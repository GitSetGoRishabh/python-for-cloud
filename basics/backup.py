import os
import shutil
import datetime
def backup(src,dest):
    today=datetime.date.today()
    backup_file=os.path.join(dest,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file.replace('.tar.gz',''),'gztar',src)

src="/home/rishabh/Github/python-for-cloud/basics"
dest="/home/rishabh/Github/python-for-cloud/basics/backup"
backup(src,dest)