Summary:	IIO sensors to D-Bus proxy
Name:		iio-sensor-proxy
Version:	3.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/
Source0:	https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/archive/%{version}/iio-sensor-proxy-%{version}.tar.bz2
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	autoconf-archive

%description
IIO sensors to D-Bus proxy.

%prep
%autosetup -p1
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-gtk-tests

%build
%make_build

%install
%make_install

%files
%{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf
%{_bindir}/monitor-sensor
%{_sbindir}/iio-sensor-proxy
/lib/systemd/system/iio-sensor-proxy.service
/lib/udev/rules.d/80-iio-sensor-proxy.rules
