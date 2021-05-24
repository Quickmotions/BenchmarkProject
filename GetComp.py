def runGetComp():
  from cpuinfo import get_cpu_info
  import platform
  cpuBrand = get_cpu_info()['brand_raw']
  OSBrand = platform.system()
  return cpuBrand, OSBrand
