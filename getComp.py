def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def runGetComp():
  print("DEBUG: begun getcomp")
  from cpuinfo import get_cpu_info
  import platform
  import psutil
  
  uname = platform.uname()
  system = uname.system
  node = uname.node
  release = uname.release
  version = uname.version
  machine = uname.machine
  
  svmem = psutil.virtual_memory()
  memTotal = get_size(svmem.total)
  memUsed = get_size(svmem.used)

  cpuBrand = get_cpu_info()['brand_raw']
  physCore = psutil.cpu_count(logical=False)
  allCore = psutil.cpu_count(logical=True)

  return "SYSTEM:", system, node,"CPU:", cpuBrand, physCore, allCore,"MEMORY:", memTotal, memUsed
