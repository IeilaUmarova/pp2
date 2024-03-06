import os
location = '/'
print([name for name in os.listdir(location)])
print([name for name in os.listdir(location) if os.path.isdir(os.path.join(location, name))])
print([name for name in os.listdir(location) if not os.path.isdir(os.path.join(location, name))])