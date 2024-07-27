import nmap

begin=75
end=80

target = '127.0.0.1'

scanner = nmap.PortScanner()

for i in range(begin,end+1):
    response = scanner.scan(target,str(i))
    state = response['scan'][target]['tcp'][i]['state']
    print(f'Port {i} is {state}.')