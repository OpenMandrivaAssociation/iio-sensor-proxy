Summary:	IIO sensors to D-Bus proxy
Name:		iio-sensor-proxy
Version:	1.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		https://github.com/hadess/iio-sensor-proxy
Source0:	https://codeload.github.com/hadess/iio-sensor-proxy/%{name}-%{version}.tar.gz
BuildRequires:	gnome-common

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
