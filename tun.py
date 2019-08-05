from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI

tun = TunTapDevice(name="mytun", flags=(IFF_NO_PI | IFF_TUN))
tun.addr = '192.168.13.10'
tun.dstaddr = '192.168.13.1'
tun.netmask = '255.255.255.0'
tun.persist(True)
tun.mtu = 1500
tun.up()
buf = tun.read(tun.mtu)
tun.write(buf)
