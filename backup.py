from dotenv import load_dotenv
import datetime, os, subprocess, shlex

load_dotenv()

mysql_backups_dir = os.getenv("MYSQL_BACKUPS_DIR")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_hosts = [
    os.getenv("MYSQL_HOST_0"),
    os.getenv("MYSQL_HOST_1"),
    os.getenv("MYSQL_HOST_2"),
    os.getenv("MYSQL_HOST_3"),
    os.getenv("MYSQL_HOST_4"),
    os.getenv("MYSQL_HOST_5"),
]
mysql_dbs = [
    os.getenv("MYSQL_DB_0"),
    os.getenv("MYSQL_DB_1"),
    os.getenv("MYSQL_DB_2"),
    os.getenv("MYSQL_DB_3"),
    os.getenv("MYSQL_DB_4"),
    os.getenv("MYSQL_DB_5"),
]
mysql_pws = [
    os.getenv("MYSQL_PW_0"),
    os.getenv("MYSQL_PW_1"),
    os.getenv("MYSQL_PW_2"),
    os.getenv("MYSQL_PW_3"),
    os.getenv("MYSQL_PW_4"),
    os.getenv("MYSQL_PW_5"),
]

date = str(datetime.datetime.now().date())

for i in range(6):
    mysql_host = mysql_hosts[i]
    mysql_db = mysql_dbs[i]
    mysql_pw = mysql_pws[i]
    filepath = os.path.join(mysql_backups_dir, f"{mysql_db}-{date}.sql")
    print(filepath)

    args = shlex.split(
        f"mysqldump -u{mysql_username} -p{mysql_pw} -h{mysql_host} --databases {mysql_db}"
    )
    p1 = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dump_output = p1.communicate()[0]

    f = open(filepath, "wb")
    f.write(dump_output)
    f.close()

os.system(
    f"cd {mysql_backups_dir} && rm mysql-backups-{date}.zip ; zip mysql-backups-{date}.zip *sql && rm {mysql_backups_dir}*sql ; cd -"
)
