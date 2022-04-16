tempGroup = 0;
totalGroup = 0;

group = input().split();
group.sort();

for i in range(len(group)):
  personFearLvl = int(group[i])
  if personFearLvl > tempGroup:
    tempGroup += 1
    if personFearLvl == tempGroup:
      totalGroup += 1
      tempGroup = 0


print(totalGroup)

//not running for some reason
//says PermissionError
/*
    PermissionError

  [Errno 13] Permission denied: '/home/runner/codingtestprep/venv/bin/python'

  at /nix/store/2vm88xw7513h9pyjyafw32cps51b0ia1-python3-3.8.12/lib/python3.8/subprocess.py:1704 in _execute_child
      1700│                     else:
      1701│                         err_filename = orig_executable
      1702│                     if errno_num != 0:
      1703│                         err_msg = os.strerror(errno_num)
    → 1704│                     raise child_exception_type(errno_num, err_msg, err_filename)
      1705│                 raise child_exception_type(err_msg)
      1706│ 
      1707│ 
      1708│         def _handle_exitstatus(self, sts, _WIFSIGNALED=os.WIFSIGNALED,
exit status 1
  */





