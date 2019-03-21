import os
import subprocess
from time import sleep, time


proc = subprocess.Popen(
    ['echo', 'Hello from the child!'],
    shell=True,
    stdout=subprocess.PIPE
)
out, err = proc.communicate()
print(out.decode('utf-8'))


proc = subprocess.Popen(['sleep', '3'], shell=True)
while proc.poll() is None:
    print('Working...')
    # Some time consuming work here
    sleep(0.3)

print('Exit status', proc.poll())


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)], shell=True)
    return proc


start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()
end = time()
print('Finished in %.3f seconds' % (end - start))


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Ql3S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        shell=True,
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)
    return proc


input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())

proc = run_sleep(10)
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())