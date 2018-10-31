Summary:	IIO sensors to D-Bus proxy
Name:		iio-sensor-proxy
Version:	1.0
Release:	3
License:	GPLv2+
Group:		System/Libraries
URL:		https://github.com/hadess/iio-sensor-proxy
Source0:	https://codeload.github.com/hadess/iio-sensor-proxy/%{name}-%{version}.tar.gz
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libsystemd)

%description
IIO sensors to D-Bus proxy.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
