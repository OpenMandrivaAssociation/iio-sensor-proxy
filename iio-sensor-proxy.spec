Summary:	IIO sensors to D-Bus proxy
Name:		iio-sensor-proxy
Version:	3.4
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
BuildRequires:	meson

%description
IIO sensors to D-Bus proxy.

%prep
%autosetup -p1
%meson \
	-Dgtk-tests=false \
	-Dgeoclue-user=geoclue

%build
%meson_build

%install
%meson_install

%files
%{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf
%{_bindir}/monitor-sensor
%{_libexecdir}/iio-sensor-proxy
%{_unitdir}/iio-sensor-proxy.service
%{_udevrulesdir}/80-iio-sensor-proxy.rules
%{_datadir}/polkit-1/actions/net.hadess.SensorProxy.policy
